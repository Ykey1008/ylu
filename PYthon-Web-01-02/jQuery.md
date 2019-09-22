# jQuery

## 1.jQuery中的选择器

要完成DOM的操作，选中元素是第一步，jQuery为我们提供了强大的，丰富的选择器。

原生代码使用document.getElementByid(id)来获取指定id的DOM对象

在jQuery中可以使用通过$标识符+选择器选择页面中任一元素

### 1.1基本选择器

#id  根据元素的id属性获取指定的元素

element  根据元素的名称来获取指定的元素

selector1，selector  匹配所有满足条件的元素

.class：根据元素的class属性获取指定的元素

js对象显示出来是一个标签的样式

jquery单个对象显示出来 是init

jquery集合对象显示出来是 init(?),集合中存储的是js的单个对象,通过.get()方法获取标签



```
<script type="text/javascript" src="../js/jquery/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //选择id=one的元素
        //$("#one").css('background','green');
        //选择span标签,当前页面中所有的span
        //$('span').css('background','pink');
        //选择p和div标签，也就是当前页面中，所有的p和div.
        //$('p,div').css('background','red');
        //选择class=one的元素
        $(".one").css('background','blue');
}
</script>

<body>
    <input type='button' value="基本选择器" onclick="t1()"/><br/>
    <p>今天好天气</p>
    <div>
            <p><span class="one">可以去旅游了</span></p>
            <span id="one">下午可能要下雪了</span>
    </div>
    <span>天气好，可以去减肥</span><br/>
    <span>天气不好，可以去吃大餐</span>
     <p  class="one">中文不吃饭啦</p>
</body>
```

### 1.2层级选择器

**ancestor (**空格**) descendant ：选取祖先元素下的所有后代元素(祖先与后代)**

**parent > child**：选择父元素下的所有子元素（父子关系）

**prev + next**：选取同级元素紧邻的下一个元素

**prev~siblings**：选取同级元素所有的同级兄弟元素

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
      //选择div下面的所有的span标签（祖先与后代）
      $("div span").css('background','red');
      //选择div下面的子元素为span的（父子关系）
      $("div>span").css('background','green');
      //选择在div后面的第一个span(兄弟节点，只有一个兄弟)
      $("div + span").css('background','blue');
      //选择与div后面的所有同级的span（同胞选择器）
      $("div ~ span").css('background','pink');
}
</script>

  <body>
    <input type='button' value="层级选择器" onclick="t1()"/><br/>
    <p>今天天气好</p>
    <span>东游记</span>
    <div>
            <p><span class="one">可以去旅游了</span></p>
            <span id="one">下午可能要下雪了</span>
            <div>南游记</div>
            <span>淑女侠</span>
    </div>
    <span>天气好，可以去减肥</span><br/>
    <span>天气不好，可以去吃大餐</span>
     <p  class="one">中文不吃饭啦</p>
     <span>西游记</span>
  </body>
```

### 1.3简单选择器

 : first ：匹配第一个元素

 : last ：匹配最后一个元素

 : even：匹配所有偶数

 : odd ：匹配所有奇数

 : eq(index) ：匹配索引为index的元素（默认索引从0开始）

 : gt(index)：匹配索引大于index的元素

 : lt(index) ：匹配索引小于index的元素

 : not(selector)：匹配除指定选择器以外的其他元素

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
      //查找当前页面中的第一个li标签
      //$("li:first").css('background','red');
      //查找当前页面中的偶数的li标签
      //$("li:even").css('background','red');
      //查询li的排序大于3的li
      //$('li:gt(3)').css('background','green');
       //查询第4个li标签
       //$('li:eq(3)').css('background','green');
       //查询大于2的li标签排除最后一个li标签。
       $("li:gt(1):not(:last)").css('background','red');
}
</script>

 <body>
    <input type='button' value="简单选择器" onclick="t1()"/><br/>
    <ul>
        <li>西游记</li>
        <li>东游记</li>
        <li>鬼吹灯</li>
        <li>诛仙传</li>
        <li>罗贯中</li>
        <li>李莫愁</li>
    </ul>
 </body>
```

