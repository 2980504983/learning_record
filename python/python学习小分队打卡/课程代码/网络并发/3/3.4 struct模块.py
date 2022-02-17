"""
    struct模块的使用
        原理:
            将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据进行解析。
            用于发送整组数据

        注: 各种编程语言都有套接字模块，且不同的编程语言套接字发送的信息是可以相互解析的，这是因为
        在发送之前，套接字可以将我们的数据转化成网络字节序的格式，不同的语言就可以根据这个格式进行解析，
        这些就要用到struct模块
"""
# 用套接字发送整组数据时，需要将数据打包成类c的二进制数据，就要靠struct来完成


import struct

# 制定打包格式
st = struct.Struct('i4sf')  # 字母对应的是c的一些数据格式，数字表示传输的最大字节数，字数不够会补零， 格式自己去搜索

# 将里面的数据按照上面的格式打包
data = st.pack(1, b'Tom', 1.65)

# 看看数据打包后的样子
print(data)

# 打包时用的什么格式，解包就要用什么格式
print(st.unpack(data))  # 这个st模块依然是上面的格式，转出来你会发现1.65变成了1.64999这是因为
#                          ，1.65无法完全转化为二进制，当转化到达一定长度就会停止，于是就会得到
#                          一个1.65的近似数，有点类似于一个数除不尽，然后保留


"""
练习: 使用udp完成，客户端不断录入学生信息，将其发送到服务端，在服务端，将学生信息写入到一个文件中，
每个学生信息占一行
    信息格式: id name age score
    id(int)  name(str)  age(int)  score(float)
"""
