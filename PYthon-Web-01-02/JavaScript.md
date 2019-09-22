# JavaScript

## 1.javas介绍

JavaScript是什么？

```

一个网页的前端由三个部分构成：
HTML：超文本标注语言，主要用来控制内容的结构的。

CSS：层叠样式表，主要用来控制HTML标签的格式的。

JavaScript：客户端的脚本程序，主要用来控制HTML标签的行为的。

JavaScript是一种小型的、轻量级的、面向对象的、跨平台的客户端脚本语言。
JavaScript是集成在浏览器当中的，只要安装了浏览器，JavaScript就有了。
JavaScript是面向对象的一种编程语言。可以把网页中的任何元素都看成是一个“对象”。

如：<b>、<a>、<p>、浏览器窗口、网页文档、历史记录、CSS等。

```

```
跨平台：可以运行在多种平台上。如：windows、linux、unix、mac os等。

客户端脚本程序：JS只能运行客户端(浏览器)。

服务端的脚本程序：PHP、ASP.NET、ASP、JSP、Python、Ruby等。
```

JavaScript能做什么？

- 表单验证是JS的最基本功能。
- DHTML动态的HTML。自动完成的动画效果。
- 交互式的功能。二级联动菜单、滚动文字。

## 2.''script>''标记

js程序代码，也是嵌入到HTML当中去的。

```
<script type="text/javascript">
/*
	这里写JS的代码
*/
</script>
```

## 3.常用的两个客户端输出方式

### 3.1 document.write(str)

- 描述：在网页中输出一个字符串的内容。

- document文档对象，一个网页看成是一个document对象。

-  document对象的属性和方法有很多。

- write()是document对象的一个方法。

- 方法是带小括号的。属性不带小括号。

- 小数点“.”是document对象和write()之间的连接号,和我们python非常相似。通过“.”去访问或调用对象的属性或方法。

- str代表要在<body>中输出的内容。字符串内容要加引号。

- 注意：JS是区分大小写的。

```
<script type="text/javascript">
	document.write("<h2>上海py1905</h2>")
	document.write("<h2>我是被输出来的</h2>")
</script>
```

### 3.2 window.alert(str)

- 描述：弹出一个警告对话框，警告对话框的信息是str。

- window浏览器窗口对象，代表一个浏览器窗口。

- alert()是window对象的一个方法。alert()的主要功能就是弹出一个警告对话框。

- window对象和alert()方法之间用小数点“.”连接。

- str表示显示的提示信息。字符串的内容要加引号。

```
<script type="text/javascript">
	alert("我是被弹出来的!")
	alert("<h2>上海你好!</h2>")
	document.write("<h2>上海py1905</h2>")
	document.write("<p>我是被踹出来的</p>")
	console.log('123');
    console.info('name','234');
</script>
```

## 4.JavaScript中的注释

- HTML的注释：<!--注释内容-->

- CSS注释：/*  注释内容 */

- JS的单行注释：//

- JS的多行注释：/*  多行注释 */

## 5.JavaScript中的变量

变量的概念与python，Java中的变量类似

### 5.1变量的声明

​	语法：`var 变量名;`

### 5.2变量的命名规则

- 变量名只能包含a-z、A-Z、0-9、_符号。

- 变量名只能以字母或下划线开头。如：n123(合法)  2a(非法)

- 变量名不能以数字开头。

- 变量名是区分大小写。如：Name和name和NamE是三个变量。

- 变量名不能是系统关键字。如：var var;

### 5.3三元运算符

var age = a > b ?  10 : 20

### 5.4JavaScript中的数据类型

- 基本数据类型：字符型、数值型、布尔型、未定义型、空型(null)

- 复合数据类型：数组型、对象型、函数型。

### 5.5JavaScript中的运算符

算术运算符：+、-、\*、/、%、++、--

字符串连接符： + 

+和+= 的两种用法

以上运算符都与python，Java中类似



# JavaScript_2

## 1.变量中的特别类型

数值型有一个特殊的类型NaN

NaN`(Not a Number)`：它不是一个数值。NaN更加的精确的话是一个浮点型.

当其它数据类型转成数值型，转不过去，此时将返回NaN的值。

```
NaN和谁都不相等，和它自己也不相等。
//判断NaN和NaN是否相等
var a = "abc";
a = a * 2;
if(a == NaN){
  document.write("相等")
}else{
  document.write("不相等")
}
```

## 2.转义字符 ''‘  \  ’'

