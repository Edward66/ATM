import os
import re
from settings.settings import BASE_DIR


def water_consumption(username):
    info = {}
    count = 0
    re_pattern = re.compile('(?P<date>^2{1}\d{3}-{1}\d{2}-\d{2})(?P<useless>.+\s)(?P<message>您.+元$)')
    try:
        with open(os.path.join(BASE_DIR, 'log/%s_consume.log' % username), 'r', encoding='utf-8') as f:
            for line in f:
                for match in re.finditer(re_pattern, line):
                    match_text = match.groupdict()
                    print("\033[31m{0}  {1}\033[0m".format(match_text['date'], match_text['message']))
    except FileNotFoundError:
        print('数据库出错或数据不存在，请稍后再试，show_consume')
