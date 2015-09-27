#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 27, 2015

@author: freestyle4568
'''


"""
this progarm is to create termfreq_list and transform it to termfreq_***.pickle
"""
import pickle
import fp_growth
import apriori


def load_termlist(termsetfile=None):
    if termsetfile != None:
        fr2 = open(termsetfile, 'rb')
        termlist = pickle.load(fr2)
        print('sub_termlist is:')
        for i in range(10):
            print(termlist[i])
        print('the number of lines :', len(termlist))
    return termsetfile

if __name__ == '__main__':
    
    min_support = 0.3
    sub_termsetfile = "/home/freestyle4568/lesson/Clothes-match-txt/sub_user_termset.pickle"
    
    termlist = load_termlist(sub_termsetfile)
    termfreq_list, support_data_term = fp_growth.fptree(termlist[0:10000], int(min_support*10000))
     
    print('termfreq_list is: ')
    for i in range(len(termfreq_list)):
        print(termfreq_list[i])
    termfreqfile = '/home/freestyle4568/lesson/Clothes-match-txt/termfreq_10000.pickle'
    fr_termfreq = open(termfreqfile, 'wb')
    pickle.dump(termfreq_list, fr_termfreq)
    fr_termfreq.close()

