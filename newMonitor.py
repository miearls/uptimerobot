import sys
import http.client

APIKEY = "uptimeRobotAPIKey"
alertContact = "contactIDNumber"

myURL = sys.argv[2]
conn = http.client.HTTPSConnection("api.uptimerobot.com")
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
}

def serverchecks():
   '''
    :param server:
    :param FQDN:
    :return: Function to create 6 different health checks (WHM, ICMP, FTP, SMTP, POP3, IMAP) based on the FQDN. Returns the status of the request.
    '''
    monitors = {'WHM': 'type=4&sub_type=99&port=2087',
                'ICMP': 'type=3',
                'FTP': 'type=4&sub_type=3',
                'SMTP': 'type=4&sub_type=4',
                'POP3': 'type=4&sub_type=5',
                'IMAP': 'type=4&sub_type=6',
                }
    for X in monitors:
	# debug payload statement
        #print("api_key=" + APIKEY + "&format=json&" + monitors[X] + "&url=" + myURL + "&friendly_name=" + myURL + "-" + X + "&alert_contacts=" + alertContact + "")
        payload = "api_key=" + APIKEY + "&format=json&" + monitors[X] + "&url=" + myURL + "&friendly_name=" + myURL + "-" + X + "&alert_contacts=" + alertContact + ""
        conn.request("POST", "/v2/newMonitor", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

def hostcheck():
   '''
    :param server:
    :param FQDN:
    :return: Function to create 1 health checks based on the FQDN. Returns the status of the request.
    '''
    monitors = {'HTTP': 'type=1'
                }
    for X in monitors:
	# debug payload statement
        #print("api_key=" + APIKEY + "&format=json&" + monitors[X] + "&url=http://" + myURL + "&friendly_name=" + myURL + "-" + X + "&alert_contacts=" + alertContact + "")
        payload = "api_key=" + APIKEY + "&format=json&" + monitors[X] + "&url=http://" + myURL + "&friendly_name=" + myURL + "-" + X + "&alert_contacts=" + alertContact + ""
        conn.request("POST", "/v2/newMonitor", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

if len(sys.argv) != 3:
    print("usage", sys.argv[0], "<HOST or SERVER> <URL>")
    sys.exit(3)

if sys.argv[1].lower() == "host":
    hostcheck()
if sys.argv[1].lower() == "server":
    serverchecks()
