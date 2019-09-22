# LInux 初识

## 1.GNU IS NOT UNIX

- 开源运动
  - GPL协议：使用我的代码，你也必须开源
  - OPENSOURCE: 开源不代表我i没有版权
  - FREESOFTWARE:自由软件不是免费软件



## 2.LInux的开发者

- 芬兰大学生：linus Torvalds
- 吉祥物Tux



## 3.重要的发行版

- RedHat：最成功的商用LInux
- CentOs: 社区版的RedHat
- Fedora:个人版的Redhat
- Debian:纯粹的自由软件的发行版，拥有最大的开源软件库
- Ubuntu:最受欢迎的Linux的发行版
- Gentoo:一切从源码开始手动安装，性能超高，非常稳定
- Arch:省区编译，手动安装一切，性能同样优异
- ElemetaryOS:华丽优雅的桌面发行版，易用性极佳
- Deepin:国人开发的，满足国人基本需求



## 4.Unix family

- 多，就是版本众多



## 5.LInux指令

### 5.1Ubuntu下的apt或apt-get指令

- search:搜索  apt search XXX
- show:查看详情  apt show XXX
- install:安装  apt install XXX
- remove:删除 apt remove XXX
- autoremove: 自动删除无效的软件包  apt autoremove
- update: 更新软件源 apt update
- upgrade: 升级软件  apt upgrade

### 5.2CentOS下的yum指令

- search:搜索  yum search XXX
- install:安装  yum install XXX
- update: 更新 yum update -y
- remove:卸载 yum remove XXX



# Shell

## shell是个什么玩意

shell是一个应用程序，它连接了用户和linux的内核，linux的内核是kernel，是操作系统的核心，直接与硬件打交道，处理底层的事件。

shell让用户能够更加高效，安全的使用Linux的内核，这是shell的本质



## Basn快捷键

- ctl + f 前进一个字符
- ctl + b 后退一个字符
- ctl + a 回到行首j
- ctl + e 回到行尾
- ctl + w 向左删除一个单词
- ctl + u 向左删除全部
- ctr + k 向有删除全部
- ctl + y 粘贴上次删除的内容
- ctr + l 清平

# 目录结构

Linux采用了一种不同的方式，在路径中不使用驱动盘符。Linux虚拟目录中比较复杂的部分是它如何协调管理各个存储设备。在linux pc上安装的第一块硬盘称为跟驱动器。跟驱动器包含虚拟目录的核心，其他目录都是从那里开始构建的。

Linux会在跟驱动器上创建一些特别的目录，我们成为挂载点mount point。挂载点是虚拟目录中用于分配额外存储设备的目录。虚拟目录会让文件和目录出现在这些挂载点目录中，然而实际上他们却存储在另一个驱动器中。





# 目录操作

- 绝对路径 /usr/local/bon
- 相对路径 ../foo/bar
- 命令列表
- pwd 显示当前目录的绝对路径
- ls  ./ 显示当前目录的文件
- ls -l  ./ 以列表形式显示为文件
- ls -lh   ./ 对人友好的方式显示文件裂变
- ls -A ./  显示隐藏文件
- cd -  回到上一次的位置 不是上层位置
- mkdir  abc   创建名为abc的文件夹
- mkdir  -p a/b/c  创建三层目录结构a/b/c
- touch abc  创建名为abc的文件





# 文件操作

- 命令列表
- cp  aa  ../bb/   将aa文件复制到../bb目录
- mv  aa  ../bb    将aa文件移动到../并更名为BB
- rm foo  删除名为foo文件
- touch   在当前文件夹创建一个abc的文件，如果有，则跳过
- ln  -s   abc  def  为abc文件创建一个名为def软连接



- cp/mv/rm的通用参数哦
- - -i   覆盖前提示
  - -n   如果目标存在，则停止操作
  - -f    如果路标存在，则强制操作，覆盖前不提示
  - -r    递归对文件夹执行某操作  mv不需要 -r
- ln 命令详解
  - 硬链接：ln foo  bar
    - 只能在同分区创建
    - 一个文件的多个硬链接相当于一个文件有多个名字，多个硬链接在磁盘上只占用一个文件的大小
    - 修改硬链接时，所有同源的硬链接都会发生变化
  - 软连接  ln  -s  foo  bar
    - 可以跨区创建
    - 内部只记录目标文件的路劲，类似Windows下的快捷方式
    - 通过软链接修改文件，源文件也会发生修改



