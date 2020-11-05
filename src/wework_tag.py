import json

import requests


def pretty(r):
    print(json.dumps(r.json(), indent=4, ensure_ascii=False))


class WeworkTag:
    data = {
        'corpid': 'wwd6da61649bd66fea',
        'corpsecret': 'heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU'
    }

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': self.data['corpid'], 'corpsecret': self.data['corpsecret']}
        )
        self.token = r.json()['access_token']
        pretty(r)
        return r

    def tag_list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token}
        )
        pretty(r)
        return r

    def tag_search(self, r, group_name):
        res = [group['group_id'] for group in r.json()['tag_group'] if group['group_name'] == group_name]
        return res[0]

        # for group in r.json()['tag_group']:
        #     if group['group_name'] == group_name:
        #         return group['group_id']

    def tag_add(self, group_name, tag_name=None):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                "group_name": group_name,
                "tag": [
                    {
                        "name": tag_name,
                    }
                ]
            }

        )
        pretty(r)
        return r

    def tag_delete(self, group_id, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={
                "tag_id": [
                    tag_id
                ],
                "group_id": [
                    group_id
                ]
            }

        )
        pretty(r)
        return r

    def tag_clear(self):
        r = self.tag_list()
        for group in r.json()['tag_group']:
            self.tag_delete(group['group_id'], None)
