"""
__init__.py: 包被导入时会被调用。一般不用。

__all__: *什么能导出，就是用__all__来定义

导包能不能成功，path中的路径加上 from  中的东西能把模块找到，导包就能成功
import sys
print(sys.path)

如果导包不成功，讲项目根目录的绝对路径加进去，就可以了。(pycharm的mark标蓝也是这种原理)
sys.path.append("项目根目录的绝对路径")


从哪开始执行，哪里就是主模块，主模块所在的文件夹我们称之为根目录

"""