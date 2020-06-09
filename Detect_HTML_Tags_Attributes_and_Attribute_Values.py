#!/usr/bin/env python

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for _attr in attrs:
                print('->' , _attr[0] , '>' , _attr[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for _attr in attrs:
            print('->' , _attr[0] , '>' ,  _attr[1])

if __name__ == '__main__':
    _n = int(input())
    _html = '' 
    for _ in range(_n):
        _html += input()

    parser = MyHTMLParser()
    parser.feed(_html)
