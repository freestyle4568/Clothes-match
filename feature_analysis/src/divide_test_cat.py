#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2015

@author: freestyle4568
'''
import predict_clothes

if __name__ == '__main__':
    test_cat_file = '/home/freestyle4568/lesson/Clothes-match-txt/test_cat.txt'
    
    test_cat = predict_clothes.load_testid2cat(test_cat_file)
    
    test_cat.sort(key= lambda p: p[1], reverse=False)
    
    len_of_test_cat = len(test_cat)
    
    test_cat_file1 = '/home/freestyle4568/lesson/Clothes-match-txt/test_cat1.txt'
    test_cat_file2 = '/home/freestyle4568/lesson/Clothes-match-txt/test_cat2.txt'
    fr1 = open(test_cat_file1, 'w')
    fr2 = open(test_cat_file2, 'w')
     
    for index in range(len_of_test_cat):
        if index <= len_of_test_cat//2:
            print(test_cat[index][0], ' ', test_cat[index][1], file=fr1)
        else:
            print(test_cat[index][0], ' ', test_cat[index][1], file=fr2)
    
    
    