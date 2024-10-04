#coding:utf-8
import numpy as np
def main():
    nd1=np.random.randint(10,51,size=10)
    print('10个10~50之间的随机数'.center(50,'_')+'\n'+str(nd1))
    nd2=np.linspace(0,1,6)
    print('6个0~1之间的等差数列'.center(50,'-'),'\n',nd2)
if __name__=="__main__":
    main()