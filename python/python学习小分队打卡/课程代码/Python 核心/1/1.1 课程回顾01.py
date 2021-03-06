"""
    复习
        面向对象：
            考虑问题从对象的角度的出发.
            抽象：从多个事物中舍弃个别的/非本质的特征，抽出共性的过程。

        三大特征：
            封装：
                将每个变化点单独分解到不同的类中。
                例如：老张开车去东北
                做法：定义人类，定义车类
            继承：
                重用现有类的功能和概念，并在此基础上进行扩展。
                （代码复用）（不推荐通过继承来代码复用，应该用组合复用，这样能减小耦合度）
            多态：
                调父执行子
                重写：覆盖父类抽象的方法
                继承是共性，多态是个性


        设计原则：
            开闭原则：
                允许增加新功能，不允许修改客户端代码。 客户端代码(在客户端运行的代码)
            单一职责：
                一个类只有一个改变的原因，一个类只干一件事
            依赖倒置：
                调用抽象(父类)，不要调用具体(子类)
                        抽象不要依赖具体
            组合复用：
                如果仅仅是代码上的复用，优先使用组合关系

        类于类的关系：
            泛化 (继承)（做成爸爸）
            关联 (做成成员变量)
            依赖 (做成方法参数)
"""

