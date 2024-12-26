# # import math

# # # a=float(input("a= "))
# # # b=float(input("b= "))
# # # c=float(input("c= "))
# # # x=float(input("x= "))

# # # k=pow((a/(2*b)),1/3)*a
# # # print(k)

# # # l=b+(a**4-(c**3)*b)**(1/2)
# # # print(l)

# # # f=9.3*b-1.5*a
# # # print(f)


# # # t=(math.tan(x**6))**3
# # # print(t)


# # # y=k-l/f+t

# # # print('y= ',l)

# # import json


# # js2='{"name":"John","age":30,"city":"New York"}'

# # js2_obj=json.loads(js2 )
# # print(js2_obj)

# # a=json.dumps(js2_obj,indent=4)
# # print(a)
# # print(type(a))

# # from os import path

# # print(path.abspath('.'))
# # print(type(path))

# from pathlib import Path

    
# # print(Path('.').absolute())

# # print(type(Path))
 
# # file=Path('index.txt')

# # print([m for m in dir(file) if not m.startswith('_')]) 

# # # print(Path.cwd())

# # print(Path('main.py').exists())
# # print(Path('main.py').is_dir())
# # print(Path('main.py').is_file())

# # K=0
# # for f in Path('..').iterdir():
     
# #      if f.is_file():
# #          K+=1
# # print(K)


# # cwd1=Path('.')
# # print(cwd1.absolute())

# # cwd=Path('C:/').joinpath('Users').joinpath('Hakim').joinpath('Desktop').joinpath('practic udemy').joinpath('mainn.py')
 
# # print(cwd.rmdir())

# # test_file=open('test.txt','w')
 

# # test_file.write('Hello world!\n')
# # test_file.write('Hello world!\n')

# # test_file.close()

# # test_file=open('test.txt')
# # print(test_file.read())


# a=int(input)


# class A:
#     def my_func(self):
#         print("Method from class A")

# class B:
#     def my_func(self):
#         print("Method from class B")

# class C(B,A):  # C наследуется от A и B
#     pass

# obj = C()
# obj.my_func()  # Какой метод вызовется?


# class A:
#     def show(self):
#         print("Method from A")

# class B(A):
#     def show(self):
#         print("Method from B")
#         super().show()

# class C(B):
#     def show(self):
#         print("Method from C")
#         super().show()

# obj = C()
# obj.show()



# lst = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# new_lst = []

# for i in lst:
#     sum +=i # Суммируем элементы списка
#     new_lst.append(sum)  # Добавляем сумму
#     new_lst.append(i)    # Добавляем сам список

# print(new_lst)
