#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 25, 2015

@author: freestyle4568
'''
"""
this progarm is to predict matching clothes
"""

import fp_growth
import apriori
import pickle

def load_dataset(catsetfile = None, termfreqfile = None):
    """导入user_catset.txt和user_termset.txt
    
    """
    catlist = []
    termlist = []
    
    if catsetfile != None:
        fr = open(catsetfile)
        for line in fr.readlines():
            catset = line.split()[1]
            catory = catset.split(',')
            new_catory = []
            for i in catory:
                new_catory.append(int(i))
            catlist.append(new_catory)
        print('catlist is:')
        for i in range(10):
            print(catlist[i])
        print('the number of lines :', len(catlist))
        print('-----------------------------------------')
    
    if termfreqfile != None:
        fr2 = open(termfreqfile, 'rb')
        termfreqlist = pickle.load(fr2)
        print('termfreqlist is:')
        for i in range(10):
            print(termfreqlist[i])
        print('the number of lines :', len(termfreqlist))

    print('load dataset finished!')
    print('-----------------------------------------')
    fr.close()
    fr2.close()
    return catlist, termlist

def load_testid2cat(test2catfile):
    fr = open(test2catfile)
    testcategory = []
    for line in fr.readlines():
        test_id = int(line.split()[0])
        testcat_id = int(line.split()[1])
        testcategory.append([test_id, testcat_id])
    print('testcategory is :')
    for i in range(10):
        print(testcategory[i])
    print('load testcategory finished!')
    print('-----------------------------------------')
    return testcategory

def load_item_terms(dim_items_file):
    fr = open(dim_items_file)
    item_terms = {}
    for item in fr.readlines():
        item_id = int(item.split()[0])
        terms = item.split()[2].split(',')
        item_terms[item_id] = terms
    print('item_terms is :')
    i = 0;
    for item in item_terms:
        if i >= 10:
            break
        print(item, item_terms[item])
        i += 1
    print('len of item_terms is:', len(item_terms))
    print('-------------------------------------')
    return item_terms
    
    
def predict_item(one_test, cat_item_dict, item_terms_dict, cat_rule_list, termfreqlist):
    """计算预测与待测商品相匹配的商品，返回由最多200个商品id组成的列表
    
    keyword argument:
    onetestcategory: 待测商品的种类
    cat_item_dict: 种类与商品id的字典
    item_terms_dict: 商品id与分词的字典
    cat_rule_list: 排好序的种类关联集列表
    termfreqlist: 分词频繁集列表
    """
    
    test_term_set = set(item_terms_dict[one_test[0]])
    len_test_term = len(test_term_set)
    test_category = one_test[1]
    
    predict_catory = list(cat_rule_list[0][1])[0]
    result_item = []
    item_grade = {}
    for item in cat_item_dict[predict_catory]:
        item_term_set = set(item_terms_dict[item])
        len_item_term = len(item_term_set)
        for termfreqset in termfreqlist:
            num_test_term_appear = len(test_term_set & termfreqset)
            num_item_term_appear = len(item_term_set & termfreqset)
            if num_item_term_appear != 0 and num_test_term_appear != 0:
                item_grade[item] = (num_item_term_appear/len_item_term) + (num_test_term_appear/len_test_term)
    item_grade_list = sorted(item_grade.items(), key=lambda p: p[1], reverse=True)
    if len(item_grade_list) > 200:
        item_grade_list = item_grade_list[0:200]
    result_item = []
    for item in item_grade_list:
        result_item.append(item[0])
    return result_item
    
    
    

if __name__ == '__main__':
    
    #===========================================================================
    # fp_growth 用法实例
    # dataset = fp_growth.load_simple_data()
    # result_list, support_data = fp_growth.fptree(dataset, 3)
    # print(result_list)
    # print(support_data)
    # print(len(support_data))
    #===========================================================================
    
    min_support = 0.3
    min_confidence = 0.4
    #===========================================================================
    # 建立文件路径
    #===========================================================================
    catsetfile = "/home/freestyle4568/lesson/Clothes-match-txt/user_catset.txt"
    testfile = "/home/freestyle4568/lesson/Clothes-match-txt/test_items.txt"
    termfreqfile = "/home/freestyle4568/lesson/Clothes-match-txt/unrepeat_termfreq.pickle"
    test2catfile = "/home/freestyle4568/lesson/Clothes-match-txt/test_cat.txt"
    
    
    #==========================================================================
    # 导入数据部分,针对test中的每个商品种类，去catlist无用集，得到sub_catlist
    #==========================================================================
    catlist, termfreqlist = load_dataset(catsetfile, termfreqfile)
    test_category = load_testid2cat(test2catfile)
    one_test = test_category[0]
    test_one_category = one_test[1] 
    print("test's category is:", test_one_category)
    sub_catlist = []
    for i in range(len(catlist)):
        if test_one_category in catlist[i]:
            sub_catlist.append(catlist[i])
             
    #===========================================================================
    # 输出sub_catlist 10行
    #===========================================================================
    print('sub_catlist is: ')
    for i in range(10):
        print(sub_catlist[i])
    print('sub_catlist\'s length is : ',len(sub_catlist))
    print('-----------------------------------------')
    #===========================================================================
    # 输出sub_catlist中的频繁项，运用fp_growth算法
    #===========================================================================
    catfreq_list, support_data_cat = fp_growth.fptree(sub_catlist, int(min_support*len(sub_catlist)))
    print('catfreq_list is: ')
    for i in range(len(catfreq_list)):
        print(catfreq_list[i])
    print('-----------------------------------------')
    #===========================================================================
    # for i in support_data.items():
    #     print(i)
    #===========================================================================
    big_rule_list = apriori.generate_rules(catfreq_list[0:2], support_data_cat, min_confidence)
    print('rule list follows: ')
    cat_rule_list = []
    for rule in big_rule_list:
        if test_one_category in rule[0] and len(rule[0]) == 1:
            cat_rule_list.append(rule)
            print(rule) 
    print('-----------------------------------------')
    cat_rule_list.sort(key= lambda p: p[2], reverse=True)
    print('cat_rule_list is :')
    for i in cat_rule_list:
        print(i)
    print('-----------------------------------------')
    
    #===========================================================================
    # 导入cat_item数据，格式为字典
    #===========================================================================
    cat_item_pickle = '/home/freestyle4568/lesson/Clothes-match-txt/cat_items.pickle'
    cat_item_dict = pickle.load(open(cat_item_pickle, 'rb'))
    print('cat_item_dict is :')
    print(cat_item_dict[6])
    print('-------------------------------------------')
    
    #===========================================================================
    # 导入item_terms数据，格式为字典
    #===========================================================================
    dim_items_file = '/home/freestyle4568/lesson/Clothes-match-txt/dim_items.txt'
    item_terms_dict = load_item_terms(dim_items_file)
    
    #===========================================================================
    # 计算结果预测的200个数据
    #===========================================================================
    predict_itemlist = predict_item(one_test, cat_item_dict, item_terms_dict, cat_rule_list, termfreqlist)
    print(predict_itemlist)
    
    
    
    