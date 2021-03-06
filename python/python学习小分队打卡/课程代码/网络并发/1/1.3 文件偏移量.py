"""
    文件偏移量:
        打开一个文件进行操作时系统会自动生成一个记录，记录中描述了我们对文件的一系列操作。
        其中包括每次操作到文件的位置，文件的读写操作都是从这个位置开始进行的。也就会说，
        文件读写的位置可以，基于上一次结束的位置开始

    tell() 获取文件偏移量的大小
    seek(移动数量, 参数) 参数（0表示开头，1表示当前位置，2表示结尾）只有以二进制打开才支持1和2
                            文本类型只能是0）

    每次文件被open打开(不传a参数时)，文件偏移量都会被移动到开头，
    读写操作共用一个文件偏移量
"""

# 按理说下面的操作会打印 hello world，但是结果什么都没有打印，就是因为文件偏移量，写操作后，
# 光标被移到最后，在进行读操作时，从最后开始读取，自然什么也没有

f = open("0 被操作的文件.py", "w+")

f.write("hello world")
f.flush()

data = f.read()

print(data)

f.close()
