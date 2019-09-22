# 配置虚拟环境与Git

# 1. MVC网站架构

为了更好的开发我们的服务器, 我们需要对我们的程序进行一些规划。
通常使用的一种方式便是 MVC 式的结构。

![](./img/mvc.png)

MVC模式（Model–view–controller）是软件工程中的一种软件架构模式, 把软件系统分为三个基本部分：

- 模型 (Model), 它是程序需要操作的数据或信息。
- 视图 (View), 它提供给用户的操作界面, 是程序的外壳。
- 控制器 (Controller), 它负责根据用户从"视图层"输入的指令, 选取"数据层"中的数据, 然后对其进行相应的操作, 产生最终结果。

这种模式的特点是构建简单, 层次清晰, 代码可复用性好, 模块之间耦合度低

对应到我们的服务器程序，简单来说，就是一些模块只负责前端页面显示，另一些模块只负责数据模型的定义和数据的操作，其他模块负责连接这两部分，并进行必要的逻辑处理。

对应到程序细节
我们可以按照程序功能不同，分为 3 个模块。

```
project/
    ├── models.py   -> Model 层
    ├── view.py     -> View 层
    ├── main.py     -> Controller 层
    │
    ├── statics/
    │   ├── img/
    │   ├── css/
    │   └── js/
    │
    └── templates/
        ├── all.html
        ├── base.html
        ├── home.html
        ├── info.html
        └── modify.html
```

# 2.虚拟环境

实际工作中，我们可能同时要维护若干个项目，每个项目使用的软件包、版本可能都不一样，比如项目 A 使用 tornado 4.3，而项目 B 使用 tornado 6.0 版，这时如果将两个版本同时装到全局的 Python 环境下就会冲突。

所以我们要为不同的项目单独设置它运行所需的环境，这就需要借助虚拟环境管理。

1.安装

```
pip install virtualenv
```

2.创建虚拟环境

```
cd ~/你的项目文件夹

# 创建虚拟环境
# 虚拟环境可以创建到任何位置，但一般与项目文件夹放到一起
virtualenv .venv
```

3.加载虚拟环境

```
source ~/项目文件夹/.venv/bin/activate  # 激活虚拟环境
```

4.退出虚拟环境

```
deactivate  # 当开发完成后，可以退出当前虚拟环境
```

5.导出虚拟环境

```
pip freeze > requirements.txt
```

6.重新激活导入虚拟环境

```
source ~/项目文件夹/.venv/bin/activate  # 重新激活虚拟环境
pip install -r requirements.txt       # 重新下载、安装依赖包
```

# 3.版本控制工具与GitHub

## 3.1作用

1. 能够追踪全部代码的状态
2. 能够进行版本之间的差异对比
3. 能够进行版本回滚
4. 能够协助多个开发者进行代码合并

## 3.2常见的版本控制工具

- CVS: 基本退出了历史舞台

- svn: 中心化的版本控制工具, 需要有一台中心服务器

  ![svn](./img/svn.png)

- git: 分布式的版本控制工具, 中心服务器不再是必需的

  ![git](./img/git.png)

- hg: 纯 Python 开发的版本控制工具

- Github: 依托 Git 而创建的一个平台，有独立的公司在运作。

- 备注：所有文本类的东西都可以交由版本控制工具来管理

# GIT的历史

Git 最初由 Linus 为了维护 Linux 内核源码而开发。

Linus 当时因不堪忍受早期版本控制工具的各种问题，最终决定自己开发了一个，并且将它开源出来，供所有人使用。

## 1.GitHub的使用

1.配置自己的账号和邮箱

```
git config --global user.name '你的名字'
git config --global user.email '你的邮箱'
```

2.设置要忽略的文件，对于不需要让 Git 追踪的文件可以在项目目录下创建 `.gitignore` 文件

```
touch .gitignore
```

.gitignore 文件中可以写需要忽略的文件名，或是某一类文件的通配符, 如下

```
*.pyc
*.log
*.sqlite3
.DS_Store
.venv/
.idea/
__pycache__/
```

2.必须掌握的git的命令

| Command  | Description                    | 与远程通信 | 操作示例                           |
| -------- | ------------------------------ | :--------: | ---------------------------------- |
| init     | 在本地初始化一个新的仓库       |     —      | `git init`                         |
| add      | 添加到暂存区                   |     —      | `git add aaa bbb ccc/`             |
| commit   | 将暂存区的修改提交到本地仓库   |     —      | `git commit -m '注释'`             |
| push     | 将本地仓库的内容推送到远程仓库 |   **有**   | `git push`                         |
| pull     | 将远程仓库的更新拉取到本地仓库 |   **有**   | `git pull`                         |
| clone    | 将远程仓库克隆到本地           |   **有**   | `git clone http://test.cn/bar.git` |
| branch   | 管理分支                       |     —      | `git branch 分支名`                |
| checkout | 切换分支 / 代码回滚 / 代码还原 |     —      | `git checkout 分支名 / 提交ID`     |
| diff     | 不同版本之间进行差异对比       |     —      | `git diff 版本1 版本2`             |
| merge    | 合并两个分支                   |     —      | `git merge 其他分支名`             |
| status   | 查看当前分支的状态             |     —      | `git status`                       |
| log      | 查看提交历史                   |     —      | `git log`                          |
| reset    | 代码重置 / 代码回滚            |     —      | `git reset`                        |
| blame    | 检查每行代码最后一次是谁修改的 |     —      | `git blame 文件名`                 |

3.解决冲突

```
git push    # 发现与别人修改的代码有冲突
git pull    # 将线上代码拉取到本地
git status  # 找到冲突文件都有哪些，冲突文件的状态是: both modified

# 然后逐一打开冲突文件，按照冲突标记逐行解决冲突
# 冲突标记一般为
#     >>>>>>> HEAD
#     hello world
#     =======
#     hello shanghai
#     <<<<<<<

# 冲突代码解决后，将代码中冲突的标记删除

git add ./
git commit -m '解决冲突，进行了一次合并'
git push
```

