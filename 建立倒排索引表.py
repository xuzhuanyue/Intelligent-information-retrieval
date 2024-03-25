import os
def is_ok(word):#筛选长度大于等于2的汉字词语
    if len(word)<2:
        return False
    for ch in word:
        if ch<'\u4e00' or ch>'\u9fff':
            return False
    return True
path1='#输入path'
for dirpath,dirnames,files in os.walk(path1):#遍历老师给出的所有文档
    for i in range(0,len(files)):
        path2=path1+'\\'+files[i]
        lst1=[]#统计所有出现的词项
        dic1={}#建立词项与出现的次数的哈希映射
        with open(path2,'r',errors='ignore') as f1:
            for c in list(f1.read().split()):
                if is_ok(c):
                    if c not in lst1:#如果还没被扫描过
                        lst1.append(c)
                        dic1[c]=1
                    else:#扫描过了，次数加一
                        dic1[c]=dic1[c]+1
        path3='#输出path'+str(i)+'.txt'
        with open(path3,'x') as f2:
            for l in lst1:
                f2.write(l+' '+str(dic1[l])+' '+str(i+1))#依次写入词项，出现的次数，文档名
                f2.write('\n')