# 压缩文件的处理

- tar$
  - 压缩  tar  -czf  abc.tar.gz  abc/
  - 解压  tar -xzf  abc.tar.gz
- zip
  - 压缩   zip  -r  abc.zip   abc/
  - 解压  unzip  abc.zip

# 查找文件find命令

- 查找当前文件夹下的全部文件  find   ./
- 只查找文件类型   find  ./  -type  f
- 只查找目录    find ./  -type d
- 只查找链接  find  ./  -type  l
- 按名称查找   find  ./  -name  '*.py'
- 按权限查找  find  ./ -perm  0644
- 按大小查找  find ./  -size  +1k  -size  -5k  大于1k,小于5K

# Linux中的用户与组

- 每个用户都有唯一的用户名，并且拥有唯一的UID
- 同样用户组也拥有唯一的用户组，并且拥有唯一的GID
- root的UID与GID都是0
- 用户名与UID的对应关系记录在 /etc/passwd
- 用户组与GID的对应关系在 /etc/group
- 用户的密码信息记录在 /etc/shadow



# passwd格式

- 单行样例:  `root:x:0:0:root:/root:/bin/bash`
- 详情
  - root  用户名
  - x  早期曾在此记录密码，现已作废，用x在位
  - 0  uid
  - 0  gid
  - root  注释随便写
  - /root  家目录
  - /bin/bash  登陆后使用的shell



#  shadow格式

- 单行样例： `root:$fdsgregs%$FDSgsg/:17877:0:99999:7:::`

- 详情

  - root   用户名
  - $fdsgregs%$FDSgsg/     加密后的密码
  - 17877   最后一次修改的密码的日期，时间戳，从1970-1-1开始
  - 0   密码几日内不可修改 0表示可以随时修改
  - 99999   密码有效天数
  - 7   密码失效前几天内提醒用户修改密码
  - ​            密码失效的宽限天数
  - ​            账号失效日期
  - ​             保留字段，暂时没用

  

  

  

# group格式

- 单行样例： `wheel：x:10:bob,tom`
- 详情
  - wheel  组名
  - x     组密码，已弃用
  - 10    组ID(GID)
  - bob，tom  该组的成员

# 用户管理

## 1.添加用户

- 用法：`useradd  -mU  -G 组名 -p 密码  用户名`
- 参数详情
  - -m  在/home目录创建用户的家目录
  - -U  创建与用户同名的组
  - -G  组名    新账户的附加组列表
  - -p 密码  加密后的新账户密码

## 2.删除用户

- 用法：`userdel  -r 用户名`
- -r   删除主目录和邮件池

## 3.修改密码

- 用法：`passwd 用户名`

## 4.切换用户

- 用法1  `su  用户名` 仅仅切换用户身份
- 用法2 `su - 用户名` 完全以这个用户进行登录，会初始化当前用户的设置

# 用户组管理

## 1.添加组

- 用法 `groupadd [选项] 组名`
- 选项
  - `-g GID`  为新组使用GID
  - `-p 密码`  为新组使用此加密过的密码
  - `-r`  创建一个系统账号

## 2.删除组

- 用法 ：  groupdel  组名

## 3.修改用户属性

- 用法： usermod [选项]  用户名
- 选项
  - -d  HOME_DIR 用户的新主目录
  - -g  GROUP  强制使用GROUP为新主组
  - -G GROUPS  新的附加组列表 GROUPS
  - -a GROUP   将用户追加至上边-G中提到的附加组，并不从其他组中删除此用户
  - -L  锁定用户账户
  - -m  将家目录内容移至新位置（仅于 -d 一起使用）
  - -s  SHELL   该用户账号的新登录shell
  - -U  解锁用户账号



# 查看登录的用户

- who      查看谁正在登录
- w   查看谁正在登录，并在显示每个登录用户正在执行的任务
- last  查看历史登录记录
- lastb  查看失败的登录记录
- lastlog  查看全部用户最后一次登录的时间



# 文件权限

## 1.权限的定义

