# Privacy Sandbox Explainer Updates

This script allows a user to print out the list of explainer commits
after a given date until the current date. `explainers.py` contains the
list of [Privacy Sandbox](https://privacysandbox.com/) explainers, and
can be easily edited.

# Set up

1. Install Python dependencies (virtual environments are recommended,
not documented here):

`pip3 install -r requirements.txt`

2. Run the following command in a terminal:

`mv copyme.env .env`

3. Put a GitHub [personal access token](https://github.com/settings/tokens) with
a `public_repo` scope as the value to `TOKEN=` inside the newly created `.env`
file. **Do not share this token**.

# Usage

`python3 pseupdates.py --since=2022-04-01`

# License

Copyright 2022 Google LLC.  
SPDX-License-Identifier: Apache-2.0
