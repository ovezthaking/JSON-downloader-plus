import requests


def get_post(index):
    if type(index) is not int:
        raise TypeError('Index must be int')

    url = f'htstps://jsonplaceholder.typicode.com/posts/{index}'
    try:
        response = requests.get(url)
    except Exception as e:
        return f'Error: {e}'
    else:
        return response.json()


def create_post(title, body):
    requests.post()


print(get_post(2))
