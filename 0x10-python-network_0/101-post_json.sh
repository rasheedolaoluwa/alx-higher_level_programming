#!/bin/bash
# Sends JSON POST request to URL $!, display response body
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
