## python的内存管理机制

### 内存管理架构

python内存管理有两套实现 由编译符号 **PYMALLOC_DEBUG**控制，当该符号被定义时，使用的是debug模式下的内存管理机制，这套机制在正常的内存管理动作之外，还会记录许多关于内存的信息，以方便python在开发时进行调试；

![image-20201016164848325](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20201016164848325.png)

第一层是python在C的内存分配接口之上提供一层包装，以便统一接口；

第一层的实现是一组以PyMem_为前缀的函数族

~~~c
[pymem.h]
PyAPI_FUNC(void *) PyMem_Malloc(size_t);
PyAPI_FUNC(void *) PyMem_Realloc(void *, size_t);
PyAPI_FUNC(void) PyMem_Free(void *);

[object.c]
void* PyMem_Malloc(size_t nbytes);
{
    return PyMem_MALLOC(nbytes);
}

void* PyMem_Realloc(void *p, size_t nbytes);
{
    return PyMem_REALLOC(p, nbytes);
}

void PyMem_Free(void *p)
{
    PyMem_FREE(p);
}

[pymem.h]
#define PyMem_MALLOC(n)        malloc((n)?(n) : 1)
#define PyMem_REALLOC(p, n)    realloc((p), (n)?(n):1)
#define PyMem_FREE			   free

~~~

第二层：是以一组PyObject_为前缀的函数族，主要提供了创建Python对象的接口。这一套函数族又被唤作Pymalloc机制

第三层主要是对象的缓冲池机制

GC所在的内存管理机制在第二层

#### 小块空间的内存池

为了避免Python在运行期间大量的执行malloc和free导致操作系统频繁地在用户态和核心态之间进行切换造成的效率降低，Python引入了内存池机制，用于管理小块内存的申请和释放。

整个小块内存池可以视为一个层次结构，一共分为四层，从下至上分别是：block、pool、arena和内存池，“内存池”只是一个概念上的东西，表示Python对于整个小块内存分配和释放行为的内存管理机制

##### Block

所有的block的长度都是8字节对齐

block大小上限为256，当申请的内存大小超过上限时，Python就会将堆内存的请求转交给第一层的内存管理机制PyMem函数族来处理



block只是一个概念，在Python源码中没有与之对应的实体存在，Python提供了pool用来管理block

##### Pool

一组block的集合称为一个pool，即一个pool管理着一堆有固定大小的内存块。

一个pool的大小通常为一个系统内存页





### 循环引用的垃圾收集

#### 引用计数与垃圾收集

引用计数

优点：实时性

弱点：影响效率，循环引用



python引入清除和分代两种计数填补循环引用的问题

#### 三色标记模型

两个阶段：垃圾检测和垃圾回收

系统中所分配的所有对象之间的引用组成了一张有向图，对象为节点，对象之间的引用为边：

1. 假设所有对象都不可达，所有对象都标记为白色。
2. 从垃圾收集的动作开始，沿着始于root object集合中的某个object的引用链，将其标记为灰色，表示其可达，之后当检测了其中所包含的所有引用之后，再将其标记为黑色，表示被检查过了。



![image-20201016205224455](C:\Users\fruhling\AppData\Roaming\Typora\typora-user-images\image-20201016205224455.png)

#### python中的垃圾收集

​	主要的内存管理手段是引用计数，标记清楚和分代收集只是打破循环引用而引入的，因此只关注会产生循环引用的对象，即container对象，如list、dict、class、instance等等。

python采用双向链表将所有的container组织在一起进行跟踪处理。