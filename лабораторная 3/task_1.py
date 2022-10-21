src = not False and True or False and not True
# TODO result = True and True or False and False - избавились от отрицаний
# TODO result = True or False - избавились от логического "и"
# TODO result = True - избавились от логического "или"

result = True

print(src == result)
