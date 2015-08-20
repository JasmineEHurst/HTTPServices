import urllib

# Base URL being accessed
url = 'http://google.com'

# Make a GET request and read the response
response = urllib.urlopen(url)
html = response.read()
print html