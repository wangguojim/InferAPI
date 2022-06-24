import requests

if __name__=='__main__':
    sentense='我们都是中国人'
    response = requests.get('http://127.0.0.1:8000/'+sentense)
    print(response.text)
