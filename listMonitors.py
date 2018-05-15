import sys
import http.client

'''
:param APIKey:
:return: This script will return all values in json format 
'''

APIKEY = "uptimeRobotAPIKey"

conn = http.client.HTTPSConnection("api.uptimerobot.com")

payload = "api_key="+APIKEY+"&format=json&logs=1"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

conn.request("POST", "/v2/getMonitors", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
