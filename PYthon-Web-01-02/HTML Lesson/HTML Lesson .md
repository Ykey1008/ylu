# HTML Lesson 1

1.html

2.css

3.js基础

4.jquery

5.vueru

c/s	

c代表终端列如手机，平板，手表            s代表服务器：web服ruan务器（nginx）

b/s    

 b代表Browser 浏览器     server 服务器，是当前最流行的网络模式，所有的功能软件都安装在服务器中，相对于客户端来说，压力就更小了

# 初始HTML

HTML Hyptertext Markup Language  超文本标注语言

HTML的主要功能是：控制网页结构的，比如什么是标题，什么地方是段落，什么是连接等

超文本：除了文本以外，还可能有图片，音乐，视频，链接等

标注：可以理解为一种标记，记号，标志。

语言：这里的语言于程序半点关系都没有

## 1.HTML结构树

![](C:\Users\yang\Documents\PYthon笔记\HTML Lesson 1\images_1\tree.png)

```
<!DOCTYPE html>    <---不是HTML标签；它告诉浏览器页面使用的是HTML什么版本。
<html>                    <--HTML标签
<head>                    <--HTML的头部标签
<meta charset="utf-8" />    <--设置字符集
<title>网页的标题</title>  <--网页的标题
</head>

<body>                    <--网页的正文内容,排版就是进行在body中的
	网页的正文内容
</body>
</html>
```



```
html></html>：表示一个网页。或者告诉浏览器是什么类型的文件。<html>有两个子标记<head>和<body>。
	<head></head>：称为文件头标记。这里的内容一般是一些控制信息，其中的信息在浏览器中是看不见的。
	<title></title>:表示网页的标题，其内容只能是纯文本。
		<meta />标记，告诉浏览器，这个网页中的汉字用什么编码解析。
			默认编码是GB2312(简体中文编码)   一共对6763个汉字进行了编码。
			GBK简体中文编码，一共对9万个汉字进行编码。
			BIG5繁体中文编码。
			JIS日文编码。
			UTF-8多国语言编码，每个国家的语言都能正常显示。
	<body></body>表示网页的正文内容。正文内容在浏览器中是可见的。
```

这是HTML4的meta的写法

```
<meta http-equiv='content-type' content='text/html;charset='utf-8' />
```

这是HTML5的写法,<meat>标记的意义是，告诉当前文件是什么类型的，汉字用utf-8来显示

```
<meat charsset='utf-8' />
```

## 2.HTML标签格式

HTML标签分两类：一是双边标记（常规标签），二是单边标签（空标签）

1. <标签 属性 = ‘属性值‘  属性 = ’属性值 ’ > 内容 </标签>
2. <标签 属性 = ‘属性值‘  / > 

## 3.“属性”的理解

按照python中类的属性，来理解

## 4.HTML标签编写规范

HTML：标签不区分大小写，标签属性可以有，也可以没有属性。 HTML标记和属性间用空格隔开，各属性之间也用空格来隔开。  HTML标签只能顺序嵌套，不能交叉嵌套。标记只能一层套一层，外层套里层，向肉夹馍一样

## 5.HTML文本修饰标记

这几个标签和word的功能非常相识

<b></b> 文本加粗 bold

<i></i>文本斜体 italic

<u></u> 下划线 underline

<s></s>删除线 strike

<sub></sub> 下标   B<sub>2</sub>

<sup></sup>上标   A<sup>2</sup>

<font></font> 文本字体

color 文本颜色

size 文字大小，数值越大，字越大

face 字体样式。取值：黑体，楷体

## 6.代码编辑器简介

代码编辑器分为两大类：1.IDE集成开发环境 2.增强的文本编辑器

## 7.静态网页和动态网页

静态网页的扩展名：.html  .htm  在很久以前，Windows32操作系统不支持，大于3个字符的尾缀名，列如以前word文档是。doc,现在是.docx

动态网页的扩展名是 .py .jsp .asp .aspx

记事本的默认字符是ansi编码，在中文操作系统，ANSI编码就是GBK

如何保证网页中的汉字不出现乱码

- 保证字符集是一致的
- 编辑环境的字符集
- <meta> 标记字符集



## 8.HTML排版标记

### 1、`<p>`段落

格式：`<p>……</p>`
常用属性
align：文本的水平对齐方式，取值：left(左)、center(居中)、right(右)
特点：在段前或段后，会有一个空行

### 2、换行标记`<br />`

换段标记，在段落前后会多一个空行。
换行标记，行间距不会发生任何改变。

