# 第3章、字典和集合

散列表是字典类型性能出众的根本原因。

集合的实现其实也依赖于散列表

大纲：

- 常见的字典方法
- 如何处理查找不到的键
- 标准库中dict类型的变种
- set和frozenset类型
- 散列表的工作原理
- 散列表带来的潜在影响(什么样的数据类型可作为键、不可预知的顺序，等等)

## 3.1 泛映射类型

```python
>>> my_dict = {}
>>> isinstance(my_dict, abc.Mapping)
True
```

**字典的多种定义方法**

~~~python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
~~~

## 3.2 字典推导

~~~python
>>> DIAL_CODES = [ 
... (86, 'China'),
... (91, 'India'),
... (1, 'United States'),
... (62, 'Indonesia'),
... (55, 'Brazil'),
... (92, 'Pakistan'),
... (880, 'Bangladesh'),
... (234, 'Nigeria'),
... (7, 'Russia'),
... (81, 'Japan'),
... ]
>>> country_code = {country: code for code, country in DIAL_CODES} 
>>> country_code
{'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
234, 'Indonesia': 62}
>>> {code: country.upper() for country, code in country_code.items() 
... if code < 66}
{1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}
~~~

### 3.3 常见的映射方法

> 以下两种方法效果相同，但第一种更少的查询次数， 多用setdefault

~~~python
my_dict.setdefault(key, []).append(new_value)

if key not in my_dict:
my_dict[key] = []
my_dict[key].append(new_value)
~~~

- defaultdict

## 3.5 字典的变种

- collections.OrderDict
- collections.ChainMap
- collections.Counter

# 5. 一等函数

~~~python
>>> def reverse(word):
... return word[::-1]
>>> reverse('testing')
'gnitset'
>>> sorted(fruits, key=reverse)
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
>>>
~~~

**列表生成器和函数式编程的对比**

~~~python
>>> list(map(fact, range(6))) ➊
[1, 1, 2, 6, 24, 120]
>>> [fact(n) for n in range(6)] ➋
[1, 1, 2, 6, 24, 120]
>>> list(map(factorial, filter(lambda n: n % 2, range(6)))) ➌
[1, 6, 120]
>>> [factorial(n) for n in range(6) if n % 2] ➍
[1, 6, 120]
# 列表生成器可读性更强，还避免了lambda函数
~~~

**判断对象能否调用，可以用python的内置函数callable()**

python数据模型文档列出了7中可调用对象

1. 用户定义的函数

   使用def语句或lambda表示创建

2. 内置函数

   使用C语言(Cpython)实现的函数

3. 内置方法

   使用C语言实现的方法，如dict.get

4. 在类的定义体中定义的函数

5. 类

   调用类时会运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始
   化实例，最后把实例返回给调用方。因为 Python 没有 new 运算符，所以调用类相当于调
   用函数。

6. 类的实例

   如果类定义了 __call__ 方法，那么它的实例可以作为函数调用

7. 生成器函数

   使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象。

**用户定义的可调用类型**

~~~python
import random
class BingoCage:
	def __init__(self, items):
		self._items = list(items) 
		random.shuffle(self._items) 
	def pick(self): 
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')
	def __call__(self):
		return self.pick()

    
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True
~~~

列出常规对象没有而函数有的属性

~~~python
>>> class C: pass # ➊
>>> obj = C() # ➋
>>> def func(): pass # ➌
>>> sorted(set(dir(func)) - set(dir(obj))) # ➍
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__',
'__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
>>>
~~~

**生成html标签**

