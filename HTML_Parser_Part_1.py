#!/usr/bin/env python

import re

def _get_attr(_info):
    if _info and '=' in _info:
        for _attributes in re.split('''([\w-]+=['"](?:.*?)['"])''', _info):
            if not _attributes:
                continue
            if _attributes.replace(' ', '') == '':
                continue
            if '=' in _attributes:
                _result.append('-> ' + re.search('([\w-]+)=(.*)', _attributes).group(1) + ' > ' + re.search('([\w-]+)=(.*)', _attributes).group(2).replace("'",'').replace('"', ''))
            else:
                for _att in _attributes.split():
                    _result.append('-> ' + _att + ' > ' + 'None')
    elif _info and not '=' in _info:
        for _attributes in re.split('\s+', _info):
            if not _attributes:
                continue
            if _attributes.replace(' ', '') == '':
                continue
            _result.append('-> ' + _attributes + ' > ' + 'None')

if __name__ == '__main__':
    _n = int(input())
    _html = []
    _result = []
    for _ in range(_n):
        _html.append(input())

    _input = ''.join(_html)
    _input_without_comments = ''.join(re.split('<!--.*?-->', _input, re.DOTALL))
    _tags = re.findall('(<.*?>)', _input_without_comments, re.DOTALL)
    if _tags:
        for _tag in _tags:
            match = re.search('<([a-zA-Z0-9]+)>', _tag)
            if match:
                _result.append('Start : ' + match.group(1))
            match = re.search('</([a-zA-Z0-9]+)>', _tag)
            if match:
                _result.append('End   : ' + match.group(1))

            if _tag[-2:] != '/>':
                match = re.search('<([a-zA-Z0-9]+)\s+(.*)>', _tag)
                if match:
                    _result.append('Start : ' + match.group(1))
                    _get_attr(match.group(2))
            else:
                match = re.search('<([a-zA-Z0-9]+)\s+(.*)/>', _tag)
                if match:
                    _result.append('Empty : ' + match.group(1))
                    _get_attr(match.group(2))

    print(*_result, sep='\n')
