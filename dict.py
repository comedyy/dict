import stardict
import sys
import io
import os

sys.stdout.reconfigure(encoding='utf-8')

# print('getcwd:      ', os.getcwd())
# print('__file__:    ', __file__)


def QueryResult(x, inputWord):
	queryResult = x.query(inputWord)

	if queryResult == None:
		print("未找到【{}】".format(inputWord))
		return


	print("\n")
	print("单词【\033[32m{}\033[0m】音标【{}】 柯林斯: {} 牛津核心: {} 分类：{}".format(queryResult["word"], queryResult["phonetic"], queryResult["collins"], queryResult["oxford"], queryResult["tag"]))
	print(queryResult["translation"])
	print("\n")
	print(queryResult["definition"])



if __name__ == '__main__':
	path = os.path.dirname(__file__)
	word = ""
	if len(sys.argv) <= 1:
		word = "hello world"
	else:
		for x in range(1, len(sys.argv)):
			if word != "":
				word += " "
			word += sys.argv[x]

	x = stardict.open_dict(path + "/xx.db")

	QueryResult(x, word)
