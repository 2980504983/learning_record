"""
    爬虫的分类:
        1 根据被爬取网站数量不同，可以分为:
            通用爬虫:
                如搜索引擎，爬取的网站数量不限
            聚焦爬虫:
                如12306抢票，或专门抓取某一个(某一类)的网站

        2 根据是否一获取数据为目的，可以分为:
            功能性爬虫: 不以数据为目的，例如给你喜欢的明星投票，

            数据增量爬虫: 以数据为目的，例如比如招聘信息

        3 根据url地址和对应页面内容是否变化，数据增量爬虫可以分为:
            1 基于url地址变化，内容也变化的数据增量爬虫
            2 url地址不变，内容变化的数据增量爬虫

        4 总体分类:
            通用爬虫:

            聚焦爬虫:
                功能性爬虫:

                数据增量爬虫:
                    url与数据同时变化的数据增量爬虫:
                    url不变，数据变化的数据增量爬虫:
"""