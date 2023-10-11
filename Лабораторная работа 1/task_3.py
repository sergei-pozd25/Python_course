# TODO Найдите количество книг, которое можно разместить на дискете

value =1.44 * 1024 * 1024 #bytes
pgs = 100
rows = 50
simbols = 25
val = 4 #bytes
value_for_one_book = val * simbols * rows * pgs
books_num = int(value // value_for_one_book)

print("Количество книг, помещающихся на дискету:", books_num)
