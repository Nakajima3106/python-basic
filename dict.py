data = {
  "みかん": 80,
  "りんご": 120,
  "バナナ": 70,
  "ぶどう": 180
}
print(tuple(data.keys()))
key = input("値段を知りたい果物は？")
print(data[key], "円です")