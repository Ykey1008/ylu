# Python基础

## 编程随笔

```
# 当 i % 2 == 0     ,判断是否取模等于0时    ，
# if i % 2  False线，也可以在if not i % 2 ，走TRUE线或者，取模出1,2等数，走TRUE线

# -------------------------------------------------------------------------------

# if 判断条件: 判断条件最好走正向， ==一类的，若判断！=，则在正向条件前加not，，活用not，，正向思维

# -------------------------------------------------------------------------------
#
# 浅拷贝是将数据拷贝一份赋予新的内存地址，前提是数据都是不可改变的数据如字符串，数字，元组，列表里镶嵌列表不行。
# 一旦数据中有可改变数据，如列表套列表，拷贝的a , b 变量的内存地址不同，但其中的元素引用的内存地址一样，修改备份数据，
# 原数据也会发生改变，注意浅拷贝变化比深拷贝复杂
# -------------------------------------------------------------------------------

# 深拷贝是将数据完全复制一份，赋予不同的内存地址，其数据中的可改变数据也是重新复制具有不同的内存地址，
# deepcopy(), 修改备份数据不影响上个数据。

# -------------------------------------------------------------------------------

# return 在函数中能够，直接结束循环
# -------------------------------------------------------------------------------

# 对于不可变类型，修改形参，不会影响实参，如数字，字符串，元组。同时修改数据，不可变类型的内存地址一定会发生变化
# 对于可改变类型，修改形参，也会影响实参，如列表，字典，集合，修改数据时，内存地址不会发生变化
# -------------------------------------------------------------------------------



```



## 1. 0 字符串 str

```
字符串str可以通过下标来获得指定的数据，下标从0开始，字符串是一个不可变的数据类型
```

```
x = 'ABCDEFGHI'
print(x[3])  # D 下标为3，第四个元素
print(x[-1])  # I  下标为-1 ，倒数第一个元素
print(x[2:5])  # CDE  从下标2切到下标5前面，前闭后开  [2:5)
print(x[0:8:2])  # ACEG  步长为2，隔一个取一个  ，步长不能为0
print(x[6:3:-1])  # GFE  -1指从右往左切，先从左边下标为6的，切到从左边下标为3的，第二个下标取不到，前闭后开，定好位置，从右边往左边切
print(x[::-1])  # 从右往左切，相当于倒序
print(x[:3])  # ABC [0:3）
print(x[3:])  # DEFGHI  从下标3到最后
print(x[:5:2])  # ACE   [0:5) 步长为2，隔一取一
```

```
len 内置函数可以获取字符串、列表、元组、字典等的长度
```

```
a = "hello python"print(len(a))
```

```
查找内容：find，index，rfind,rindex
find 获取指定字符在字符串里第一次出现的下标位置
可以指定开始和结束区间(包含开始，不包含结束区间)
如果查找不到指定字符，返回 -1
```

```
print(a.find('w', 6, 7))
print(a.find('x'))  # -1
```

```
# index 如果未找到指定的字符，会直接报错# print(a.index('x'))print(a.rfind('l'))print(a.find('l'))print(a.rindex('l'))# print(a.rindex('x'))
```

```
# 判断:startswith,endswith,isalpha,isdigit,isalnum,isspace
b = 'good morning'
print(b.startswith('s'))  # False
print(b.startswith('g'))  # True
print(b.endswith('g'))  # True
```

```
# isalpha 是否是纯字母
print(b.isalpha())  # False
print('hi'.isalpha())  # True
```

```
# isdigit 是否是纯数字
print(b.isdigit())  # False
print('123'.isdigit())  # True
print('123.454'.isdigit())  # False
print('Ⅲ'.isnumeric())
```

```
# isalnum  判断是否是有数字和字母组成
print('hello'.isalnum())  # Trueil-
print('123'.isalnum())  # True
print('hello123'.isalnum())  # True
print('hello.123'.isalnum())  # False
```

```
# isspace 判断是否全是空格
print('hello world'.isspace())  # False
print('    '.isspace())  # True
```

```
# 计算出现次数:count  可以指定start和end用来查找指定范围字符出现的次数
print('今天天气好晴朗，处处好风光呀好风光'.count('好'))
print('今天天气好晴朗，处处好风光呀好风光'.count('好', 0, 8))
# print('今天天气好晴朗，处处好风光呀好风光'.count('好', end=8, start=0))
```

