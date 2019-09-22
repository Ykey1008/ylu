# JavaScript_函数

## 1.函数的概念

将一段公共的代码，起个名字，就叫“函数”。

函数的特点：减少代码量、提高工作效率、后期维护十分方面。

```
function functionA(形参1,形参2,形参3...){  
  函数的功能;
  [return  返回值]
}
```

-  function关键字，必须的。

-  functionName函数名称，命名与变量一样。

- ()函数的形参(形式参数)。

```
 多个形参之间用英文下逗号隔开。

 形参可有有无，如果没有形参，小括号不能省略。

 形参不能是具体的值，只能是一个变量。

 形参主要用来接收调用函数者，传递过来的数据。
```

-  {}中存放函数的功能代码。如：求最大值、验证用户名是否含有特殊符号、邮箱格式是否正确等。

-  return语句：向调用函数者，返回一个值。

```
 return语句一旦执行，函数剩余的代码不再执行。

 return语句结束函数运行。
```

- **注意：函数只定义是没有任何效果的，函数必须被调用，才能看到效果。**

- 函数只定义是不会执行的。

## 2.函数参数

- 形参(形式参数)：定义函数时的参数，叫形参。主要用来接收调用函数者传递的一个值。

- 实参(实际数据)：调用函数时的参数，叫实参。主要用来向定义函数传值。

- 形参与实参个数必须一样。

```
function showInfo(name,action) //<---这里的是形参
{
  //代码体
}
showInfo("tom","吃饭"); //<---实参
```

## 3.return语句

- return语句，只能用于函数中。

- return语句中止函数执行，也就是 return语句之后的其它代码不再执行。

- return语句，用于向调用函数者返回一个值。

如果不使用return语句返回的话，则函数返回undefined值。

```
//定义函数
function showInfo(name,action){
  var str = name + "在" + action + "!<br />";
  return str;
}
//调用函数
var str2 = showInfo("张三","打游戏");
//输出结果
document.write(str2);
```

## 4.拷贝传值和引用传值

4.1  拷贝传值：将一个变量的值，“复制”一份，传给另一个变量。这两个变量没有任何关系。

这两个变量是相互独立的，修改其中一个，另一个不会受影响。

基本数据类型都是拷贝传值：字符型、数值型、布尔型、undefined、null。



4.2  引用传地址：将一个变量的“数据地址”，“复制”一份，传给了另一个变量。

那么，这样来，两个变量指向了“同一物”“同一空间”。

这两个变量之间是有联系的，修改其中一个，另一个也会变。

哪些数据类型是引用传地址？复合数据类型：数组、对象、函数。

## 5.匿名函数

匿名函数，就是没有名字的函数。

```
//定义匿名函数
function() {
  document.write("ok");
}
//怎么调用????
```

匿名函数，一般是用来给其它变量赋值用的。

将匿名函数的定义，作为一个数据，赋给另一个变量。

这样一来，该变量就是函数型了。

```
var a = function(){
  document.write("ok");
}
//调用函数
var b = a; //引用地址:将变量a的地址给b
b(); //调用函数
```

多维数组：

二维数组的访问

​	一维数组，数组变量名，后跟一个中括号[]，[]中是元素所在的下标值。如：'arr[9]'

​	二维数组，数组变量名，后跟两个连续的[]，[]中是元素所在的下标值。如：'arr[2][3]'

​	三维数组，数组变量名，后跟三个连续的[]，[]中是元素所在的下标值。如：arr[1][2][2]

# JavaScript_对象

对象是由属性和方法构成的。

学习对象，就是学习对象的属性和方法。

## 1. JavaScript对象分类

-  String对象：一个字符就是一个String对象。如：var str = “12345678”;  var len = str.length;

-  Number对象：一个数值数据就是一个Number对象。如：var a = 100.9888;  a.toFixed(2)

- Boolean对象：一个布尔值就是一个Boolean对象。

-  Math对象：数学对象。如：Math.PI、Math.abs()、Math.random()

- Function对象：一个函数就是一个function对象。

-  Array对象：一个数组变量，就是一个Array对象。如：var len = arr.length

-  BOM对象：window、location、history、screen、document

-  DOM对象：a对象、p对象、html对象等。CSS对象。

## 2.自定义对象的创建方法

