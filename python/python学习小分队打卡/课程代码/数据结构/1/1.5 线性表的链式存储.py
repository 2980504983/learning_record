"""
    线性表:

        线性表的顺序存储:
            就是将线性表的各元素一次存储在一片连续的空间里(列表或元组就是)
            特点:
                1 优，逻辑上相邻的元素，存储位置也相邻
                2 优，存储密度高，方便对数据的遍历查找
                3 缺，对表的插入和删除等运算效率较差(插入一个数据，后面的数据都要移动)

        线性表的链式存储:
            线性表中各元素分布在存储器的存储块，称为结点，每个结点中都持有指向下一个结点的引用
            特点:
                1 优：存储稀疏，不必开辟整块存储空间
                2 优：删除，增加操作


"""

# 链式结构
c = 3
b = (2, c)
a = (1, b)


# linklist
# 实现单链表的建构和功能操作


class Node:  # 创建结点类
    def __init__(self, val, next=None):
        self.val = val  # 数据
        self.next = next  # 下一个节点
    pass


node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)
