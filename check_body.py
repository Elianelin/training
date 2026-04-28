import urllib.request, json
req = urllib.request.Request(
    'http://localhost:8000/api/auth/login',
    data=json.dumps({'username':'linxy28','password':'123456'}).encode('utf-8'),
    headers={'Content-Type':'application/json'}
)
resp = urllib.request.urlopen(req)
body = resp.read()
print('Length:', len(body))
print('Body:', body)
print('Decoded:', body.decode('utf-8'))