```
如果直接使用的话，会报“语法出错”的。

那么，如何使用呢？

也就是，将里面的双引号单引号，进行转义()。如：\”、\’、\n、\r

\” ：将“\”之后的字符，当成“普通字符”来看待。如：将 \”  当成普通字符 a 看待，不会看成“引号”。

\’  ：看成普通的字符。

\n  ：换行符，只能在弹框中看到效果。

\r  ：回车符
```

## 3.未定义

```
当一个变量定义了，但未赋值，此时，该变量的类型是**未定义型**。

未定义型，只有一个值，就是undefined。

//变量声明
var a;//未复制,其值为undefined
document.write(a);
```

## 4.空型

当一个对象不存在，则为空型。空型只有一个值就是null。

null代表一个空对象，或者是对象的一个占位符。



## 5.判断变量的数据类型: typeof()



## 6.从字符串中提取整数或浮点数函数

### 6.1系统函数 parseint()

- 描述：在一个字符串，**从左往右**提取整型；如果遇到非整型的内容，则停止提取，并返回其值。

- 注意：如果第一个字符不是整型的话，则直接返回NaN。

### 6.2系统函数 parseFloat()

- 描述：在一个字符串中，从左往右提取浮点数；如果遇到非浮点数的字符，则停止提取，并返回提取的值。

- 如果第一个字符是非浮点数字符，则直接返回NaN。





## 7.比较运算符 ==，===，!=,!==

```
'=' 赋值号
"==" 是比较号(松散).比较左右两个操作数的值是否一致。如果值一样，则结果为true，否则结果为false。
"==="全等于(严格)。比较左右两个操作数的值和类型是否都一致。如果都一致返回true，否则结果为false。
```

##  8.逻辑运算符：&&、||、!

```
逻辑运处算符的运算结果，一定是一个布尔值。

逻辑运算符又称为“多条件比较”。

“&&”逻辑与(并且)。如果左右两个条件同时为true，则结果为true。反之，结果为false。

“||”逻辑或(或者)。如果左右有一个条件为true，则总结果为true。反之，结果为false。

“!”逻辑非(取反)。!true = false，!false = true。!100 = false，!null=true
```

## 9.window.prompt() ,提示用户进行输出

- 描述：用于显示可提示用户进行输入的对话框

- 语法：**window.prompt(text,defaultText)**

- 参数：

  text可选。表示输入框的提示信息。

  defaultText可选。表示输入框中的默认数据。

- 返回值

- 单击“确定”返回一个字符串的数据。

  单击“取消”返回null。

-  举例：var year = window.prompt("请输入一个年份")



# JavaScript_3

## 1.特殊运算符

### 1.1new运算符

```
//创建一个Date对象的实例
var today = new Date();
document.write("类型是:"+typeof(today)+",值为"+today);
```

### 1.2delete运算符

- 描述：删除对象的属性或数组中的元素。

- 举例：delete arr[0]  // 删除数组中索引为0的元素

### 1.3typeof运算符

-  描述：判断一个变量的数据类型。

- 语法：typeof name 或 typeof(name)

### 1.4小数点(.)

- 描述：主要用来调用对象的属性或方法。
-  举例：window.prompt()、window.alert()、document.write()

### 1.5小括号() 或 [ ] 运算符

-  ()运算符：主要用优先级方面。也是方法参数的小括号，函数参数小括号。

-  []运算符：主要用于存取数组中的元素。



## 2.运算符优先级

![](C:\Users\yang\Documents\PYthon笔记\HTML Lesson\images_1\image_4.png)

## 3.if条件判断语句

```
if(条件判断:结果是一个布尔值true false){
  条件为true,执行代码
}
var max;
if(max = (20 > 10 ? 0 :1) || (20 > 10 ? "abc" : "")){
  //条件为true,执行代码
  document.write("条件成立");
}
```

```
if(条件判断:结果是一个布尔值true或false){
  条件为true,执行的代码
}else{
  条件为false,执行的代码
}
```

```
if(条件一){
  代码一
}else if(条件二){
  代码二
}else if(条件三){
  代码三
}else{
  如过上面条件都不满足,则执行默认的代码
}
```

## 4.switch分支语句

```
switch(条件判断,是一个变量的不同取值){
  case 值1:
  	  代码1;
  	  break;
   case 值2:
  	  代码2;
  	  break;
   case 值3:
  	  代码2;
  	  break;
  	default:
  		如果以上条件都不满足,则默认执行的代码
}
```

