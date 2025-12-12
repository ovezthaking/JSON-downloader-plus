import requests
import json
import time


url = 'https://jsonplaceholder.typicode.com/posts'


def get_post(index):
    if type(index) is not int:
        raise TypeError('Index must be int')

    try:
        response = requests.get(f'{url}/{index}')
    except Exception as e:
        return f'Error: {e}'
    else:
        return response.json()


def save_file(filename, title='', body=''):
    if not title and not body:
        title = input('Type the title')
        body = input('Type the content')
    elif not title and body:
        title = input('Type the title')
    elif not body and title:
        body = input('Type the content')

    now = str(time.time())[:12].replace('.', '')
    payload = {"title": title, "body": body, "userId": 1}

    try:
        file = open(f'{filename}_{now}', 'w')
        file.write(json.dumps(payload, indent=2))
    except Exception as e:
        return f'Error: {e}'
    finally:
        file.close()


def save_json(filename, get_payload):

    now = str(time.time())[:12].replace('.', '')
    payload = get_payload

    try:
        file = open(f'{filename}_{now}.json', 'w')
        file.write(json.dumps(payload, indent=2))
    except Exception as e:
        return f'Error: {e}'
    finally:
        file.close()


def read_post(filename):
    try:
        file = open(filename, 'r')
        file.read()
    except Exception as e:
        raise f'Error: {e}'
    finally:
        file.close()

    return file.read()


def create_post(filename):
    requests.post()


if __name__ == '__main__':
    print(get_post(2))
    save_json('jsonplaceh', get_post(3))
