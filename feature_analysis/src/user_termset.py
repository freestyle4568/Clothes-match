#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 26, 2015

@author: freestyle4568
'''

if __name__ == '__main__':
    useritemfile = '/home/freestyle4568/lesson/Clothes-match-txt/user_bought_history.txt'
    itemfile = '/home/freestyle4568/lesson/Clothes-match-txt/dim_items.txt'
    
    fr1 = open(useritemfile)
    fr2 = open(itemfile)
    
    user_item = {}
    for line in fr1.readlines():
        user_id = int(line.split()[0])        
        item_id = int(line.split()[1])
        if user_id in user_item:
            if item_id not in user_item[user_id]:
                user_item[user_id].append(item_id)
        else:
            user_item[user_id] = [item_id]
    
    item_terms = {}
    for line in fr2.readlines():
        item_id = int(line.split()[0])
        terms = line.split()[2]
        item_terms[item_id] = terms
        
    #===========================================================================
    # print("user_item is :")
    # j = 0
    # for i in user_item.items():
    #     j += 1
    #     print(i)
    #     if j > 10:
    #         break
    # 
    # print("item_terms is :")
    # j = 0
    # for i in item_terms.items():
    #     j += 1
    #     print(i)
    #     if j > 10:
    #         break
    # print(len(item_terms))
    #===========================================================================
    
    usertermsetfile = '/home/freestyle4568/lesson/Clothes-match-txt/user_termset.txt'
    
    fr3 = open(usertermsetfile, 'w')
    for user in user_item:
        termset = set()
        for item in user_item[user]:
            termset = termset | set(item_terms[item].split(','))
        print(user, file=fr3, end=' ')
        for term in termset:
            print(term, file=fr3, end=' ')
        print('', file=fr3)
    fr3.close()
        
        
        
        
        
    
    
    
    