myset = {1, 2, 3, 4, 5}

# 集合型をリストに変換
mylist = list(myset)
print(type(mylist))
print(mylist)

## 集合型をタプルに変換
mytuple = tuple(myset)
print(type(mytuple))
print(mytuple)

## リストを集合型に変換
myset = set(mylist)
print(type(myset))
print(myset)