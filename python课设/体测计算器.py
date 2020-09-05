'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 体测计算器.py
# @Author: 华中豪
# @Date  : 2020/6/8
# @Desc  :功能：将用户输入的体测数据根据不同的标准计算出各体测项目相应的分数并评级，最后以相应权重输出体测成绩。
          说明：
          1.单项指标与权重：BMI指数(15%);肺活量(15%);引体向上(10%);立定跳远(10%);坐位体前屈(10%);50米跑(20%);1000米跑(20%)
          2.体测成绩由标准分与附加分之和构成，满分为120分。
          3.标准分由各单项指标得分(满分为100)与权重乘积之和组成，满分为100分。
          4.附加分根据实测成绩确定，即对成绩超过100分的加分指标进行加分，满分为20分。
          5.大学的加分指标为男生引体向上和1000米跑，女生1分钟仰卧起坐和800米跑，各指标加分幅度均为10分。
          6.本程序只计算大一大二男生体测成绩。
          7.为方便计算，本程序中肺活量单项满分为200分，1000m跑单项满分为150分。
            即体测成绩总分 = 100*0.15 + 100*0.15 + 150*0.1 +100*0.1 +100*0.1 +100*0.2 + 150*0.2 =120
          8.体测成绩保留两位有效数字
          
          注：评分标准来源于《国家学生体质健康标准说明》(见附件1)

'''
#定义等级函数(Rank)
def Rank(n):
    l = ["不及格","及格","良好","优秀"]
    if n < 60:
        i = 0
    elif n < 80:
        i = 1
    elif n < 90:
        i = 2
    else:
        i = 3
    return l[i]   #返回等级
    
#定义身高体重函数(BMI)
def BMI():          
    height = eval(input("请输入您的身高(m):"))
    weight = eval(input("请输入您的体重(kg):"))
    l = ["偏低","正常","超重","肥胖"]
    #计算bmi
    bmi = weight/height**2      
    #根据bmi的值确定bmi的成绩
    if bmi <= 17.8:
        rbmi,i = 80,0
    elif 17.8 < bmi <= 23.9:
        rbmi,i = 100,1
    elif 23.9 < bmi < 28.0:
        rbmi,i = 80,2
    else:
        rbmi,i = 60,3
    print("您的BMI指数为:{:.2f},成绩:{} {}".format(bmi,rbmi,l[i]))
    return rbmi     #返回结果

#定义肺活量函数(LUNGS)
def LUNGS():        
    lungs = eval(input("请输入您的肺活量(ml):"))
    #建立空列表
    datals = []     
    #打开肺活量文件，每行数据由"a,b,c"(a<b)形式存入，表示输入数据在a,b之间的，成绩为c
    fo = open("肺活量.txt","r")    
    for line in fo:
        line = line.replace("\n","")
        datals.append(list(map(eval, line.split(","))))
    fo.close()
    rlungs = 0
    for i in range(len(datals)):
        if datals[i][0] <= lungs < datals[i][1]:
            rlungs = datals[i][2]
    print("您的肺活量成绩为:{} {}".format(rlungs,Rank(rlungs)))
    return rlungs   #返回结果

#定义引体向上函数(UP)
def UP():           
    up = eval(input("请输入您的引体向上个数(个):"))
    #以分段函数形式计算成绩
    if up < 5:
        rup = 0
    elif up <= 10:
        rup = (up-4)*10
    elif up <= 15:
        rup = (up-10)*4 + 60
    elif up <= 19:
        rup = (up-15)*5 + 80
    elif up < 30:   #由于引体向上成绩占比10%且有附加分10分，所以把引体向上成绩总分定于200
        rup = (up-19)*10 + 100
    elif up >= 30:
        rup = 200
    print("您的引体向上成绩为:{} {}".format(rup,Rank(rup)))
    return rup      #返回结果

#定义立定跳远函数(JUMP)
def JUMP():         
    jump = eval(input("请输入您的立定跳远距离(cm):"))
    datals = []
    #打开立定跳远文件，每行数据由"a,b,c"(a<b)形式存入，表示输入数据在a,b之间的，成绩为c
    fo = open("立定跳远.txt","r")
    for line in fo:
        line = line.replace("\n","")
        datals.append(list(map(eval, line.split(","))))
    fo.close()
    rjump = 0
    for i in range(len(datals)):
        if datals[i][0] <= jump < datals[i][1]:
            rjump = datals[i][2]
    print("您的立定跳远成绩为:{} {}".format(rjump,Rank(rjump)))
    return rjump     #返回结果  


#定义坐位体前屈函数(FORWARD)
def FORWARD():
    forward = eval(input("请输入您的坐位体前屈距离(cm):"))
    datals = []
    #打开坐位体前屈文件，每行数据由"a,b,c"(a<b)形式存入，表示输入数据在a,b之间的，成绩为c
    fo = open("坐位体前屈.txt","r")
    for line in fo:
        line = line.replace("\n","")
        datals.append(list(map(eval, line.split(","))))
    fo.close()
    rforward = 0
    for i in range(len(datals)):
        if datals[i][0] <= forward < datals[i][1]:
            rforward = datals[i][2]
    print("您的坐位体前屈成绩为:{} {}".format(rforward,Rank(rforward)))
    return rforward  #返回结果

#定义50m跑函数(SRUN)
def SRUN():
    srun = eval(input("请输入您的50m跑时间(s):"))
    datals = []
    #打开50m跑文件，每行数据由"a,b,c"(a<b)形式存入，表示输入数据在a,b之间的，成绩为c
    fo = open("50m跑.txt","r")
    for line in fo:
        line = line.replace("\n","")
        datals.append(list(map(eval, line.split(","))))
    fo.close()
    rsrun = 0
    for i in range(len(datals)):
        if datals[i][0] <= srun < datals[i][1]:
            rsrun = datals[i][2]
    print("您的50m跑成绩为:{} {}".format(rsrun,Rank(rsrun)))
    return rsrun     #返回结果

#定义1000m跑函数(LRUN)
def LRUN():
    lrun = eval(input("请输入您的1000m跑时间(s):"))
    datals = []
    #打开1000m跑文件，每行数据由"a,b,c"(a<b)形式存入，表示输入数据在a,b之间的，成绩为c
    #由于1000m跑占比20%且有附加分10分，所以把1000m跑成绩总分定于150(文件中查看)
    fo = open("1000m跑.txt","r")
    for line in fo:
        line = line.replace("\n","")
        datals.append(list(map(eval, line.split(","))))
    fo.close()
    rlrun = 0
    for i in range(len(datals)):
        if datals[i][0] <= lrun < datals[i][1]:
            rlrun = datals[i][2]
    print("您的1000m跑成绩为:{} {}".format(rlrun,Rank(rlrun)))
    return rlrun   #返回结果      

#定义结果函数(RESULT)
def RESULT(a,b,c,d,e,f,g):
    result = a*0.15 + b*0.15 + c*0.10 + d*0.10 + e*0.10 +f*0.20 + g*0.20
    #输出体测成绩和等级
    print("您的体测成绩为:{:.2f} {}".format(result,Rank(result)))

def main():
    print("{:*^40}".format("欢迎使用体测计算器！"))
    a = BMI()
    b = LUNGS()
    c = UP()
    d = JUMP()
    e = FORWARD()
    f = SRUN()
    g = LRUN()
    RESULT(a,b,c,d,e,f,g)
    print("{:*^40}".format("感谢您的使用！"))

main()

