import requests
import json


url = 'htstps://jsonplaceholder.typicode.com/posts'


def get_post(index):
    if type(index) is not int:
        raise TypeError('Index must be int')

    try:
        response = requests.get(f'{url}/{index}')
    except Exception as e:
        return f'Error: {e}'
    else:
        return response.json()


def save_json(title='', body=''):
    title = input('Type the title')
    body = input('Type the content')

    payload = {"title": title, "body": body, "userId": 1}

    try:
        file = open('post.json', 'w')
        file.write(json.dumps(payload, indent=2))
    except Exception as e:
        return f'Error: {e}'
    finally:
        file.close()


def create_post(u_file):
    
    requests.post()


print(get_post(2))

save_json()
