## 一.Java开发介绍

#### 1.常用的DOS命令

+ dir：列出当下目录下的文件及文件夹
+ md :   创建目录
+ rd :   删除目录
+ cd :   进入指定目录
+ cd.. : 退回上一级目录
+ cd\ :  退回到根目录
+ del :  删除文件
+ exit : 退出 dos 命令行
+ txt :  删除所有txt类型的文件

---

#### 2.package及import

+ package 的包名一个小数点即有一个文件目录，如com.week.study

+ 同一个包下，不能命名同名的接口、类，不同的包下可以

+ 可以使用 import java.util.*的方式，一次性导入util包下所有的类或接口

+ Java.lang 包或本包下定义的，可以省略 import

+ 导入不同包且重名结构的，在使用声明时需写出完整的包名结构
  如 com.week.study.Add  a1 =new com.week.study.Add();
  
  ![](https://inpast-qiq.oss-cn-beijing.aliyuncs.com/img/20210623145743.png)

---

#### 3.单元测试方法

```java
  import java.util.Date;

  import org.junit.Test;

  /*
   * Java中的JUnit单元测试
   *
   * 步骤：
   * 1.选中当前工程 - 右键选择：build path - add libraries - JUnit 4 - 下一步
   * 2.创建Java类，进行单元测试。
   *   此时的Java类要求：① 此类是public的  ②此类提供公共的无参的构造器
   * 3.此类中声明单元测试方法。
   *   此时的单元测试方法：方法的权限是public,没有返回值，没有形参
   *
   * 4.此单元测试方法上需要声明注解：@Test,并在单元测试类中导入：import org.junit.Test;
   *
   * 5.声明好单元测试方法以后，就可以在方法体内测试相关的代码。
   * 6.写完代码以后，左键双击单元测试方法名，右键：run as - JUnit Test
   *
   * 说明：
   * 1.如果执行结果没有任何异常：绿条
   * 2.如果执行结果出现异常：红条
   * 3.用于测试方法是否符合要求
   * 4.只执行最新的一个 @test
   * 5.开发中，在测试类中直接写 @test 和测试方法，再纠错导包
   */
  public class JUnitTest {

      int num = 10;

      @Test
      public void testEquals(){
          String s1 = "MM";
          String s2 = "MM";
          System.out.println(s1.equals(s2));
          //ClassCastException的异常
  //      Object obj = new String("GG");
  //      Date date = (Date)obj;

          System.out.println(num);
          show();
      }

      public void show(){
          num = 20;
          System.out.println("show()....");
      }

      @Test
      public void testToString(){
          String s2 = "MM";
          System.out.println(s2.toString());
      }
  }
```

---

#### 4.快捷键

* 1.补全代码的声明：alt + /
* 2.快速修复: ctrl + 1
* 3.批量导包：ctrl + shift + o
* 去除无用包：ctrl + alt + o
* 4.使用单行注释：ctrl + /
* 5.使用多行注释： ctrl + shift + /
* 6.取消多行注释：ctrl + shift + \
* 7.复制指定行的代码：ctrl + alt + down 或 ctrl + alt + up
* 8.删除指定行的代码：ctrl + d
* 9.上下移动代码：alt + up 或 alt + down
* 10.切换到下一行代码空位：shift + enter
* 11.切换到上一行代码空位：ctrl + shift + enter
* 12.如何查看源码：ctrl + 选中指定的结构 或 ctrl + shift + t
* 13.退回到前一个编辑的页面：alt + left
* 14.进入到下一个编辑的页面(针对于上面那条来说的)：alt + right
* 15.光标选中指定的类，查看继承树结构：ctrl + t
* 16.复制代码： ctrl + c
* 17.撤销： ctrl + z
* 18.反撤销： ctrl + y
* 19.剪切：ctrl + x
* 20.粘贴：ctrl + v
* 21.保存： ctrl + s
* 22.全选：ctrl + a
* 23.格式化代码： ctrl + shift + f
* 24.选中数行，整体往后移动：tab
* 25.选中数行，整体往前移动：shift + tab
* 26.在当前类中，显示类结构，并支持搜索指定的方法、属性等：ctrl + o
* 27.批量修改指定的变量名、方法名、类名等：alt + shift + r
* 28.选中的结构的大小写的切换：变成大写： ctrl + shift + x
* 29.选中的结构的大小写的切换：变成小写：ctrl + shift + y
* 30.调出生成 getter/setter/构造器等结构： alt + shift + s
* 31.显示当前选择资源(工程 or 文件)的属性：alt + enter
* 32.快速查找：参照选中的 Word 快速定位到下一个 ：ctrl + k
* 33.关闭当前窗口：ctrl + w
* 34.关闭所有的窗口：ctrl + shift + w
* 35.查看指定的结构使用过的地方：ctrl + alt + g
* 36.查找与替换：ctrl + f
* 37.最大化当前的 View：ctrl + m
* 38.直接定位到当前行的首位：home
* 39.直接定位到当前行的末位：end

##### （IDEA补充）

* 40.万能解错/生成返回值变量：alt + enter
* 41查看继承关系(type hierarchy)：F4
* 42提示方法参数类型(Parameter Info)：ctrl+alt+/

![](https://inpast-qiq.oss-cn-beijing.aliyuncs.com/img/20210623145749.png)
