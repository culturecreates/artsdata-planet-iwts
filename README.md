Artsdata Planet IWTS
---------------------

Scripts to import and export data between IWTS and Artsdata.


IWTS --> Artsdata
=====================

The data from IWTS is loaded into the Artsdata graph http://kg.artsdata.ca/culture-creates/artsdata-planet-iwts/iwts-ca


Artsdata --> IWTS
================

IWTS can call the Artsdata Query API to get Artsdata URIs mapped to IWTS agents (people/organizations):

https://api.artsdata.ca/query?format=json&frame=https://raw.githubusercontent.com/culturecreates/artsdata-planet-iwts/refs/heads/main/frame/iwts_frame.jsonld&sparql=https://raw.githubusercontent.com/culturecreates/artsdata-planet-iwts/refs/heads/main/sparql/agents_matched_artsdata_uri.sparql

Meeting summaries
https://docs.google.com/document/d/1M1y2gtGkb-jlxVTEVviGbzGt0KzwjR3QbhojHkZDhrc/edit?tab=t.0


