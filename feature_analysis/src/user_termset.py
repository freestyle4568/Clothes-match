#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 26, 2015

@author: freestyle4568
'''

import pickle

def loadtestitems(filename):
    """导入待测商品id
    """
    testitems = []
    fr = open(filename)
    for i in fr.readlines():
        testitems.append(int(i))
    
    print("testitems is:")
    for i in range(10):
        print(testitems[i])
    print('len of testitems is:', len(testitems))
    return testitems



if __name__ == '__main__':
    useritemfile = '/home/freestyle4568/lesson/Clothes-match-txt/user_bought_history.txt'
    itemfile = '/home/freestyle4568/lesson/Clothes-match-txt/dim_items.txt'
    testfile = '/home/freestyle4568/lesson/Clothes-match-txt/test_items.txt'
    
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
    
    #===========================================================================
    # test_item = loadtestitems(testfile)
    # one_test = test_item[0]
    # sub_user_item = []
    # for user in user_item:
    #     if one_test in user_item[user]:
    #         sub_user_item.append(user_item[user])
    # 
    # print('len of sub_user_item:', len(sub_user_item))
    #===========================================================================
    
    
    
    
    item_terms = {}
    for line in fr2.readlines():
        item_id = int(line.split()[0])
        terms = line.split()[2]
        item_terms[item_id] = terms
        
    print("user_item is :")
    j = 0
    for i in user_item.items():
        j += 1
        print(i)
        if j > 10:
            break
      
    print("item_terms is :")
    j = 0
    for i in item_terms.items():
        j += 1
        print(i)
        if j > 10:
            break
    print(len(item_terms))
     
    usertermsetfile = '/home/freestyle4568/lesson/Clothes-match-txt/user_termset.txt'

    #===========================================================================
    # fr3 = open(usertermsetfile, 'w')
    # for user in user_item:
    #     termset = set()
    #     for item in user_item[user]:
    #         termset = termset | set(item_terms[item].split(','))
    #     print(user, file=fr3, end=' ')
    #     for term in termset:
    #         print(term, file=fr3, end=' ')
    #     print('', file=fr3)
    # fr3.close()
    #===========================================================================
    
    sub_usertermfile = '/home/freestyle4568/lesson/Clothes-match-txt/sub_user_termset.pickle'
    fr_sub = open(sub_usertermfile, 'wb')  
    sub_usertermlist = []
    num = 0
    for user in user_item:
        if num >= 100000:
            break
        termset = set()
        for item in user_item[user]:
            termset = termset | set(item_terms[item].split(','))
        sub_usertermlist.append(list(termset))
        num += 1
    print('len of sub_usertermlist is: ', len(sub_usertermlist))
    for i in range(10):
        print(sub_usertermlist[i])
    
    pickle.dump(sub_usertermlist, fr_sub)
    fr_sub.close()    
    
    
    
    
        
        
        
        
    
    
    
    