### 3、水平线标记`<hr />`

语法：`<hr  属性 = “属性值”/>`
属性:

```
color：线条颜色。
size：线的粗细
width：线的宽度
align：线的水平对齐方式，取值：left、center、right
noshade：是否要去阴影。该属性没有值。
<hr noshade size='1'/>
<hr color='red' size='1' />
<hr color='blue' size='5' width='50%' align='center'/>
```

### 4、预排版标记：`<pre></pre>`

描述：可以保留所有的空白字符(换行、空行、空格)，换句句说：原封不动的输出。
语法：`<pre 属性 = “属性值”>……</pre>`
属性：`width`，元素的宽度。

### 5、标题标记`<h1>…<h1>`

描述：一共有六个标题标记，分别为`<h1>`、`<h2>`、`<h3>`、`<h4>`、`<h5>`、`<h6>`，其中`<h1>最大`，`<h6>最小`。
语法：`<h1 属性 = “属性值”>`……</h1>
属性：`align`，水平对齐方式，取值：`left、center、right`

## 9.块元素与行内元素

‘<div>`’和`‘<span>`’是两个最没有意义的标记，但是，又是使用最多的标记。

### 1、块元素

特点：
块元素的宽度`撑满整个网页`(父元素)。
块元素一定要`另起一行`排版。
块元素`单独占一行`，不管有多少内容。
常用的块元素有哪些？`<p>、<h1>、<h2>、<h3>、<pre>、<div>、<table>`等。

### 2.行内元素

特点：
行内元素`没有宽度`，行内元素的宽度主要由`内容`决定。
行内元素`不会另起一行`排版。
多个行内元素排在同一行。
常用的行内元素有哪些？`<font>、<b>、<i>、<u>、<sup>、<sub>、<span>`等
注意事项：行内元素和块元素，`相互嵌套时，块元素中嵌套行内元素`。

### 3.HTML字符实体

```
空格：&nbsp;     (一个汉字占用两个空格的空间)
<：&lt;
>：&gt;
&：&amp;
版权号：&copy;
￥：&yen;
×：&times;
÷：&divide;
```

## 10.ul,li,HTML中的列表-无序列表

‘<ul>’`和`‘<li>`’的公共属性
`type`：项目符号的类型，取值：`disc`(小黑点)、`circle`(圆圈)、`square`(小方块)

```

<ul type='square'> 
<li>内容</li>    
<li type='disc'>内容</li>  
<li>内容</li> 
<li type='circle'>内容</li> 
<li>内容</li>
</ul>
```

## 11.ol,li,HTML-有序列表

‘<ol>’`和‘`<li>`’的公共属性
type：编号的类型。取值：a、A、1、i、I
start：从第几个开始。该值一定是正整数。

```
<h1>省份城市列表<h1>
<ol>
	<li>安徽
		<ol type='a' start='2'>
			<li>合肥</li>
			<li>芜湖</li>
			<li>黄山</li>
		</ol>
	</li>
	<li>江苏
		<ol type='I' start='2'>
			<li>苏州</li>
			<li>无锡</li>
			<li>常州</li>
		</ol>
	</li>
</ol>
```

## 12.dl,dt,ddHTML自定义列表

‘<dl>`’ 标签用于结合 `‘<dt>`’ （定义列表中的项目）和 `‘<dd>` ’（描述列表中的项目）。

```
<dl>
	<dt>省份</dt>
		<dd>上海</dd>
		<dd>福建</dd>
		<dd>浙江</dd>
	<dt>货币</dt>
		<dd>人民币</dd>
		<dd>美元</dd>
		<dd>英镑</dd>
</dl>
```



## 13.marquee滚动字幕标记

语法：`<marquee 属性 = “属性值”>……</marquee>`
属性:



```
Direction：滚动的方向，取值：left、right、up、down
Width：宽度
Height：高度
bgColor：背景色
scrollAmount：滚动步长值。值越大滚动的越快。默认值为6px。
scrollDelay：延时时间，两步之间停留的时间，以毫秒为单位。1秒＝1000毫秒
```

```
<marquee direction='left' width='400px' height='300px' bgcolor='#ffff66' scrollAmount='100' scrollDelay='40'>
<p>我是漂浮物</p>
</marquee>
```

# HTML Lesson 2

## 1.img图片标签

语法格式:`<img  属性 = “属性值” />`
常用属性:

