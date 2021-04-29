#!/bin/bash
export PORT=8080
export CLIENT_APP_ORIGIN=http://130.60.156.181:80
export OAUTH2_SUCCESS_FORWARD=http://130.60.156.181
export OAUTH2_AUTHORIZE=https://www.csg.uzh.ch/ddosgrid/ddosdb/o/authorize/
export OAUTH2_TOKEN=https://www.csg.uzh.ch/ddosgrid/ddosdb/o/token/
export OAUTH2_CLIENTID=z7yhn6PyBgeFBgnYQahON4S9qVqpgbTyIKjDqRZg
export OAUTH2_CLIENTSECRET=zxEWUDvNHAlOqDY8o4cdNROGsnDAC6hYaANITpMMnSwwvLJCku6GbNAvjZTvRzKBPyS88AXe7fZagFXQaowVlVQCaolYaCpX1IbQmIGTNboeZOBMEsxkDYMa2rkv5AZN
export OAUTH2_CALLBACK=http://130.60.156.181:8080/auth/provider/callback/
export DDOSDB_PROFILEINFO=https://www.csg.uzh.ch/ddosgrid/ddosdb/api/profileinfo
export DDOSDB_PCAPEXPORT=https://www.csg.uzh.ch/ddosgrid/ddosdb/
export DDOSDB_ATTACKTRACE_PATH=https://www.csg.uzh.ch/ddosgrid/ddosdb/api/attack-trace
export DDOSDB_FILTEREXPORT=https://www.csg.uzh.ch/ddosgrid/ddosdb/api/upload-filter_rules
export DDOSDB_HOST=www.csg.uzh.ch

node index.js
