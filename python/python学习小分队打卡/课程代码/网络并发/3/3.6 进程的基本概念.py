"""
    进程(process)
        1 定义:
            程序在计算机中的一次运行

        程序是一个可执行的文件，是静态的占有磁盘
        而进程是一个动态的描述过程，占有计算机运行资源，有一定的生命周期

        2 系统中如何产生一个进程
            1 用户空间通过调用程序接口或者命令发起请求 (运行一个程序)
            2 操作系统接收用户请求，开始创建进程
            3 操作系统调配计算机资源，确定进程状态等
            4 操作系统将创建的进程提供给用户使用

        3 进程基本概念
            cpu时间片:
                如果一个进程占有CPU内核则称这个进程在cpu时间片上

            pcb(进程控制块):
                在内存中开辟一块空间，用于存放进程的基本信息，也用于系统查找识别进程，这个内存
                区域就是pcb

            进程ID(PID):
                系统为每个进程分配的一个大于0的整数，作为进程ID。每个进程不重复
                linux 查看进程ID: ps -aux

            父子进程:
                系统中每一个进程(除了系统初始化进程)都有唯一的父进程，但是可以有0个或多个子进程，
                父子进程关系便于进程管理。 我们认为是父进程初始化了子进程
                linux 查看进程树: pstree
"""