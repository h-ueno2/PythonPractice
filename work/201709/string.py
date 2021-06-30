# - coding:utf-8 -
print("a" + "b")
print("a" + str(10))
s = "テキストABCabcテキスト"
print(s.count("テキスト"))
print(s.lower())
print(s.find("abc"))
print(s[9:12])

# タプル
t = (1, 2, "foo")
print(t)
print(t[1])
print(t[0:2])

# リスト
list = [1, "hoge"]
list.append("foo")
print(list)

list = [1]
s = ["a", "b"]
list.append(s)
s.append("c")
print(list)

