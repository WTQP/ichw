"""Tiles.py: 设计目标：对任意给定长方形墙面和长方形砖块，输出合理的用砖块铺满这个墙壁
             的方法，并用 Turtle 模块实现可视化。


__author__ = "Wangtie"
__pkuid__  = "1800011811"
__email__  = "1800011811@pku.edu.cn"
"""


import turtle
import random
a = int(input('墙的长度是多少？'))
b = int(input('墙的宽度是多少？'))
c = int(input('砖的长度是多少？'))
d = int(input('砖的宽度是多少？'))
qiang = []
qiangf = []
for j in range(a * b):
    qiang.append(0)  # 初始化墙壁
    qiangf.append(1)  # 设置对照的贴满墙壁
ans_count = 0
all_ans = []


def tstheng(next, qiang):
    '''检查下一块砖能不能横着铺'''
    global a, b, c, d
    if (a - next % a) < c or (b - next // a) < d:
        return False
    for k in range(c):
        if qiang[next + k] != 0:
            # 若任意同行小块被占据，则报错
            return False
        else:
            for m in range(d):
                if qiang[next + k + m * a] != 0:
                    # 若下面的任意小块被占据，则报错
                    return False
                else:
                    pass
    return True  # 每一块都没问题，可以横着铺


def tstzong(next, qiang):
    '''检查下一块砖能不能竖着铺'''
    global a, b, c, d
    if (a - next % a) < d or (b - next // a) < c:
        return False
    for k in range(d):
        if qiang[next + k] != 0:
            return False
        else:
            for m in range(c):
                if qiang[next + k + m * a] != 0:
                    return False
                else:
                    pass
    return True  # 每一块都没问题，可以竖着铺


def pu(ans, qiang):
    global a, b, c, d, qiangf, ans_count, all_ans
    if qiang == qiangf:  # 证明铺满了
        if all_ans == []:  # 如空，则填入
            ans_count = ans_count + 1
            print('Answer ' + str(ans_count))
            print(ans)
            all_ans.append(ans.copy())
            return
        else:
            if ans != all_ans[ans_count - 1]:  # 如非空，则判断是否与前一个相同
                ans_count = ans_count + 1
                print('Answer ' + str(ans_count))
                print(ans)
                all_ans.append(ans.copy())
                return
            if ans == all_ans[ans_count - 1]:
                pass  # 判断下一个解法是否与前一个相同，简单规避1 * 1的砖
    else:
        next = qiang.index(0)
        if tstzong(next, qiang):
            ans1 = [(next + k + m * a) for k in range(d)
                    for m in range(c)]  # 写入本组答案
            for i in ans1:
                qiang[i] = 1  # 装在墙上
            ans.append(ans1.copy())
            pu(ans, qiang)
            # 由于每个pu函数最后都会把自己铺好的瓷砖拆下来
            # 因此回溯到这里，说明在next之后位置的方块的瓷砖都是被拆下来了。
            # 为了尝试竖着铺，因此需要把铺好的瓷砖先拆下来
            lastans = ans.pop()  # 从答案总集中去除上一块
            for i in lastans:
                qiang[i] = 0  # 从墙上清除上一块
        if tstheng(next, qiang):
            ans1 = [(next + k + m * a) for k in range(c)
                    for m in range(d)]  # 写入本组答案
            for i in ans1:
                qiang[i] = 1  # 装在墙上
            ans.append(ans1.copy())
            pu(ans, qiang)
            # 由于每个pu函数最后都会把自己铺好的瓷砖拆下来
            # 因此回溯到这里，说明在next之后位置的方块的瓷砖都是被拆下来了。
            # 为了尝试竖着铺，因此需要把铺好的瓷砖先拆下来
            lastans = ans.pop()  # 从答案总集中去除上一块
            for i in lastans:
                qiang[i] = 0  # 从墙上去除上一块
    return


def main():
    ''' main module '''
    global a, b, c, d, qiang, qiangf, ans_count
    if (a * b) % (c * d) != 0 or (c > a and c > b) or (d > a and d > b)\
       or a == 0 or b == 0 or c == 0 or d == 0:
        print('这组数据铺不了哟~')
    else:
        pu([], qiang)
        print(str(ans_count) + ' answer(s) in total.')
        print(all_ans)


if __name__ == '__main__':
    main()
