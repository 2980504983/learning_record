"""
    网络编程基础

        互联网由来:
            网络从 军用 转向 公司 在转向民用，但是，后面各大公司的网络不统一，于是iso(国际标
            准化组织) 就出来制定了一个 osi七层模型，使网络工程标准化，（但是还仍有一些公司内部
            不是用osi七层模型，他们有自己的网络结构）

        osi七层模型:
            应用层: 提供用户服务，具体功能由应用程序实现
            表示层: 数据的压缩优化加密
            会话层: 建立用户级连接，选择适当的传输服务
            传输层: 提供传输服务 (根据应用层（上面三层）的需求，让底层(下三层)提供不同的服务)
            网络层: 路由选择，网络互联
            链路层: 进行数据交换，控制具体数据的发送
            物理层: 提供数据传输的硬件保证，网卡接口，传输介质

        tcp/ip模型(四层模型):
            实际工作中工程师无法完全按照七层模型要求操作，逐渐演化为跟符合实际情况的四层
            应用层:
                应用层：TFTP FTP NFS WAIS
                表示层： Telnet Rlogin SNMP Gopher
                会话层：SMTP DNS
            传输层:
                传输层: TCP UDP
            网际层:
                网络层：...
            网络接口:
                数据链路层:
                物理层:

        网络数据传输过程:
            1 发送端由应用程序发送消息，逐层添加首部信息，最终在物理层发送消息包

            2 发送的消息经过多个节点(交换机，路由器)传输，最终到达目标主机

            3 目标主机由物理层开始逐层解析首部消息包，最终到应用程序呈现消息

             详细见网络并发示意图，网络数据传输流程.jpg

        网络协议:
            在网络数据传输中，都遵循的规定
            

"""