```
//（1）使用new关键字，结合Object()构造函数，创建一个自定义对象
//创建一个空的对象
var obj = new Object();
//添加属性
obj.name = "周润发";
obj.sex  = "男";
obj.age  = 24;
obj.isMarried = true;
obj.edu  = "小学";
obj.school;
//添加方法：方法就是函数
//将一个函数定义赋给了对象属性，因此该属性变成了方法。
obj.showInfo = function()
{
	var str = "";
	str += "<h2>"+obj.name+"的基本信息如下</h2>";
	str += "姓名："+obj.name;
	str += "<br>性别："+obj.sex;
	str += "<br>年龄："+obj.age;
	str += "<br>婚否："+(obj.isMarried ? "已婚" : "未婚");
	str += "<br>学历："+obj.edu;
	str += "<br>毕业院校："+(obj.school ? obj.school : "未填写");
	document.write(str);
};
//重新赋值
obj.name = "吴亦凡";
obj.school = "装B大学";
//调用方法
obj.showInfo();
```

```
//（2）使用{}创建一个对象
var obj = {
			   name		: "周更生",
			   sex		: "男",
			   age		: 24,
			   isMarried: true,
			   edu		: "大专",
			   showInfo : function(){
					//this是系统关键字，代表当前对象
					//this应用于对象内部。
					var str = "<h2>"+this.name+"的基本信息如下</h2>";
					str += "姓名："+this.name;
					str += "<br>性别："+this.sex;
					str += "<br>年龄："+this.age;
					str += "<br>婚否："+(this.isMarried ? "已婚" : "未婚");
					str += "<br>学历："+this.edu;
					str += "<br>毕业院校："+(this.school ? this.school : "未填写");
					document.write(str);
			   },
			   school	: ""

		  };
//对象赋值
obj.name = "马化腾";
obj.isMarried = false;
obj.school = "互联网抄袭大学";
//调用对象方法
obj.showInfo();
```

# JavaScript内置对象

- String对象：提供了一些对字符串处理的属性和方法。

- Array对象：对数组操作的属性和方法。

- Date对象：提供了对系统时钟副本操作的属性和方法。

- Boolean对象：一个布尔值，就是一个Boolean对象。

- Number对象：一个数值就是一个Number对象。toFixed(2)

- Math对象：数学方面的属性和方法。

## 1. String对象--字符串对象

一个字符串的变量，就是一个String对象。

### 1. length属性

- 描述：动态获取字符串的长度。

- 语法： var len = strObj.length

### 2. toLowerCase()和toUpperCase()

- strObj.toLowerCase() 将字母转成全小写。

- strObj.toUpperCase() 将字母转成全大写。

### 3 . charAt(index)

- 描述：返回字符串中指定下标处的**一个**字符。

- 说明：字符串的下标与数组下标一样，都是从0开始的正整数。第1个字符的下标为0，第2个字符的下标为1，第3个字符的下标为2，以此类推。

- 语法：**str**Obj.charAt(index)

- 参数：index是指字符的下标。strObj是原字符串。

- 返回值：字符型的数据。如果参数 index 不在 0 与 string.length 之间，该方法将返回一个空字符串。

### 4. indexOf()

- 描述：在原始字符串，从左往右查找指定的字符串，如果找到，返回其下标值。如果没有找到，返回-1。

- 语法：**str**Obj****.indexOf(****substr**)**

- 参数：substr就是要查找的子字符串。

- 注意：只查找第一次出现的字符，第二个相同的不再查找。

### 5. lastIndexOf()

-  描述：在原始字符串，从右往左查找指定的字符。只查找第一次出现的字符，第二个相同的不再查找。

-  返回值：如果找到返回对应的索引值，如果没有找到，返回-1。

-  语法：**strObj.lastIndexOf(substr)**

### 6. substr()

- 描述：从原始字符串，提取指定的子字符串。

- 语法：**strObj.substr(startIndex [ , length])**

- 参数：

```
 startIndex是要查找的子字符串的开始位置(索引号)。

 length可选项。从startIndex处往后提取length个字符。如果length省略，则一直提取到结尾。
```

### 7. substring()

-  描述：从原始字符串，提取指定的子字符串。

-  语法：**strObj.substring(startIndex [ , endIndex])**

-  参数：

```
startIndex是要查找的子字符串的开始位置(索引号)。

endIndex可选项。从startIndex到endIndex处的所有字符。如果endIndex省略，则一直提取到结尾。

如果开始索引和结束索引都使用，则返回的字符应该包含开始索引处的字符，不包含结束索引处的字符(含前不含后)。
```

### 8. split()——将字符串转成数组

- 描述：将一个字符串切成若干段，将一个字符串分割成一个数组。

