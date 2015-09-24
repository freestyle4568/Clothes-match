#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on Sep 20, 2015

@author: freestyle4568
'''
"""
this progarm is to test fp-growth algorithm
user guide: result_list, support_data_dict = fptree(dataset, min_support)
该函数返回列表格式的result_list， 元素为列表， [[1元素项集], [2元素项集]]
子列表元素为固定集合 -- frozenset({, , ,})
support_data_dict为字典格式，元素为(frozenset({}): number)
"""
from operator import itemgetter
import apriori

class TreeNode:
    def __init__(self, name_value, num_occur, parent_node):
        self.name = name_value
        self.count = num_occur
        self.nodelink = None
        self.parent = parent_node
        self.children = {}
    
    def inc(self, num_occur):
        self.count += num_occur
    
    def disp(self, index=1):
        print('    '*index, self.name, '  ', self.count)
        for child in self.children.values():
            child.disp(index+1)
        return



def create_tree(dataset, min_support=1):
    header_table = {}
    for trans in dataset:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + dataset[trans]
    tmp_keys = list(header_table.keys())
    for k in tmp_keys:
        if header_table[k] < min_support:
            header_table.pop(k)
    
    freqitem_set = set(header_table.keys())
    if len(freqitem_set) == 0:
        return None, None
    
    for k in header_table:
        header_table[k] = [header_table[k], None]
    
    result_tree = TreeNode('NullNode', 1, None)
    for transaction, count in dataset.items():
        local_data = {}
        for item in transaction:
            if item in freqitem_set:
                local_data[item] = header_table[item][0]
        if len(local_data) > 0:
            ordered_items = [v[0] for v in sorted(local_data.items(), 
                                                  key = itemgetter(1, 0), reverse = True)]
            update_tree(ordered_items, result_tree, header_table, count)
    return result_tree, header_table



def update_tree(items, tree, header_table, count):
    if items[0] in tree.children:
        tree.children[items[0]].inc(count)
    else:
        tree.children[items[0]] = TreeNode(items[0], count, tree)
        if header_table[items[0]][1] == None:
            header_table[items[0]][1] = tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1],
                          tree.children[items[0]])
    if len(items) > 1:
        update_tree(items[1:], tree.children[items[0]], header_table, count)
    return

def update_header(node_to_test, target_node):
    while (node_to_test.nodelink != None):
        node_to_test = node_to_test.nodelink
    node_to_test.nodelink = target_node
    return

def load_simple_data():
    simple_data = [['r', 'z', 'h', 'j', 'p'],
                   ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                   ['z'],
                   ['r', 'x', 'n', 'o', 's'],
                   ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                   ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']
                   ]
    return simple_data

def create_init_set(dataset):
    result_dict = {}
    for d in dataset:
        result_dict[frozenset(d)] = 1
    return result_dict


def ascend_tree(leaf_node, prefix_path):
    if leaf_node.parent != None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)
    return 

def find_prefix_path(tree_node):
    condition_path = {}
    while tree_node != None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            condition_path[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.nodelink
    return condition_path


def mine_tree(tree, header_table, min_support, prefix, freqitem_list, support_list):
    big_list = [v[0] for v in sorted(header_table.items(), key = lambda p: p[1][0])]
    
    for base in big_list:
        new_freq_set = prefix.copy()
        new_freq_set.add(base)
        freqitem_list.append(new_freq_set)
        print(new_freq_set)
        support_list.append(header_table[base][0])
        condition_path = find_prefix_path(header_table[base][1])
        condition_tree, condition_header_table = create_tree(condition_path, min_support)
        
        if condition_header_table != None:
            mine_tree(condition_tree, condition_header_table, min_support, new_freq_set, freqitem_list, support_list)

def resultlist2dict(freqitem_list, support_list):
    result_list = []
    len_result = len(freqitem_list)
    support_data = {}
    max_element_number = 0
    for i in range(len_result):
        support_data.update({frozenset(freqitem_list[i]): support_list[i]})
        if max_element_number < len(freqitem_list[i]):
            max_element_number = len(freqitem_list[i])
    
    for k in range(max_element_number):
        c = []
        tmp_list = freqitem_list.copy()
        for freqset in tmp_list:
            if len(freqset) == k+1:
                c.append(frozenset(freqset))
                freqitem_list.remove(freqset)
        result_list.append(c)
    return result_list, support_data
                


def fptree(dataset, min_support):
    dataset_dict = create_init_set(dataset)
    FPtree, header_table = create_tree(dataset_dict, min_support)
    freqitem_list = []
    support_list = []
    mine_tree(FPtree, header_table, min_support, set([]), freqitem_list, support_list)
    result_list, support_data = resultlist2dict(freqitem_list, support_list)
    return result_list, support_data

if __name__ == '__main__':
    filename = '/home/freestyle4568/lesson/Clothes-match-txt/user_catset.txt'
    fr = open(filename)
    dataset = []
    for line in fr.readlines():
        catset = line.split()[1]
        dataset.append(catset.split(','))
    for i in range(10):
        print(dataset[i])
    dataset = load_simple_data()
    result_list, support_data = fptree(dataset[0:1000], 100)
    for i in result_list:
        print(i)
    print(len(support_data))
    for j in support_data.items():
        print(j)


    
    
    