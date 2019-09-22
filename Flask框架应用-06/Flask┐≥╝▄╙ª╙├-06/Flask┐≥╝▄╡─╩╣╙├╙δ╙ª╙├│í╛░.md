# Flask框架的使用与应用场景

## 1.框架的简介

基于python的web （微） 框架

```
重量级框架 django
	为了方便业务程序的开发，提供了丰富的工具及其组件
轻量级框架 flask
	只提供web核心功能，自由灵活，高度定制，Flask也被称为 “microframework” ，因为它使用简单的核心，用 extension 增加其他功能
```

官方文档

```
http://flask.pocoo.org/docs/0.12/      英文
http://docs.jinkan.org/docs/flask/     中文
```

flask依赖库

```
flask依赖三个库
 jinja2         模板引擎
 Werkzeug  WSGI 工具集
 Itsdangerous   基于Django的签名模块
 现在不仅仅是三个  但是依然前两个有用
 安装时候会出现6个 看看就可以了
```

flask流行的原因

```
 1 有非常齐全的官方文档，上手非常方便
 2 有非常好的扩展机制和第三方扩展环境，工作中常见的软件都会有对应的扩展，动手实现扩展
 也很容易
 3 社区活跃度非常高    flask的热度已经超过django好几百了
 4 微型框架的形式给了开发者更大的选择空间
```

## 2.BS/CS

```
BS:B browser 浏览器   S server  服务器   主流
CS:C client  客户端   S server  服务器
B/S结构是WEB兴起后的一种网络结构模式，WEB浏览器是客户端最主要的应用软件。这种模式统一了客户端，将系统功能实现的核心部分集中到服务器上，简化了系统的开发、维护和使用。
```

![](./img/BS-CS区别.png)

## 3.MVC/MTV

```
MVC：软件架构思想
	简介：
		MVC开始是存在于桌面程序中的，M是指业务模型 model，V是指用户界面 view，C则是控制器 controler，使用MVC的目的是将M和V的实现代码分离，从而使同一个程序可以使用不同的表现形式。比如一批统计数据可以分别用柱状图、饼图来表示。C存在的目的则是确保M和V的同步，一旦M改变，V应该同步更新
实现了模型层的复用
	核心思想: 
		解耦合
	面向对象语言：高内聚  低耦合
	Model
		模型
		封装数据的交互操作
			CRUD
	View
		视图
		是用来将数据呈现给用户的
	Controller
		控制器
		接受用户输入输出
		用来协调Model和View的关系，并对数据进行操作，筛选
	流程
		控制器接受用户请求
		调用模型，获取数据
		控制器将数据展示到视图中
```

![](https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=7948cf4dbf096b63951456026d5aec21/b03533fa828ba61edbddc04d4034970a304e59a4.jpg)

MTV也叫MVT

```
MTV
	也叫做MVT
	本质上就是MVC，变种
	Model
		同MVC中Model
	Template
		模板
		只是一个html，充当的是MVC中View的角色，用来做数据展示
	Views
		视图函数
		相当于MVC中Controller
```

## 4.Flask的基本使用