- 语法：**array strObj.split(separator)**

- 参数：separator是一个字符串的分割符，可以为空字符串。

- 返回值：是一个数组。

## 2. Array对象

一个数组量，就是一个Array对象。

### 2.1 length属性

### 2.2 join()

- 描述：将一个数组各元素，用指定的连接号，连成一个字符串。

- 语法：string arrObj.join(separator)

- 参数：separator代表元素之间的连接号。

### 2.3 添加和删除数组元素

-  delete删除元素的值，而下标还在(长度不会减少)。

- push从后面插入新的元素。

-  shift()删除第1个数组元素，数组长度减1。并返回删除元素的值。

-  pop()删除最后1个数组元素，数组长度减1。并返回删除元素的值。

- unshift()在数组的开头添加一个或多个元素，数组长度会变化。

- push()在数组的结尾添加一个或多个元素，数组长度会变化。

### 2.4 reverse()

- 描述：对数组中各元素进行反转顺序。

- 语法：arrObj.reverse()

## 3.Date对象

1.创建当前Date对象的副本

```
//创建当前Date对象副本
var today = new Date();
document.write(today);
```

2.创建指定时间戳的Date对象

时间戳：就是指距离(格林威治)1970年1月1日0时0分0秒，过去了多少毫秒。1秒 = 1000毫秒

```
//根据指定的时间戳的Date对象
//Date()的参数是一个毫秒值,而我们python的时间戳是秒值
var date2 = new Date("1990-10-12 10:09:34").getTime();
document.write(date2);
```

3.根据指定时间字符串的参数，来创建Date对象

```
//根据指定的时间戳的Date对象
//Date()的参数是一个毫秒值,而我们python的时间戳是秒值
var date2 = new Date("1990-10-12 10:09:34").getTime();
document.write(date2);
```

4.根据指定的年、月、日、时、分、秒的数值，来创建Date对象

```
var date2 = new Date(1990+100,10,12);
document.write(date2);
```

5.Date对象的方法

- getFullYear()：获得四位年份。如：2015

- getMonth()：月份，取值0-11。

- getDate()：天数。

-  getHours()：小时数。

-  getMinutes()：分钟数

- getSeconds()：秒数

- getMilliseconds()：毫秒数

-  getDay()：星期值，0-6

-  getTime()：总的毫秒值

# Math数学对象

- Math.PI：圆周率

- Math.abs()绝对值。如：Math.abs(-9) = 9

- ceil()向上取整(整数加1，舍去小数)。如：Math.ceil(9.23) = 10 、Math.ceil(9.98) = 10

- floor()向下取整(舍去小数)。如：Math.floor(9.87) = 9

- round()四舍五入。如：Math.round(9.8)=10  Math.round(9.4) = 9

- pow()幂次数。如：Math.pow(2,4) = 16

- sqrt()开方。如：Math.sqrt(9) = 3 

- random()返回0-1之间的随机小数。Math.random() = 0.9026920931341323

- toFixed(2) 属于数值对象，保留小数点后面的几位数

- 随机整数公式  Math.random()*(max-min)+min  

# BOM和DOM简介

## 1.BOM

- BOM Browers Object Model ，浏览器对象模型。

- BOM它提供了访问或操作浏览器各组件的方法或途径。

- 浏览器各组件，以下对象都是浏览器对象，不是JS的对象

```
window浏览器窗口。

location地址栏对象。

history历史记录对象。

screen屏幕对象。

navigator浏览器软件对象。

document文档对象
```

- BOM只是一个标准，是一个模型，是一个概念。它不是真正能操作的对象。

- JavaScript是Netscape(网景)公司的产品。

- BOM是W3C制定的一种操作浏览器各组件的标准。

- W3C是制定互联网标准的。如：XHTML、CSS、XML、js、DOM、BOM、HTML5等。

- BOM或DOM**标准**，是在**浏览器**当中，**以对象的形式**，得以实现。

## 2.DOM

- DOM Document Object Model，文档对象模型。

- DOM主要用来：访问或操作网页中各元素(标记)对象的一种方法途径。

- DOM模型中，把网页中各标记，都看成是一个一个的对象。

```
 <p>对象

 <a>对象

<html>对象

<body>对象
```

## 3.BOM对象结构图

![](C:\Users\yang\Documents\PYthon笔记\HTML Lesson\images_1\images_3.png)

## 4. for....in循环

for in 循环主要用来遍历数组下标，或对象属性。

