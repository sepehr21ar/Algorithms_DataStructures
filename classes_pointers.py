# class Cookie:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self, color):
#         self.color = color
#
#
# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')
#
# print('Cookie one is', cookie_one.get_color())
# print('Cookie two is', cookie_two.get_color())
#
# cookie_one.set_color('yellow')
#
# print('\nCookie one is now', cookie_one.get_color())
# print('Cookie two is still', cookie_two.get_color())

num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


