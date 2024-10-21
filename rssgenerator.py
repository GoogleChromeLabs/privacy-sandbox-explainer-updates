# Copyright 2024 Google LLC
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

from datetime import datetime
import os
import xml.etree.ElementTree as ET
from explainers import EXPLAINERS

def generate_opml():
  """
  Generates an OPML file for GitHub commit feeds.
  """

  opml = ET.Element("opml", {"version": "1.0"})
  head = ET.SubElement(opml, "head")
  ET.SubElement(head, "title").text = "Privacy Sandbox Explainer Updates"

  # Add dateCreated field
  date_created = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
  ET.SubElement(head, "dateCreated").text = date_created

  body = ET.SubElement(opml, "body")
  outline = ET.SubElement(body, "outline", {"text": "privacy-sandbox-explainer-updates"})

  explainers_set = set()
  for text, url in EXPLAINERS:
    # Assume the url format: https://github.com/{user}/{repo_name}/blob/{branch_name}/*
    repo_url = url.split('blob')[0]
    repo_name = repo_url.split("/")[-2] # Extract repo name from URL
    branch_name = url.split('blob')[1].split("/")[1]
    explainers_set.add((repo_url, repo_name, branch_name))

  for repo_url, repo_name, branch_name in explainers_set:
    ET.SubElement(outline, "outline", {
        "text": f"Recent Commits to {repo_name}:{branch_name}",
        "type": "rss",
        "xmlUrl": os.path.join(repo_url, "commits.atom"),
        "htmlUrl": os.path.join(repo_url, "commits", branch_name)
    })

  tree = ET.ElementTree(opml)
  ET.indent(tree, space="\t", level=0)
  tree.write("privacy-sandbox-explainer-updates.opml", encoding="UTF-8", xml_declaration=True)

def main():
    generate_opml()

if __name__ == "__main__":
    main()