```
//遍历数组的语法
for(var index in arrObj){
  循环代码;
}
```

```
//使用for in循环求以下数组的和
var arr = [1,3,5,7,9,11];
//定义一个和的初始值
var sum = 0;
var n = 0 //循环次数
//只查找有效数据的下标
//如果数组是undefined,则直接跳过
for(var index in arr){
  sum += arr[index];
  n++;
}
document.write("sum="+sum+",n="+n);
```

# window对象---浏览器窗口对象

## 1.window对象属性

- name：代表窗口的名称。用于<a>标记的taget属性。

- top：代表最顶层窗口，top也是window对象。常用在框架当中。

- parent：代表父窗口，也是window对象。常用在框架当中。

- self：代表当前窗口，也是window对象。常用在框架当中。如：self.alert()

- innerWidth：窗口的内宽，不含菜单栏、工具栏、滚动条、地址栏等。(Firefox支持)
- 在IE中，使用 document.documentElement.clientWidth 来代替 
- documentElement指<html>元素对象。 document.body指<body>元素对象。

## 2.window对象方法

### 1. alert()方法

弹出一个警告对话框，只有一个确定按钮。

### 2. prompt()方法

弹出一个输入对话框，有确定和取消两个按钮。单“确定”返回字符串数据。单击“取消”返回null。

### 3. confirm()

-  描述：弹出一个确认对话框。

-  语法：**window.confirm(msg)**

-  参数：msg是提示信息。

-  返回值：单击“确定”返回true，单击“取消”返回false。

### 4. close()

-  描述：关闭window窗口。

-  语法：**window.close()**

  

 如何使用 window.close() 关闭窗口？

 修改Firefox浏览器的配置。

 在Firefox浏览器的地址栏，输入：**about:config** 并回车。



### 5.  window.open()

- 描述：打开一个新的浏览器窗口。

- 语法：**var winObj = window.open(url,name,options)**

- 参数：

```
url：在新窗口中打开的文件的URL地址，可以为空。

name：新窗口的名字。可以通过window.name属性来获取，用于<a>标记的target属性。

options：新窗口的规格。

menubar：是否显示菜单栏，取值：yes、no

toolbar：是否显示工具栏。

status：是否显示状态栏。

scrollbars：是否显示滚动条。

location：是否显示地址栏。

width：新窗口的宽度

height：新窗口的高度

left：新窗口距离屏幕左边距离。

top：新窗口距离屏幕顶边距离。

三个参数都可以为空，为空后打开一个空白窗口。
```

- 返回值：返回一个window对象。通过该winObj变量，可以跟踪新窗口。



- 举例：var winObj = window.open(“test.html” , “newWin” , “width=400,height=300,left=300,top=200”)

```
//实例：弹出一个新窗口
/*
	(1)当网页加载完成，弹出一个新窗口，新窗口名字叫“win2”
	(2)新窗口的尺寸：width=400，height=300
	(3)新窗口在显示屏幕中居中显示
	(4)单击原窗口中的链接，在新窗口中显示内容
	(5)新窗口10秒钟后，自动关闭
*/
//网页加载完成后，调用一个匿名函数
window.onload = function()
{
	//变量初始化
	var url2 = "";
	var name2 = "win2";
	var winWidth = 400;
	var winHeight = 300;
	var screenWidth = screen.width;
	var screenHeight = screen.height;
	var x = (screenWidth-winWidth)/2;
	var y = (screenHeight-winHeight)/2-100;
	var options2 = "width="+winWidth+",height="+winHeight+",left="+x+",top="+y;
	//打开一个新窗口
	var winObj = window.open(url2,name2,options2);
	//给新窗口添加背景色
	winObj.document.write("<h2>新窗口的标题</h2>");
	winObj.document.body.bgColor = "gray";
	//新窗口在5秒钟后，自动关闭
	winObj.setTimeout("window.close()",5000);
}
```

# 延时器:时间一到，执行一次

## 1.setTimeout()——设定延时器

- 描述：在指定的毫秒时间后，执行JS代码**一次**。

- 语法：var timer = window.setTimeout(code,millisec)

- 参数

```
code是合法的JS代码，一般是JS函数或对象方法。如果是函数的话，必须加引号。加引号相当于“传地址”。

millisec是毫秒值。1秒＝1000毫秒

返回值：返回延时器的变量id，是一个整型。用来被 clearTimeout() 清除。

举例：

var timer = window.setTimeout(“func()” , 1000)  //1秒后调用func()函数，带引号，带括号，是传地址。

var timer = window.setTimeout( func , 1000)  // 1秒后调用func()函数，不带引号不带括号，是传地址。
```