- 三种权限    标记   含义
- r         read  读权限
- w       write 写权限
- x        execute 执行权限
  - 用户身份分为三种
  - owner   文件拥有者
  - group  同组人
  - other 其他人
- ls  -l  可以看到文件权限信息
  - -rwxr-xr-x   为例
  - rwx  文件拥有者可以对文件进行 读 写 可执行 的权限
  - r-x  同组人 具有 读 可执行的权限
  - r--  其他人只有读权限

## 2.权限修改

- 连续设置所有的权限  `chmod u=rwx,g=rx,o=x  test.py`
- 给自己和同组人增加权限  `chmod ug+rw  test.py`
- 给同组人和其他人删除权限  `chmod  go-w  test.py`
- 给所有人增加权限  `chmod  a+x  test.py`

## 2.通过数字修改权限

- `chmod 753 tesy.py`
  - 身份7/5/3  分别对应owner/group/others
  - r=4   w=2   x=1   421 

## 3.修改文件拥有者

- 用法 `chown  用户：组  文件`



# 文本操作

- `echo xyz`打印文本
- `echo xyz > a.txt` 将输出的文本重定向到文件a.txt,  a的内容会被覆盖
- `echo xyz >> a.txt`  将输出的文本追加到文件a.txt,  a原有的内容不会覆盖
- `cat 文件名`  查看文件
- `head -n N 文件名` 查看文件的前N行
- `tail -n N 文件名` 查看文件的后N行
- `less  文件`  快速浏览文件
  - 按j向下
  - 按k向上
  - 按f向下翻屏
  - 按b向上翻屏
  - 按g到全文开头
  - 按G到全文结尾
  - 按q 退出
- `sort  文本或文件` 将结果按升序排序
- `sort -r 文本或文件` 按降序排序
- `uniq`  去重，依赖排序，常更在sort后面使用
- `awk  '{print  $N}'`打印出第N列
- `wc`字符统计
  - -c   统计字符
  - -w   统计单词
  - -l  统计行
  - 样例  wc   -l   abc.py
- 管道符  ：`|`
  - 管道符可以连接连个命令，将前面的输出作为后面的输入
  - 统计自己最多的10个命令
  - `history | awk '{print $2}' | sort |uniq -c |sort -gr |head -n 10`



# VIM编辑器之神

VIM分为三种模式：命令模式，插入模式，底栏命令模式、

- 按ESC键，进入命令模式
  - `h,j,k,l`光标左下上右移动vim
  - `ctl+e`向下滚动
  - `ctl+y`向上滚动
  - `ctl+f`向下翻屏
  - `ctl+b`向上翻屏
  - `yy`复制整行
  - `yw`复制整行
  - `p`粘贴到下一行
  - `dd`删除整行
  - `d3w`向前删除3个单词
  - `7x`删除7个字符
  - `u`撤销
  - `ctr + r`重做
  - `c3w`剪切3个单词
  - `gg`跳至文件首行
  - `shift + g`跳至文件结尾
  - `shift + h`跳至屏幕首行
  - `shift + m`跳至屏幕中间
  - `shift + l`跳至屏幕结尾
  - `ctl + v`列编辑
  - `shift + v`选中整列
  - `shift + >`向右缩进
  - `shift + <`向左缩进
- 按I 键，进入插入模式
  - 插入模式正常输入
  - 想做其他操作，必须先按ESC键回到命令模式
- `在命令模式时按`：键，进入底栏命令模式
  - `33`跳至文件的第33行
  - `%s/abc/123/g`把文件中所有的abc替换成123
  - `set nu`打开行号
  - `set nonu`关闭行号
  - w 保存
  - q  退出
  - wq  保存并退出
- VIM `配置文件 ~/.vimrc`

# 系统状态与管理

## 1.进程状态

Linux是一个多任务操作系统，同一时刻允许多个任务同时工作，运行中的每一个任务就是一个进程。查看进程信息常用的命令有ps和top

- ## ps命令

- ps即process status 的意思，用来查看进程状态  ps不带参数时能看到的信息很少

- ps命令支持3中不同类型的命令行参数

  - Unix风格的参数 如  ps -ef
  - BSD风格的参数   ps aux
  - GNU风格的参数   ps  --pid 123

