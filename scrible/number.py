# Integer
say = "Result:"
a = 2.0
b = 7
c, d = 8, 30
result = a * b + (c * a) - (b / d)

# 29.766666666666666 floating point
print(f"{say} {result}")

result = c / a
print(f"{say} {result}")  # 4.0 floating point

result = c // a
print(f"{say} {result}")