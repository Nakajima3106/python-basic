def eat(food, count, unit = "個"):
    text = "私は{}を{}{}食べました。".format(food, count, unit)
    print(text)
eat("みかん", 3)
eat("プリン", 2)
eat("バナナ", 1, "本")