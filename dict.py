import stardict
import sys
import io

sys.stdout.reconfigure(encoding='utf-8')

word = len(sys.argv) > 1 and sys.argv[1] or "move"

x = stardict.open_dict("xx.db")
queryResult = x.query(word)

print("\n")
print("单词【{}】音标【{}】 柯林斯: {} 牛津核心: {} 分类：{}".format(queryResult["word"], queryResult["phonetic"], queryResult["collins"], queryResult["oxford"], queryResult["tag"]))
print("\n")
print(queryResult["definition"])
print(queryResult["translation"])