### 1.4内容选择器

: contains(text)：匹配内容包含指定文本的元素

: empty ：匹配内容为空的元素

: has(selector) ：匹配具有指定选择器的元素

: parent：匹配具有子元素的元素（内容不为空的元素）

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
     //选择li元素中包含"记"的li元素
     //$("li:contains('记')").css('background','red');
     //选择li中为空的li元素。
     //$("li:empty").css('background','green');
     //选择li中有span标签的li
     //$("li:has('span')").css('background','blue');
     //选择li中有子元素的li(不为空，自己做了父亲)
     $("li:parent").css('background','pink');
}
</script>
<style type="text/css">
</style>
</head>
    <body>
    <input type='button' value="内容选择器" onclick="t1()"/><br/>
    <ul>
        <li>西游记</li>
        <li>东游记</li>
        <li>鬼吹灯</li>
        <li>诛仙传</li>
        <li><span>罗贯中</span></li>
        <li>李莫愁</li>
        <li></li>
    </ul>
    </body>
```

### 1.5可见性选择器

**:hidden**：匹配所有隐藏元素(display:none，input type=’hidden’) 

**:visible**：匹配所有可见元素(display:block) 

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
    //选择隐藏的div,让其显示，并设置样式 
     //$("div:hidden").css('background','red');
     //$("div:hidden").show();
     //选择显示的div,让其隐藏
     $("div:visible").hide();
}
</script>

<style type="text/css">
#one{width:400px;height:200px;background:gray;}
#two{width:400px;height:200px;background:gold;display:none;}
</style>

<body>
    <input type='button' value="可见性选择器" onclick="t1()"/><br/>
    <div id="one">我是显示的</div>
    <div id="two">我是隐藏的</div>
</body>
```

### 1.6属性选择器

根据元素里面的属性进行选择。

**[attribute] ：匹配具有指定属性的元素**

**[attribute=value]：匹配属性值等于value的元素**

**[attribute!=value] ：匹配属性值不等于value*的元素**

**[attribute^=value] ：匹配属性值以value开始的元素**

**[attribute$=value] ：匹配属性值以value结尾的元素**

**[attribute\*=value] ：匹配属性值包含value的元素**

**[selectorN]：匹配包含多个属性的元素**

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
    //选择具有name属性的div
    //$('div[name]').css('background','red');
    //选择name属性值为username的div
    //$('div[name=username]').css('background','green');
     //选择name属性值不等于username的div  注意：会选择所有的div的。
    //$('div[name!=username]').css('background','green');
    //选择name属性值以user开头的div
    //$('div[name^=user]').css('background','red');
    //选择name属性值以age结尾的div
    //$('div[name$=age]').css('background','red');
     //选择具有name属性和color属性的div
    $('div[name][color]').html('<p>我的薪水是2300</p>');;
}
</script>
</head>
<body>
    <input type='button' value="属性选择器" onclick="t1()"/><br/>
    <div name="username">程咬金</div>
    <div name="userage">12</div>
    <div name="age">45</div>
    <div name="salary" color="red">23000</div>
</body>
```

### 1.7表单选择器

: input ：匹配所有表单元素

: text ：匹配所有文本框

: password：匹配所有密码框

: radio ：匹配所有单选按钮

: checkbox：匹配所有复选框

: submit ：匹配提交按钮

: reset：匹配重置按钮

: image：匹配图像域

: button：匹配按钮

: file：匹配文件域

: hidden：匹配隐藏表单

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //匹配所有的表单元素
        //$(':input').css('background','yellow');
        //匹配所有的文本框
        //$(":text").css('background','yellow');
        //匹配所有的单选框
         //$(":radio").attr('disabled',true);
          //匹配所有的复选框
         //$(":checkbox").attr('disabled',true);
         //$("input[name=age]").val('请选择你的年龄');
}
</script>

<body>
    <input type='button' value="子元素选择器" onclick="t1()"/><br/>
     <form>
            姓名:<input type="text" name="name"/><br/>
            年龄:<input type="text" name="age"/><br/>
            性别:<input type="radio" name="sex"  value="男"/>男
                   <input type="radio" name="sex" value="女"/>女
                   <input type="radio" name="sex" value="妖"/>妖<br/>
            爱好:
                    <input type="checkbox" name="hobby[]" value="读书"/>读书
                    <input type="checkbox" name="hobby[]" value="写诗"/>写诗
                    <input type="checkbox" name="hobby[]" value="学习"/>学习
                    <input type="checkbox" name="hobby[]"  value="运动"/>运动
                    <input type="checkbox" name="hobby[]" value="唱歌"/>唱歌<br/>
           介绍 ：
                    <textarea cols="20" rows="5"></textarea>
                    <input type="submit" value="提交"/>      
     </form>
</body>
```

