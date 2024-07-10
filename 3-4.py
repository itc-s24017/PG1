for i in range(10):
    if i % 2 == 0:
        continue
        print(i * 10)
    print(i)
print("breakにすると")
for i in range(10):
    if i % 2 == 0:
        print(i + 100)
        break
    print(i)
a, b = 0, 1
while b <= 100:
    print(b)
    a, b = b, a + b
