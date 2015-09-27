#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 27, 2015

@author: freestyle4568
'''

import csv
import pickle
if __name__ == '__main__':
    cat_items_file = '/home/freestyle4568/lesson/Clothes-match-txt/cat_items.csv'
    cat_items_csv = csv.reader(open(cat_items_file), delimiter=';')
    cat_items = {}
    for onelist in cat_items_csv:
        if onelist[0] != 'cat_id':
            category = int(onelist[0])
            item_list = onelist[1].split(',')
            new_item_list = []
            for i in range(len(item_list)):
                if item_list[i] != '':
                    new_item_list.append(int(item_list[i]))
                    cat_items[category] = new_item_list
    
    print(cat_items[6])
    
    cat_items_pickle = '/home/freestyle4568/lesson/Clothes-match-txt/cat_items.pickle'
    fr = open(cat_items_pickle, 'wb')
    pickle.dump(cat_items, fr)
    fr.close()
     
   