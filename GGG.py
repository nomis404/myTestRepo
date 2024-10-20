#This code sample uses the 'requests' library:
#http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://cloudnative015.atlassian.net/rest/api/3/issue"
API_TOK= ""
auth = HTTPBasicAuth("cloudnative015@gmail.com", API_TOK)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Desc 2st order",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10008"
    },
    "project": {
      "key": "P02"
    },
    "summary": "My Second Jira ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))