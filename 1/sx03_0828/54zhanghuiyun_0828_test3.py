#coding:utf-8
import numpy as np
def main():
    np.set_printoptions(threshold=np.inf)
    score=np.random.randint(1,101,size=(43,5))
    print('学生成绩如下: '.center(50,'-'),'\n',score)
    print(score.mean(axis=0))
    score_2_avg=round(score.mean(axis=0)[1],2)
    print('第2门课程的平均分='.center(50,'-'),score_2_avg)
    sum_8=score.sum(axis=1)[7]
    print('第8个同学的总分= '.center(50,'-'),sum_8)
    course_3=score[:,2]
    count=len(course_3[(course_3>=60)&(course_3<70)])
    print('第3门课程60-70分的人数： '.center(50,'-'),count)
if __name__=="__main__":
    main()