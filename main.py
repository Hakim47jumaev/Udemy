# def create_spiral_matrix(n):
#     matrix = [[0] * n for _ in range(n)]
#     num = 1
#     left, right, top, bottom = 0, n - 1, 0, n - 1

#     while left <= right and top <= bottom:
#         # Fill top row
#         for i in range(left, right + 1):
#             matrix[top][i] = num
#             num += 1
#         top += 1

#         # Fill right column
#         for i in range(top, bottom + 1):
#             matrix[i][right] = num
#             num += 1
#         right -= 1


#         # Fill bottom row
#         for i in range(right, left - 1, -1):
#             matrix[bottom][i] = num
#             num += 1
#         bottom -= 1

#         # Fill left column
#         for i in range(bottom, top - 1, -1):
#             matrix[i][left] = num
#             num += 1
#         left += 1

#     return matrix

# # Print the matrix
# size = 10000
# spiral_matrix = create_spiral_matrix(size)
# for row in spiral_matrix:
#     print(' '.join(map(str, row)))


# def addd(a):
#     return a.append(5)

# a=[1,2,3]
# print(id(a))
# addd(a)
# print(a)
# print(id(a))

# def ad(a):
#     return a+1

# p=9
# print(id(p))
# print(ad(p))
# p=p+1
# print(id(p))


# import pandas as pd


# date={
#     'name':["Ali",'Vali','JAke'],
#     'age':[24,35,23],
#     'city':['Dushanbe','bokhtar','Kulob']
    
# }

# table=pd.DataFrame(date)

# print(table)
# print(table.info())
# print(table.describe())




# while True: print(eval(input(">>>")))

 
# def my_func(a):
#     if '/' in a:
#         k=a.index('/')
#         print(float(a[0:k])/float(a[ k+1:]))
#     if '*' in a:
#         k=a.index('*')
#         print(float(a[0:k])*float(a[ k+1:]))
#     if '+' in a:
#         k=a.index('+')
#         print(float(a[0:k])+float(a[ k+1:]))
#     if '-' in a:
#         k=a.index('-')
#         print(float(a[0:k])-float(a[ k+1:]))
    
# while True:my_func(input("---> "))

# import time

# def custom_random(min_value, max_value):
    
#     seed = int(time.time() * 1000000) % 1000000
    
#     # Простейший генератор псевдослучайного числа на основе остатка деления
#     random_value = (seed * 214013 + 2531011) & 0x7FFFFFFF  # Линейный конгруэнтный метод
#     return min_value + (random_value % (max_value - min_value + 1))

# print(custom_random(1,10))


# from docx