```
src：指图片的路径，该路径可以是相对地址，也可以是绝对地址。
width：图片的宽度。
height：图片的高度。
alt：图片说明。当图片不存在时，显示一个提示信息。
border：图片边框的粗细。
left或right：可以实现图文混排。
left或right的功能相当于CSS中的“浮动”效果。

小技巧:如何保证图片等比例缩放：只需要设置width和height其中一个值即可`。
<img src='images_2/qf_01.jpg' width='40%' border='2' align='left'/>

如何实现图片在某个元素中居中对齐？
<p align='center' style='border:5px solid red;'><img src='images_2/qf_01.jpg' width='40%'/></p>
```

## 2.a超级链接

语法格式：`<a  属性 = “属性值”>……</a>`
常用属性:

href：链接的地址。该地址可以是绝对路径，也可以是相对路径。
target：链接的目标文件在哪个窗口中来打开。
		_blank：弹出一个空白窗口来打开文件。
		_self：在当前窗口中来打开目标文件。
		_parent：在父窗口中来打开目标文件。(常用于框架网页中)
		_top：在最顶层窗口中来打开目标文件。(常用于框架网页中)
name：指定一个锚点名称。所谓“锚点”用于长网页当中。

1.绝对路径

```
1）远程的绝对路径
以 `http://` 开头的网址，就是“绝对路径”。
<h2>远程绝对路径</h2>
<ul>
	<li><a href='http://www.baidu.com' target='_blank'>百度</a></li>
	<li><a href='http://www.taobao.com' target='_self'>淘宝</a></li>
	<li><a href='http://www.jd.com' target='_blank'>京东</a></li>
</ul>
2）本地的绝对路径
以 file:/// 协议开头的网址，也是“绝对路径”
<h2>远程绝对路径</h2>
<ul>
	<li><a href='file:///E:/1000phone/demo.html' target='_blank'>练习</a></li>
	<li><a href='file:///E:/1000phone/marquee.html' target='_blank'>滚动字幕</a></li>
</ul>
相对路径
####（1）当前文件和目标文件在同一个目录下
如果当前文件和目标文件在同一个目录下，是同一级情况下，链接地址：`直接写目标文件名即可`。
<a herf='demo.html' target='_blank'>文件</a>


```

## 3.table表格标签

```
<table>
	<caption>我是一个表格</caption>
	<tr>
		<th>内容</th>
		<th>内容</th>
		<th>内容</th>
	</tr>
	<tr>
		<td>内容</td>
		<td>内容</td>
		<td>内容</td>
	</tr>
</table>
```

<table>`代表表格标记。`<tr>`代表行标记。`<td>`普通单元格。
餐后甜点:`<td>`可以理解为X轴,也就是一列;`<tr>`可以理解为Y轴,也就是一行;

```
1.table属性
border：边线粗细。
bordercolor：边线颜色。
width：表格宽度。
height：表格高度。
align：水平对齐方式，取值：left、center、right
bgColor：背景颜色
background：背景图片
rules：合并所有单元格边线。取值：all
cellpadding：内填充距离(单元格边线到内容间的距离)
cellspacing：单元格间距(两个单元格边线之间的距离)

2.tr属性
height：行高。
bgColor：背景色
background：背景图片
align：水平对齐方式，取值：left、center、right
valign：垂直对齐方式，取值：top、middle、bottom

3.td或th属性
<th>`代表标题行，其中的内容居中加粗显示。`<td>`代表普通单元格。
width：单元格宽度。
height：单元格高度。
bgColor：背景色
background：背景图片
align：水平对齐方式
valign：垂直对齐方式
colspan：合并列的单元格。
rowspan：合并行的单元格。

4.caption表格标题
含义：给表格添加一个标题。
语法：<caption>……</caption>
说明：<caption>标记，放在<table>开始标记之后，所有的<tr>标记之前。一个表格只能有一个<caption>标记。
```

## 4.flash标签<embed>

```
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" width="778" height="202">
    <param name="movie" value="../../resource/banner.swf">
    <param name="quality" value="high">
    <param name="wmode" value="transparent">
    <embed src="images_2/banner.swf" width="100%"  quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent"></embed>
</object>

<embed>的属性
height='100'pixels	设置嵌入内容的高度。
src='url'	嵌入内容的 URL。
type='application/x-shockwave-flash'	定义嵌入内容的类型。
width='100'	设置嵌入内容的宽度。

进程在大规模运算中使用

线程在读取文件，网络连接

携程与CPU无关，核心YEID ，生成器，