- ps的命令非常强大，参数也很多，记住一些常用的参数组合即可，如ps -ef

  - 参数详情
    - -e   参数指定显示所有运行在系统上的进程
    - -f    参数则扩展了输出
  - 每列详情
    - UID  启动这些进程的用户
    - PID 进程的进程ID
    - PPID  父进程的进程号
    - C  进程生命周期中CPU利用率
    - STIME  进程启动时的系统时间
    - TTY  进程启动时的终端设备
    - TIME  程序累计占用CPU的时间
    - CMD  进程运行的命令

- ps   aux

  - 参数详情
    - a  显示跟任意终端关联的所用进程
    - u  采用基于用户的格式显示
    - x  显示所有的进程，甚于包括未分配任何终端的进程
  - 每列信息
    - USER  执行这个进程的用户
    - PID  进程ID
    - %CPU  当前进程的CPU占用
    - %MEM 当前进程的内存占用
    - VSZ  进程占用的虚拟内存大小，以千字节KB为单位
    - RSS 进程占用的物理内存大小
    - TTY  进程启动时的终端设备
    - STAT 进程状态
    - START 进程启动时刻
    - TIME  程序累计占用CPU的时间
    - COMMAND  启动进程的命令
  - 关于STAT
    - 代表当前进程状态的双子符状态码
    - 第一个字符表明进程状态
      - O  代表正在运行
      - S  代表在休眠
      - R 代表可运行，正等待CPU
      - Z 代表僵化，进程已结束但父进程以不存在
      - T 代表停止
    - 第二个参数进一步说明进程的状态细节
      - <    该进程运行在高优先级上
      - N   该进程运行在低优先级上
      - L  该进程有页面锁定在内存中
      - s  该进程是控制进程
      - l  该进程是多进程
      - `+` 该进程运行在前台



## `top`命令

ps命令只能查看一瞬间的进程状态，如果想要持续查看某些进程的状态可以使用top

- 头信息逐行详解
- 系统运行的整体状态：开机时长，登录用户数，系统负载
  - 系统负载 `load average: 0.00  0.02  0.05`
  - 分别代表  一分钟负载  五分钟负载  十五分钟负载
  - 负载值越高代表服务器压力越大
  - 负载值不要超过CPU的核心数，如果超过核心数意味着有很多进程在等待使用CPU
  - 与 uptime 命令的结果一样
- 任务情况：任务总数，运行中的数量，休眠数量，停止数量，僵尸进程数量
- cpu 使用情况
  - us  user  用户态占用
  - sy  system  内核态占用
  - id  idle  空闲的CPU
- 内存占用情况：内存总量，空闲内存，使用的内存，缓冲区占用的内存
- 交换分区的占用
  - 交换分区是一种将内存数据保存到硬盘的技术，一般在内存不足的时候使用
- 进程区
  - PID  进程的ID
  - USER  进程属主的名字
  - PR  进程的优先级
  - NI  进程的谦让度值
  - VIRT  进程占用的虚拟内存总量
  - RES  进程占用的物理内存总量
  - SHR  进程和其他进程共享的内存总量
  - S  进程的状态，与ps基本相同
  - %CPU  进程使用的CPU时间比例
  - %MEM  进程使用的内存占可用内存的比列
  - TIME+ 自进程启动到目前为止的CPU时间总量
  - COMMAND  进程所对应的命令行名称，也就是启动的程序名
- 小技巧
- 进程太多时，可以通过-p参数指定需要查看的进程ID，让进程信息更精简
- `top  -p  PID1,PID2,PID3`



# `htop`命令

如果感觉top还不够直观，可以使用htop，htop不是系统默认指令，需要额外安装

- `安装 sudo apt install htop`



# 进程的管理

- kill  杀死进程，或者给进程发送信号
  - -1      （HUP）平滑重启
  - -9       （KILL） 强制杀死进程
  - -15  （TERM)  正常终止进程  kill的默认信号
- pkill  名字       按名字处理进程
- killall  名字   处理名字匹配的进程

# 其他状态

### 1.`内存状态  free`

- `可以通过 -m 或者 -g  参数调整 free 命令显示数值的单位`

### 2.硬盘

- `iostat` 查看硬盘写入和读取的状态
- `df -lh`查看硬盘分区，及每个分区的剩余空间
- `du -hs ./`查看当前目录占用的硬盘大小