```
**问题：在**jQuery****中使用****`$(":input")与$("input")`****的区别****?

`$(":input")与$("input")` 

答：`$(":input")`匹配所有表单元素，包括select与textarea元素

`$("input")`只能匹配input标签
```

### 1.8表单属性选择器

: enabled ：匹配所有可用元素

: disabled ：匹配所有不可用元素

: checked ：匹配复选框单选框所有选中元素(问题多)

: selected ：匹配下拉选框所有选中元素

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
  function t1(){
       //把禁用的元素设置为开启状态
       //$(":disabled").attr('disabled',false);
       //把开启的元素设置禁用状态
       $(":enabled").attr('disabled',true);
       //获取单选框里面的值
       alert($(":checked").val());
}
</script>
<body>
    <input type='button' value="子元素选择器" onclick="t1()"/><br/>
     <form>
            姓名:<input type="text" name="name"/><br/>
            年龄:<input type="text" name="age"/><br/>
            性别:<input type="radio" name="sex"  value="男"/>男
                   <input type="radio" name="sex" value="女"/>女
                   <input type="radio" name="sex" value="妖"/>妖<br/>
            爱好:
                    <input type="checkbox" name="hobby[]" value="读书"/>读书
                    <input type="checkbox" name="hobby[]" value="写诗"/>写诗
                    <input type="checkbox" name="hobby[]" value="学习"/>学习
                    <input type="checkbox" name="hobby[]"  value="运动"/>运动
                    <input type="checkbox" name="hobby[]" value="唱歌"/>唱歌<br/>
           介绍 ：
                    <textarea cols="20" rows="5"></textarea>
                    <input type="submit" value="提交"/>      
     </form>
</body>
```

```
面试题：在表单元素中disabled='true'和readonly='readonly'区别：

答：disabled与readonly虽然都可以限定文本框被编辑，但是两者还是有区别的，主要区别在于readonly可以在python页面接收设置为readonly属性表单的值。而disabled是接收不到任何数据的。
```

## 2.DOM对象与jQuery对象

dom对象和jQuery对象是否是一回事？ 答：不是

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
window.onload=function(){
        var oBtn = document.getElementById('btn');
        oBtn.onclick=function(){
               var oDiv = document.getElementsByTagName('div')[0];
               //oDiv.style.backgroundColor = 'red';//效果正常
               $("div").style.backgroundColor = 'red';//效果不正常
               //说明，dom对象和jquery对象不是同一个对象。
        } 
        /*
        $("#btn").onclick=function(){
                alert('ok');
        }*/
}
</script>

 <body>
    <input type='button' value="单击" id="btn"/><br/>
    <div>你好，welcome to shanghai</div>
 </body>
```

### 2.1什么是dom对象和jQuery对象

- 使用document.getElementById或document.getElementsByTagName获取的对象就是dom对象。

- 使用$符号选择的元素就是jquery对象。



### 2.2jQuery对象与dom对象的关系

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
window.onload=function(){
      console.log(document.getElementsByTagName('div')[0]);
      console.log($('div')[0]);
}
</script>
<style type="text/css">
</style>

<body>
    <div>东游记</div>
    <div>西游记</div>
 
</body>


通过上面测试，发现$(‘div’)里面，包含div的dom对象的。jquery对象是对dom对象的重新封装，他们之间是可以相互转换的。

