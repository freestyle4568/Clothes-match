#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 26, 2015

@author: freestyle4568
'''

if __name__ == '__main__':
    filename = "/home/freestyle4568/lesson/Clothes-match-txt/user_termset.txt"
    fr = open(filename)
    i = 0
    for line in fr.readlines():
        print(line)
        i += 1
        if i > 10:
            break
        