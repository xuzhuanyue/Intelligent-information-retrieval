import os
import time
import math
dic1={}#dic1为词项与包含词项的文件名的哈希映射，键值为所有词项
dic2={}#dic2为1-532与老师给出的已分词的文件名的映射，方便之后对这些文件名按照老师给出的顺序打印进入txt文件
dic3={}#词项与idf值之间的哈希映射
my_list=[]
def import_InvertedFile():
    path='C:\\Users\\Xu Zhuanyue\\Desktop\\倒排索引表\\InvertedFile.txt'
    with open(path,'r') as f:#读入已经建好的倒排索引表，倒排索引表每一行按如下格式存储：词项 df 包含词项的文件
        for line in f.readlines():#读入倒排索引表的每一行
            lst=list(line.split())
            dic1[lst[0]]=[]#lst[0]为词项，lst[2]之后的元素为包含词项的文件名
            for i in range(2,len(lst)):
                dic1[lst[0]].append(lst[i])#建立词项与包含关键词文件的文件名的哈希映射
            idf=math.log(532/int(lst[1]),10)#计算每个词项的idf值
            dic3[lst[0]]=idf#建立词项与idf值之间的哈希映射
    #file_txt为老师给出的已分词的txt文件保存的绝对路径
    with open("C:\\Users\\Xu Zhuanyue\\Desktop\\file_list.txt",'r') as f:
        lst=f.readlines()
        for i in range(1,len(lst)+1):
            dic2[i]=lst[i-1]
    for i in range(0,532):
        dic4={}
        path='C:\\Users\\Xu Zhuanyue\\Desktop\\余弦长度归一化值\\'+str(i)+'.txt'
        with open(path,'r') as f:
            for line in f.readlines():
                lst3=list(line.split())
                dic4[lst3[0]]=float(lst3[1])
        my_list.append(dic4)
#输出提示信息
def menu():
    print("欢迎使用简易布尔检索系统")
    print("请输入对应的数字选择所需的检索")
    print("[1]AND查询")
    print("[2]OR查询")
    print("其他数字退出系统")
#进行只有and连接的查询
def and_search():
    dic4={}#查询词项的tf-weight值的哈希映射
    dic5={}#查询词项的weight值的哈希映射
    dic7={}#文档与文档得分的哈希映射
    print("请输入查询的关键词（用AND连接）")
    s=input().replace(' ','')#去除用户输入可能多输的空格
    start_time=time.time()#用户输入结束，计时开始
    try:
        lst1=list(s.split("AND"))#以AND分割词项
        r=list(set(dic1[lst1[0]]).intersection(dic1[lst1[1]]))#包含词项1和词项2的文件名列表求交集
        if len(lst1)>2:#如果查询超过两个词项
            for i in range(2,len(lst1)):
                r=list(set(r).intersection(dic1[lst1[i]]))#对包含剩下词项的文件名列表求交集
        lst2=list(set(lst1))
        #统计查询词项的tf-row值
        for l1 in lst2:
            for l2 in lst1:
                if l1==l2:
                    if l1 not in dic4.keys():
                        dic4[l1]=1
                    else:
                        dic4[l1]=dic4[l1]+1
        #由tf-row值计算得到tf-weight值
        for k in dic4.keys():
            dic4[k]=1+math.log(dic4[k],10)
        #计算查询词项的weight值
        for k in dic4.keys():
            dic5[k]=dic4[k]*dic3[k]
        #计算每个文档的余弦长度归一化值
        for i in r:
            i=int(i)
            n=0
            for k in dic5.keys():
                n=n+dic5[k]*my_list[i-1][k]
            dic7[i]=n
        #将文档得分按降序排列
        dic7SortList=sorted(dic7.items(),key=lambda x:x[1],reverse=True)
        end_time=time.time()#找到所有文档，计时结束
        print("共找到"+str(len(r))+"篇文档")
        print("程序运行时间：%.6f毫秒\n"%((end_time-start_time)*1000))
        with open("QueryResults.txt",'w') as f:#将结果写入txt文件    
            for l in dic7SortList:
                l=list(l)
                f.write(dic2[l[0]])
    except:
        print("输入错误！输出的词项不在语料库中！请重新输入...")
#进行只有or连接的查询
def or_search():
    dic4={}#查询词项的tf-weight值的哈希映射
    dic5={}#查询词项的weight值的哈希映射
    dic7={}#文档与文档得分的哈希映射
    print("请输入查询的关键词（用OR连接）")
    s=input().replace(' ','')#去除用户输入可能多输的空格
    start_time=time.time()#用户输入结束，计时开始
    try:
        lst1=list(s.split("OR"))#以OR分割词项
        for l in lst1:#判断词项是否在语料库中
            if l not in dic1.keys():
                print("输入的词项不在语料库中，输入错误！系统退出...")
        r=list(set(dic1[lst1[0]]).union(dic1[lst1[1]]))#包含词项1和词项2的文件名列表求并集
        if len(lst1)>2:#如果查询超过两个词项
            for i in range(2,len(lst1)):
                r=list(set(r).union(dic1[lst1[i]]))#对包含剩下词项的文件名列表求并集
        lst2=list(set(lst1))
        #统计查询词项的tf-row值
        for l1 in lst2:
            for l2 in lst1:
                if l1==l2:
                    if l1 not in dic4.keys():
                        dic4[l1]=1
                    else:
                        dic4[l1]=dic4[l1]+1
        #由tf-row值计算得到tf-weight值
        for k in dic4.keys():
            dic4[k]=1+math.log(dic4[k],10)
        #计算查询词项的weight值
        for k in dic4.keys():
            dic5[k]=dic4[k]*dic3[k]
        #计算每个文档的余弦长度归一化值
        for i in r:
            i=int(i)
            n=0
            for k in dic5.keys():
                if k in my_list[i-1].keys():
                    n=n+dic5[k]*my_list[i-1][k]
            dic7[i]=n
        #将文档得分按降序排列
        dic7SortList=sorted(dic7.items(),key=lambda x:x[1],reverse=True)
        end_time=time.time()#找到所有文档，计时结束
        print("共找到"+str(len(r))+"篇文档")
        print("程序运行时间：%.6f毫秒\n"%((end_time-start_time)*1000))
        with open('result' + i + '.txt', 'w') as f:#将结果写入txt文件
            for l in dic7SortList:
                l=list(l)
                f.write(dic2[l[0]])
    except:
        print("输入错误！输出的词项不在语料库中！请重新输入...")
import_InvertedFile()#导入倒排索引表
#用户可一直查询，直至选择退出
while True:
    menu()
    n=input()
    if n=='1':
        and_search()
    elif n=='2':
        or_search()
    else:
        break 