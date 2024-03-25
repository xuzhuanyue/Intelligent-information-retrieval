#计算每个文档的余弦长度归一化值
import math
for i in range(0,532):
    dic={}#建立词项和余弦长度归一化的哈希映射
    path='词项文档的关联矩阵\\'+str(i)+'.txt'
    with open(path,'r') as f:
        for line in f.readlines():
                lst=list(line.split())
                dic[lst[0]]=int(lst[1])
        #计算文档词项的weight值
        for k in dic.keys():
            dic[k]=1+math.log(dic[k],10)
        #计算余弦归一化值
        n_lized=0
        for k in dic.keys():
            n_lized=n_lized+dic[k]*dic[k]
        n_lized=math.sqrt(n_lized)
        for k in dic.keys():
            dic[k]=dic[k]/n_lized
    path='\\余弦长度归一化值\\'+str(i)+'.txt'
    with open(path,'x') as f:#每个文档都建立余弦归一化值
        for k in dic.keys():
            f.write(k+' '+str(dic[k]))#格式为词项 余弦归一化值
            f.write('\n')
