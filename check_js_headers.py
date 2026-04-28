import urllib.request
resp = urllib.request.urlopen('http://localhost:8000/static/js/app.js?v=5')
print('Status:', resp.status)
print('Content-Type:', resp.getheader('Content-Type'))
