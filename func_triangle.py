def triangle_area(bottom, height):
    area = bottom * height / 2
    return area

area_A = triangle_area(15, 7) # 戻り値「52.5」が変数 area_A に代入される
area_B = triangle_area(8, 12) # 戻り値「48」が変数 area_B に代入される

print("２つの面積の合計は{}平方cmです".format(area_A + area_B))