```

### 2.3jQuery对象与DOM对象相互转换

- jQuery对象转换成dom对象

语法：

DOM对象 = jQuery对象[下标]; 

DOM对象 =jQuery对象.get(下标); 

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //先获取jquery对象,
        $('div')[1].style.backgroundColor='green';
        $('div').get(2).style.backgroundColor='red';
}
</script>


<body>
    <input type="button" value="单击" id="btn" onclick="t1()"/>
    <div>东游记</div>
    <div>西游记</div>
    <p><div>红楼梦</div></p>
</body>
```

- 把dom对象转换成jquery对象

语法：jQuery对象 = $(DOM对象); 

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //先获取对象,
       var div2 = document.getElementsByTagName('div')[2];
       $(div2).css('background','red');
}
</script>


<body>
    <input type="button" value="单击" id="btn" onclick="t1()"/>
    <div>东游记</div>
    <div>西游记</div>
    <p><div>红楼梦</div></p>
</body>

jQuery对象的实质就是一个数组，每个数组元素本质就是一个DOM对象
```

## 3.jQuery中的属性

### 3.1 attr属性

attr(name)：获取指定元素的属性

attr(key,value)：设置元素的属性

attr(object)：为元素同时设置多个属性，要求参数是一个json数据

attr(key,fn)：通过函数的返回值设置元素属性

removeAttr(name)：移除元素属性

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //获取img的src属性
       //alert($('img').attr('src'));//one.jpg
       //设置img的src属性，
       //$('img').attr('src','two.jpg');
       //设置img的多个属性值属性，
       //$('img').attr({src:'two.jpg',width:'600',height:'200'});
       //属性值，可以是函数的返回值
       //$('img').attr('src',function(){
                //return 'two.jpg';
       //});
       //把img的src属性给移除
       $('img').removeAttr('src');

}
</script>
<style type="text/css">
</style>
</head>
    <body>
    <input type="button" value="获取属性" id="btn" onclick="t1()"/><br/>
    <img src="one.jpg" width="300"/>
    </body>
```

### 3.2 class属性

addClass(class)：为元素添加class属性

removeClass(class)：移除元素的class属性

toggleClass(class)：切换样式，如果元素不存在该属性则添加，否则移除

hasClass(class)：判断元素是否具有某个css类样式

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
        //给div1添加 class属性。
        //$("#one").addClass('one');
        //给div2删除 class属性
        $('#two').removeClass('two');
}
</script>

<style type="text/css">
.one {
        width:100px;
        height:100px;
        background:gray;
}
.two {
        width:100px;
        height:100px;
        background:red;
}
</style>

<body>
    <input type="button" value="class属性操作" onclick="t1()"/>
    <div id="one">第一个div</div>
    <div id="two"class="two">第二个div</div>
</body>
```

```
<script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
       //判断div里面是否有off的class属性，如果有，就删除，如果没有就添加
       /*if($("#one").hasClass('off')){
                $('#one').removeClass('off');
       }else{
                $('#one').addClass('off');
       }*/
       //判断div里面是否有off的class属性，如果有，就删除，如果没有就添加
       $("#one").toggleClass('off');
}
</script>

<style type="text/css">
#one{width:109px;height:147px}
.on{background:url('on.jpg')}
.off{background:url('off.jpg')}
</style>

<body>
    <input type="button" value="class切换操作" onclick="t1()"/>
    <div id="one"  class="on"></div>
</body>
```

### 3.3 CSS属性

**css(name)**：获取元素样式属性

**css(name,value)**：设置元素样式属性

**css(object)**：同时为元素设置多个样式属性，要求参数是一个**object**数据

```
script type="text/javascript" src="script/jquery-1.8.3.js"></script>
<script type="text/javascript">
function t1(){
     //给id=one的div添加高度，宽度，背景颜色
     $("div").css({width:'200px',height:'200px','background':'red'});
}
</script>

<body>
    <input type="button" value="css方法操作" onclick="t1()"/>
    <div id="one"></div>
</body>
```

注意：通过css方法添加的样式是行内样式：