```
# 替换内容:replace# oldchar:旧的字符
# newchar:替换后新的字符# 字符串是不可变的！！！
# replace 不会改变原有的字符串，而是得到一个新的字符串
# 这个新的字符串保存了修改后的结果
x = 'good'
y = x.replace('o', 'm')
print(x)  # good
print(y)  # gmmd
```

```
# 切割字符串:split,rsplit,splitlines,partition,rpartition
# split 使用指定的字符来对字符串进行分割，得到的结果是一个列表
# sep: 分隔符，要使用哪个字符来分割
# maxsplit: 最大分割数
z = 'hello_hi_how_good_better_bad_worse'
a = z.split('_')
print(a)
b = z.split('_', 1)
print(b)
print(z.rsplit('_', 1))
```

```
# splitlines是按照行来切割
# 注意和split('\r\n')的区别
print(z.splitlines())
m = 'hello\r\nhi\r\ngood\r\nbetter\r\n'
print(m.splitlines())
print(m.split('\r\n'))
```

```
# partition,rpartition
print('hello'.partition('e'))  # ('h', 'e', 'llo')
print(z.partition('_'))
print(z.rpartition('_'))
```

```
# 修改大小写:capitalize,title,upper,lower
# 第一个单词的首字母变大
print('hello world.hi\r\ngood'.capitalize())
# title 每个单词的首字母大写
print('hello world'.title())
```

```
# upper全大写；lower全小写
print('hello'.upper())
print('Hi'.lower())
```

```
# 空格处理:ljust,rjust,center,lstrip,rstrip,strip
print('yes'.ljust(10, "_"))  # 使用指定的字符左对齐填充到指定长度
print('no'.rjust(10, '-'))
print('you'.center(10, '*'))
```

```
print('    hello     '.lstrip())
print('    hello     '.rstrip())
print('    hello     '.strip())
print('hello,hi,good,yes,no'.split(','))
# 字符串拼接:join
print('-'.join(['你好', '热', 'hello', 'thanks']))  # 你好-热-hello-thanks
print('*'.join('abc'))  # a*b*c
```

## 1.1 字符串format()用法

```
# 使用 {} 作为占位符
s1 = '你好，我的名字是{},我今年{}岁了'.format('zhangsan', 18)print(s1)

# {数字}
s2 = '你好，我的名字是{0},我今年{1}岁了'.format('jerry', 20)
print(s2)

# format后面的参数个数可以多于前面占位符的个数
s3 = '你好，我的名字是{1},我今年{0}岁了,我同学也{0}岁了'.format(23, 'chris', 'hello')
print(s3)

# 使用关键字参数  {arg}
s4 = '你好，我的名字是{name},我今年{age}岁了'.format(age='32', name='tony', gender='female')
print(s4)

# 使用数字和关键字混合使用。
# 位置参数和关键字参数注意:关键字参数一定要写在位置参数的后面
# s5 = '你好，我的名字是{0},我今年{age}岁了.他的名字是{1}'.format(age=23,'tom', 'jerry')
s5 = '你好，我的名字是{1},我今年{age}岁了.他的名字是{0}'.format('tom', 'jerry', age=12)
print(s5)

# 使用空和关键字参数混合使用
s6 = '你好，我的名字是{},我今年{age}岁了.他的名字是{}'.format('rose', 'jack', age=18)
print(s6)

# 空和数字不能混合使用
# s6 = '你好，我的名字是{0},我今年{2}岁了.他的名字是{}'.format('rose', 'jack',18)
# print(s6)

# 可以传入一个元组或者列表
# 但是需要注意：元组或者列表需要添加 * 进行拆包
infos = ('henry', 18, 'helen')
s7 = '你好，我的名字是{},我今年{}岁了.他的名字是{}'.format(*infos)
print(s7)

# 可以传入一个字典，对应关键字参数
# 传入字典的时候，需要添加  ** 进行拆包
xxx = {'name': 'stark', 'age': 34, 'his_name': 'john'}
s8 = '你好，我的名字是{name},我今年{age}岁了.他的名字是{his_name}'.format(**xxx)
print(s8)

```



## 2. 元组tuple

