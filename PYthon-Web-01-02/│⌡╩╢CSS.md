# 初识CSS



- CSS Cascading style sheet   层叠 样式 表

- HTML 控制网页的结构;

- CSS控制结构中的元素的样式或者说,控制网页的外观;

- JS是控制网页的动作的;

- "层叠"是指多个外层元素的样式,会被内层去继承

- "样式"主要指的是外观,包括'字体,文本,背景图,定位,浮动等等'

  

## 1.css 语法格式

```
<style type="text/css">
	h1 {color:red;font-size:12px;}
</style>
```

- 一个CSS规则,由`选择器`和CSS格式构成的.
- "选择器"选择了一个HTML标记,并给其加上样式.
- "CSS"格式是放在`{}`中.CSS格式是有多条语句构成.
- 每一条CSS格式语句必须以`英文格式`下的`;`结束,最后一条可以不加;
- 每一条CSS格式语句是由`属性名:属性值`构成
- "属性名"是CSS中规定的,不能自己定义.



## 2.CSS选择器

### 2.1基本选择器

#### 2.1.1.通配符  ‘*’

- 描述:将代表HTML所有的标签
- 注意:通配符的兼容性不是太好,`IE6不支持的`
- 举例:`*{color:red;font-size:12px;text-align:center;}`

#### 2.1.2.标签选择器

描述:标签选择器于HTML标签一一对应,但是不加`</>

```
比如：
<style type="text/css">
div{color:blue;font-size:12px;background-color:yellow;}
</style>

<div class="div">
你好
</div>

```

#### 2.1.3.类选择器(类样式)

- 描述:给一类的HTML标记添加样式.只要HTML标记的`class`属性是一样的,浏览器就认为是一类.
- HTML里的公共属性,就是每个标签都可以拥有的属性;比如`id`,`name`,`class`,`style`,`title`等.
- 说明:类选择器,是以小数点开头的`.`,比如`.div{color:red;}`.
- 同一个类样式可以给不同的HTML,一个HTML`class`属性可以包含多个类样式;



比如：

```
.style_1{color:blue;}
.style_2{font-size:12px};
.style_3{border:1px solid red};

<p class='style_1 style_2 style_3'>样式1</p>
<p class='style_1 style_2'>样式2</p>
<p class='style_1'>样式3</p>
```

#### 2.1.4.id选择器

- 描述:给网页中指定id属性的HTML样式.
- 要求:在一个网页中，不能有多个相同id值的元素。id相当于身份证号码，只能使用一次(具有唯一性)。
- 说明：`class属性用来给元素添加CSS的，而id属性一般是用来加JS的`
- id选择器命名：必须以“#”开头命名。

比如：

```
#idCard{color:red;}
<span id='idCard'></span>

```

### 2.2组合选择器

#### 2.2.1.多元素选择器

- 描述：同时给多个元素，加同一种样式。多个元素之间用英文下的逗号隔开.

比如:

ul,ol,li,dl,dt,dd{margin:0px;padding:0px;}

#### 2.2.2.后代元素选择器

- 描述:给某个元素的所有后代元素，添加样式。两个选择器之间用空格隔开.

```
<div><sapn></span></div>`这里面的`span`就是`div`的后代元素.
比如:
#div h2{color:blue;border:1px solid blue;background-color:yellow;}
<div id='div'>
	<h2>新闻标题1</h2>
	<div>
		<h2>新闻标题2</h2>
	</div>
</div>
```

#### 2.2.3.子元素选择器

- 描述：给当前元素的子元素添加样式。两个选择器之间用大于号(>)隔开。

  ```
  #div>h2{color:blue;border:1px solid blue;background-color:yellow;}
  <div id='div'>
  	<h2>新闻标题1</h2>
  	<div>
  		<h2>新闻标题2</h2>
  	</div>
  </div>
  ```

#### 2.2.3.后代元素选择

- #div h2{color:blue;border:1px solid blue;background-color:yellow;}



### 2.2.4.伪类选择器

