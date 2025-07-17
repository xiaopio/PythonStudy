# _*_ encoding: utf-8 _*_
"""
PyCharm 09-多态
2025年07月17日 15时12分15秒
by LiXiaoYang
"""
# 多态：同一个行为，使用不同的对象获得不同的状态

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


class AC:
    def cool_wind(self):
        # 制冷
        pass

    def hot_wind(self):
        # 制热
        pass

    def swing_l_r(self):
        # 左右摆风
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


def make_hot(ac: AC):
    ac.hot_wind()


def swing(ac: AC):
    ac.swing_l_r()


midea_ac = Midea_AC()
gree_ac = Gree_AC()

make_cool(midea_ac)
make_cool(gree_ac)

make_hot(midea_ac)
make_hot(gree_ac)

swing(midea_ac)
swing(gree_ac)
