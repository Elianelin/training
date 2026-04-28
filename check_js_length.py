import urllib.request
resp = urllib.request.urlopen('http://localhost:8000/static/js/app.js?v=5')
body = resp.read()
print('Status:', resp.status)
print('Content-Length header:', resp.getheader('Content-Length'))
print('Actual body length:', len(body))
print('Last 100 bytes:', body[-100:])
