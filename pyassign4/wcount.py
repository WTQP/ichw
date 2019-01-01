"""wcount.py: count words from an Internet file.

__author__ = "Wangtie"
__pkuid__  = "1800011811"
__email__  = "1800011811@pku.edu.cn"
"""


import sys
from urllib.request import urlopen


def wcount(topn=10):
    """count words of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    topn = int(topn)
    url = sys.argv[1]  # 用于命令行输入网址
    doc = urlopen(url)  # 打开网址
    docs = str(doc.read())  # 读取文本
    tore = ['!', ';', "'s'", '.', '"', ':', '?', '/', '-', '_', '&', ', ', '#',
            ']', '[', '*', "'", "{", "}", "+", '=', '@', '$', "%", "^", "*",
            '(', ')', '`', "~", "|", '\r\n\r\n', '''\\r\\n''', "\\"]
    words = []  # 储存分隔开的单词用的空列表
    for i in tore:
        docs = docs.replace(i, ' ')  # 把所有的符号全转成空格
    word = docs.split()
    ans = {}  # 记总数
    for wd in word:
        wd = wd.lower()  # 全部转化为小写
        if wd not in ans.keys():
            ans[wd] = 1  # 之前未遇到，创建新计数器
        else:
            ans[wd] = ans[wd] + 1  # 遇到过，加一即可
    rever = dict(zip(ans.values(), ans.keys()))  # 只能反转一部分
    keylist = list(ans.values())  # 取出所有计数
    keylist.sort(reverse=True)  # 倒序排列
    for i in range(topn):
        n = keylist[i]
        print(rever[n], n)
    pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output.\
               If not given, will output top 10 words')
        sys.exit(1)
    if len(sys.argv) == 2:  # 按默认值操作
        wcount()
    if len(sys.argv) == 3:  # 按给定值操作
        wcount(sys.argv[2])
