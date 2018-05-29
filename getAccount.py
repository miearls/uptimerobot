import http.client

'''
:param APIKey:
:return: This script will return all Account details (max number of monitors that can be added 
:and number of up/down/paused monitors) output values in json format 
'''

APIKEY = "uptimeRobotAPIKey"

conn = http.client.HTTPSConnection("api.uptimerobot.com")

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

payload = "api_key="+APIKEY+"&format=json"

conn.request("POST", "/v2/getAccountDetails", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
