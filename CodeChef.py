# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://cloudnative015.atlassian.net/rest/api/3/project"
API_TOK= "3"
auth = HTTPBasicAuth("cloudnative015@gmail.com", API_TOK)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output = json.loads(response.text)
#dict = output[0]["name"]
for i in output:
    print(i["name"])