# آموزش کلاس‌ها
class Cookie:
    def __init__(self, color):
        # هنگام ساخت شی، رنگ کوکی تعیین می‌شود
        self.color = color

    def get_color(self):
        # متد برای دریافت رنگ کوکی
        return self.color

    def set_color(self, color):
        # متد برای تنظیم رنگ کوکی
        self.color = color


# ایجاد دو شی از کلاس Cookie
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# نمایش رنگ‌های اولیه کوکی‌ها
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# تغییر رنگ اولین کوکی
cookie_one.set_color('yellow')

# نمایش رنگ جدید کوکی‌ها
print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

# ------------------------------------------------------------

# آموزش اشاره‌گرها (Pointers) با استفاده از متغیرهای ساده
num1 = 11
num2 = num1  # num2 به همان مقداری که num1 دارد ارجاع می‌دهد

print("\n\nBefore num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# نشان دادن آدرس حافظه (ID) متغیرها
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# تغییر مقدار num2
num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# آدرس‌های حافظه بعد از تغییر
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# ------------------------------------------------------------

# آموزش اشاره‌گرها با استفاده از دیکشنری‌ها
dict1 = {'value': 11}
dict2 = dict1  # dict2 به همان دیکشنری که dict1 به آن اشاره دارد ارجاع می‌دهد

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# نشان دادن آدرس حافظه
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# تغییر مقدار دیکشنری
dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# آدرس‌های حافظه بعد از تغییر
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