```

## 5.锚点链接

锚点链接：可以实现在一个网页的不同部分实现跳转，用在长网页当中(`一定要有滚动条`)。锚点可以理解为一个`记号`。
锚点的制作两个步骤。

定义锚点(记号):`<a  name = “top”></a>`
锚点的命名规则:

```
名称可以包含 a-z、A-Z、0-9、_这些符号。
不能以数字开头。
可以以字母或下划线开头。

跳转到锚点（记号）
省略文件名：<a  href = “#top”>返回顶部</a>
不省略文件名：<a  href = “index.html#top”>返回顶部</a>
文件名可以省略。如果省略，跳转到当前网页的那个记号处。
<a name='top'>i'm top</a>
<a href='#top'>go back</a>

```



# HTML Lesson 3

## 1.form表单介绍

```
1.表单的工作原理
表单的制作大致分为两个步骤 1.前端表单页面的制作。2.服务器端对表单数据的处理。

2.表单的工作原理
填写有表单的网页，单击某个按钮提交表单。
服务器上有专门的程序(Python程序或者其他PHP语言)，对提交的表单数据进行验证。
如果验证通过，服务器会返回一个成功的消息。
如果验证失败，服务器会返回一个失败的消息。

3.表单结构
<form name="login"  method="post" action="http://www.xxxx.com/path" style='border:1px solid black'>
	<span>用 户 名 : </span><input type="text" name="username"  value="" placeholder='请输入账号'/>
    <br/>
	<span>登录密码:</span><input type="password" name="pwd"  value="" placeholder='请输入密码'/>
    <br/>
	<input type="submit" name="submit"   value="登录" disabled />
</form>

4.注意事项
所有表单数据传给服务器的话，必须要有`<form>`标记。
如果哪一个表单元素的值不想传到服务器的话，可以不写`name`属性。

5.form标记-块元素
name：表单名称。用来区分不同的表单，JS可以通过name的值，对表单进行前端的验证。
method：表单数据的发送方式，取值：get和post
action：指定表单数据的处理程序。一般是服务器端的脚本程序(PHP/Python)。如果为空，则提交给自己来处理。
enctype：表单数据的一个加密(编码)方式。enctype属性只能在 method = post 的表单中。
	application/x-www-form-urlencoded   所有字符都进行加密，这种方式不能上传附件
	multipart/form-data //只对附件进行加密码(编码)，不对普通字符进行编码，如果上传文件，必须使用该值。
	
6.GET方法和POST方法
GET提交的表单，它是把表单中的数据(名称=值)，追加到action处理程序的后面，向服务器发送。
GET提交的表单数据，是在地址栏显示的。
https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com&username=123&pwd=789;
注意事项
action处理程序文件名和表单提交数据之间用“?”隔开。
表单元素名称和元素的值之间用“=”隔开。
多个表单的(名=值对)之间用“&”隔开。
get提交方法的特点
相对来说不太安全，因为密码不应该显示在地址栏。
不能传递海量数据，因此地址长度有限制。url字符最大长度65535
最大不能超过4kb chrome8k
不能上传附件。
注意：`只要是通过地址栏，向服务器传数据的，一定是GET传递方式。`

POST提交方式
POST方式直接将表单数据发给了服务器，`不会在地址栏显示`。
POST的特点
相对来说比较安全。包传递
可以传递海量数据，长度没有限制。
可以上传附件。
注意：`POST方式只能用在表单中，其它地方不会用来。

<form name="form"  method="post" action="">
	<table width='50%' style='border:1px solid #ccc'>
		<tr>
			<td width='80' align='left'>用户名:</td>
			<td><input type="text" name="username" value="" placeholder='请输入账号'/></td>
		</tr>
		<tr>
			<td align='left'>密码:</td>
			<td><input type="password" name="password" value="" placeholder='请输入密码'/></td>
		</tr>
	</table>
</form>
```

## 2.表单中的各种元素

```
1.单行文本域：用户名、地址、电话、邮箱等
语法格式：`<input type = “text” 属性 = “属性值” />`
常用属性:
type：元素的类型。取值：text、password、radio、checkbox、button、submit、reset等。
name：表单元素的名称。可以包含a-z、A-Z、0-9、_这些符号，但不能以数字开头。
value：元素的值。
size：文本框的长度，以字符为单位。
maxlength：最多可以输入的字符数
readonly：只读属性。如：readonly = “readonly”
disabled：禁用属性。如：disabled = “disabled”
注意：`单行文本框是有长度限制的，最多只能输入255个字节`。
账号:<input type="text" name="username" value="请输入账号" placeholder='请输入账号'/>
```

