import requests

url = 'http://127.0.0.1:5000/ask'
data = {
    'question': 'What is the capital of France?',
    'context': 'Paris is the capital of France. London is the capital of the United Kingdom.'
}

response = requests.post(url, json=data)
print(response.json())
