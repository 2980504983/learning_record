"""
    前情回顾:
        1 文件的读写缓冲区:
            内存中开辟的一块区域，先把内容存放在缓冲区中，等达到了一定条件在与磁盘交互
            flush()刷新缓冲区

        2 文件偏移量:
            就是指针所处的位置，tell()查看文件偏移量，seek()

        3 文件处理函数:
            os

        4 网络基本概念理论:
            osi七层模型:
            tcp/ip模型:
            三次握手四次挥手:
            tcp udp的理解

            IP地址，域名， 端口

        5 套接字编程:
            流式套接字:
            数据报套接字:

        6 tcp服务端:
            socket --> bind --> listen --> accept --> recv/send --> close
             
"""