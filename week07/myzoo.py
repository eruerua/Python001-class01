from abc import ABC,abstractmethod
class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.animals=[]
    def add_animal(self,animal):
        if animal not in self.animals:
            self.animals.append(animal)
        else:
            print('动物已添加，请添加另外一种动物')

    def __getattr__(self,item):
        for i in self.animals:
            if i.__class__.__name__ == item:
                return True
        return False


class Animal(ABC):#抽象类不可以实例化，可以继承
    @abstractmethod
    def __init__(self,a_type,a_size,a_character):
        self.a_type = a_type
        self.a_size = a_size
        self.a_character = a_character

    def a_ferocious(self):
        if (self.a_size == '中' or self.a_size == '大') and self.a_type =='食肉' and self.a_character == '凶猛':
            return True
        else:
            return False

class Cat(Animal):
    sound='喵喵'
    def __init__(self,name,a_type,a_size,a_character):
        super().__init__(a_type,a_size,a_character)
        self.name=name
    
    def is_pet(self):
        if self.a_character == '温顺':
            return True
        else:
            return False
    


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    #猫是不是凶猛动物
    print(cat1.a_ferocious())
    #猫是不是宠物
    print(cat1.is_pet())
    #猫的叫声
    print(cat1.sound)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    #不能重复添加同意动物
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    print(getattr(z, 'Cat'))
    #动物类不允许被实例化
    a = Animal()