```
2.单行密码框
语法格式：`<input type = “password” 属性 = “属性值”  />`
常用属性:
type：元素的类型。
name：元素的名称
value：元素的值
size：密码框的长度，以字符为单位
maxlength：最多可以输入的字符数
readonly：只读属性。如：readonly = “readonly”
disabled：禁用属性。如：disabled = “disabled”
密码:<input type="password" name="password" value="123456" placeholder='请输入密码'/>
```

```
3.单选按钮
语法格式：`<input  type = “radio” 属性 = “属性值” />`
常用属性:
type：元素类型
name：元素名称
value：元素的值
checked：是否默认选中。如：checked = “checked”
注意：`单选按钮是一组相互排斥的，名称应该一样，但提交的值只能是其中一个`。
性别:<input type="radio" name="sex"  value="1" checked>男&nbsp;&nbsp;&nbsp;&nbsp;<input type="radio" name="sex"  value="0">女
```

```
4.复选框
语法格式：`<input  type = “checkbox” 属性 = “属性值” />`
常用属性:
type：元素类型
name：元素名称
value：元素的值
checked：是否默认选中。如：checked = “checked”
注意：`复选框也是一组选项，名称必须一致。可以全选，也可以都不选
兴趣爱好:
<input type="checkbox" name="hobby[]"  value="1" checked>打游戏
<input type="checkbox" name="hobby[]"  value="2">看书
<input type="checkbox" name="hobby[]"  value="3">看姑娘
<input type="checkbox" name="hobby[]"  value="4">泡吧
注意:`复选框的name后面要带[],是一个数组.
```

```
5.下拉列表
`<select>`标记的属性
name：元素的名称。
<option>`标记的属性
value：元素的值
selected：是否默认选中。如：selected = “selected”
想去什么地方旅游:
<select name="dot">
	<option value="">..请选择</option>
	<option value="1">巴厘岛</option>
	<option value="2">马尔代夫</option>
	<option value="3">巴黎</option>
	<option value="4">悉尼</option>
	<option value="5">千锋</option>
</select>

```

```
6.文本区域
描述：使用文本区域来存放大段的文本。
语法：`<textarea  属性 = “属性值”></textarea>`
常用属性:
name：元素名称
value：元素的值，不能直接给<textarea>元素添加value属性。
cols：宽度，是多少个字符宽。
rows：几行的高度。
提示：默认文本内容的应该放在`<textarea>`和`</textarea>`之间。
注意：`你不能直接给<textarea>加一个value属性，不可以。可以通过JS来操作value中的内容`。
输入你的留言:<br/>
<textarea name="info" rows="10" cols="50" value="" style='resize: none;'>..请输入你的信息</textarea>
多学一招:`style='resize: none;'`让文本框不能被拖动;
```

```
7.隐藏域
描述：看不见的表单元素，可以用它来传递一些值，这些值又不想让客户看见。
语法：`<input  type = “hidden”  name = “”  value = “”  />`
<input type='hidden' name='hidden' value='123'>

#CSRF攻击  钓鱼网站
```

```
8.上传文件域
语法格式：`<input  type = “file”  属性 = “属性值”  />`
常用属性:
name：元素的名称。
value：元素的值，应该是上传的文件名称。
注意：基于安全方面的考滤，value属性是只读属性。
<form name="uploadFile" method="post" action="upload.php" enctype="multipart/form-data">
	<input type="file" name="upload"  id="" value=""/>
</form>
多学一招:文件上传的方式只能是`post`,`form`表单必须要多加一个属性和值`enctype="multipart/form-data"`
```

```
9.表单中的各种按钮
提交按钮：提交表单。如：`<input  type = “submit”  value = “提交表单”  />`
重置按钮：重新填写。如：`<input  type = “reset”  value = “重新填写”  />`
图片按钮(不常用)：指定图片的路径，功能也是提交表单。如：`<input type="image" src="images/btn02.png" />`
普通按钮：不具备任何功能，一般要绑定JS程序，来实现各种功能。
<input type='button' name='button' value='按钮' />
<button>按钮</button>

打印网页：<input type="button" value="打印窗口" onclick="javascript:window.print()" />
弹出一个对话框：<input type="button" value="弹出提示" onclick="javascript:window.alert('你好！')" />
`onclick`是当鼠标点击时会发生的事件;
<input type="submit" id="" value="提交表单">
<input type="reset" value="重置">
<input type="image" src='images_3/button.png' >

```