~~~python
def tag(name, *content, cls=None, **attrs):
"""生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) 
                           for attr, value in sorted(attrs.items()))
    else:
    	attr_str = ''
    if content:
    	return '\n'.join('<%s%s>%s</%s>' %
    					(name, attr_str, c, name) for c in content)
    else:
    	return '<%s%s />' % (name, attr_str)
    
>>> tag('br') ➊
'<br />'
>>> tag('p', 'hello') ➋
'<p>hello</p>'
>>> print(tag('p', 'hello', 'world'))
<p>hello</p>
<p>world</p>
>>> tag('p', 'hello', id=33) ➌
'<p id="33">hello</p>'
>>> print(tag('p', 'hello', 'world', cls='sidebar')) ➍
<p class="sidebar">hello</p>
<p class="sidebar">world</p>
>>> tag(content='testing', name="img") ➎
'<img content="testing" />'
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
... 'src': 'sunset.jpg', 'cls': 'framed'}
>>> tag(**my_tag) ➏
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
~~~

**指定长度截断字符串的函数**

~~~python
def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()

>>> from clip import clip
>>> clip.__defaults__
(80,)
>>> clip.__code__ # doctest: +ELLIPSIS
<code object clip at 0x...>
>>> clip.__code__.co_varnames
('text', 'max_len', 'end', 'space_before', 'space_after')
>>> clip.__code__.co_argcount
2


>>> from clip import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig # doctest: +ELLIPSIS
<inspect.Signature object at 0x...>
>>> str(sig)
'(text, max_len=80)'
>>> for name, param in sig.parameters.items():
... print(param.kind, ':', name, '=', param.default)
...
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
    
    
>>> import inspect
>>> sig = inspect.signature(tag) ➊
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
... 'src': 'sunset.jpg', 'cls': 'framed'}
>>> bound_args = sig.bind(**my_tag) ➋
>>> bound_args
<inspect.BoundArguments object at 0x...> ➌
>>> for name, value in bound_args.arguments.items(): ➍
... print(name, '=', value)
...
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
>>> del my_tag['name'] ➎
>>> bound_args = sig.bind(**my_tag) ➏
Traceback (most recent call last):
...
TypeError: 'name' parameter lacking default value
~~~

**attrgetter与itemgetter**

~~~python
metro_data = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for i in sorted(metro_data, key=itemgetter(0)):
    print(i)
    
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long') #
Metropolis = namedtuple('Metropolis', 'name cc pop coord') #
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,long=139.691667))
print(metro_areas[0].coord.lat)
from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat') #

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
~~~

**methodcaller详解**

可以冻结某些参数

~~~python
from operator import methodcaller


ss = "the time has come"

class MyMethod:
    def __init__(*args, **kwargs):
        if len(args) < 2:
            msg = "methodcaller needs at least one argument, the method name"
            raise TypeError(msg)
        self = args[0]
        self._name = args[1]
        if not isinstance(self._name, str):
            raise TypeError('method name must be a string')
        self._args = args[2:]
        self._kwargs = kwargs

    def __call__(self, obj):
        return getattr(obj, self._name)(*self._args, **self._kwargs)

print(methodcaller("upper")(ss))
m = MyMethod("upper")
print(m(ss))
print(getattr(ss, "upper")())
~~~

**partial**

~~~python
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(10))))
~~~

# 6. 设计模式

**经典策略模式**

~~~python
from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
            return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromotion(Promotion): #  第一个具体策略
    def discount(self, order):
        """为积分为1000或以上的顾客提供5%折扣"""
        return order.total()*0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromotion(Promotion):
    """单个商品为20个或以上时提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion): # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
~~~

**函数实现策略模式**

~~~python
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
            return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promotion(order):
    return order.total()*0.5 if order.customer.fidelity >= 1000 else 0


def bulk_item_promotion(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promotion(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, fidelity_promotion))
~~~

# 第7章、函数装饰器和闭包

###### 上一章策略模式的改进

~~~python
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)
~~~

###### 变量的作用域规则

~~~python
>>> b = 6
>>> def f2(a):
... print(a)
... print(b)
... b = 9
...
>>> f2(3)
3
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
~~~

> 对比两个函数

~~~python
>>> b = 6
>>> def f3(a):
... global b
... print(a)
... print(b)
... b = 9
...
>>> f3(3)
3
6
>>> b
9
>>> f3(3)
3
9
~~~

**nonlocal声明**

~~~python
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
~~~

###### 单分派泛函数

~~~python
import html
from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1,2,3}))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(abs))
print(htmlize(['alpha', 66, {3, 2, 1}]))
~~~

###### 叠放装饰器

~~~python
# 以下两种形式等价

@d1
@d2
def f():
    print('f')

def f():
	print('f')
f = d1(d2(f))
~~~

###### 参数化装饰器

~~~python
registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))

        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f2()')

print(registry)

register()(f3)
print(registry)
~~~

###### 参数化clock装饰器

