# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
import requests
import re
import typer
import webbrowser

from dotenv import dotenv_values
from explainers import EXPLAINERS
from progress.bar import IncrementalBar

app = typer.Typer()
config = dotenv_values(".env")
today = datetime.datetime.now().strftime("%Y-%m-%d")

API_ENDPOINT = 'https://api.github.com/repos/'
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {config.get("TOKEN")}',
    'User-Agent': 'privacy-sandbox-explainer-updates'
}


def get_api_url(repo_dict: dict, since: str, until: str):
    """
    Returns a suitable URL to query the GitHub commits API
    https://docs.github.com/en/rest/commits/commits#list-commits-on-a-repository
    """
    return (
        f"https://api.github.com/repos/{repo_dict['repo']}/commits"
        f"?per_page=100&path={repo_dict['path']}&since={since}&until={until}"
    )


def get_html_url(api_url: str):
    """Get the HTML url for an API endpoint"""
    return re.sub(r'//api\.github\.com\/repos', '//github.com', api_url)


def parse_repo_url(explainer_url: str):
    """Chop up a URL to a README into some useful components that
    we need to give the GitHub history API."""
    owner_repo = explainer_url.split("https://github.com/")[1]
    owner_repo = owner_repo.split("/")
    owner_repo = "/".join(owner_repo[0:2])
    explainer_path = explainer_url.split("/")[-1]
    return {"repo": owner_repo, "path": explainer_path}

def verify_token():
    """Make sure that we have a valid GitHub token.

    We do this by requesting the /issues endpoint, which we should have access
    to with the public_repo scope. If it's invalid - it'll return a 401 and we
    can bail."""
    rv = requests.get("https://api.github.com/user/issues", headers=HEADERS)
    if rv.status_code == 401:
        return False
    return True


def get_explainers(file: any, since: str, until: str):
    bar = IncrementalBar("Fetching changes from GitHub", max=len(EXPLAINERS))
    file.write(
        f"""<!DOCTYPE html><body style="font-family: sans-serif"><h3>The following changes have been made to Explainers covered in Annex 1 from {since} to {until}:</h3><ul>""")
    for explainer in sorted(EXPLAINERS, key=lambda x: x[0]):
        shortname = explainer[0]
        parsed = parse_repo_url(explainer[1])
        api_url = get_api_url(parsed, since, until)
        try:
            rv = requests.get(api_url, headers=HEADERS)
            rv.raise_for_status()
        except Exception as e:
            print(e)
        commits = rv.json()
        if len(commits):
            file.write(
                f'<li>{shortname} - {len(commits)} {"changes" if len(commits) > 1 else "change"}, see <a href="{get_html_url(api_url)}">GitHub</a>.</li>')
        bar.next()
    file.write('</ul></body>\n')
    bar.finish()


def main(since: str = typer.Option(today),
         until: str = typer.Option(today),
         file: typer.FileTextWrite = typer.Option('explainers.html')):
    if verify_token():
        get_explainers(file, since, until)
        webbrowser.open_new(f"file://{os.path.realpath('explainers.html')}")
    else:
        print("Double check your GitHub token at https://github.com/settings/tokens - it seems to be invalid.")


if __name__ == "__main__":
    typer.run(main)