- 伪类选择器，一般是用来选择`<a>`元素的。
- 超级链接有四种状态：正常状态、放上状态、访问过状态、激活状态。
- 四种状态正好对应四种选择器。
  - `:link` 正常链接效果。
  - `:visited` 访问过的效果
  - `:hover` 鼠标放上的效果
  - `:active` 激活状态(鼠标点击的一瞬间出现一般不用)
  - `这4个的顺序一定不能弄错,弄错了就没有效果`
- `text-decoration`属性
  - `none`     默认。定义标准的文本。
    - `underline`定义文本下的一条线。
    - `overline`定义文本上的一条线。
    - `line-through`定义穿过文本下的一条线。
    - `blink`定义闪烁的文本。



```
/*全局的链接样式,所有的样式都会改变*/
	a:link{color:gray;text-decoration:none;}
	a:visited{color:green;text-decoration:underline;}
	a:hover{color:red;}
	a:active{color:yellow;}
/*局部的链接样式,只有对应的几个类才有样式*/
	a.a1:link{color:black;text-decoration:none;}
	a.a1:visited{color:gray;text-decoration:underline;}
	a.a1:hover{color:blue;}
	a.a2:link{color:red;text-decoration:none;}
	a.a2:visited{color:black;text-decoration:underline;}
	a.a2:hover{color:green;}
	
<a href="#">在吗</a>
<a href="#">干嘛</a>
<a href="#" class='a1'>借钱</a>
<a href="#" class='a2'>不在</a>	

```

## 3.CSS属性

#### 3.1.css尺寸属性

- width：元素的宽度。
- height：元素的高度。

```
img{width:100px;height:100px;}
img{width:50%;height:50%;}
```

#### 3.2.css字体属性

- font-size：文字大小。
- font-weight：加粗效果。取值：bold
- font-style：斜体效果。取值：italic
- font-family：字体。

#### 3.3.css文本属性

- color：文本颜色。
- line-height：行高，可以是百分比，也可以是固定值。
- text-align：文本的水平对齐方式，取值：left、center、right
- letter-spacing：字间距。
- text-decoration：文本修饰线，取值：underline(下划线)、none、overline(上划线)、line-through(删除线)
- text-indent：首行缩进。

#### 3.4.px和em以及rem

- px像素（Pixel）。相对长度单位。像素px是相对于显示器屏幕分辨率而言的。
- em是相对长度单位。相对于当前对象内文本的字体尺寸。如当前对行内文本的字体尺寸未被人为设置，则相对于浏览器的默认字体尺寸。em是根据父类的变化而变化的
- rem和em类似,`rem:root em`;相对于根的比较;
- 默认的大小是16px

比如:
`需要在css中的body选择器中声明font-size=80%`才能使用

```
body{font-size:100%;}
div{font-size:1.5em;}
span{font-size:2rem;}

<body>
	<p>你好</p>
	<div>你好<br/>
	<span>你好</span>
	</div>
</body>


```



# CSS Lesson 2

## 1.css列表属性

list-style`：列表样式，指定样式的符号。取值：none(无符号)

```
.ul{list-style:none;}

	<ul>
		<li>你好</li>
		<li>干嘛</li>
	</ul>
	<ul class='ul'>
		<li>再见</li>
		<li>拜拜</li>
	</ul>
```



## 2.css边框属性

```
border-left：左边框线。
	格式：border-left: 粗细 线型 颜色;(px)
	线型：none(无线)、solid(实线)、dotted(点状线)、dashed(虚线)、double(双线)
	颜色:十进制  十六  单词
	注意：多个参数值之间用空格隔开。
	举例：div{border-left:5px solid red;}
border-right：右边框线。
border-top：上边框线。
border-bottom：下边框线。
简写方式：
	border：四个边框都加同一种边线。
	举例：div{border:2px solid blue;}
	
比如：
.box{
		border-left:5px solid blue;
		border-right:5px dotted red;
		border-top:5px dashed black;
		border-bottom:5px double green;
		width:200px;
		height:200px;
	}
	
