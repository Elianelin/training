import urllib.request
resp = urllib.request.urlopen('http://localhost:8000/static/js/app.js?v=5')
js = resp.read().decode('utf-8')
print('Status:', resp.status)
print('Length:', len(js))
print('First 100 chars:', js[:100])
print('Has setupLogin:', 'setupLogin' in js)
print('Has showMainApp:', 'showMainApp' in js)