~~~python
import time
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

    @clock('{name}:{elapsed}s')
    def snooze2(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze2(0.123)


    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze3(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze3(0.123)
~~~

# 第8章 对象引用、可变性和垃圾回收

##### 变量是标注，而不是盒子

##### 在==和is之间选择

每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变；你可以把标识理解为对象在内存中的地址。is 运算符比较两个对象的标识；id() 函数返回对象标识的整数表示。

##### 函数的参数作为引用时

python唯一支持的参数传递模式是共享传参(call by sharing)。

共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名。

这种方案的结果是，函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识（即不能把一个对象替换成另一个对象）

~~~python
>>> def f(a, b):
... a += b
... return a
...
>>> x = 1
>>> y = 2
>>> f(x, y)
3
>>> x, y ➊
(1, 2)
>>> a = [1, 2]
>>> b = [3, 4]
>>> f(a, b)
[1, 2, 3, 4]
>>> a, b ➋
([1, 2, 3, 4], [3, 4])
>>> t = (10, 20)
>>> u = (30, 40)
>>> f(t, u)
(10, 20, 30, 40)
>>> t, u ➌
((10, 20), (30, 40))
~~~

**不要将可变对象作为参数的默认值**

**防御可变参数**

~~~python
def __init__(self, passengers=None):
    if passengers is None:
    	self.passengers = []
    else:
    	self.passengers = list(passengers)
~~~

##### 弱引用

弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们说，弱引用不会妨碍所指对象被当作垃圾回收

~~~python
>>> import weakref
>>> a_set = {0, 1}
>>> wref = weakref.ref(a_set) ➊
>>> wref
<weakref at 0x100637598; to 'set' at 0x100636748>
>>> wref() ➋
{0, 1}
>>> a_set = {2, 3, 4} ➌
>>> wref() ➍
{0, 1}
>>> wref() is None ➎
False
>>> wref() is None ➏
True
~~~

弱引用的局限

不是每个 Python 对象都可以作为弱引用的目标（或称所指对象）。基本的 list 和 dict实例不能作为所指对象，但是它们的子类可以轻松地解决这个问题：

~~~python
class MyList(list):
"""list的子类，实例可以作为弱引用的目标"""
a_list = MyList(range(10))

a_list可以作为弱引用的目标

wref_to_a_list = weakref.ref(a_list)
~~~

set 实例可以作为所指对象，用户定义的类型也没问题，但是，int 和 tuple 实
例不能作为弱引用的目标，甚至它们的子类也不行

# 第9章、符合python风格的对象

##### classmethod和staticmethod

~~~python
>>> class Demo:
... @classmethod
... def klassmeth(*args):
... return args # ➊
... @staticmethod
... def statmeth(*args):
... return args # ➋
...
>>> Demo.klassmeth() # ➌
(<class '__main__.Demo'>,)
>>> Demo.klassmeth('spam')
(<class '__main__.Demo'>, 'spam')
>>> Demo.statmeth() # ➍
()
>>> Demo.statmeth('spam')
('spam',)
~~~

**\_\_slots\_\_的使用**

在类中声明 \_\_slots\_\_属性可以防止设置新实例属性

不建议只为了避免创建实例属性而使用 __slots__ 属性。__slots__ 属性只应该用于节省内存，而且仅当内存严重不足时才应该这么做

# 第10章、序列的修改散列和切片

**__getattr__的查找顺序**

对 my_obj.x 表达式，Python 会检查 my_obj 实例有没有名为 x 的属性；如果没有，到类（my_obj.__class__）中查找；如果还没有，顺着继承树继续查找。 如果依旧找不到，调用 my_obj 所属类中定义的 __getattr__ 方法，传入self 和属性名称的字符串形式（如 'x'）

~~~python
>>> v = Vector(range(5))
>>> v
Vector([0.0, 1.0, 2.0, 3.0, 4.0])
>>> v.x # ➊
0.0
>>> v.x = 10 # ➋
>>> v.x # ➌
10
>>> v
Vector([0.0, 1.0, 2.0, 3.0, 4.0]) # 并没有将第一个数修改为10，这是getattr的后备机制导致的
~~~

zip

~~~python
def __eq__(self, other):
	return len(self) == len(other) and all(a == b for a, b in zip(self, other))
~~~

~~~python
>>> zip(range(3), 'ABC') # ➊
<zip object at 0x10063ae48>
>>> list(zip(range(3), 'ABC')) # ➋
[(0, 'A'), (1, 'B'), (2, 'C')]
>>> list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])) # ➌
[(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]
>>> from itertools import zip_longest # ➍
>>> list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
[(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]
~~~

# 第11章、接口、从协议到抽象基类

##### python没有真正意义上的受保护变量和私有变量

~~~python
class Student:
    def __init__(self):
        self._name = 'zhangsan'
        self.__name = 'lisi'

    def name(self):
        return self._name

s = Student()
print(s._name) # zhangsan
print(s._Student__name) # lisi
设置私有属性在子类继承的时候子类也会生成相应的私有属性
~~~

##### getitem

~~~python
>>> class Foo:
... def __getitem__(self, pos):
... return range(0, 30, 10)[pos]
...
>>> f = Foo()
>>> f[1]
10
>>> for i in f: print(i)
...
0
10
20
>>> 20 in f
True
>>> 15 in f
False

虽然没有 __iter__ 方法，但是 Foo 实例是可迭代的对象，因为发现有 __getitem__ 方法时，Python 会调用它，传入从 0 开始的整数索引，尝试迭代对象（这是一种后备机制）。尽管没有实现 __contains__ 方法，但是 Python 足够智能，能迭代 Foo 实例，因此也能使用 in 运算符：Python 会做全面检查，看看有没有指定的元素。
综上，鉴于序列协议的重要性，如果没有 __iter__ 和 __contains__ 方法，Python 会调用 __getitem__ 方法，设法让迭代和 in 运算符可用
~~~

##### 使用猴子补丁在运行时实现协议

~~~python
from collections import namedtuple
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
shuffle(deck)
    
Traceback (most recent call last):
  File "D:/Files/fluent_python/chapter11/poker_shuffle.py", line 9, in <module>
    shuffle(deck)
  File "D:\work_Files\anaconda3\lib\random.py", line 278, in shuffle
[0, 6, 7, 4, 3, 1, 2, 5, 8, 9]
    x[i], x[j] = x[j], x[i]
TypeError: 'FrenchDeck' object does not support item assignment
    
    
    
>>> def set_card(deck, position, card): ➊
... deck._cards[position] = card
...
>>> FrenchDeck.__setitem__ = set_card ➋
>>> shuffle(deck) ➌
>>> deck[:5]
[Card(rank='3', suit='hearts'), Card(rank='4', suit='diamonds'), Card(rank='4',
suit='clubs'), Card(rank='7', suit='hearts'), Card(rank='9', suit='spades')]
~~~

这里的关键是，set_card 函数要知道 deck 对象有一个名为 _cards 的属性，而且_cards 的值必须是可变序列。然后，我们把 set_card 函数赋值给特殊方法_\_setitem__，从而把它依附到 FrenchDeck 类上。这种技术叫猴子补丁：在运行时修改类或模块，而不改动源码。猴子补丁很强大，但是打补丁的代码与要打补丁的程序耦合十分紧密，而且往往要处理隐藏和没有文档的部分。

##### Alex的水禽

~~~python
>>> class Struggle:
... def __len__(self): return 23
...
>>> from collections import abc
>>> isinstance(Struggle(), abc.Sized)
Ture
~~~

##### collections.abc模块中的抽象

![image-20200831175618842](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831175618842.png)

Iterable、Container 和 Sized各个集合应该继承这三个抽象基类，或者至少实现兼容的协议。Iterable 通过
__iter__ 方法支持迭代，Container 通过 __contains__ 方法支持 in 运算符，Sized通过 __len__ 方法支持 len() 函数

##### 异常类的部分层次结构

![image-20200831182034093](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831182034093.png)

在函数上堆叠装饰器的顺序通常很重要，@abstractmethod 的文档就特别指出：
与其他方法描述符一起使用时，abstractmethod() 应该放在最里层，……
也就是说，在 @abstractmethod 和 def 语句之间不能有其他装饰器。



##### Tombola的虚拟子类

```python
# tombola.py
import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素， 然后将其返回
        如果实例为空，这个方法应该抛出‘LookupError’。
        """

    def loaded(self):
        """如果至少有一个元素，返回‘True’，否则返回‘False’。"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成。"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
```

```python
# tombolist.py
from random import randrange
from tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)


print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))
print(t.pick())
print(TomboList.__mro__)

# 输出
True 
True
95
(<class '__main__.TomboList'>, <class 'list'>, <class 'object'>)
```

![image-20200831211123215](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831211123215.png)

##### 鹅的行为可能像鸭子

~~~python
class Sized(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod
    def __len__(self):
    	return 0
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__): 
            return True
        return NotImplemented
~~~

# 第12章、多重继承

##### 避免继承list，dict，string等内置类

会出现一些意想不到的的意外

使用UserDict,UserList,UserString等

> 综上，本节所述的问题只发生在 C 语言实现的内置类型内部的方法委托上，而且只影响
> 直接继承内置类型的用户自定义类。如果子类化使用 Python 编写的类，如 UserDict 或
> MutableMapping，就不会受此影响。

~~~python
查看几个类的__mro__属性
>>> bool.__mro__ ➊
(<class 'bool'>, <class 'int'>, <class 'object'>)
>>> def print_mro(cls): ➋
... print(', '.join(c.__name__ for c in cls.__mro__))
...
>>> print_mro(bool)
bool, int, object
>>> from frenchdeck2 import FrenchDeck2
>>> print_mro(FrenchDeck2) ➌
FrenchDeck2, MutableSequence, Sequence, Sized, Iterable, Container, object
>>> import numbers
>>> print_mro(numbers.Integral) ➍
Integral, Rational, Real, Complex, Number, object
>>> import io ➎
>>> print_mro(io.BytesIO)
BytesIO, _BufferedIOBase, _IOBase, object
>>> print_mro(io.TextIOWrapper)
TextIOWrapper, _TextIOBase, _IOBase, object
~~~

**tkinter中的Text的继承图**

![image-20200831223510952](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831223510952.png)

![image-20200831223820080](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831223820080.png)

~~~python
>>> import tkinter
>>> print_mro(tkinter.Toplevel)
Toplevel, BaseWidget, Misc, Wm, object
>>> print_mro(tkinter.Widget)
Widget, BaseWidget, Misc, Pack, Place, Grid, object
>>> print_mro(tkinter.Button)
Button, Widget, BaseWidget, Misc, Pack, Place, Grid, object
>>> print_mro(tkinter.Entry)
Entry, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, object
>>> print_mro(tkinter.Text)
Text, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, YView, object
~~~

##### django通用视图

![image-20200831232006366](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831232006366.png)

![image-20200831232459942](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200831232459942.png)

# 第13章。正确重载运算符

~~~python
def __add__(self, other):
    pairs = itertools.zip_longest(self, other, fillvalue=0.0) # ➊
    return Vector(a + b for a, b in pairs)


>>> v1 = Vector([3, 4, 5, 6])
>>> v3 = Vector([1, 2])
>>> v1 + v3
Vector([4.0, 6.0, 5.0, 6.0])


def __add__(self, other):
    try:
    	pairs = itertools.zip_longest(self, other, fillvalue=0.0)
    	return Vector(a + b for a, b in pairs)
    except TypeError:
    	return NotImplemented
    
    def __radd__(self, other):
    	return self + other
    
    
class Vector:
    typecode = 'd'
    def __init__(self, components):
    	self._components = array(self.typecode, components)

    def __mul__(self, scalar):
    	if isinstance(scalar, numbers.Real):
    		return Vector(n * scalar for n in self)
    	else:
    		return NotImplemented
    def __rmul__(self, scalar):
    	return self * scalar
~~~

不能重载内置类型的运算符
不能新建运算符，只能重载现有的
某些运算符不能重载——is、and、or 和 not（不过位运算符 &、| 和 ~ 可以）

# 第14章、可迭代的对象、迭代器和生成器

**迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。这就是迭代器模式（Iterator pattern）**

在 Python 中，所有集合都可以迭代。在 Python 语言内部，迭代器用于支持：

- for循环
- 构建和扩展集合类型
- 逐行遍历文本文件
- 列表推导、字典推导和集合推导
- 元组拆包
- 调用函数时，使用*拆包实参

~~~python
>>> class Foo:
... def __iter__(self):
... pass
...
>>> from collections import abc
>>> issubclass(Foo, abc.Iterable)
True
>>> f = Foo()
>>> isinstance(f, abc.Iterable)
True
~~~



##### 可迭代的对象与迭代器的对比

~~~python
下面是一个简单的 for 循环，迭代一个字符串。这里，字符串 'ABC' 是可迭代的对象。背后是有迭代器的，只不过我们看不到
>>> s = 'ABC'
>>> for char in s:
... print(char)
...
A
B
C


>>> s = 'ABC'
>>> it = iter(s) # ➊
>>> while True:
... try:
... print(next(it)) # ➋
... except StopIteration: # ➌
... del it # ➍
... break # ➎
...
A
B
C
~~~

**迭代器是这样的对象：实现了无参数的 __next__ 方法，返回序列中的下一个元素；如果没有元素了，那么抛出 StopIteration 异常。Python 中的迭代器还实现了\_\_iter__ 方法，因此迭代器也可以迭代**



**把Sentence变成迭代器：坏主意
构建可迭代的对象和迭代器时经常会出现错误，原因是混淆了二者。要知道，可迭代的对
象有个 __iter__ 方法，每次都实例化一个新的迭代器；而迭代器要实现 __next__ 方
法，返回单个元素，此外还要实现 __iter__ 方法，返回迭代器本身。
因此，迭代器可以迭代，但是可迭代的对象不是迭代器。**



迭代器模式可用来：

- 访问一个聚合对象的内容而无需暴露它的内部表示
- 支持对聚合对象的多种遍历
- 为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）

##### 生成器函数的工作原理

只要 Python 函数的定义体中有 yield 关键字，该函数就是生成器函数。调用生成器函数时，会返回一个生成器对象。也就是说，生成器函数是生成器工厂。

##### 生成器表达式

**生成器表达式是语法糖：完全可以替换成生成器函数，不过有时使用生成器表达式更便利**

~~~python
import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
    	self.text = text
    def __repr__(self):
    	return 'Sentence(%s)' % reprlib.repr(self.text)
    def __iter__(self):
    	return (match.group() for match in RE_WORD.finditer(self.text))
~~~

生成器表达式和列表推导式的区别是小括号和中括号

![image-20200901162044537](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901162044537.png)

##### 等差数列生成器

itertools中的生成器

~~~python
import itertools
gen = itertools.count(1, .5)

print(next(gen))
print(next(gen))

gen = itertools.takewhile(lambda n: n<3, itertools.count(1,.5))

print(list(gen))


1
1.5
[1, 1.5, 2.0, 2.5]
~~~

~~~python
import itertools


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


"""
注意，示例中的 aritprog_gen 不是生成器函数，因为定义体中没有 yield 关键
字。但是它会返回一个生成器，因此它与其他生成器函数一样，也是生成器工厂函数
"""
~~~

##### 标准库中的生成器

![image-20200901170832171](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901170832171.png)

~~~python
>>> def vowel(c):
... return c.lower() in 'aeiou'
...
>>> list(filter(vowel, 'Aardvark'))
['A', 'a', 'a']
>>> import itertools
>>> list(itertools.filterfalse(vowel, 'Aardvark'))
['r', 'd', 'v', 'r', 'k']
>>> list(itertools.dropwhile(vowel, 'Aardvark'))
['r', 'd', 'v', 'a', 'r', 'k']
>>> list(itertools.takewhile(vowel, 'Aardvark'))
['A', 'a']
>>> list(itertools.compress('Aardvark', (1,0,1,1,0,1)))
['A', 'r', 'd', 'a']
>>> list(itertools.islice('Aardvark', 4))
['A', 'a', 'r', 'd']
>>> list(itertools.islice('Aardvark', 4, 7))
['v', 'a', 'r']
>>> list(itertools.islice('Aardvark', 1, 7, 2))
['a', 'd', 'a']
~~~

![image-20200901171516880](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901171516880.png)

~~~python
>>> sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
>>> import itertools
>>> list(itertools.accumulate(sample)) # ➊
[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
>>> list(itertools.accumulate(sample, min)) # ➋
[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
>>> list(itertools.accumulate(sample, max)) # ➌
[5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
>>> import operator
>>> list(itertools.accumulate(sample, operator.mul)) # ➍
[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
>>> list(itertools.accumulate(range(1, 11), operator.mul))
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


>>> list(enumerate('albatroz', 1)) # ➊
[(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]
>>> import operator
>>> list(map(operator.mul, range(11), range(11))) # ➋
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> list(map(operator.mul, range(11), [2, 4, 8])) # ➌
[0, 4, 16]
>>> list(map(lambda a, b: (a, b), range(11), [2, 4, 8])) # ➍
[(0, 2), (1, 4), (2, 8)]
>>> import itertools
>>> list(itertools.starmap(operator.mul, enumerate('albatroz', 1))) # ➎
['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
>>> sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
>>> list(itertools.starmap(lambda a, b: b/a,
... enumerate(itertools.accumulate(sample), 1))) # ➏
[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
5.0, 4.375, 4.888888888888889, 4.5]
~~~

![image-20200901172343767](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901172343767.png)

~~~python
>>> list(itertools.chain('ABC', range(2))) # ➊
['A', 'B', 'C', 0, 1]
>>> list(itertools.chain(enumerate('ABC'))) # ➋
[(0, 'A'), (1, 'B'), (2, 'C')]
>>> list(itertools.chain.from_iterable(enumerate('ABC'))) # ➌
[0, 'A', 1, 'B', 2, 'C']
>>> list(zip('ABC', range(5))) # ➍
[('A', 0), ('B', 1), ('C', 2)]
>>> list(zip('ABC', range(5), [10, 20, 30, 40])) # ➎
[('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
>>> list(itertools.zip_longest('ABC', range(5))) # ➏
[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
>>> list(itertools.zip_longest('ABC', range(5), fillvalue='?')) # ➐
[('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]



>>> list(itertools.product('ABC', range(2))) # ➊
[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
>>> suits = 'spades hearts diamonds clubs'.split()
>>> list(itertools.product('AK', suits)) # ➋
[('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
>>> list(itertools.product('ABC')) # ➌
[('A',), ('B',), ('C',)]
>>> list(itertools.product('ABC', repeat=2)) # ➍
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
>>> list(itertools.product(range(2), repeat=3))
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
(1, 0, 1), (1, 1, 0), (1, 1, 1)]
>>> rows = itertools.product('AB', range(2), repeat=2)
>>> for row in rows: print(row)
...
('A', 0, 'A', 0)
('A', 0, 'A', 1)
('A', 0, 'B', 0)
('A', 0, 'B', 1)
('A', 1, 'A', 0)
('A', 1, 'A', 1)
('A', 1, 'B', 0)
('A', 1, 'B', 1)
('B', 0, 'A', 0)
('B', 0, 'A', 1)
('B', 0, 'B', 0)
('B', 0, 'B', 1)
('B', 1, 'A', 0)
('B', 1, 'A', 1)
('B', 1, 'B', 0)
('B', 1, 'B', 1)
~~~

![image-20200901173009466](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901173009466.png)

~~~python
>>> ct = itertools.count() # ➊
>>> next(ct) # ➋
0
>>> next(ct), next(ct), next(ct) # ➌
(1, 2, 3)
>>> list(itertools.islice(itertools.count(1, .3), 3)) # ➍
[1, 1.3, 1.6]
>>> cy = itertools.cycle('ABC') # ➎
>>> next(cy)
'A'
>>> list(itertools.islice(cy, 7)) # ➏
['B', 'C', 'A', 'B', 'C', 'A', 'B']
>>> rp = itertools.repeat(7) # ➐
>>> next(rp), next(rp)
(7, 7)
>>> list(itertools.repeat(8, 4)) # ➑
[8, 8, 8, 8]
>>> list(map(operator.mul, range(11), itertools.repeat(5))) # ➒
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
~~~

~~~python
>>> list(itertools.combinations('ABC', 2)) # ➊
[('A', 'B'), ('A', 'C'), ('B', 'C')]
>>> list(itertools.combinations_with_replacement('ABC', 2)) # ➋
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
>>> list(itertools.permutations('ABC', 2)) # ➌
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
>>> list(itertools.product('ABC', repeat=2)) # ➍
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'),
('C', 'A'), ('C', 'B'), ('C', 'C')]
~~~

![image-20200901174147494](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901174147494.png)

~~~PYTHON
>>> list(itertools.groupby('LLLLAAGGG')) # ➊
[('L', <itertools._grouper object at 0x102227cc0>),
('A', <itertools._grouper object at 0x102227b38>),
('G', <itertools._grouper object at 0x102227b70>)]
>>> for char, group in itertools.groupby('LLLLAAAGG'): # ➋
... print(char, '->', list(group))
...
L -> ['L', 'L', 'L', 'L']
A -> ['A', 'A',]
G -> ['G', 'G', 'G']
>>> animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
... 'bat', 'dolphin', 'shark', 'lion']
>>> animals.sort(key=len) # ➌
>>> animals
['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark',
'giraffe', 'dolphin']
>>> for length, group in itertools.groupby(animals, len): # ➍
... print(length, '->', list(group))
...
3 -> ['rat', 'bat']
4 -> ['duck', 'bear', 'lion']
5 -> ['eagle', 'shark']
7 -> ['giraffe', 'dolphin']
>>> for length, group in itertools.groupby(reversed(animals), len): # ➎
... print(length, '->', list(group))
...
7 -> ['dolphin', 'giraffe']
5 -> ['shark', 'eagle']
4 -> ['lion', 'bear', 'duck']
3 -> ['bat', 'rat']



>>> list(itertools.tee('ABC'))
[<itertools._tee object at 0x10222abc8>, <itertools._tee object at 0x10222ac08>]
>>> g1, g2 = itertools.tee('ABC')
>>> next(g1)
'A'
>>> next(g2)
'A'
>>> next(g2)
'B'
>>> list(g1)
['B', 'C']
>>> list(g2)
['C']
>>> list(zip(*itertools.tee('ABC')))
[('A', 'A'), ('B', 'B'), ('C', 'C')]
~~~

##### yield from

~~~python
>>> def chain(*iterables):
... for it in iterables:
... for i in it:
... yield i
...
>>> s = 'ABC'
>>> t = tuple(range(3))
>>> list(chain(s, t))
['A', 'B', 'C', 0, 1, 2]


>>> def chain(*iterables):
... for i in iterables:
... yield from i
...
>>> list(chain(s, t))
['A', 'B', 'C', 0, 1, 2]


可以看出，yield from i 完全代替了内层的 for 循环。在这个示例中使用 yield from
是对的，而且代码读起来更顺畅，不过感觉更像是语法糖。除了代替循环之外，yield
from 还会创建通道，把内层生成器直接与外层生成器的客户端联系起来。把生成器当成
协程使用时，这个通道特别重要，不仅能为客户端代码生成值，还能使用客户端代码提供
的值。第 16 章会深入讲解协程，其中有几页会说明为什么 yield from 不只是语法糖而
已。
~~~

##### 可迭代的归约函数

![image-20200901185525892](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901185525892.png)

# 第15章、上下文管理器和 else 块

else 子句的行为如下。
for
仅当 for 循环运行完毕时（即 for 循环没有被 break 语句中止）才运行 else 块。
while
仅当 while 循环因为条件为假值而退出时（即 while 循环没有被 break 语句中止）
才运行 else 块。
try
仅当 try 块中没有异常抛出时才运行 else 块

~~~python
for item in my_list:
	if item.flavor == 'banana':
		break
else:
	raise ValueError('No banana flavor found!')
~~~

##### 上下文管理器和with块

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。with 语句开始运行时，会在上下文管理器对象上调用 \_\_enter__ 方法。with 语句运行结束后，会在上下文管理器对象上调用 \_\_exit__ 方法，以此扮演 finally 子句的角色。

> 上下文管理器是相当新颖的特性，Python 社区肯定还在不断寻找新的创意用法。标准库中
> 有一些示例。
>
> - 在 sqlite3 模块中用于管理事务，参见“12.6.7.3. Using the connection as a context
>   manager”（https://docs.python.org/3/library/sqlite3.html#using-the-connection-as-a-context-manager）。
> - 在 threading 模块中用于维护锁、条件和信号，参见“17.1.10. Using locks, conditions,
>   and semaphores in the with statement”（https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement）。
> - 为 Decimal 对象的算术运算设置环境，参见 decimal.localcontext 函数的文档
>   （https://docs.python.org/3/library/decimal.html#decimal.localcontext）。
> - 为了测试临时给对象打补丁，参见 unittest.mock.patch 函数的文档
>   （https://docs.python.org/3/library/unittest.mock.html#patch）。

##### contextlib模块中的实用工具

closing
如果对象提供了 close() 方法，但没有实现 __enter__/__exit__ 协议，那么可以
使用这个函数构建上下文管理器。
suppress
构建临时忽略指定异常的上下文管理器。
@contextmanager
这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器
协议了。
ContextDecorator
这是个基类，用于定义基于类的上下文管理器。这种上下文管理器也能用于装饰函
数，在受管理的上下文中运行整个函数。
ExitStack
这个上下文管理器能进入多个上下文管理器。with 块结束时，ExitStack 按照后进
先出的顺序调用栈中各个上下文管理器的 __exit__ 方法。如果事先不知道 with 块要进
入多少个上下文管理器，可以使用这个类。例如，同时打开任意一个文件列表中的所有文
件。
显然，在这些实用工具中，使用最广泛的是 @contextmanager 装饰器，因此要格外留
心。这个装饰器也有迷惑人的一面，因为它与迭代无关，却要使用 yield 语句。由此可
以引出协程，这是下一章的主题。

##### 使用@contextmanager

![image-20200901215119057](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200901215119057.png)

~~~python
import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
~~~

# 第16章、协程

##### 用作协程的生成器的基本行为

协程可以身处四个状态中的一个。当前状态可以使用inspect.getgeneratorstate(...) 函数确定，该函数会返回下述字符串中的一个。

- GEN_CREATED

  等待开始执行

- GEN_RUNNING

  解释器正在执行

- GEN_SUSPENDED

  在yield表达式处暂停

- GEN_CLOSED

  执行结束

~~~python
>>> def simple_coro2(a):
... print('-> Started: a =', a)
... b = yield a
... print('-> Received: b =', b)
... c = yield a + b
... print('-> Received: c =', c)
...
>>> my_coro2 = simple_coro2(14)
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(my_coro2) ➊
'GEN_CREATED'
>>> next(my_coro2) ➋
-> Started: a = 14
14
>>> getgeneratorstate(my_coro2) ➌
'GEN_SUSPENDED'
>>> my_coro2.send(28) ➍
-> Received: b = 28
42
>>> my_coro2.send(99) ➎
-> Received: c = 99
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>> getgeneratorstate(my_coro2) ➏
'GEN_CLOSED
~~~

##### 使用协程计算移动平均值

~~~python
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
~~~

##### 预激协程的装饰器

~~~python
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
~~~

##### 终止协程和异常处理

~~~python
class DemoException(Exception):
    """为这次演示定义的异常类型"""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')
~~~

~~~python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
本文档由Linux公社 www.linuxidc.com 整理
 >>> exc_coro.send(22)
-> coroutine received: 22
>>> exc_coro.close()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
~~~

~~~python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(DemoException)
*** DemoException handled. Continuing...
>>> getgeneratorstate(exc_coro)
'GEN_SUSPENDED'
~~~

~~~python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(ZeroDivisionError)
Traceback (most recent call last):
...
ZeroDivisionError
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
~~~

##### 使用yield from

~~~python
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


if __name__ == '__main__':
    main(data)
~~~



![image-20200902012405903](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200902012405903.png)

##### yield from 的意义

![image-20200902020652161](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200902020652161.png)

##### 出租车队运营仿真

~~~python
from collections import namedtuple
import queue
import random
Event = namedtuple('Event', 'time proc action')
DEPARTURE_INTERVAL = 5


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')

    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')


def compute_duration(previous_action):
    if previous_action in ['leave garage', 'drop off passenger']:
        interval = 5
    elif previous_action == 'pick up passenger':
        interval = 20
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1 / interval)) + 1


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '    ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


num_taxis = 3
taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
         for i in range(num_taxis)}
sim = Simulator(taxis)


if __name__ == '__main__':
    sim.run(100)
~~~

# 第17章、使用期物处理并发

##### 阻塞型I/O和GIL

CPython 解释器本身就不是线程安全的，因此有全局解释器（GIL），一次只允许使用一个线程执行 Python 字节码。因此，一个 Python 进程通常不能同时使用多个 CPU 核心。

> Python 标准库中的所有阻塞型 I/O 函数都会释放 GIL，允许其他线程运行。time.sleep() 函数也会释放 GIL。因此，尽管有 GIL，Python 线程还是能在 I/O密集型应用中发挥作用。

##### Executor.map方法

```python
from time import sleep, strftime
from concurrent import futures


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


main()


[19:05:32] Script starting.
[19:05:32] loiter(0): doing nothing for 0s...
[19:05:32][19:05:32] loiter(0): done.
 	loiter(1): doing nothing for 1s...
[19:05:32] 		loiter(2): doing nothing for 2s...
[19:05:32][19:05:32] 			loiter(3): doing nothing for 3s...
 results: <generator object Executor.map.<locals>.result_iterator at 0x000001E09A61D660>
[19:05:32] Waiting for individual results:
[19:05:32] result 0: 0
[19:05:33] 	loiter(1): done.
[19:05:33][19:05:33]  				loiter(4): doing nothing for 4s...result 1: 10

[19:05:34] 		loiter(2): done.
[19:05:34] result 2: 20
[19:05:35] 			loiter(3): done.
[19:05:35] result 3: 30
[19:05:37] 				loiter(4): done.
[19:05:37] result 4: 40
```

##### 显示下载进度并处理错误

> 进度条tqdm的使用
>
> pip install tqdm
>
> ~~~python
> >>> import time
> >>> from tqdm import tqdm
> >>> for i in tqdm(range(1000)):
> ... time.sleep(.01)
> ...
> >>> # -> 进度条会出现在这里 <-
> ~~~

# 第18章、使用asyncio包处理并发

![image-20200902194934864](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20200902194934864.png)

# 第19章、动态属性和特性