### 3.网络状态

- `ifconfig`查看网卡状态，常用来检查自身IP地址
- `netstat  -natp` 查看网络连接状态
  - -a   显示所有选项
  - -t   显示所有与TCP相关的选项
  - -u  显示所有与UDP相关的选项
  - -x  显示所有与unix域相关的套接字选项
  - -n  拒绝显示别名，能显示数字的全部转换为数字显示
  - -p  显示建立相关连接的程序名
  - -l   显示所有状态为LIsten的连接
  - -e  显示扩展信息，如当前链接所对应的用户
  - -c  间隔一段时间执行一次netstat命令
  - -s  显示统计信息，对每种类型进行汇总
- `ping  -i 0.5  -c  100  xx.xx.xx.xx`
  - `-i`间隔
  - `-c` 数量
  - `-q`安静模式，只打印结果
- `lsof`
  - `lsof -i :[port]`查看占用端口的程序
  - `lsof -i tcp`查看所有TCP链接
  - `lsof  -u abc` 查看用户abc打开的所有文件
  - `lsof -p  123`查看pid 为123的进程打开的所有文件
- 路由追踪： `traceroute [HOST]`
- DNS 查询
  - `dig [DOMAIN]`
  - `host [DOMAIN]`
  - `nslookup [DOMAIN]`

# 时间和日期

- date  查看日期与时间
- cal   查看日历
  - --one  查看本月的日历
  - --three  查看最近三个月的日历
  - --year  查看全年的日历



# 下载

- curl  执行HTTP访问。也可用来下载
- wget  下载
- scp  `在服务器之间上传或下载  scp root@x.x.x.x:/root/abc  ./abc`

# shell编程与运维

## 1.shell脚本概述

通过shell中的各种命令，开发者和运维人员可以对服务器进行维护工作。但每次都手动输入命令，效率太低为了能够批量处理执行操作，我们可以将需要执行的命令写入文件，批量执行，这种文件便是shell脚本。shell`脚本一般是以 .sh `结尾的文本文件，当然也可以省略扩展名

## 2.shell脚本首行

脚本文件第一行通过注释的方式执行脚本的程序。在shell脚本中，` #`开头的文本是注释。`但第一句 #！ `开头的这句话比较特殊，他会告诉shell应该使用哪个程序来执行当前脚本。

- 常见的方式有：
- `#!/bin/sh`
- `#!/bin/bash`
- `#!/usr/bin/env bash`
- python`脚本的第一句一般是 #!/user/bin/env python`

## 3.第一个脚本

1.创建cpu-count.sh 文件

2.将下面文本写入cpu-count.sh中

```
#!/bin/bash

echo "Hello" 
echo "I am `whoami`" 
echo "I love Linux" 
echo "The CPU in my PC has `cat /proc/cpuinfo |grep -c processor` cores" 
exit 0
```

3.`执行 chmod a+x cpu-coutn.sh`对脚本授予可执行权限

4.`输入 ./cpu-count.sh`执行

5.查看脚本的退出脚本  `echo $?`

- linux中的所有程序执行结束后都有状态码
- 状态码为 0 表示正常，状态码为正整数代表异常退出

# 变量

1.定义

```
#变量定义与一般语法无区别，但要注意等号前后没有空格

a=12345
b=xyz
```

2.使用

使用变量时，注意前面加上 `$`符号 ，俗称没钱不干活

```
echo "---$a---\n===$b===" 
printf "---$a---\n===$b===\n"
```

3.注意引号的区别  双引号里面的变量能够使用，单引号里面写什么打印什么，没特殊效果

```
echo "---$a---\n===$b===" 
echo '---$a---\n===$b==='
```

4.定义当前shell下的全局变量

- 定义 `export  abc=13483645`
- 定义完成后，在终端里用source加载脚本  `source ./tesh.sh`
- 常用的系统环境变量
  - `$PATH` 可执行文件目录
  - `$PWD` 当前目录
  - `$HOME` 家目录
  - `$USER` 当前用户名
  - `$UID` 当前用户的UID

# 分支语句：if

分支控制语句完整格式为：

```
if command
then
    commands
elif command
then
    commands
esle
    commands
fi    
```

