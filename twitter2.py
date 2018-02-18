import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
COUNT_OF_USER = 10

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def make_recuest():
    tags = ['id', 'name', 'location', 'description', 'url']
    return tags

def change_request(request, info):
    data = dict()
    for r in request:
        data[r] = info[r]
    return data

def make_data(request):
    data = []
    for count in range(COUNT_OF_USER):
        data.append(change_request(request, js['users'][count]))
    return data


def printing(request, data):
    count = 0
    for count in range(COUNT_OF_USER):
        for r in request:
            print(r + " : ", data[count][r])
        print("\n______________________\n")

def make_js():
    #while True:
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): return
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': str(COUNT_OF_USER)})
    # print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    global js
    js = json.loads(data)
    with open("n.txt", "w") as f:
        f.write(str(js))
    # print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    # print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        # print(u['screen_name'])
        if 'status' not in u:
            # print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
