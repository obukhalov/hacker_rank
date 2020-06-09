#!/usr/bin/env python

if __name__ == '__main__':
    N, M = map(int,input().split())
    count = 1

    for i in range(N):
        if i < N // 2:
            print(('.|.' * count).center(M, '-'))
            count += 2
        elif i == N // 2:
            count -= 2
            print('WELCOME'.center(M, '-'))
        elif i > N // 2:
            print(('.|.' * count).center(M, '-'))
            count -= 2
