import stardict
import sys
import io
import os

sys.stdout.reconfigure(encoding='utf-8')

# print('getcwd:      ', os.getcwd())
# print('__file__:    ', __file__)

def GetWeight(x):
	collins = x['collins'] if x['collins'] != None else 0
	frq = x["frq"]
	return collins * 100000 - frq

path = os.path.dirname(__file__)
word = ""
if len(sys.argv) <= 1:
	word = "再见"
else:
	for x in range(1, len(sys.argv)):
		if word != "":
			word += " "
		word += sys.argv[x]

x = stardict.open_dict(path + "/xx.db")
queryResult = x.queryZH(word)

queryResult.sort(key=GetWeight, reverse=True)
count = min(len(queryResult), 5)

print("查询【{}】".format(word))
for x in range(count):
	resultItem = queryResult[x]
	print("[{}]. 【{}】 {}-{}  {}".format(x, resultItem["word"], resultItem["collins"], resultItem["frq"], resultItem["translation"]))
	
