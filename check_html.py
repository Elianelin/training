import urllib.request
resp = urllib.request.urlopen('http://localhost:8000/')
html = resp.read().decode('utf-8')
print('Status:', resp.status)
print('Length:', len(html))
for el in ['login-page', 'main-app', 'login-form', 'login-username', 'login-password']:
    if f'id="{el}"' in html:
        print(f'OK: {el} found')
    else:
        print(f'ERROR: {el} NOT found')
