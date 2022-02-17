"""
    线程基本概念:
        1 什么是线程:
            1 线程被称为轻量级的进程
            2 线程也可以使用计算机多核资源，是多任务编程方式
            3 线程是系统分配内核的最小单元，而进程是系统分配资源的最小单元
            4 线程可以理解为进程的分支任务
            注: 进程也可以分到多个计算机内核，进程就好比一个家庭，线程是家庭中的成员，进程中分
                配到的资源，由会被分配给线程，没有线程的进程称为单进程，详细见  进程与线程的关系.jpg

        2 线程特征:
            1 一个进程中可以包含多个线程
            2 线程也是一个运行行为，消耗计算机资源
            3 一个进程中的所有线程共享这个进程的资源
            4 多线程之间的运行互不影响各自运行
            5 线程的创建和销毁消耗资源小于进程
            6 线程也有自己的id等特征

"""