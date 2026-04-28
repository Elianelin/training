import urllib.request
resp = urllib.request.urlopen('http://localhost:8000/')
html = resp.read().decode('utf-8')
for line in html.split('\n'):
    if 'app.js' in line:
        print('Script tag:', line.strip())
        break
