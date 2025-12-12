import requests
import json
import time
import subprocess


url = 'https://jsonplaceholder.typicode.com/posts'
now = str(time.time())[:12].replace('.', '')


def logs(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt', 'a') as file:
            file.write(f'\n--{now}-- {func.__name__}')
            result = func(*args, **kwargs)
            file.write(f'\n{result}')
            file.write('\n--finished--')
        return result
    return wrapper


@logs
def get_post(index):
    if type(index) is not int:
        raise TypeError('Index must be int')

    try:
        response = requests.get(f'{url}/{index}')
    except Exception as e:
        return f'Error: {e}'
    else:
        return response.json()


@logs
def save_file(filename, title='', body=''):
    if not title and not body:
        title = input('Type the title')
        body = input('Type the content')
    elif not title and body:
        title = input('Type the title')
    elif not body and title:
        body = input('Type the content')

    payload = {"title": title, "body": body, "userId": 1}

    try:
        file = open(f'{filename}_{now}', 'w')
        file.write(json.dumps(payload, indent=2))
    except Exception as e:
        return f'Error: {e}'
    finally:
        file.close()


@logs
def save_json(filename, get_payload):

    now = str(time.time())[:12].replace('.', '')
    payload = get_payload

    try:
        file = open(f'{filename}_{now}.json', 'w')
        file.write(json.dumps(payload, indent=2))
    except Exception as e:
        return RuntimeError(f'Error: {e}')
    finally:
        file.close()


@logs
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = json.load(file)
    except Exception as e:
        return f'Error: {e}'
    finally:
        file.close()

    return content


@logs
def upload_post(filename):
    try:
        with open(filename, 'r') as file:
            payload = json.load(file)
    except Exception as e:
        raise RuntimeError(f'Error: {e}')

    try:
        res = requests.post(url, json=payload, timeout=10)
    except Exception as e:
        return RuntimeError(f'Error: {e}')

    if not (200 <= res.status_code < 300):
        return RuntimeError(f'Error status code: '
                            f'{res.status_code}, body: {res.text}')
    return res


def search_log(keyword):
    with open('logs.txt', 'r') as f:
        for line in f:
            if keyword in line:
                print(line)


if __name__ == '__main__':
    print(get_post(1))
    save_json('jsonplaceh', get_post(3))
    print(read_file('jsonplaceh_17655012183.json'))
    print(upload_post('post.json'))
    search_log('Error')
    subprocess.run(["python", "--version"])