## 2.clearTimeout()——清除延时器变量

- 描述：清除由setTimeout()设置的延时器变量。

- 语法：window.clearTimeout(timer)

 

# 定时器——周期性执行

## 1.setInterval()

- 描述：每隔指定的毫秒值，执行JS程序一次(周期性执行)。

- 语法：var timer = window.setInterval(code,millisec)

- 参数

```
code是合法的JS代码，一般是JS函数或对象方法。如果是函数的话，必须加引号。加引号相当于“传地址”。

millisec是毫秒值。1秒＝1000毫秒
```

- 返回值：返回定时器的变量id，是一个整型。用来被 clearInterval() 清除。

```
var timer = window.setInterval(“func()” , 1000)  //每隔1秒调func()函数。

var timer = window.setInterval( func , 1000)  // 每隔1秒调用func()函数。
```

## 2.clearInterval()——清除定时器变量

- 描述：清除由setInterval()设置的定时器变量。

- 语法：window.clearInterval(timer)



# screen屏幕对象

- Width：屏幕总宽度，包括任务栏。

- Height：屏幕总高度，包括任务栏。

- availWidth：屏幕有效宽度，不含任务栏。

- availHeight：屏幕有效高度，不含任务栏。



# navigator对象

- appName：浏览器软件名称。如果是Firefox显示 “Netscape”。如果是IE的话，显示“Microsoft Internet Explore”

- appVersion：浏览器软件的版本号，是核心版本号。

- systemLanguage：系统语言。

- userLanguage：用户语言。

- platform：平台。



# location地址栏对象

html的跳转:

<meta http-equiv="refresh" content="2;url=http://www.baidu.com">

js的跳转

location.href = “http://www.sina.com.cn”;

注意：以下所有属性，重新赋值后，将重新刷新网页。

-  href：获取或设置地址栏中的地址。如：location.href = “http://www.sina.com.cn”

-  host：获取或设置主机名。

-  hostname：主机名。

-  pathname：文件及路径。

- search：查询字符串。指地址栏中“?”之后的字符。如：**?**name=yao&password=123456

-  protocol：协议。如：http://、ftp://、file:///

-  hash：锚点名称。如：#top

-  reload()：刷新网页，相当于工具栏中“刷新”按钮。

# history对象

- go(n)：既可以前进，也可以后退

```
history.go(0)  //刷新当前网页

history.go(1)  //前进一步

history.go(2)  //前进二步

history.go(-1)  //后退一步

history.go(-2)  //后退二步
```

- forward()：相当于“前进”按钮。



- back()：相当于“后退”按钮。

```
//实例：图片切换效果
/*
	(1)当网页加载完成时，开始图片切换。
	(2)给<img>指定id。
	(3)获取id=img01的元素的对象
	(4)使用延时器或定时器实现。
*/
//(1)当网页加载完成时，调用一个普通函数。
window.onload = init;//将函数地址传给事件
                     //函数传地址，不带括号
					 //带括号，是将函数的执行结果传事件。
					 //函数结果，就是返回值，默认返回undefined
//定义函数
function init()
{
	//定时器开关
	window.setInterval("start2()",1000);
}
//动画主函数
var i = 1;
function start2()
{
	if(i>6)
	{
		i = 1;
	}
	//获取id=img01的图片对象
	var imgObj = document.getElementById("img01");
	//给imgObj对象src属性重新赋值
	imgObj.src = "images/image_"+i+".jpg";
	i++;
}
```

```
//实例：图片切换效果
/*
	(1)当网页加载完成时，开始图片切换。
	(2)给<img>指定id。
	(3)获取id=img01的元素的对象
	(4)使用延时器或定时器实现。
*/
//(1)当网页加载完成时，调用一个普通函数。
window.onload = init;//将函数地址传给事件
                     //函数传地址，不带括号
					 //带括号，是将函数的执行结果传事件。
					 //函数结果，就是返回值，默认返回undefined
var i = 1;
//定义函数
function init()
{
	if(i>6)
	{
		i = 1;
	}
	//获取id=img01的图片对象
	var imgObj = document.getElementById("img01");
	//给imgObj对象src属性重新赋值
	imgObj.src = "images/image_"+i+".jpg";
	i++;
	//延时器开关
	window.setTimeout("init()",1000);
}
```

```
<img id="img01" src="images/image_1.jpg" />
```