(1）虚拟环境的创建

```
1.创建flask的虚拟环境
	mkvirtualenv Flaskpython1905 -p /usr/bin/python3
2.查看虚拟环境
	pip freeze
	pip list

3.虚拟环境迁移
	pip freeze > requirements.txt
		迁出
	pip install -r requirements.txt
		迁入
```

(2)Flask项目的创建

```
1.安装
	国外源  pip install flask
	国内源  pip install flask -i https://pypi.douban.com/simple
2.创建项目
	mkdir python1905 mkdir Flaskday01  mkdir FirstFlask  vim HelloFlask.py
	代码结构
		from flask import Flask
         app = Flask(__name__)

        @app.route("/")
        def index():
            return "Hello"
        app.run()
3.启动服务器  python  文件名字.py
	默认端口号  5000  只允许本机连接
```

（3）启动服务器参数修改

```
run方法中添加参数
	在启动的时候可以添加参数  在run（）中
	debug
		是否开启调试模式，开启后修改过python代码自动重启
		如果修改的是html/js/css 那么不会自动重启
	host
		主机，默认是127.0.0.1 指定为0.0.0.0代表本机ip
	port
		指定服务器端口号
	threaded
		是否开启多线程
```

扩展：PIN码

```
全称Personal Identification Number.就是SIM卡的个人识别密码。手机的PIN码是保护SIM卡的一种安全措施，防止别人盗用SIM卡，如果启用了开机PIN码，那么每次开机后就要输入4到8位数PIN码。
在输入三次PIN码错误时，手机便会自动锁卡，并提示输入PUK码解锁，需要使用服务密码拨打运营商客服热线，客服会告知初始的PUK码，输入PUK码之后就会解锁PIN码。
```

（4）命令行参数

```
	1.安装
		pip install flask-script
		作用
			启动命令行参数
	2.初始化
		修改  文件.py为manager.py
		manager = Manager(app=app)
		修改 文件.run()为manager.run()
	3.运行
		python manager.py runserver -p xxx -h xxxx -d -r
          参数
          - p  端口 port
          - h  主机  host
          - d  调试模式  debug
          - r  重启（重新加载） reload（restart）
```

## 5.视图函数返回值

```
	（1）index返回字符串
		@app.route('/index/')
         def index():
            return 'index'
	（2）模板first.html
		@app.route('/first/')
         def hello():
            return render_template("test.html")
      静态文件css
           注意
           <link rel="stylesheet" href="/static/css/hello.css">
```

## 6.Flask基础结构

```
App
	templates
		模板
		默认也需要和项目保持一致
	static
		静态资源
		默认需要和我们的项目保持一致，在一个路径中，指的Flask对象创建的路径
	views
	models
	坑点
		执行过程中manager.py和其他的文件的路径问题
	第二个坑--封装__init__文件--
```

## 7.蓝图

```
蓝图
	1. 宏伟蓝图（宏观规划）
	2. 蓝图也是一种规划，主要用来规划urls（路由）
	3. 蓝图基本使用
  	- 安装
     - pip install flask-blueprint
     - 初始化蓝图   blue = Blueprint('first',__name__)
     - 调用蓝图进行路由注册  app.register_blueprint(blueprint=blue)
```

## 8.Flask请求流程

```
Flask请求流程
	请求到路由   app.route()
	视图函数   
	视图函数和models交互
	模型返回数据到视图函数
	视图函数渲染模板
	模板返回给用户
```

![img](https://upload-images.jianshu.io/upload_images/1801379-02bfe06281d809cf.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200)

## 9.Flask路由参数

```
带参数的请求
	从客户端或者浏览器发过来的请求带参数
	      @blue.route('/getstudents/<id>/')
          def getstudents(id):
              return '学生%s'+id
	路由参数
		基础语法
			<converter:var_name>
				书写的converter可以省略，默认类型就是string
		converter
			（1）string
                      接收的时候也是str， 匹配到 / 的时候是匹配结束
                      @blue.route('/getperson/<string:name>/')
                      def getperson(name):
                          print(name)
                          print(type(name))
                          return name
			（2）path
                      接收的时候也是str， / 只会当作字符串中的一个字符处理
                      @blue.route('/getperson1/<path:name>/')
                        def getperson1(name):
                            print(name)
                            print(type(name))
                            return name
			（3）int
                       @blue.route('/makemoney/<int:money>/')
                       def makemoney(money):
                            print(type(money))
                            return '1'
			（4）float
                        @blue.route('/makemoneyfloat/<float:money>/')
                        def makemoney(money):
                              print(type(money))
                              return '1'
			
			（5）uuid
                        uuid 类型，一种格式
                        @blue.route(('/getuu/'))
                        def getuu():
                              uu = uuid.uuid4()
                              print(uu)
                              return str(uu)

                        ------------------------------------
                        @blue.route('/getuuid/<uuid:uuid>/')
                        def getuuid(uuid):
                              print(uuid)
                              print(type(uuid))
                              return '2'
			（6）any
                        任意一个
                        已提供选项的任意一个 而不能写参数外的内容  注意的是/
                        @blue.route('/getany/<any(a,b):p>/')
                        def getany(p):
                            return '1'
```

## 10.postman

```
请求方式
	postman
		模拟请求工具
			方法参数中添加methods=['GET','POST']
	安装
		https://blog.csdn.net/Shyllin/article/details/80257755
	1. 默认支持GET，HEAD，OPTIONS
	2. 如果想支持某一请求方式，需要自己手动指定
	3. 在route方法中，使用methods=["GET","POST","PUT","DELETE"]
```

## 11.反向解析

```
反向解析
	（1）概念：
		获取请求资源路径
	（2）语法格式：
		url_for(蓝图的名字.方法名字)
	（3）使用：
         @blue.route("/heheheheheheheheheehhehe/", methods=["GET","POST","PUT"])
          def hehe():
              return "呵呵哒"


          @blue.route("/gethehe/")
          def get_hehe():
              p = url_for("first.hehe")
          return p

```

## 12.request

```
request是一个内置对象
内置对象：不需要创建就可以直接使用的对象
属性
	method  **
		请求方法
	base_url
		去掉get参数的url
	host_url
		只有主机和端口号的url
	url
		完整的请求地址
	remote_addr **
		 请求的客户端地址
		 
     一般情况下  get请求方式都是在浏览器的地址栏上显示
     eg：http：//www.baiduc.com/s?name=zs&age=18
     获取get请求方式的参数的方式：
	request.args.get('name')
	args  **
		1. args
         - get请求参数的包装，args是一个ImmutableMultiDict对象，类字典结构对象
         - 数据存储也是key-value
         - 外层是大列表，列表中的元素是元组，元组中左边是key，右边是value
     一般情况下 post请求方式都是通过表单形式使用的
     eg：
     	<form action='xxx' method='post'>
     		<input type='text' name='name'>
     获取post请求方式的参数的方式
     request.form.get('name')
	form   **
		2. form
         - 存储结构个args一致
         - 默认是接收post参数
         - 还可以接收 PUT，PATCH参数
	files   **   form标签中有一个参数 enctype=maltipart/form-data  请求方式必须是post  使用files接收
		文件上传
	headers	
		请求头
	path
		路由中的路径
	cookies
		请求中的cookie
	session	
		与request类似  也是一个内置对象  可以直接打印 print（session）
```

## 13 Response

```
创建方式
	返回字符串
		如果只有字符串，就是返回内容，数据
		还有第二个返回，放的是状态码
		@blue.route('/response/')
        def get_response():
               return '德玛西亚',404
	render_template
		渲染模板
		将模板变成字符串
		@blue.route('/rendertemplate/')
        def render_temp():
              resp = render_template('Response.html')
              print(resp)
              print(type(resp))
              return rese,500
	make_response
		Response对象
		返回内容
		状态码
		@blue.route('/makeresponse/')
		def  make_resp():
              resp = make_response('<h2>xxxxxxxx</h2>',502)
              print(resp)
              print(type(resp))
              return rese
	redirect
		重定向
		@blue.route('/redirect/')
        def  make_redir():
             return redirect('/makeresponse/')
		反向解析 url_for
		@blue.route('/redirect/')
		def  make_redir():
       		return redirect(url_for('first.make_resp'))
	response()
```

### 异常

```
abort
	直接抛出 显示错误状态码  终止程序运行
	abort(404)
	eg:
		@blue.route('/makeabort/')
         def make_abort():
              abort(404)
              return '天还行'
```

```
捕获
	@blue.errorhandler()
		- 异常捕获
		- 可以根据状态或 Exception进行捕获
		- 函数中要包含一个参数，参数用来接收异常信息
	eg:
	@blue.errorhandler(502)
    def handler502(exception):
        return '不能让你看到状态码'
```

## 14.会话技术

```
1.请求过程Request开始，到Response结束
2.连接都是短连接
3.延长交互的生命周期
4.将关键数据记录下来
5.Cookie是保存在浏览器端/客户端的状态管理技术
6.Session是服务器端的状态管理技术
```

### cookie

```
Cookie
	1.客户端会话技术
	2.所有数据存储在客户端
	3.以key-value进行数据存储层
	4.服务器不做任何存储
	5.特性
		支持过期时间
			max_age
			expries
		根据域名进行cookie存储
		不能跨网站（域名）
		不能跨浏览器
		自动携带本网站的所有cookie
	6.cookie是服务器操作客户端的数据
	7.通过Response进行操作
```

```
cookie登陆使用
	设置cookie    response.set_cookie('username',username)
		response
	获取cookie    username = request.cookies.get('username','游客')
		request
	删除cookie     response.delete_cookie('username')
		response
```

### session

```
Session
	1.服务端会话技术
	2.所有数据存储在服务器中
	3.默认存在服务器的内存中
		- django默认做了数据持久化（存在了数据库中）
	4.存储结构也是key-value形势，键值对
	【注】单纯的使用session是会报错的，需要使用在__init__方法中配置app.config['SECRET_KEY']=‘110’
```

```
session登陆使用
	设置    session['username'] = username
	获取    session.get('username')
	删除
		   resp.delete_cookie('session')
		   session.pop('username')
```

### session持久化问题

```
Session
	- django中对session做了持久化，存储在数据库中
    - 可以修改到redis中
		flask中没有对默认session进行任何处理
    - flask-session 可以实现session的数据持久化
    - 各种位置，更推荐使用redis
        - 缓存在磁盘上的时候，管理磁盘文件使用lru, 最近最少使用原则
	服务端会话技术
	Flask中没有对默认Session进行处理，默认存在内存中
	Session需要持久化  Redis中
	实现方案
		插件 flask-session
		pip install flask-session
		在国内源安装
			pip install flask-sessin -i https://pipy.douban.com/simple
		初始化Session对象 
			配置init中app.config['SESSION_TYPE'] = 'redis'
				持久化的位置
			初始化
				创建session的对象有2中方式 分别是以下两种
				1 Session(app=app)
				2 se = Session()   se.init_app(app = app)
			安装redis
				pip install redis
			需要配置SECRET_KEY='110'
			其他配置--视情况而定
				app.config['SESSION_KEY_PREFIX']='flask'
		查看redis内容
			redis-cli
			keys *
			get key
	session生存时间31天	
		ttl session
			flask的session的生存时间是31天，django的session生存时间是15天
```

## 15.Template

```
简介：
	MVC中的View，MTV中的Template
	主要用来做数据展示的
	模板处理过程分为2个阶段
            1 加载
            2 渲染
     jinja2模板引擎
            1.本质上是html
            2.支持特定的模板语法
            3.flask作者开发的   一个现代化设计和友好的python模板语言  模仿的django的模板引擎
            4.优点
                    速度快，被广泛使用
                    HTML设计和后端Python分离
                    减少Python复杂度
                    非常灵活，快速和安全
                    提供了控制，继承等高级功能

```

```
模板
	1.静态html   前后端分离
	2.模板语言动态生成的html
		{{ var }}  变量的接收
			从views传递过来的数据
			前面定义出来的数据
		案例
			www.jq22.com/cdn/
		{% tag %}
			结构标签
				block
					首次出现挖坑操作
					第二次出现填坑操作
					第N次出现，填坑操作，会覆盖前面填的坑
					不想被覆盖，需要添加 {{ super() }}
				extends
					继承
				include
					包含，将一个指定的模板包含进来
			宏定义
				macro
					可以在模板中定义，调用函数
					无参
						{% macro say()%}
    							你饿了吗？？？
						{% endmacro %}
					有参
						{% macro createUser(name,age)%}
   								 欢迎{{ name }} 心理没点数吗 你都{{ age }}大了
						{% endmacro %}
						
					函数还是用来生成html的	
					外文件中的宏定义调用需要导入也可以include
					{% macro getUser(name)%}
    						欢迎光临红浪漫{{ name }},拖鞋手牌拿好,楼上2楼左转,男宾一位
					{% endmacro %}
						{% from ‘html文件’ import yyy %}
					{{ getUser('action') }}
			循环控制
				for
					for .. in 
					loop  循环信息
						索引  index
						第一个   first
						最后一个last
				if
					if 
					else
					elif
			过滤器 
				{{ var|xxx|yyy|zzz }}
				没有数量限制
				lower
				upper
				title
				trim
				reverse
				striptags
					渲染之前将值中的标签去掉
				safe
					标签生效
				eg:
				{% for c in config %}
                       <li>{{ loop.index0 }}:{{ loop.index}}:{{ c|lower|reverse }}</li>
    			{% endfor %}
```

## 16.models

```
1.数据交互的封装
2.Flask默认并没有提供任何数据库操作的API
	Flask中可以自己的选择数据，用原生语句实现功能
		原生SQL缺点:
              代码利用率低，条件复杂代码语句越过长，有很多相似语句
              一些SQL是在业务逻辑中拼出来的，修改需要了解业务逻辑
              直接写SQL容易忽视SQL问题
	也可以选择ORM
		SQLAlchemy
		MongoEngine
		将对象的操作转换为原生SQL
		优点
			 易用性，可以有效减少重复SQL
              性能损耗少
              设计灵活，可以轻松实现复杂查询
              移植性好
3.Flask中并没有提供默认ORM
	ORM 对象关系映射
	通过操作对象，实现对数据的操作
```

```
flask-sqlalchemy
     使用步骤：1.pip install flask-sqlalchemy
              2.创建SQLALCHEMY对象
                                   ①：db=SQLAlchemy(app=app)
                                   ②：db=SQLAlchemy()  上面这句话一般会放到models中  因为需要db来调                                       用属性 db.init_app(app=app)
              3.config中配置  SQLALCHEMY_DATABASE_URI
                dialect+driver://username:password@host:port/database
                数据库 + 驱动 :// 用户:密码@ 主机:端口/数据库
                mysql是需要全部配置
                sqlite
                    轻量级数据库，配置简单
                    sqlite:///xxxx（sqlite3.db）
                执行
                    views中db.create_all()
                        有坑
                            primary-key
                                添加主键
                            SQLALCHEMY_TRAKE_MODIFICATIONS
                                app.config[‘SQLALCHEMY_TRAKE_MODIFICATIONS’]=False
                  
```

```
使用：
	定义模型
			继承Sqlalchemy对象中的model
	定义字段
              主键
                  一定要添加
              所需要字段
              语法
                  db.Column( db.类型（）,约束 )
     创建
	db.create_all()
	删除
	db.drop_all()
	修改表名
	__tablename__ = "Worker"
    数据操作
        创建对象
        添加
            db.session.add(对象)
            db.session.commit()
        查询
            模型.query.all()
```

## 17.项目拆分

```
	（1）开发环境
                开发环境
                测试环境
                演示环境-类似线上环境也叫做预生产环境
                线上环境 也叫做 生产环境
	（2）拆分项目
                规划项目结构
                    manager.py
                        app的创建
                        Manager （flask-script管理对象）
                    App
                        __init__
                            创建Flask对象
                            加载settings文件
                            调用init_ext方法
                            调用init_blue方法
                        settings
                            App运行的环境配置
                            运行环境
                        ext（扩展的，额外的）
                            用来初始化第三方的各种插件
                            Sqlalchemy对象初始化 数据库
                            Session初始化
                        views
                            蓝图
                            创建
                            注册到app上
                        models
                            定义模型
```

## 18.flask-migrate

```
使用步骤
        （1）安装
            	pip install flask-migrate
        （2）初始化
                1.创建migrate对象
                  需要将app 和 db初始化  	ext
                       migrate = Migrate()
                       migrate.init_app(app=app, db=db)
                2.懒加载初始化
                  结合flask-script使用
                  在manage上添加command (MigrateCommand)
                       manager.add_command("db", MigrateCommand)
        （3）python manager.py db xxx
                1.init     第一次使用
                2.migrate  生成迁移文件
                           不能生成有2种情况
                                （1）模型定义完成从未调用
                                （2）数据库已经有模型记录
                3.upgrade  升级
                4.downgrade 降级
          扩展：
                创建用户文件
                    python manager.py db migrate  --message ‘创建用户’
```

## 19.DML

```
1.增
	创建对象
		（1）添加一个对象
                  db.session.add()
                         eg:
                         @blue.route("/addperson/")
                          def add_person():
                              p = Person()
                              p.p_name = "小明"
                              p.p_age = 15
                              db.session.add(p)
                              db.session.commit()
                              return "添加成功"
         （2）添加多个对象
                  db.session.add_all()
                          eg:
                          @blue.route("/addpersons/")
                          def app_persons():
                              persons = []
                              for i in range(5):
                                  p = Person()
                                  p.p_name = "猴子请来的救兵%d" % random.randrange(100)
                                  p.p_age = random.randrange(70)
                                  persons.append(p)
                              db.session.add_all(persons)
                              db.session.commit()
                              return "添加成功"
```

```
2.删除
	db.session.delete(对象)
		基于查询
```

```
3.修改
	db.session.add(对象)
		基于查询
```

### 查

```
1.获取单个数据
	（1）get
            主键值
            获取不到不会抛错
            person = Person.query.get(3)
            db.session.delete(person)
            db.session.commit()
	（2）first
		   person = Person.query.first()
```

```
2.获取结果集
	（1）xxx.query.all
			persons = Person.query.all()
	（2）xxx.query.filter_by
			persons = Person.query.filter_by(p_age=15)
	（3）xxx.query.filter
			persons = Person.query.filter(Person.p_age < 18)
			persons = Person.query.filter(Person.p_age.__le__(15))
			persons = Person.query.filter(Person.p_name.startswith("小"))
			persons = Person.query.filter(Person.p_name.endswith("1"))
			persons = Person.query.filter(Person.p_name.contains("1"))
			persons = Person.query.filter(Person.p_age.in_([15, 11]))
```

```
3.数据筛选
	（1）order_by
			persons = Person.query.order_by("-p_age")
	（2）limit
			persons = Person.query.limit(5)
	（3）offset
			persons = Person.query.offset(5).order_by("-id")
	（4）offset和limit不区分顺序，offset先生效
			persons = Person.query.order_by("-id").limit(5).offset(5)
			persons = Person.query.order_by("-id").limit(5)
		 	persons = Person.query.order_by("-id").offset(17).limit(5)
	（5）order_by 需要先调用执行
		 	persons = Person.query.order_by("-id").offset(17).limit(5)
```

```
4.pagination
	（1）简介：分页器
              需要想要的页码
              每一页显示多少数据
	（2）原生：
		 	 persons = Person.query.offset((page_num - 1) * page_per).limit(page_per)
	（3）封装：
          	 参数（page，page_per,False(是否抛异常）
         	 persons = Person.query.paginate(page_num, page_per, False).items
```

```
5.逻辑运算
	（1）与
		    and_     filter(and_(条件))
			huochelist = kaihuoche.query.filter(and_(kaihuoche.id == 1,kaihuoche.name == 'lc'))

	（2）或
			or_          filter(or_(条件))
			huochelist = kaihuoche.query.filter(or_(kaihuoche.id == 1,kaihuoche.name =='lc'))

	（3）非
			not_         filter(not_(条件))  注意条件只能有一个
			huochelist = kaihuoche.query.filter(not_(kaihuoche.id == 1))

	（4）in
		    huochelist = kaihuoche.query.filter(kaihuoche.id.in_([1,2,4]))

```

## 20.数据定义

```
	（1）字段类型
                Integer
                String
                Date
                Boolean
	（2）约束
		primary_key   （主键）   			
		autoincrement （主键自增长）     			
		unique        （唯一） 			
		default       （默认）   			
		index         （索引）    			
		no't'null     （非空）			
		ForeignKey    （外键）                       
                        用来约束级联数据
                        db.Column( db.Integer, db.ForeignKey(xxx.id) )
                        使用relationship实现级联数据获取
                            声明级联数据
                            backref="表名"
                            lazy=True
```

## 21.模型关系

### 1.一对多

```
（1）模型定义
          class Parent(db.Model):
              id=db.Column(db.Integer,primary_key=True,autoincrement=True)
              name=db.Column(db.String(30),unique=True)
              children=db.relationship("Child",backref="parent",lazy=True)
              def __init__(self):
                  name=self.name

          class Child(db.Model):
              id = db.Column(db.Integer, primary_key=True)
              name = db.Column(db.String(30), unique=True)
              parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
              def __init__(self):
                  name = self.name
```

```
 （2）参数介绍:
 		 1.relationship函数
                    sqlalchemy对关系之间提供的一种便利的调用方式，关联不同的表；
          2.backref参数
                    对关系提供反向引用的声明，在Address类上声明新属性的简单方法，之后可以在my_address.person来获取这个地址的person；
          3.lazy参数
                    （1）'select'（默认值）
                        SQLAlchemy 会在使用一个标准 select 语句时一次性加载数据；
                    （2）'joined'
                        让 SQLAlchemy 当父级使用 JOIN 语句是，在相同的查询中加载关系；
                    （3）'subquery'
                        类似 'joined' ，但是 SQLAlchemy 会使用子查询；
                    （4）'dynamic'：
                        SQLAlchemy 会返回一个查询对象，在加载这些条目时才进行加载数据，大批量数据查询处理时推荐使用。
          4.ForeignKey参数
                    代表一种关联字段，将两张表进行关联的方式，表示一个person的外键，设定上必须要能在父表中找到对应的id值
```

```
（3）模型的应用
            添加
                eg：@blue.route('/add/')
                    def add():
                        p = Parent()
                        p.name = '张三'
                        c = Child()
                        c.name = '张四'
                        c1 = Child()
                        c1.name = '王五'
                        p.children = [c,c1]

                        db.session.add(p)
                        db.session.commit()

                        return 'add success'
            查
                  eg:
                  主查从 --》 Parent--》Child
                  @blue.route('/getChild/')
                  def getChild():
                      clist = Child.query.filter(Parent.id == 1)
                      for c in clist:
                          print(c.name)
                      return 'welcome to red remonce'
                  从查主
                  @blue.route('/getParent/')
                  def getParent():
                      p = Parent.query.filter(Child.id == 2)
                      print(type(p))
                      print(p[0].name)
                      return '开洗'
```

### 2.一对一

```
   一对一需要设置relationship中的uselist=Flase，其他数据库操作一样。
```

### 3.多对多

```
（1）模型定义
          class User(db.Model):
              id = db.Column(db.Integer,primary_key=True,autoincrement=True)
              name = db.Column(db.String(32))
              age = db.Column(db.Integer,default=18)

          class Movie(db.Model):
              id = db.Column(db.Integer,primary_key=True,autoincrement=True)
              name = db.Column(db.String(32))

          class Collection(db.Model):
              id = db.Column(db.Integer,primary_key=True,autoincrement=True)
              u_id = db.Column(db.Integer,db.ForeignKey(User.id))
              m_id = db.Column(db.Integer,db.ForeignKey(Movie.id))
```

```
（2）应用场景
          购物车添加
              @blue.route('/getcollection/')
              def getcollection():
                    u_id = int(request.args.get('u_id'))
                    m_id = int(request.args.get('m_id'))
                    c = Collection.query.filter(Collection.u_id == u_id).filter_by(m_id = m_id)

                    if c.count() > 0:
                        print(c.first().u_id,c.first().m_id)
                        # print(c)
                        # print(type(c))
                        # print('i am if')
                        return '已经添加到了购物车中'
                    else:
                        c1 = Collection()
                        c1.u_id = u_id
                        c1.m_id = m_id
                        db.session.add(c1)
                        db.session.commit()
                        return 'ok'
```

## 22.分页器方法

```
分页器
	BaseQuery.paginate()
		page
		per_page
		False
	Pagination
		items
		pages         （获取总页数）
		prev_num      （上一页的页码）
		has_prev      （是否有上一页）
		next_num      （下一个页码）
		has_next	  （是否有下一页）
		iter_pages
```

## 23.flask-bootstrap

```
插件安装
	pip install  flask-bootstrap
ext中初始化
	Bootstrap（app=app）
	
bootstrap案例--bootstrap模板   {% extends ‘bootstrap/base.html’%}
```

## 24.flask-debugtoolbar

```
辅助调试插件
安装
	pip install flask-debugtoolbar
初始化  ext 
    app.debug = True (最新版本需要添加)
	debugtoolbar = DebugToolBarExtension()
	debugtoolbar.init_app(app=app)
```

