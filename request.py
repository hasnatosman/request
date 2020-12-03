import requests
import os
import webbrowser as wb

url = 'https://github.com/'

response = requests.get(url)

with open('test.html', 'w', encoding=response.encoding) as f:
    f.write(response.text)
file_path = os.path.realpath('test.html')
print(file_path)

wb.open('file://' + file_path)
