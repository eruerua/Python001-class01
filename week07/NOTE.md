学习笔记

本周作业难度不大，基本为课程内容，但是偏理论基础，这正是我学习的弱项，需要继续加强

## 1.基础知识

### [定义接口或者抽象基类](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p12_define_interface_or_abstract_base_class.html#id1)
1.抽象类的一个特点是它不能直接被实例化。
2.抽象类的目的就是让别的类继承它并实现特定的抽象方法。
3.抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口。
4.标准库中有很多用到抽象基类的地方。collections 模块定义了很多跟容器和迭代器(序列、映射、集合等)有关的抽象基类。 numbers 库定义了跟数字对象(整数、浮点数、有理数等)有关的基类。io 库定义了很多跟I/O操作相关的基类。

### [__new__和__init__的区别](https://juejin.im/post/6844903597143130120)
Python中真正的构造方法是\_\_new\__,\_\_new\_\_方法用于创建对象并返回对象，当返回对象时会自动调用\_\_init\_\_方法进行初始化。

应用：singleton 类只实例化一次

```
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2) 
```
### [__getattribute__ 和  __getattr__](https://www.jianshu.com/p/885d59db57fc)
1.getattr会在没有查找到相应实例属性时被调用
2.当访问某个实例属性时， getattribute会被无条件调用，如未实现自己的getattr方法，会抛出AttributeError提示找不到这个属性，如果自定义了自己getattr方法的话，方法会在这种找不到属性的情况下被调用.

