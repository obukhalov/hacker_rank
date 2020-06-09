#!/usr/bin/env python

if __name__ == '__main__':
    
    K = int(input())
    room_list = input().split()

    _counter_dict = {}
    for room in room_list:
        if _counter_dict.get(room):
            _counter_dict[room] += 1
        else:
            _counter_dict[room] = 1

    for i in _counter_dict.items():
        if i[1] != K:
            print(i[0])
            break
        
