#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2015

@author: freestyle4568
'''
import pickle
import random

def random_221_itemlist(cat_item_dict):
    len_of_cat = len(cat_item_dict[221])
    item_list = []
    num_item = 0
    item_index_list = []
    while num_item < 200:
        index = random.randint(0, len_of_cat-1)
        while(index in item_index_list):
            index = random.randint(0, len_of_cat-1)
            item_index_list.append(index)
        item_list.append(cat_item_dict[221][index])
        num_item += 1
    #===========================================================================
    # print(item_list)
    # print(len(item_list))
    #===========================================================================
    return item_list
        
        
        
if __name__ == '__main__':
    resultfile1 = '/home/freestyle4568/lesson/Clothes-match-txt/fm_submissions.txt'
    resultfile2 = '/home/freestyle4568/lesson/Clothes-match-txt/fm_submissions2.txt'
    resultfile_end = '/home/freestyle4568/lesson/Clothes-match-txt/fm_submissions_1000.txt'
    cat_item_pickle = '/home/freestyle4568/lesson/Clothes-match-txt/cat_items.pickle'
    test_item_file = '/home/freestyle4568/lesson/Clothes-match-txt/test_items.txt'
    fr = open(test_item_file, 'r')
    test_item = []
    for line in fr.readlines():
        test_item.append(int(line.split()[0]))
    
    for i in range(10):
        print(test_item[i])
    
    
    
    cat_item_dict = pickle.load(open(cat_item_pickle, 'rb'))    
    fr1 = open(resultfile1)
    fr2 = open(resultfile2)
    fail_test = []
    result_list = {}
    for line in fr1.readlines():
        if (len(line.split()) == 1):
            fail_test.append(int(line.split()[0]))
            result_list[int(line.split()[0])] = random_221_itemlist(cat_item_dict)
        else:
            result_list[int(line.split()[0])] = line.split()[1].split(',')
    
    
    for line in fr2.readlines():
        if (len(line.split()) == 1):
            fail_test.append(int(line.split()[0]))
            result_list[int(line.split()[0])] = random_221_itemlist(cat_item_dict)
        else:
            result_list[int(line.split()[0])] = line.split()[1].split(',')
    
    
    print('len of result is:', len(result_list))
    fr_end = open(resultfile_end, 'w')
    for test_id in test_item:
        print(test_id)
        print(test_id, end='', file=fr_end)
        print(' ', end='', file=fr_end)
        print(','.join([str(x) for x in result_list[test_id]]), file=fr_end)

    
    