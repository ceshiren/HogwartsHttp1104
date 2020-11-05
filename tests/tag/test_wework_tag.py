import pytest

from src.wework_tag import WeworkTag


#todo: 作业：完善todo部分，把自己的代码地址贴到 https://ceshiren.com/t/topic/7681 回复里

class TestWeworkTag:

    def setup_class(self):
        self.tag = WeworkTag()
        r = self.tag.get_token()

        assert r.status_code == 200
        assert self.tag.token

        self.tag.tag_clear()

    def test_tag_list(self):
        r = self.tag.tag_list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # todo: 增加测试用例，中文 英文 数字 特殊字符等等

    @pytest.mark.parametrize('group_name, tag_name', [
        ['hogwarts1105_group_01', 'hogwarts1105_tag_01'],
        ['hogwarts1105_group_abc', 'hogwarts1105_tag_abc'],
        ['hogwarts1105_group_中文', 'hogwarts1105_tag_中文'],
    ])
    def test_tag_add(self, group_name, tag_name):
        # todo: 清理数据的操作放到setup_class里
        # todo: 每次新增数据添加时间戳
        r = self.tag.tag_add(group_name, tag_name)

        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # todo: 判断前台能不能出现新增数据

        r = self.tag.tag_list()

        assert r.status_code == 200

    def test_tag_delete(self):
        group_name = 'hogwarts1105_group_delete'
        tag_name = 'hogwarts1105_tag_delete'
        r = self.tag.tag_add(group_name, tag_name)

        r = self.tag.tag_list()
        group_id = self.tag.tag_search(r, group_name)
        tag_id = None

        r = self.tag.tag_delete(group_id, tag_id)

        assert r.status_code == 200
        assert r.json()['errcode'] == 0
