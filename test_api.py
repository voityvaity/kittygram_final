#!/usr/bin/env python3
import requests
import json

def test_api():
    url = "http://localhost:8000/api/users/"
    data = {
        'username': 'newuser',
        'password': ''
    }
    
    try:
        response = requests.post(url, data=data, timeout=15)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Content: {response.text}")
        
        # Проверяем, является ли ответ JSON
        try:
            json_data = response.json()
            print(f"JSON Data: {json_data}")
            return True
        except json.JSONDecodeError:
            print("Response is not valid JSON")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

if __name__ == "__main__":
    test_api()
