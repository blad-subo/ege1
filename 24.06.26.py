# num = int(input())
# #324
# a = num % 10
# b = num // 10 % 10
# c = num // 100
#
# cnt = 0
# if a %  == 0 or a % 2 == 0:
#     cnt += 1
# if b % 5 == 0 or a % 2 == 0:
#     cnt += 1
# if c % 5 == 0 or a % 2 == 0:
#     cnt += 1

# Напишите программу, для вычисления корней
# квадратного уравнения вида: ax2+bx+c=0,
# которая принимает от пользователя значения коэффициентов
# a, b и c, причем с проверкой условия: a≠0.

# import math
# a = float(imput())
# b = float(imput())
# c = float(imput())
#
# if a == 0:
#     print("oshibka")
# else:
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         print("korney net")
#     elif d == 0:
#         x = -b / (2 * a)
#         print("odin koren:", x)
#     else:
#         x1 = (-b + math.sqrt(d)) / (2 * a)
#         x2 = (-b - math.sqrt(d)) / (2 * a)
#         print("dva koren:", x1, x2)



# math <вырадение>:
#   case <шаблoн 1>:
#        <deistvie 1>
#   case _:
#         <deistvie po umolch>

# value = 3

# if value == 1 or value == 2:
#     print ("odi ili dva")

# match value:
#     case 1 | 2:
#         print("один ли два")
#
#     case _:
#         print("другое 3анчение")
#
# match value:
#     case x:
#         print(x)

# point = (0,1)

# match point:
#     case (0, 0):
#         print("В начале координат")
#     case (0, y):
#         print("0,y")
#     case (x, 0):
#         print(x, 0)
#     case (x, y):
#         print("произврльная точка",x,y)

# a = eval(input())
# print(a)

# value = int(input())
# match value:
#     case x if x > 0:
#         print("x-положтьельное число")
#     case x if x < 0:
#         print("x-отрицательнок число")
#     case _:
#         print("ноль")


# value = int(input())
# data = value / 10 if value > 10 else value % 10
# print(data)


# num = int(input())
# match num:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(31)
#     case 4 | 6 | 9 | 11:
#         print(30)
#     case 2:
#         print(28)
#     case _:
#         print("неправильно")


# old = int(input())
# match old:
#     case x if x < 7:
#         print("дошкольник")
#     case x if 7 <= x < 18:
#         print("школьник")
#     case x if 18 <= x < 22:
#         print("учченик")
#     case x if 22 <= x <= 67:
#         print("раьочий")


# sign = input() #str
# num1 = float(input())
# num2 = float(input())
# match sign:
#     case "+":
#         print(num1 + num2)

# x = int(input())
# y = int(input())
#
# match (x,y):
#     case (0,0):
#         print("начало кординат")
#     case (0, _):
#         print("а оси игрик")
#     case (_, 0):
#         print("на оси икс")
#     case (x,y) if x > 0 and y > 0:
#         print("1 четверть")
#     case (x,y) if x < 0 and y > 0:
#         print("2 чктверть")
#     case (x, y) if x < 0 and y < 0:
#         print("3 чктверть")
#     case (x, y) if x < 0 and y > 0:
#         print("4 чктверть")















