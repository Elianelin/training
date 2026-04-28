import urllib.request, json
req = urllib.request.Request(
    'http://localhost:8000/api/auth/login',
    data=json.dumps({'username':'linxy28','password':'123456'}).encode('utf-8'),
    headers={'Content-Type':'application/json'}
)
resp = urllib.request.urlopen(req)
print('Status:', resp.status)
print('Content-Type:', resp.getheader('Content-Type'))
body = resp.read()
print('Body bytes:', body[:200])
print('Body decoded:', body.decode('utf-8')[:200])
