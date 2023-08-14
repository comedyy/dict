import stardict
import sys
import io
import os
import dict

sys.stdout.reconfigure(encoding='utf-8')
path = os.path.dirname(__file__)
x = stardict.open_dict(path + "/xx.db")


while True:
	inputWord = input("输入要查询的单词语:")
	dict.QueryResult(x, inputWord)
