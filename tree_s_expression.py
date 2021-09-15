#!/usr/bin/env python

def branch_search(pair, pair_lst,branch=''):
    pair_lst.remove(pair)
    #print(pair[0])
    branch += '(' + pair[0]
    for i in range(len(pair_lst)):
        if pair_lst[i][0] == pair[1]:
            return branch_search(pair_lst[i], pair_lst,branch)
    branch += '(' + pair[1]
    return branch

def build_tree(root, branch):
    if root == '':
        return branch
    if not branch[1] in root:
        print('E4')
        exit(0)
    for s in branch[2:]:
        if s != '(' and s != ')' and s in root:
            print('E3')
            exit(0)
    _idx = root.index(branch[1])
    _o = 0
    _c = 0
    while _o == 0 or _c == 0 or _o != _c:
        _idx += 1
        if root[_idx] == '(':
            _o += 1
        elif root[_idx] == ')':
            _c += 1
    root = root[:_idx+1] + branch[2:-1] + root[_idx+1:]

    return root


if __name__ == '__main__':
    pairs = input()
    try:
        pair_lst = [ [p[1],p[3]] for p in pairs.split() ] 
    except:
        print('E5')
    r_dict = {}
    pair_lst.sort()
    root = ''
    while pair_lst:
        pair = pair_lst[0]
        if pairs.count('(' + pair[0] + ',' + pair[1] + ')') > 1:
            print('E2')
            exit(0)
        if pairs.count('(' + pair[0] + ',') > 2:
            print('E1')
            exit(0)
        pair = pair_lst[0]
        branch = branch_search(pair, pair_lst)
        branch += ')' * (len(branch) // 2)
        #print(branch)
        root = build_tree(root,branch)

    print(root)

