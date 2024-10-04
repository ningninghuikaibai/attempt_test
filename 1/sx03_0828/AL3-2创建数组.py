#coding:utf-8
import numpy as np
def main():
    a=[np.arange(0,5)]
    nd=np.array(a*5)
    nd.reshape(5,5)
    print(nd)
    b=np.zeros(shape=(6,6),dtype=np.int8)
    print(b)
    b[[0,5]]=1
    b[:,[0,5]]=1
    print(b)
if __name__=="__main__":
    main()