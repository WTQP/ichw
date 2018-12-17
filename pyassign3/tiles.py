def tstheng(next):
    global a,c,d
    for k in range(c):
        for m in range(d):
            print(qiang[next % a + k + m * a])
            if qiang[next % a + k + m * a] != 0:
                return False
            else:
                pass
    return True


def tstzong(next):
    global a,c,d
    for k in range(d):
        for m in range(c):
            print(qiang[next % a + k + m * a])
            if qiang[next % a + k + m * a] != 0:
                return False
            else:
                pass
    return True


def pu(ans,qiang):
    global a, b, c, d
    if qiang == qiangf:
        return ans
        print('done')
    else:
        next = qiang.index(0)
        print(next)
        if tstheng(next):
            ans = []
            ans1 = [(next % a + k + m * a) for k in range(c)\
            for m in range(d)]
            for i in ans1:
                qiang[i] = 1
            ans.append(ans1.copy())
            print(ans1)
            print(qiang)
            print('heng')
            pu(ans,qiang)
            aa = ans.pop()
            for i in aa:
                qiang[i] = 0
        if tstzong(next):
            ans1 = [(next % a + k + m * a) for k in range(d)\
            for m in range(c)]
            for i in ans1:
                qiang[i] = 1
            ans.append(ans1.copy())
            print(ans1)
            print(qiang)
            print('shu')
            pu(ans,qiang)
            aa = ans.pop()
            for i in aa:
                qiang[i] = 0
    print(ans)
    print(qiang)
    return ans


#a = int(input('墙的长度是多少？'))
#b = int(input('墙的高度是多少？'))
#c = int(input('砖的长度是多少？'))
#d = int(input('砖的宽度是多少？'))
a=3
b=2
c=2
d=1
if (a * b) % (c * d) != 0 or c > a or d > b \
    or a == 0 or b == 0 or c == 0 or d == 0:
    print('这组数据铺不了哟~')
else:
    qiang = []
    qiangf = []
    for j in range(a * b):
        qiang.append(0)  # 初始化墙壁
        qiangf.append(1)
pu([],qiang)
