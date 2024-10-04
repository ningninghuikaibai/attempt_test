#coding:utf-8
import numpy as np
def main():
    a=np.array([np.arange(0,5)]*5).reshape(5,5)
    print('每一行都是从0到4的5*5矩阵'.center(50,'-')+'\n',a)
    b=np.eye(8).astype(np.int8)
    b[[0,7]]=5
    b[:,[0,7]]=5
    print('矩阵边界全为5，里面主对角线为1，其余为0的8行8列矩阵'.center(50,'-')+'\n',b)
    c=np.random.normal(loc=70,scale=5,size=43).astype(np.int8)
    print('平均值为70，标准差为5的43个同学的Python语言程序设计成绩的随机分数'.center(50,'-')+'\n',c)
if __name__=="__main__":
    main()