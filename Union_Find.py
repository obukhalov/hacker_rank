#!/usr/bin/env python


if __name__ == '__main__':
    _comb_weight_lst = [[20, [1, 2]], [30, [2, 3]], [40, [3, 4]], [50, [1, 3]], [60, [4, 5]], [70, [1, 4]], [90, [1, 5]]]
    g_nodes = 5

    _node_sets = [[i] for i in range(1,g_nodes+1)]
    print(_node_sets)

    for _comb in _comb_weight_lst:
        for i in range(len(_node_sets)):
            if _comb[1][0] in _node_sets[i]:
                _va = i
            if _comb[1][1] in _node_sets[i]:
                _vb = i
        if _va == _vb:
            print('Edge: {}-{} makes loop'.format(_comb[1][0],_comb[1][1]))
        else:
            _va_set = _node_sets[_va] 
            _vb_set = _node_sets[_vb]
            _node_sets.remove(_va_set)
            _node_sets.remove(_vb_set)
            _union = _va_set + _vb_set
            _node_sets.append(_union)



