#!/bin/bash
#Takes in a URL, sends a GET request to the URL, and displays the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
