from main import get_post, save_file
import json


def test_get_post():
    result = dict(get_post(1))
    test_dict = {
        'userId': 1,
        'id': 1,

        'title': 'sunt aut facere repellat provident '
        'occaecati excepturi optio reprehenderit',

        'body': 'quia et suscipit\nsuscipit recusandae consequuntur'
        ' expedita et cum\nreprehenderit molestiae ut ut quas totam\n'
        'nostrum rerum est autem sunt rem eveniet architecto',
    }

    assert result == test_dict


def test_save_file(tmp_path):
    filename = str(tmp_path/'testingxyz')
    save_file(filename, 'test title', 'test body')

    import glob
    matches = glob.glob(f'{filename}_*')
    assert len(matches) > 0, 'No file'
    with open(f'{matches[0]}', 'r') as f:
        data = json.load(f)
        assert data["title"] == 'test title'
        assert data["body"] == 'test body'
