import requests

# Define API URL
url = "http://127.0.0.1:8000/predict"

# Sample Input Data (Use the exact field names from your cURL request)
data = {
    "pclass": 1,
    "age": 29,
    "sibsp": 0,
    "parch": 0,
    "fare": 211.3375,
    "embarked": 2,
    "sex": 1,
    "cabin": 1,
    "ticket": 12345,
    "body": 0,
    "home_dest": 3,
    "boat": 2
}

# Send POST request
response = requests.post(url, json=data)

# Print response from API
print("Response:", response.json())