<div class="box"></div>
```



## 3.css填充属性

### 3.1.内边距

内边距：边线到内容间的距离

```
padding-left：左内填充距离(左边线到内容之间的距离)。
padding-right：右内填充距离。
padding-top：上内填充距离。
padding-bottom：下内填充距离。
简写方式:
	padding:10px; //四个内填充都是10px
	padding:10px 20px; //上下内填充为10px，左右内填充为20px
	padding:5px 10px 15px; //上填充为5px，左右为10px，下为15px
	padding:5px 10px 15px 20px;  //顺序一定为：上右下左
```

### 3.2.外边距

外边距：边框线往外的距离

```
margin-left：左外边距(左边框线再往外的距离)
margin-right：右外边距。
margin-top：上外边距。
margin-bottom：下外边距。
简写方式:
	margin:10px;   //四个外边距分别为10px
	margin:10px 20px;  //上下外边距10px，左右外边距20px
	margin:5px 10px 15px;  //上外边距5px，左右外边距10px，下外边距15px
	margin:5px 10px 15px 20px;  //顺序一定是：上右下左
```

## 4.css背景属性

```
background-color：背景颜色
background-image：图片的路径(相对路径或绝对路径)。如：background-image:url(images/bg.gif);
background-repeat：控制图片的平铺方式。
	no-repeat：不平铺。
	repeat-x：水平方向平铺。
	repeat-y：垂直方向平铺。
repeat：水平和垂直都平铺(默认)。
background-position：背景图片的定位方式。
	格式：background-position：水平方向定位 垂直方向定位
	定位的单词：left、center、right、top、bottom
	举例：background-position:center center; //图片居中容器的正中
	定位也可以使用百分比值。如：background-position:0% 50%;
	定位也可以使用固定像素值。如：background-position:5px 5px; //背景图距离容器左边和上边都是5px
```

```
注意事项：`要想使用图片定位功能，该图片不能进行平铺`。
简写方式:
	格式：background：背景色 图片的路径 平铺方式 定位方式
	举例：background:red url(images/bg.gif) no-repeat center center;
	举例：background:url(images/bg.gif) no-repeat center 50%;
	举例：background:url(images/bg.gif) repeat-y;
	
