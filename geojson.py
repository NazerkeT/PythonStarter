import json
import urllib.request, urllib.error,urllib.parse,ssl

basis="http://py4e-data.dr-chuck.net/geojson?"

ctx=ssl.create_default_context
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    address=input("Enter location: ")
    if (len(address)<1): break
    url=basis + urllib.parse.urlencode({'address':address})
    print('Retrieving ', url)
    data=urllib.request.urlopen(url).read().decode()
    print('Retrieved ', len(url), 'characters')
    try:
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id=js['results'][0]['place_id']


    print(json.dumps(js, indent=4))
    print('Place id ', place_id)
