import requests


def test_get():
    r = requests.get(
        'https://ceshiren.com/search.json',
        params={'q': '头条'}
    )
    print(r.status_code)
    assert r.status_code == 200
    assert '今日头条' in r.text
