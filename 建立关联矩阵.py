dic1={}#建立词项与出现的该词的文档名的哈希映射
lst1=[]#包含所有的词项
for i in range(0,532):#处理所有的词项文档的关联矩阵文档
    path1=''+str(i)+'.txt'
    with open(path1,'r',errors='ignore') as f1:
        for l in f1.readlines():
            lst2=list(l.split())
            x=lst2[0]#词项
            y=lst2[2]#文档名
            if x not in lst1:#词项未被统计过，先建立哈希映射
                lst1.append(x)
                dic1[x]=[]
                dic1[x].append(y)
            else:#词项已经统计过了，加入该哈希映射中
                dic1[x].append(y)
path='InvertedFile.txt'
with open(path,'w') as f2:#写入倒排索引表中，格式为词项 df 出现该词的文档名
    for k in dic1.keys():
        f2.write(k+' '+str(len(dic1[k]))+' ')
        for c in dic1[k]:
            f2.write(c+' ')
        f2.write('\n') 
            