```
# 元组和列表很像，也是用来保存一堆数据
# 区别：# 1. 表示方式不一样。列表使用[]或者list();元组使用()或者tuple
# 2. 列表是可变的，元组是不可变的！！！
# 如果是逗号，会把它当做一个元组
a = 1, 2, 3  
print(a)
b = (1, 2, 3)
```

```
# int() float()  str()  bool()  list()  tuple()
c = tuple((4, 5, 6))
print(c)
d = tuple([4, 5, 6])
print(d)
```

```
# 如何定义只有一个数据的元组(元素,)
y = ('hello',)
z = y
print(y)
print('x修改以前的地址是%X' % id(y))
```

```
# 元组是一个不可变的数据类型，它不支持添加元素和修改以及删除元素的操作
# x.append('hi')
# x[0] = 'yes'
# del x[0]
# print(x)
```

```
y = y + ('hi', 'good')
print(y)
print('y修改以后的地址是%X' % id(y))
print(z)
```

## 3. 列表list

创建列表的主要方式有 [ ]  和 list() 两种

```
# 列表里也可以放入数据，每个数据之间使用逗号来进行分割
# 一个数据我们称之为一个元素
# 一个列表里可以存放不能类型的数据，但是我们建议一个列表只存一种类型的数据，便于数据的管理
b = ['hello', 7, 'good', 23.45, True, 'hi']
```

```
# 使用list创建一个列表
x = list()  # 空列表
print(x)

# 还可以使用list创建列表并且插入元素
y = list((1, 2, 3, 4, 5))
print(y)
z = list([6, 7, 8, 9, 10])
print(z)
```

```
# 增删改查
names = ['张三', '李四', 'tom', 'jerry', 'chris', 'henry', 'tom', 'tony']

# 查找数据。len获取长度的
# 下标：从0开始，每个元素都有一个对应的位置
# 下标的取值范围  [0,len)
print(names[3])
print(names[-1])
print(names[len(names) - 1])

# name = input('请输入您要查找的姓名')
# if name in names:
#     value = names.index(name)
#     print('您要查找的姓名编号是%d' % value)
# else:
#     print('您查找的姓名不存在')

# value = names.rindex('helen')  列表没有rindex方法
# names.find('helen')   列表没有find方法

# 修改数据
# 列表是可变的
names[1] = '尼古拉斯赵四'
print(names)

# 往列表里加入数据
# append 在列表的最后面添加一个数据
names.append('stark')
print(names)
# insert 在指定位置插入数据
names.insert(2, '迪迦奥特曼')
print(names)
# extend可以加入多个数据，但是需要的参数是可迭代对象
names.extend(('jack', 'rose'))
print(names)
# 使用 + 运算符可以直接加入一个列表
names += ['苏克', '贝塔']
print(names)

# 删除数据
# pop 方法可以删除最后一个元素
# pop 方法还有一个返回值，返回被删掉的数据
result = names.pop()
print(result)
print(names)
# remove 可以移除指定的元素
# 如果被移除的元素不在列表里，remove方法会报错
names.remove('迪迦奥特曼')
print(names)
# names.remove('迪迦奥特曼')
# del 运算符可以删除指定位置的元素
del names[3]
print(names)
# del 运算符可以删除一个变量
# a = 2
# del a
# print(a + 1)

# 列表不支持减法运算
# names - ['henry']
# print(names)

# enumerate 实现带下标的遍历
for i, name in enumerate(names):
    print('第%d个姓名是%s' % (i, name))

# 3. 有一个组无序的数据，让这组数据实现升序排序
nums = [6, 5, 3, 1, 8, 7, 2, 4]
nums.sort(reverse=True)
print(nums)

```

## 4.字典 dict

```
#字典 dict
# 字典数据类型
# 字典也可以保存多个数据，保存数据的格式是以键值对的形式保存   key-value
# 每一对键值对之间使用 , 进行分割
# 使用一对 {} 来表示字典
# 字典里的key不允许重复，如果出现重复的kye,后出现的key会覆盖之前出现的kye
# value可以是任意类型的数据
info = {'name': 'zhangsan', 'gender': 'female', 'score': 89, 'height': 170, 'gender': 'male'}
print(info)
```

```
# 字典里的key 也可以是任意类型的数据，但是一般使用字符串作为字典的key
# info2 = {'ddd': 'hello', 0: 'hi', True: 'good'}
# print(info2)
```