1.if语句检查判断的依据实际上是，后面所跟的命令的状态码 0 为true 其他值为false

```
if ls /xxx
then
     echo 'exist xxxx'
else
     echo  'not exist xxxx'
fi
```

2.条件测试命令  `[.....]`

- shell 提供了一种专用做条件测试的语句  `[....]`

- 这一对方括号本质上是一个命令，里面的条件是其参数，所以 [  的后面和  ]  的前面必须有空格，否则会报错

- 它可以进行三种比较

  - 数值比较
  - 字符串比较
  - 文件比较

- 用法

  - ```
    if [ condittion ]
    then
        commands
    fi
    ```

3.条件列表

- 数值比较

  - | Condition | 说明               |
    | --------- | ------------------ |
    | n1 -eq n2 | 检查n1是否与n2相等 |
    | n1 -ge n2 | 是否大于等于       |
    | n1 -gt n2 | 是否大于           |
    | n1 -le n2 | 是否小于等于       |
    | n1 -lt n2 | 是否小于           |
    | n1 -ne n2 | 是否不等于         |

- 字符串比较

  - | Condition     | 说明                   |
    | ------------- | ---------------------- |
    | str1 = str2   | 检查str1是否和str2相同 |
    | str1 !=  str2 | 是否不同               |
    | str1 <  str2  | 小于                   |
    | str1 >  str2  | 大于                   |
    | -n str1       | 检查str1的长度是否非0  |
    | -z  str1      | 检查str1的长度是否为0  |

- 文件比较

  - | CONDITION         | 说明                                     |
    | ----------------- | ---------------------------------------- |
    | -d  file          | 检查file是否存在并是一个目录             |
    | -e  file          | 检查file是否存在                         |
    | -f  file          | 检查file是否存在并是一个文件             |
    | -r  file          | 检查file是否存在并可读                   |
    | -w  file          | 检查file是否存在并可读                   |
    | -x  file          | 检查file是否存在并可执行                 |
    | -s  file          | 检查file是否存在并非空                   |
    | -O  file          | 检查file是否存在并属当前用户所有         |
    | -G  file          | 检查file是否存在并且默认组与当前用户相同 |
    | file1  -nt  file2 | 检查file1 是否比file2新                  |
    | file1  -ot  file2 | 检查file1 是否比file2旧                  |

    

# 循环语句：for

shell 中的循环结构有三种 for  ，while ， until ，这里重点介绍for循环

1.for 循环的基本格式

```
for 变量  in  序列
do
    要执行的命令
done
```

2.练习：打印1到10中的偶数

```
for  i  in  `seq 1  10`
do
   if [[ $[ $i % 2] == 0]]
   then
       echo  "偶数  $i"
   else
        echo  "奇数  $i"
    fi
done
```

2.1  `seq START END`语句用来产生一个数字序列

2.2  `$[ NUM1 + NUM2 ]`  语句用来进行基本的数学运算

2.3  `[[...]]`语句用来更方便的进行比较判断

3.C语言风格的for循环

```
for ((i=0; i<10;i++))
do
  echo "num  is $i  "
done
```



# 函数

1.函数定义

​      定义时   `function`  不是必须的，可以省略

​      

```
function  foo() {
    echo "--------------------"
    echo  "hello  $1 , nice to meet you"
    echo  "----------------------"
} 
```

2.函数的使用

- 在终端或脚本中直接输入函数名即可
- 传参也只需要将参数加到函数名后面，以空格做间隔，向正常使用命令那样   ` foo  zhangsan`

3.函数的参数

```
bar() {
     echo "执行者是  $0"
     echo "参数数量是  $#"
     echo "全部的参数  $@"
     echo "全部的参数  $*"
     
     if [ -d $1 ]; then  #检查传入的第一个参数是否是文件夹
        for f in  `ls  $1`
        do
           echo  $f
        done
      elif [ -f $1 ]; then
          echo 'this is a file $1'  #单引号内的变量不会被识别
          echo  "this is a file  $1"  #如果不是文件夹，直接显示文件名
      else
           echo  'not valid'  #前面都不匹配显示默认语句
      fi
}  
```



# 获取用户输入

```
read -p  "请输入一个数字： "  num
echo  "你输入的是： $num "
```





