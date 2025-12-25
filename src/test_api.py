import requests

base_url = "https://api.waqi.info/feed"
Token = "400745d035f6815c76fce78f4623e967b58f4d58"
City = 'delhi'

def test_requests():
    url = f"{base_url}/{City}/?token={Token}"
    print("Requesting url: ",url)

    response = requests.get(url)
    print("Status code: ",response.status_code)

    data = response.json()
    print(data)

if __name__ = __main__:
    test_requests()