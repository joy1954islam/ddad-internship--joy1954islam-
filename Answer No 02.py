def fibonacci(n):
    fn = [0, 1, ]
    for i in range(2, n):
        fn.append(fn[i - 1] + fn[i - 2])
    return fn


id = int(input())

list1 = fibonacci(id)
str1 = ', '.join(str(e) for e in list1)

print(str1)