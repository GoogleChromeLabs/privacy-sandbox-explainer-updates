# Privacy Sandbox Explainer Updates

This script allows a user to print out the list of explainer commits
after a given date until the current date. `explainers.py` contains the
list of [Privacy Sandbox](https://privacysandbox.com/) explainers, and
can be easily edited.

# Set up

Note: these instructions assume a unix-like environment. On Windows, make
sure that the Windows Subsystem for Linux is first installed, then a
bash-like shell in Windows can be installed.

## Virtual Environment

A virtual environment is an optional, but recommended step:

1. Create a new virtual environment. Here we give it a name `env`, but
you can name it whatever you like:

    `python3 -m venv env`

2. Activate the virtual environment:

    `source env/bin/activate`

## Getting the code and configuring the tool

1. Clone the repository and navigate to the working directory:

    ```bash
    git clone https://github.com/GoogleChromeLabs/privacy-sandbox-explainer-updates.git
    cd privacy-sandbox-explainer-updates/
    ```

2. Install Python dependencies (virtual environments are recommended,
not documented here):

    `pip3 install -r requirements.txt`

3. Run the following command in a terminal:

    `mv copyme.env .env`

4. Create a [personal access token](https://github.com/settings/tokens).
You only need to select the `public_repo` scope, and the expiry is up to
you.

5. Paste the token inside the newly created `.env` file, after `TOKEN=`.

# Usage

Navigate to the `privacy-sandbox-explainer-updates` directory in your terminal and run the following:

    `python3 pseupdates.py --since=2022-04-01`

# License

Copyright 2022 Google LLC.
SPDX-License-Identifier: Apache-2.0
