'''
# 学习函数的一些东西，这里是参数的应用
'''

import math

# 定义函数


def my_abs(num):
    '''计算绝对值
    Args:
        num (int): 传入的数字
    Returns
        int: abs
    Raises:
        TypeError: 错误的参数类型
    '''
    if not isinstance(num, (int, float)):
        raise TypeError("错误的参数类型")
    if num > 0:
        return num
    else:
        return -num


def move(x, y, step, angle=0):
    """计算移动之后的位置
    Args:
        x (float): 当前位置的x坐标
        y (float): 当前位置的y坐标
        step (int): 行走的步数
        angle (float): 行走的方向(默认值为0)
    Returns:
        nx (float): 移动结束位置的x坐标
        ny (float): 移动结束位置的y坐标
    """
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

# 计算一元二次方程


def checkNumTypeError(*nums):
    '''检查参数是否正常
    Args:
        nums (tuple): 一组数据
    '''
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("%s：不是一个数字" % (num))


def quadratic(a, b, c):
    '''计算一元二次方程的解
    Args:
        a (float): 二次项的参数
        b (float): 一次项的参数
        c (float): 常数
    Returns:
        None: 无解
        OR
        result1 (float): 解1
        result2 (float): 解2
    '''
    checkNumTypeError(a, b, c)

    if a == 0:
        if b == 0:
            return None
        else:
            result1 = -b/c
            result2 = result1
            return result1, result2
    else:
        middle = b*b - 4*a*c
        if middle < 0:
            return None
        else:
            result1 = (-b + math.sqrt(middle))/2*a
            result2 = (-b - math.sqrt(middle))/2*a
            return result1, result2

# 函数的参数


def power(x, n=1):
    '''计算次方
    Args:
        x (int, float): 基数
        n (int): 指数
    Return:
        result (int, float): 计算结果
    '''
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result

# 默认参数应该指向不变量


def add_end(list=None):
    '''在list结尾添加END
    如果默认为"END",多次调用会重复添加
    因为L是默认声明的
    '''
    if list is None:
        list = []
    list.append('END')
    return list