```
switch语法说明：
  switch、case、break、default都是系统关键字。
  原理：如果switch中变量的取值，与每个case进行比对，如果匹配，则执行对应case中的代码。
  所有case都是并列关系，每时每刻只有一个case语句会运行。
  Break语句：用于中止代码继续向下运行。
  Default语句：如果以上条件都不满足，则执行的代码。
```

![](C:\Users\yang\Documents\PYthon笔记\HTML Lesson\images_1\image_2.png)

```
switch和if多条件的区别
  if是多条件判断，if的条件一般是一个范围。如：(a > 10)、 (a>10 && a <20 || a =30)
  switch的条件，一般来说，是一个变量，该变量会有不同的值。它不能用于一个范围。
  switch和if都是多选一。每时每刻只会有一个条件满足，有一个代码被执行。
```

## 5.while循环--重复执行

```
while(条件判断){
  	如果条件true,重复执行的代码
  	循环体代码,一般完成某项功能
}
```

- 变量初始化。在循环开始前要进行变量初始化，只执行一次。

- 条件判断。如果条件为true，则执行循环体代码；如果条件为false，则退出循环(转到结束大括号之后)。

-  变量更新。变量更新，可以距离结束的条件越来越近。可以避免出现“死循环”。是放在循环体中的。

## 6.for循环

```
for(变量初始值;条件判断;变量更新){
  	循环体的代码
}
for(i in arr){
    i是下标索引
}
```

## 7.1break语句--中断

break语句，用于无条件中断各种循环(while、for、for in)或switch语句。

一般情况下，需要在break语句之前加一个条件判断。如果条件为true，则退出循环。

break语句只能退出一层循环，不能直接跳出2层或多层循环。

## 7.2continue语句--继续

continue语句，用于结束本次循环，而开始下一次新的循环。也就是：本次循环的剩余代码不再执行。

一般情况下，需要加一个条件判断。

continue只能退出一层循环，也不能退出多层循环。

## 8.数组 [ ]

1、数组的概念

​	数组，就是一组数(值)的集合。

​	var arr = [10,20,30,40,50]

​	var arr = [“Mary”, “女”, 24 , “大专”, true , null]

2、数组元素

​	数组中的每个值，就称为“数组元素”。

​	数组的下标只能是从0开始的正整数，而数组的值可以是任何类型(字符串、数值、布尔型、未定义型、空型、数组、对象、函数)。

​	数组是复合数据类型。

3、数组索引(下标) 

​	var arr = [10,20,30,40,50]

​	数组的编号(下标)，是**从0开始的正整数**。

​	第1个元素的下标为0，第2个元素的下标为1，第3个元素的下标为2，依次类推。

4.数组元素的访问

​	访问方法是：数组变量名，后跟一个中括号[]，中括号[]内是元素所在的下标值。

5.数组的长度

​	数组中元素的总个数，就是数组长度。

## 8.1数组的创建方法

```
1、使用new关键字和Array()来创建数组
//(1)使用new关键字,结合Array()构造函数,创建数组
var arr = new Array(); //创建一个空的数组
//添加数组元素
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
arr[3] = 40;
//输出结果
//使用document.write()输出数组
//将数组个元素用逗号连成一个字符串
//然后输出结果
document.write(arr);
```

```
2.使用[]来创建
//(2)使用[]来创建一个数组
var arr = ["Mary" , 24, true, "大专",undefined];
document.write(arr);
```

## 8.2数组的操作

1、增加元素

​	只要是指定的数组下标不存在，则就是“添加元素”。

2、修改元素

​	只要指定的数组下标存在，就是“修改元素”。

3、删除元素

​	使用delete运算符，来删除数组元素。如：delete arr[2];

​	delete只能删除数组元素的值，而所占空间依然保留，也就是说下标还在，下标就是一个占位符。

​	删除数组元素后，数组的总长度不会改变。

```
//实例:数组操作
//创建一个空的数组
var arr = new Array();
//添加元素:指定下标不存在
arr[0] = "Mary";
arr[1] = "女";
arr[2] = 24;
arr[99] = 99; //数组长度是最大下标加1

document.write(arr + "<hr />");
//修改元素:对已存在的元素进行修改
arr[0] = "nono";
arr[1] = "不男不女";
arr[2] = 240;

document.write("数组长度:"+ arr.length+",数组的值:"+arr+"<hr />");
```

## 8.3数组对象属性length

一个数组，就是一个Array对象。

一个字符串，就是一个String对象。

一个数值，就是一个Number对象。

length属性

-  描述：动态获取数组元素的个数。

- 语法：var len = arrObj.length

-  参数：arrObj代表数组变量。一个数组变量，就是一个Array对象。