```
# 使用dict 类也可以创建一个字典
# info = dict({'name': 'lisi'})
# print(info)
```

```
person = {'name': 'zhangsan', 'age': 18, 'gender': 'male'}

# 查找数据
# print(person[0])  字典里的数据不能通过下标来获取,字典里的数据是无序的

# 使用 [] 通过key来获取到对应的value
print(person['name'])  # 通过key可以获取到对应的value
# print(person['xxx'])  使用中括号语法来获取数据，如果对应的key不存在，会报错

# key = input('请输入你要查询的key:')
# if key in person:
#     print(person[key])
# else:
#     print('您要查找的key不存在')

# 使用get方法也可以获取一个数据
# 使用get方法来获取数据，如果key不存在，不会报错，会返回None
print(person.get('name'))  # get参数需要传入要查询的key
print(person.get('xxxx'))  # None

# get方法可以设置一个默认值
# 如果key存在，就获取key对应的值；如果key不存在，使用默认值
print(person.get('score', 89))  # 89
print(person.get('age', 34))  # 18
# get方法的默认值，不会改变原有的字典
print(person)

# 修改元素和增加元素的语法是一样的
# 如果key在字典里已经存在了，是修改；如果key在字典里不存在，是新增
# 修改数据
person['name'] = 'lisi'
print(person)

# 增加数据
person['address'] = '上海'
print(person)

# 删除数据
# 使用pop(key) 删除指定的key,并且返回对应的value
# print(person.pop('address'))  # 上海
# print(person)

# popitem 删除一个元素，并且返回元组。元组里有两个数据，第0个是被删除的key,第一个是value
# print(person.popitem())  # ('address', '上海')
# print(person)

# del 运算符也可以删除一个指定的元素
# del person['address']
# print(person)

person = {'name': 'zhangsan', 'age': 18, 'gender': 'male'}

# 如果使用for...in循环遍历一个字典，默认会拿到所有的key
# for x in person:
#     print('%s的值是%s' % (x, person[x]))

# 使用enumerate得到的x是下标，y是key
# for x, y in enumerate(person):
#     print('%s的值是%s' % (x, y))


# 拿到所有的key组成的一个列表
# ks = person.keys()
# print(ks)
# for k in ks:
#     print('%s的值是%s' % (k, person[k]))

# 拿到所有的值。只能拿到值
# vs = person.values()
# for v in vs:
#     print(v)

its = person.items()
print(its)  # [('name', 'zhangsan'), ('age', 18), ('gender', 'male')]
```

## 5.集合set

```
# set 数据结构有点儿像list,但是又使用 {} 而不是 [] 来包裹
# set 和 list 很像，但是它有一下几个特点
# 1. set 里的数据不允许重复
# 2. set 里的数据是无序的

# 表示一个空的set:使用set()来创建一个空的set
sss = set()
print(type(sss))  # <class 'set'>

xxx = {}  # 空字典，而不是一个空set
print(type(xxx))  # <class 'dict'>

# 使用 set 类
# provinces = {'湖北', '湖南', '河南', '安徽'}
provinces = set(('湖北', '湖南', '河南', '安徽'))
print(provinces)

companys = {'百度', '阿里', '华为'}
# add 只能添加一个元素
companys.add('腾讯')
print(companys)
# 把元组作为一个整体添加到set里
companys.add(('搜狗', '字节跳动'))
print(companys)

# update 添加多个数据
companys.update(('小米', '京东'))
print(companys)

# 随机移除一个元素
# companys.pop()
# print(companys)

# companys.remove('百度')
# print(companys)
```

## 6.random模块

```
import random

# randint(a,b) 生成[a,b]的随机整数
# print(random.randint(2, 4))

# randrang(a,b)  生成[a,b)的随机整数
print(random.randrange(2, 10))

# random() 生成 [0,1) 的随机浮点数
print(random.random())

# choice从列表里速记选取一个数据
print(random.choice(['hello', 'hi', 'how', 'are', 'you']))

# sample从列表里随机选择指定个数的元素  ,可以指定好列表参数，生成随机验证码
print(random.sample(['hello', 'hi', 'how', 'are', 'you'], 3))

```

# 闭包，装饰器

```

```

