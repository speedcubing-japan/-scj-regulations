#!/usr/bin/env python
# this script on only PYTHON3
import urllib.request
import urllib.parse
with open('scj-regulations.md', 'br') as file:
    data = file.read()
request = urllib.request.Request('https://api.github.com/markdown/raw')
request.add_header('Content-Type', 'text/plain')
f = urllib.request.urlopen(request, data)
with open('scj_regulations.html', 'bw') as file:
    file.write(f.read())

with open('scj_regulations.html') as file:
    data_lines = file.read()

data_lines = data_lines.replace('h1', 'h4')
data_lines = data_lines.replace('h2', 'h5')

with open('scj_regulations.html', 'w') as file:
    file.write(data_lines)
