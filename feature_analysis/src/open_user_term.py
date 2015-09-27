#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 26, 2015

@author: freestyle4568
'''

import pickle

if __name__ == '__main__':
    #===========================================================================
    # filename = "/home/freestyle4568/lesson/Clothes-match-txt/user_termset.txt"
    # fr = open(filename)
    # i = 0
    # for line in fr.readlines():
    #     print(line)
    #     i += 1
    #     if i > 10:
    #         break
    #===========================================================================
    sub_usertermfile = '/home/freestyle4568/lesson/Clothes-match-txt/sub_user_termset.pickle'
    fr_sub = open(sub_usertermfile, 'rb')
    sub_usertermlist = pickle.load(fr_sub)
    for i in range(10):
        print(sub_usertermlist[i])
    print(len(sub_usertermlist))
    fr_sub.close()