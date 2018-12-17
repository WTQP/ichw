"""Tiles.py: 设计目标：对任意给定长方形墙面和长方形砖块，输出合理的用砖块铺满这个墙壁
             的方法，并用 Turtle 模块实现可视化。

             但目前尚未完成，目前程序仅能尝试出部分简单的解法，而且无法有效输出。

__author__ = "Wangtie"
__pkuid__  = "1800011811"
__email__  = "1800011811@pku.edu.cn"
"""


def tstheng(next, qiang):
    '''检查下一块砖能不能横着铺'''
    global a, c, d
    for k in range(c):
        if qiang[next % a + k] != 0:
            print('falseh')
            return False
        else:
            for m in range(d):
                if qiang[next % a + k + m * a] != 0:
                    # 若有任一块非空，就会冲突。
                    print('falseh')
                    return False
                else:
                    pass
    return True  # 每块儿都没问题


def tstzong(next, qiang):
    '''检查下一块砖能不能横着铺'''
    global a, c, d
    for k in range(d):
        if qiang[next % a + k] != 0:
            print('falseh')
            return False
        else:
            for m in range(c):
                if qiang[next % a + k + m * a] != 0:
                    # 若有任一块非空，就会冲突。
                    print('falseh')
                    return False
                else:
                    pass
    return True  # 每一块都没有问题

def pu(ans, qiang):
    global a, b, c, d
    if qiang == qiangf:
        return ans
        print('done')
    else:
        next = qiang.index(0)
        print(next)
        if tstheng(next):
            ans = []
            ans1 = [(next % a + k + m * a) for k in range(c)
                    for m in range(d)]
            for i in ans1:
                qiang[i] = 1
            ans.append(ans1.copy())
            pu(ans, qiang)
            # 由于每个pu函数最后都会把自己铺好的瓷砖拆下来
            # 因此回溯到这里，说明在next之后位置的方块的瓷砖都是被拆下来了。
            # 为了尝试竖着铺，因此需要把铺好的瓷砖先拆下来
            lastans = ans.pop()  # 从答案总集中去除上一块
            for i in lastans:
                qiang[i] = 0  # 从墙上取下上一块
        if tstzong(next):
            ans1 = [(next % a + k + m * a) for k in range(d)
                    for m in range(c)]
            for i in ans1:
                qiang[i] = 1
            ans.append(ans1.copy())
            pu(ans, qiang)
            # 由于每个pu函数最后都会把自己铺好的瓷砖拆下来
            # 因此回溯到这里，说明在next之后位置的方块的瓷砖都是被拆下来了。
            # 为了尝试竖着铺，因此需要把铺好的瓷砖先拆下来
            lastans = ans.pop()  # 从答案总集中去除上一块
            for i in lastans:
                qiang[i] = 0  # 从墙上取下上一块
    # 运行到这里说明两种方法都尝试过了，回溯到上一个瓷砖尝试铺法
    return


if '__name__' == '__main__':
    a = int(input('墙的长度是多少？'))
    b = int(input('墙的高度是多少？'))
    c = int(input('砖的长度是多少？'))
    d = int(input('砖的宽度是多少？'))
    if (a * b) % (c * d) != 0 or c > a or d > b \
       or a == 0 or b == 0 or c == 0 or d == 0:
        print('这组数据铺不了哟~')
    else:
        qiang = []
        qiangf = []
        for j in range(a * b):
            qiang.append(0)  # 初始化墙壁
            qiangf.append(1)
        pu([], qiang)
