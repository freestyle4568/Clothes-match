#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 27, 2015

@author: freestyle4568
'''

import pickle
if __name__ == '__main__':
    dim_item_file = '/home/freestyle4568/lesson/Clothes-match-txt/dim_items.txt'
    cat_items = {}
    fr = open(dim_item_file)
    for line in fr.readlines():
        item_id = int(line.split()[0])
        category = int(line.split()[1])
        if category in cat_items:
            cat_items[category].append(item_id)
        else:
            cat_items[category] = [item_id]
    print(cat_items[486])
    
    cat_items_pickle = '/home/freestyle4568/lesson/Clothes-match-txt/cat_items.pickle'
    fr = open(cat_items_pickle, 'wb')
    pickle.dump(cat_items, fr)
    fr.close()
     
   