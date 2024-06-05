```
 [toc]      #目录
```

[TOC]

## 标题



# 一级标题

## 二级标题

### 三级标题

#### 四级标题



## 样式

*斜体*

**粗体**

***加粗+斜体***

==高亮== 

~~删除线~~

> 一级引用
> 
> > 二级引用

H~2~O 下标

2^10^ 上标

\*反斜杠注释markdown标记\*

空格&nbsp;&nbsp;&nbsp;空格

*[缩略]: 详细解释

## 列表

#### 无序列表

- 列表项1
* 列表项2
+ 列表项3

#### 有序列表

1. 列表项1
2. 列表项2
3. 列表项3

#### 待办列表

- [ ] Incomplete item
- [x] Complete item

## 链接

自动链接：

+ 邮件:<example@example.com>
+ 引用存储文件 [example](…/…/example.md)

[文字链接](https://www.jianguoyun.com)

图片: 
![Alt](https://inpast-qiq.oss-cn-beijing.aliyuncs.com/img/202202121743410.png)

图像大小改变:
<img src="https://inpast-qiq.oss-cn-beijing.aliyuncs.com/img/202202121743410.png" width="60%">

图像位置改变：
<img src="" style="margin: 0,10px,0,0">

## 代码

`内嵌代码`

```
// 代码块
var foo = 'bar';
```

```javascript
// js代码块
var foo = 'bar';
```

```javascript{.line-numbers}
// 代码行数显示
//代码名称后加 {.line-numbers}
var foo = 'bar';
```

## 表格

| 产品  | 价格    |
| --- | ----- |
| 电脑  | ¥5600 |
| 手机  | ¥2200 |
| 数据线 | ¥15   |

<br/>

| 列1  | 列2  | 列3  |
|:---:| ---:|:--- |
| 居中  | 右对齐 | 左对齐 |

<br/>

[//]:MPE的设置enableExtendedTableSyntax

| 列1      | 列2  | 列3     |
|:-------:| ---:|:------ |
| 居中      | 右对齐 | 左对齐    |
| 121     | >   | 右侧合并：> |
| 左侧合并：空格 |     | 1      |
| 上侧合并：^  | 12  | 1      |
| ^       | 121 | 1      |

## 自定义列表

Markdown
: Text-to-HTML conversion tool

Authors
: John
: Luke

## 脚注

一段带脚注的文字.[^1]

[^1]: 脚注详情.

## 缩写

Markdown 可以将文本内容转换为 HTML.

*[HTML]: HyperText Markup Language

## 文件导入

> @import "你的文件"

## 公式

#### 示例1

$\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$

#### 示例2

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$



#### 图像大小改变

> 在 html 中添加 `style="width:70%;"`



#### 图像位置改变

> 在 html 中添加 `style="margin-left: 40px;"`



