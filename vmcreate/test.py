# 定义一个名为Dog的类
class Dog:
    # 定义一个构造方法，它接受一个名字和品种参数，并将它们初始化为实例变量
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # 定义一个名为bark的方法，它打印出狗的名字和指示它正在叫的消息
    def bark(self):
        print(f"{self.name}正在叫！")

# 创建一个名为"Fido"，品种为"Golden Retriever"的Dog类实例
my_dog = Dog("Fido", "Golden Retriever")

# 在my_dog实例上调用bark方法
my_dog.bark()
