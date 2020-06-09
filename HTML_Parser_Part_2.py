#!/usr/bin/env python

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split('\n')) > 1:
            print('>>> Multi-line Comment')
            for i in range(len(data.split('\n'))):
                print(data.split('\n')[i])
        else:
            print('>>> Single-line Comment')
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            for i in range(len(data.split('\n'))):
                print(data.split('\n')[i])

if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
