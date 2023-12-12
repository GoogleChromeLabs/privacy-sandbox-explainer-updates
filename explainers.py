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

# Note: new explainers can be added to the end of the list, we sort them
# before fetching from the GitHub API.
EXPLAINERS = [
    ("Aggregation Service for the Attribution Reporting API",
     "https://github.com/WICG/attribution-reporting-api/blob/main/AGGREGATION_SERVICE_TEE.md"),
    ("Attribution Reporting API with Aggregatable Reports",
     "https://github.com/WICG/attribution-reporting-api/blob/main/AGGREGATE.md"),
    ("Attribution Reporting with event-level reports",
     "https://github.com/WICG/attribution-reporting-api/blob/main/EVENT.md"),
    ("Bounce Tracking Mitigations",
     "https://github.com/wanderview/bounce-tracking-mitigations/blob/main/explainer.md"),
    ("CHIPS API",
     "https://github.com/privacycg/CHIPS/blob/main/README.md"),
    ("Core Attribution API",
     "https://github.com/WICG/attribution-reporting-api/blob/main/README.md"),
    ("Cross-Environment Attribution API",
     "https://github.com/WICG/attribution-reporting-api/blob/main/app_to_web.md"),
    ("Federated Credential Management (FedCM)",
     "https://github.com/fedidcg/FedCM/blob/main/explainer.md"),
    ("Fenced Frames API",
     "https://github.com/WICG/fenced-frame/blob/master/explainer/README.md"),
    ("Related Website Sets",
     "https://github.com/WICG/first-party-sets/blob/main/README.md"),
    ("Protected Audience API",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE.md"),
    ("IP Protection",
     "https://github.com/GoogleChrome/ip-protection/blob/master/README.md"),
    ("Network State Partitioning",
     "https://github.com/MattMenke2/Explainer---Partition-Network-State/blob/main/README.md"),
    ("Privacy Budget",
     "https://github.com/mikewest/privacy-budget/blob/master/README.md"),
    ("Shared Storage API",
     "https://github.com/WICG/shared-storage/blob/main/README.md"),
    ("Storage Partitioning",
     "https://github.com/wanderview/quota-storage-partitioning/blob/main/explainer.md"),
    ("Topics API",
     "https://github.com/patcg-individual-drafts/topics/blob/main/README.md"),
    ("Private State Tokens API",
     "https://github.com/WICG/trust-token-api/blob/main/README.md"),
    ("User-Agent Client Hints",
     "https://github.com/WICG/ua-client-hints/blob/main/README.md"),
    ("3PCD Exemption Heuristics",
     "https://github.com/amaliev/3pcd-exemption-heuristics/blob/main/explainer.md"),
    ("Private Aggregation API",
     "https://github.com/patcg-individual-drafts/private-aggregation-api/blob/main/README.md"),
    ("Private Aggregation API Report Verification",
     "https://github.com/patcg-individual-drafts/private-aggregation-api/blob/main/report_verification.md"),
    ("Storage Access API",
     "https://github.com/cfredric/chrome-storage-access-api/blob/main/README.md"),
    ("Storage Access API for Non-Cookie Storage",
     "https://github.com/arichiv/saa-non-cookie-storage/blob/main/README.md"),
    ("Form Factor User-Agent Client Hint",
     "https://github.com/djmitche/web-explainers/blob/main/sec-ch-ua-form-factor.md"),
    ("Fenced Frames Ads Reporting",
     "https://github.com/WICG/turtledove/blob/main/Fenced_Frames_Ads_Reporting.md"),
    ("FLEDGE Key/Value Server API",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_Key_Value_Server_API.md"),
    ("FLEDGE Key/Value Service trust model",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_Key_Value_Server_trust_model.md"),
    ("FLEDGE Browser Bidding & Auction API",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_browser_bidding_and_auction_API.md"),
    ("Extended Private Aggregation Reporting in FLEDGE",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_extended_PA_reporting.md"),
    ("Fledge k-Anonymity Differential Privacy",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_k_anonymity_differential_privacy.md"),
    ("Privacy Sandbox k-Anonymity Server",
     "https://github.com/WICG/turtledove/blob/main/FLEDGE_k_anonymity_server.md"),
    ("Protected Audience Services documentation",
     "https://github.com/privacysandbox/protected-auction-services-docs/blob/main/README.md"),
    ("Protected Audience Services discussion",
     "https://github.com/WICG/protected-auction-services-discussion/blob/main/README.md"),
]
