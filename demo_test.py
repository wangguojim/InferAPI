import requests

if __name__=='__main__':
    response = requests.get('http://127.0.0.1:8000')
    print(response.text)
