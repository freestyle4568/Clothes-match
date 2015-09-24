#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on Sep 17, 2015

@author: freestyle4568
'''
"""
this progarm is to create Apriori algorithm.
"""
def load_dataset():
    """创建测试数据集，返回列表形式的数据集
    
    keyword argument:
    None
    """
    return [[0, 1, 3]]
#sdfas鼎折覆餗
def create_c1(dataset):
    """根据dataset，创建一元素项集集合，返回列表形式的一元项集集合
    
    从dataset中扫描每个元素，将每个不重复元素以不动集的形式加入c1列表中
    keyword argument:
    dataset -- 列表形式的数据集
    """
    
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    #print(c1)
    c1 = [x for x in map(frozenset, c1)]
    return c1

def support_of_ck(dataset, ck, min_support):
    """扫描数据集，找出所给k元素项集集合的支持率，返回大于最小支持率的k元素项集组成的列表和所有项集对应的支持率列表
    
    keyword argument:
    dataset -- 列表形式的数据集
    ck -- k元素项集集合（列表形式）
    min_support -- 最小支持率
    """
    num_items = len(dataset)
    dataset = map(set, dataset)
    ksetcount = {}   #k元素项集的频率字典 字典元素（frozenset(): count）
    for transaction in dataset:
        for kset in ck:
            if kset.issubset(transaction):
                if kset in ksetcount:
                    ksetcount[kset] += 1
                else:
                    ksetcount[kset] = 1
    kset_list = []
    support_data = {}
    for key, counts in ksetcount.items():
        support = counts / num_items
        if support >= min_support:
            kset_list.append(key)
        support_data[key] = support
    return kset_list, support_data

def create_ck(kset_list, k):
    """产生k元素的项集，返回列表形式的项集集合
    
    取（k-1）元素项集集合中两项，合并成k元素项集集合
    keyword argument:
    kset_list -- 列表形式的k-1元素项集集合
    k -- 元素个数
    """

    result_list = []
    lenlist = len(kset_list)
    for i in range(lenlist):
        for j in range(i+1, lenlist):
            list1 = list(kset_list[i])[:k-2]
            list2 = list(kset_list[j])[:k-2]
            list1.sort(); list2.sort()
            if list1 == list2:
                result_list.append(kset_list[i] | kset_list[j])
    return result_list


def apriori(dataset, min_support = 0.5):
    """找出在数据集中支持率大于50%的项集集合，返回各元素项集的集合,形如[[1元素项集集合]， [2元素项集集合]， [3元素项集集合]，...]，和项集字典
    
    从c1开始，产生ck，组成集合
    keyword argument
    dataset -- 列表的数据集
    min_support -- 指定最低支持率
    """
    c1 = create_c1(dataset)
    set1_list, support_data = support_of_ck(dataset, c1, min_support)
    result_list = [set1_list]
    k = 2
    while (len(result_list[k-2]) > 0):
        ck = create_ck(result_list[k-2], k)
        kset_list, ksup_data = support_of_ck(dataset, ck, min_support)
        support_data.update(ksup_data)
        result_list.append(kset_list)
        k += 1
    return result_list, support_data 

def calculate_confidence(freq_set, H, support_data, big_rule_list, min_confidence=0.7):
    """计算针对后项集H的各个可信率，返回可信率大于最低可信率的后项集
    
    keyword argument:
    freq_set -- 固定字典形式的k项集
    H -- 后项集，格式为列表形式，元素为固定字典
    support_data -- 频繁项集的支持率字典
    big_rule_list -- 总的关联集合，以列表形式出现，元素为元组
    min_confidence -- 最小可信率
    """
    qualified_H = []
    for conseq in H:
        confidence = support_data[freq_set] / support_data[freq_set - conseq]
        if confidence >= min_confidence:
            print(freq_set - conseq, '-->', conseq, '  confidence:', confidence)
            qualified_H.append(conseq)
            big_rule_list.append((freq_set - conseq, conseq, confidence))
    return qualified_H
    
def rules_from_conseq(freq_set, H, support_data, big_rule_list, min_confidence=0.7):
    """对于一个k元素项集，打印所有符合要求的关联项，构建关联项集列表，无返回项
    
    对于一个K元素项集，找到所有一元后项集合，然后找出符合要求的关联项，然后递归调用自己，直到后项集合元素<=1，或者后项大小>=（项集大小-1），
    则退出递归，构建总的关联集合
    keyword argument:
    freq_set -- 固定字典形式的k项集
    H -- 后项集，格式为列表形式，元素为固定字典
    support_data -- 频繁项集的支持率字典
    big_rule_list -- 总的关联集合，以列表形式出现，元素为元组
    min_confidence -- 最小可信率
    """
    
    m = len(H[0])
    if (len(freq_set) > (m + 1)):
        Hmp1 = create_ck(H, m+1)
        Hmp1 = calculate_confidence(freq_set, Hmp1, support_data, big_rule_list, min_confidence)
        if (len(Hmp1) > 1):
            rules_from_conseq(freq_set, Hmp1, support_data, big_rule_list, min_confidence)
    return


def generate_rules(set_list, support_data, min_confidence=0.7):
    """产生各项集的关联规则，返回总的关联集合，以列表形式返回，元素为元组
    
    keyword argument:
    set_list -- 符合支持率的各元素项集集合
    support_data -- 频繁项集的支持率字典
    big_rule_list -- 总的关联集合，以列表形式出现，元素为元组
    min_confidence -- 最小可信率
    """
    big_rule_list = []
    for i in range(1, len(set_list)):
        for freq_set in set_list[i]:
            H = [frozenset([item]) for item in freq_set]
            if (i > 1):
                calculate_confidence(freq_set, H, support_data, big_rule_list, min_confidence)
                rules_from_conseq(freq_set, H, support_data, big_rule_list, min_confidence)
            else:
                calculate_confidence(freq_set, H, support_data, big_rule_list, min_confidence)
    return big_rule_list

    

if __name__ == '__main__':
 #   filename = '/home/freestyle4568/lesson/machineLearning/machinelearninginaction/Ch11/mushroom.dat'
 #   fr = open(filename)
 #   mush_dataset = [lines.split() for lines in fr.readlines()] dataset = load_dataset()
    dataset = load_dataset()
    kset_list, support_data = apriori(dataset, 1)
    big_rule_list = generate_rules(kset_list, support_data, 1)
    for i in big_rule_list:
        print(i)
    #print(big_rule_list[2])
    #dataset = load_dataset()
    #result_list, support_data = apriori(dataset, 1/3)
    #for i in result_list:
    #    print(i)
    #ck = create_ck([frozenset([0, 1]),frozenset([0, 2]),frozenset([1, 3])], 3)
    #print(ck)
    

    
    
    
    
    
    
    
    
    