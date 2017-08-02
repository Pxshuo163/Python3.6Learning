'''
递归
'''

# 尾递归改写


def factOld(num):
    '''普通递归'''
    if num == 1:
        return 1
    return num * factOld(num-1)


def fact(num):
    '''尾递归调用'''
    return fact_iter(num, 1)


def fact_iter(num, product):
    '''尾递归实现'''
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 实际上没有优化，233333

# 汉诺塔


def move(n, a, b, c):
    '''汉诺塔
    把n个盘子从a移动到c
    '''
    if n == 1:
        print("#", a, "-->", c)
    else:
        move(n-1, a, c, b)       # 先把n-1个盘子从a放到b上
        print("#", a, "-->", c)  # 然后把一个盘子放到c上
        move(n-1, b, a, c)       # 再把n-1个盘子从b放到c上


move(3, "A", "B", "C")