例题：
/*局部样式设置*/
body,h2,p{margin:0px;padding:0px;}
body{font-size:14px;color:#333;background-color:#ccc;}
/*局部样式设置*/
.box{
	width:600px;
	margin:30px auto;
	padding:10px 10px 130px;
	background:white url(images/02.gif) no-repeat 480px bottom;

}
.box h2{
	text-align:center;
	padding:10px 0px;
	color:red;
}
.box p{
	line-height:160%;
	text-indent:28px;
	color:blue;
}
```

```
<div class="box">
<h2>一带一路</h2>
<p>“一带一路”（英文：The Belt and Road，缩写B&R）是“丝绸之路经济带”和“21世纪海上丝绸之路”的简称。它将充分依靠中国与有关国家既有的双多边机制，借助既有的、行之有效的区域合作平台，一带一路旨在借用古代丝绸之路的历史符号，高举和平发展的旗帜，积极发展与沿线国家的经济合作伙伴关系，共同打造政治互信、经济融合、文化包容的利益共同体、命运共同体和责任共同体。
2015年3月28日，国家发展改革委、外交部、商务部联合发布了《推动共建丝绸之路经济带和21世纪海上丝绸之路的愿景与行动》。</p>
</div>
```

## 5.css浮动和清除

### 5.1.css浮动(飘起来)

- float：浮动属性，取值：left或right。
- CSS浮动可以使元素向左或向右浮动。浮动到父元素的边上或者上一个浮动元素的边上。
- 浮动的元素不再占空间了。
- 浮动的元素层级高于普通元素(没有浮动)。
- 浮动的元素一定是块元素，不管以前是什么元素。换句话：行内元素浮动以后，也变成了块元素。

```
.box {border:5px solid black; width:400px;}
.box .box1{width:100px;height:100px;float:left;background-color:red;}
.box .box2{width:100px;height:100px;float:left;background-color:blue;}
.box .box3{width:100px;height:100px;float:left;background-color:green;}

<div class='box'>
	<div class="box1"></div>
	<div class="box2"></div>
	<div class="box3"></div>
</div>

```

### 5.2.清除浮动

- clear：清除浮动，取值：left、right、both(两者)`clear:both;`

- 一般情况下，上面有浮动，下面就得清除浮动

- 先浮动，后清除；有浮动，必须要有清除浮动

- 清除浮动后，可以让父元素在“视觉”上包含浮动元素

- 清除浮动后，清除浮动之后的其它元素，将恢复默认排版(不再继承上面的浮动特性)

  

  ```
  .box {border:5px solid black; width:400px;}
  .box .box1{width:100px;height:100px;float:left;background-color:red;}
  .box .box2{width:100px;height:100px;float:left;background-color:blue;}
  .box .box3{width:100px;height:100px;float:left;background-color:green;}
  .box p{clear:both;}
  
  <div class='box'>
  	<div class="box1"></div>
  	<div class="box2"></div>
  	<div class="box3"></div>
  	<p>你在哪里</p>
  </div>
  ```

  

## 6.css继承性和优先级

### 6.1.css继承性

多个外层元素的样式，最终都要叠加到内层元素上。
内层元素的样式，可以从多个外层元素上去继承。
哪些`CSS`属性会被`继承`呢？
主要是文本和字体方面的样式。如：font-size、font-weight、font-style、font-family、line-height、text-indent、text-align、color、text-decoration、letter-spacing、word-spacing等。

### 6.2.css选择器优先级

（1）单个选择器优先级
 行内样式 > Id选择器 > 类选择器 > 标签选择器>通配符

   (2）组合选择器的优先级
` 组合选择器`如何确定优先级？
 基本思路：`指向越精确，优先级越高`。
 平常把不同的选择器假设不同的值：

```
（1）单个选择器优先级
行内样式 > Id选择器 > 类选择器 > 标签选择器>通配符

(2）组合选择器的优先级
`组合选择器`如何确定优先级？
基本思路：`指向越精确，优先级越高`。
平常把不同的选择器假设不同的值：


例如：`div.news .title{color:red;}`  优先级为21
例如：`.news .title{color:blue;} `   优先级为20
例如：`#title{color:green;}  `      优先级为100
```



# CSS Lesson 3

## 1.display属性

- 描述：控制元素显示方式。
- 取值：`none`(不显示)、`block`(块显示)、`inline`(以行内元素显示)
- 注意：元素隐藏不再占空间了。

## 2.overflow属性

- 描述：当内容溢出如何处理。
- 取值：scroll(出现滚动条)、hidden(隐藏)、auto(自动)、visible(显示)

## 3.cursor光标类型

- 描述：改变光标的显示类型。
- 取值：pointer(手形)、help(帮助)、text(文本)、wait(等待)等。

## 4.CSS定位属性

### 4.1.`position`：定位属性，

取值static、fixed、relative、absolute
`static`：静态定位，不定位，默认值。
`fixed`：固定定位。
`relative`：相对定位。相对所有标记的高度和
`absolute`：绝对定位。 相对的浏览器的边框

### 4.2.定位坐标值

`left`：距离目标元素左边的距离。
`right`：距离目标元素右边的距离。
`top`：距离目标元素顶边的距离
`bottom`：距离目标元素底边的距离。
提示：如果不指定定位坐标值，定位元素在“原地不动”。

### 4.3.固定定位

——position:fixed

固定定位元素，是相对于浏览器窗口，来进行的定位。
固定定位元素，不再占空间了。
固定定位元素层级高于普通元素。
固定定位元素，一定是块元素，不管原来是什么元素。

如果不指定定位坐标，则该元素“原地不动”，位置不会改变。

### 4.4相对定位

相对定位—— position:relative

相对定位，是相对于“原来的自己”进行的定位。
相对定位元素，所占的空间依然存在。
相对定位元素，层级要高于普通元素。
如果不指定定位坐标，该元素“原地不动”。
原来是什么元素，进行相对定位后，还是什么元素。
定位元素可以超出父元素的边界，而浮动元素，是不可以超出父元素的边界。

### 4.5绝对定位

绝对定位—— position:absolute

绝对定位元素，是相对于上层定位元素来进行定位的。如果父元素没有指定定位的话，继续向上查找定位元素。如果一直找到<body>都没有找到定位元素，则相对于<body>来定位。
绝对定位元素，不占空间。
绝对定位元素层级高于普通元素。
绝对定位元素的上层定位元素，一般会用相对定位。因为相对定位的空间还在。

## 5.HTML引入CSS的方法

### 5.1嵌入式

描述：通过`<style>`标记来书写CSS代码。
格式：`<style  type = “text/css”>……</style>`
说明：这种方式只能在当前HTML文件中使用，不能被多个HTML文件共享。
说明：`<style>`标记可以在网页中多次出现，想写在什么地方，就写在什么地方。

### 5.2外联式

描述：将外部的 `.css`文件引入到当前的HTML文件中。
说明：可以将公共的CSS代码放在外部的文件，通过`<link>`标记将其引入，可以实现多个网页共享同一个CSS文件。
格式：`<link href = “css/public.css” type = “text/css” rel = “stylesheet” />`
属性：
`href`：指定外部的CSS文件路径。
`type`：指链入文件的类型。
`rel`：链接入文件与当前HTML文件的关系。取值：`stylesheet`。
说明：`<link>`标记是`<head>`的子标记。一个网页中也可出现多个`<link>`。`<link>`标记可以放在HTML网页的任何地方。

### 5.3行内式

描述：直接给HTML标记添加`style`属性。
每一个HTML标记，都有一些公共的属性：`id`、`class`、`style`、`title`等。
其中，`style`属性的值，就是CSS的代码。
行内样式的优先级最高。

## 6.盒子模型

可以把任何的HTML标记，都看成是一个`盒子`。
`盒子`包括哪些部分？内容的宽和高、边框线、内填充、外边距。

![](C:\Users\yang\Documents\PYthon笔记\HTML Lesson\images_1\box.png)

`一个“盒子”的总宽度计算 ＝ width(内容宽度)  +  padding(内填充)  +  border(边框线)  +  margin(外边距)`

上下外边距合并问题
当上下两个普通的块元素(不是浮动元素，也不是定位元素)的上下外边距碰在一起时，会发生“外边距合并”的现象。
外边距合并后，外边距取其中较大的一个值。

## 7.CSS表格属性

border-collapse`：合并表格边框线。取值：`collapse`(合并)
注意：不要再使用`rules`属性合并单元格边线了，因为兼容性不好。



# 网页兼容性

- 全局CSS设置
- 常用兼容性技巧
- CSS HACK



## 全局CSS设置

1、所有HTML标记都要清除内外边距

```
html,body,ul,li,a,img,p,h1,h2,h3,h4,input{margin:0;padding:0;}

*{margin:0px;padding:0px;}
```

2、去除有序列列或无序列表前面的符号

```
	ul,li,ol{list-style:none;}
```

3、全局的链接样式

```
a:link , a:visited{color:#444;text-decoration:none;}

a:hover{color:red;}
```

4.网页中所有文字的大小及颜色

```
 body{ font-size:18px; color:#444; font-family:Arial , 楷体 , 宋体;}
```

5.去除图片的边框线

```
img{border:0;}
```

6.自定义样式

```
.red{color:red;}

.blue{color:blue;}

.floatL{float:left;}

.floatR{float:right;}

.clear{clear:both;}

.blank10{height:10px; clear:both;}

.left{}

.right{}

 ……
```

7.常用的兼容性技巧---将文本的行高，设置与容器的高度一样

