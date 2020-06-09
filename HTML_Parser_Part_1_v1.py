#!/usr/bin/env python

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for _attr in attrs:
                print('->' , _attr[0] , '>' , _attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for _attr in attrs:
            print('->' , _attr[0] , '>' ,  _attr[1])

if __name__ == '__main__':
    _n = int(input())
    _html = []
    _result = []
    for _ in range(_n):
        _html.append(input().strip())

    parser = MyHTMLParser()
    parser.feed(''.join(_html).strip())
