"""
    爬虫:
        Context-Type(请求内容的类型)

        常见的请求头:
            host  域名
            connection  长连接
            Upgrade-Insecure-Requests  升级为https请求
            User-Agent  用户代理，提供系统信息和浏览器信息
            Referer  页面跳转出，防盗链(图片/视频)
            Cookie  状态保持

            后面三个用的最多，网站检测的频率最多

        常见的响应头:
            Set-Cookie

        常见的状态码:
            200 成功
            302 跳转，新的url在响应的Location头中给出
            303 浏览器对于POST的响应进行重定向至新的url
            307 浏览器对于GET的响应重定向至新的url
            403 资源不可用，服务器理解客户请求，单拒绝处理(没有权限)
            404 找不到该页面
            500 服务器内部错误
            503 服务器由于维护或者负载过重未能应答

            状态码不一定就是真的，比如服务器已经识别出你是爬虫了，就故意给你发错误的状态码。
            判断是否被骗了，直接那浏览器去访问，看看什么情况
            所有状态码都不可信(它是服务器发给你的)，一切以是否从抓包中获取的响应数据为准
            network中抓包得到的源码才是判断依据，elements中的源码是渲染之后的源码，不能
            作为判断标准


"""