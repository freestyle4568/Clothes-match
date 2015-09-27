#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 27, 2015

@author: freestyle4568
'''

import pickle

def load_termfreq(filename):
    fr = open(filename, 'rb')
    termfreq_list = pickle.load(fr)
    #===========================================================================
    # print('termfreq_list is :')
    # for i in range(5):
    #     print(termfreq_list[i])
    #===========================================================================
    print('len of termfreq is: ', len(termfreq_list))
    return termfreq_list

if __name__ == '__main__':
    termfreq_file = '/home/freestyle4568/lesson/Clothes-match-txt/termfreq_10000.pickle'
    termfreq_list = load_termfreq(termfreq_file)
    
    #===========================================================================
    # 去除重复频繁项集
    #===========================================================================
    unrepeat_termfreq = []
    for i in range(1, len(termfreq_list)-1):
        for freqset in termfreq_list[i]:
            flag = 0
            for bigfreqset in termfreq_list[i+1]:
                if freqset.issubset(bigfreqset) == True:
                    flag = 1
            if flag == 0:
                unrepeat_termfreq.append(freqset)
    unrepeat_termfreq.extend(termfreq_list[-1])
    
    for i in range(40):
        print(unrepeat_termfreq[i])
    
    unrepeat_termfreq_file = '/home/freestyle4568/lesson/Clothes-match-txt/unrepeat_termfreq.pickle'
    fr = open(unrepeat_termfreq_file, 'wb')
    pickle.dump(unrepeat_termfreq, fr)
    fr.close()
    
    