"""
    数据模型
"""


class DirectionModel:
    """
        方向数据模型
        枚举：在整数基础上，添加一个人容易识别胡"标签"
        常量(字母全大写)
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Location:
    """
        位置
    """
    def __init__(self, r, c):
        self.r_index = r
        self.c_index = c
