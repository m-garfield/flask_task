import requests
import json

data = {'user': 'Jack', 'headers': 'Welcom', 'text': 'Welcome Jack'}
headers = {'Content-Type': 'application/json'}
# response = requests.post('http://localhost:5000/message', data=json.dumps(data), headers=headers)
# response = requests.get('http://localhost:5000/message')
response = requests.delete('http://localhost:5000/message/4')

print(response.status_code)
print(response.text)
