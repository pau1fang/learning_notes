# 二、分区

### 1、基本概念

1. **扇区**
2. **柱面**

## 2、MBR(MS-DOS)与GPT磁盘分区表(partition table)

#### 2.1 MBR

- 主引导记录：可以安装启动引导程序的地方，有466字节；
- 分区表：记录整块硬盘分区的状态，有64字节。

由于分区表所在区块仅有64字节容量，因此最多仅能有四组记录区，每组记录区记录了该区段的起始与结束的柱面号码。

- - 其实所谓的分区只是针对那个64字节的分区表进行设置而已
  - 硬盘默认的分区仅能写入四组分区信息
  - 这四组划分信息我们成为主要(primary)或扩展(Extended)分区
  - 分区的最小单位通常为柱面(Cylinder)
  - 当系统要写入磁盘时，一定会参考磁盘分区表，才能针对某个分区进行数据的处理
- 分区的目的
- 1. 数据的安全性
  2. 系统的性能考虑

###### MBR主要分区、扩展分区与逻辑分区的特性简单定义：

- 主要分区与扩展分区最多可以有四个(硬盘的限制)
- 扩展分区最多只能有一个(操作系统的限制)
- 逻辑分区是由扩展分区持续划分出来的分区；
- 能够被格式化后作为数据存取的分区是主要分区与逻辑分区，扩展分区无法格式化；
- 逻辑分区的数量依操作系统而不同，在Linux系统中SATA硬盘已经可以突破63个以上的分区限制；

###### MBR的局限性

- 操作系统无法使用2.2TB以上的磁盘容量
- MBR仅有一个区块，若被破坏后，经常无法或很难恢复
- MBR内的存放启动引导程序的区块仅446字节，无法存储较多的程序代码。

#### 2.2 GPT



# 三、安装centos

## 安装centos7

### 选择安装模式与启动

切换成gpt分区须添加额外的内核参数修改安装程序inst.gpt

### 磁盘分区与文件系统设置

1. 添加BIOS boot 大小设置为2M 标准分区（BIOS boot：gpt分区表可能会使用到的东西，若使用mbr，则不需要）
2. 建立/boot挂载点的文件系统 容量1G
3. 根目录/ 容量 10G LVM分区
4. 配置volume group 固定大小 30G
5. /home 容量5G LVM分区
6. /swap 容量1G LVM分区
7. 完成，接受更改

### 内核管理与网络设置

1. kdump 默认启用
2. 网络和主机名设置

### 开始安装、设置root密码与一般用户

### 最小化安装后的一些配置

内容来自[CentOS7 最小化安装后的必备操作](https://blog.csdn.net/qq_34160679/article/details/79800584)

关闭防火墙并关闭自动启动

```shell
systemctl stop firewalld
systemctl disable firewalld.service 
# 安装IPtables防火墙 
yum install -y iptables-services
```

修改iptables配置文件，开放以下端口 (默认开启了22端口，以便putty等软件的连接，实例开启80端口和3306端口，以便后期lamp环境使用，注：80 为Apache默认端口，3306为MySQL的默认端口）

```shell
vi /etc/sysconfig/iptables 
#添加下面三句话到默认的22端口这条规则的下面 
-A INPUT -m state –state NEW -m tcp -p tcp –dport 80 -j ACCEPT 
-A INPUT -m state –state NEW -m tcp -p tcp –dport 3306 -j ACCEPT
```

重启iptables

```shell
systemctl restart iptables.service 
添加iptables开机自启项 
systemctl enable iptables.service
```

修改源文件

```shell
#先进入源的目录 
cd /etc/yum.repo.d 
#备份一下官方源 
mv CentOS-Base.repo CentOS-Base.repo.bak 
#将阿里源文件下载下来 
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
#重建源数据缓存 
yum makecache 
ok,换源完成
```

安装vim `yum install -y vim-enhanced`

更新或升级已安装的软件 `yun update && yum upgrade`

关闭Selinux

```shell
# 编辑配置文件
vi /etc/sysconfig/selinux 
# 将selinux项改为关闭
SELINUX=disabled 
```

# Linux的文件权限与目录配置

##### 如何修改文件属性与权限

- chgrp 修改文件所属用户组

- chown 修改文件拥有者

- chmod 修改文件的权限，SUID,SGID,SBIT等的特性

  > 前两个使用场景：cp文件给他人时可以用
  >
  > -R 表示递归修改
  >
  > chmod两种修改方式
  >
  > 1. 数字
  > 2. 参数 (u/g/o/a)(+-=)(rwx)

##### 文件种类和扩展名

- l开头link文件
- b开头设备文件：硬盘软盘等块设备
- c开头设备文件：串行端口的接口设备
- s数据接口文件
- p

# 六、Linux文件与目录管理

##### 目录的目录与路径

~~~bash
- 代表前一个工作目录
~ 代表user所在的家目录
~account 代表account这个使用者的家目录
~~~

**rmdir只能删除空目录**

##### 添加环境路径

~~~bash
PATH="${PATH}:/NEW"
~~~

##### 文件内容查看

- cat

  > -n 显示行号

- tac 从最后一行开始显示

- nl 同时显示行号

- more 一页一页的显示文件

- less 同more但是可以向前翻

- head

- tail

- od 以二进制的方式读取内容

##### 修改文件时间或创建新文件：touch

##### 文件默认权限：umask

- 用户建立为文件则默认没有x权限也即666对应的umask为000
- 用户建立为目录时，默认所有权限开放，及777

umask的数字指的是新建默认值需要减去的权限

##### 文件的隐藏属性

- chattr配置文件隐藏属性

  >-a 只能增加数据不能删除和修改
  >
  >-i 不能被删除，改名，设置链接，写入或增加数据

- lsattr显示文件隐藏属性

##### SUID,SGID,SBIT

SUID仅对二进制文件有效

SGID可以针对文件或目录设置

SBIT仅对目录有效

- 4为SUID

- 2为SGID

- 1为SBIT

  > chmod 4755 filename

##### 观察文件类型：file

##### 命令与文件的查找

- which：查找可执行文件

- 文件查找

  - whereis

  - locate

    ~~~bash
    updatedb
    loacte
    ~~~

- find

  > -mtime n
  >
  > -mtime +n
  >
  > -mtime -n
  >
  > exec到\;额外操作
  >
  > find / -perm /7000 -exec ls -l {} \;

# 八、文件与文件系统的压缩

打包命令

> -c 建立打包文件
>
> -t 查看打包文件的信息
>
> -x 解包
>
> -z gzip
>
> -j bzip
>
> -J xz
>
> -v 显示正在处理的文件
>
> -f 后面立刻接被处理的文件名，建议-f单独写一个选项7



# 九、vim程序编辑器

vim man_db.conf恢复未保存丢失的文件

ctrl+v可以用矩形的方式选择数据

vim file1 file2  实现多文件编辑:n下一个:N上一个文件

:sp 多窗口功能

关键字补全功能

> [ctrl] +x -> [ctrl] + n 通过目前正在编辑的这个[文件的内容文字]作为关键字，予以补齐
>
> [ctrl] +x -> [ctrl] + f		目录内的文件名作为关键字
>
> [ctrl] +x -> [ctrl] + o		以扩展名作为补充，以vim内置的关键字，予以补齐