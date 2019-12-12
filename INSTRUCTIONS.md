# 项目介绍与后续开发说明

外星人入侵项目是一个带界面用户可交互的项目，这类项目的运转流程大致如下：

1. 用户输入交互指令（键鼠点击释放）；
2. 跟据输入改变项目模型的内在状态；
3. 在界面上显示状态更新后的结果；
4. 回到1重复运行；

我们看一下项目最初的状态，有三类主要部件，即为飞船、外星人舰队和子弹。main.py 第 6 行 ai = AlienInvasion()  实例化 AlienInvasion 类的过程即创建了这三类部件，然后第 7 行调用   ai.run_game(). 可以看到 alien_invasion.py 的函数 run_game 即在实现上面说的运转流程。

run_game  的第 46 行 self._check_events() 检测用户的输入，该项目没有鼠标输入只有键盘输入，可以看到下面又分别用了两个函数 _check_keydown_events 和 _check_keyup_events 来检测键盘相关按键的按下和释放指令，这对应上面的第1步。

然后第 49~53 行根据键盘输入改变模型的内在状态，比如改变飞船位置信息（第49行）。第50行更新模型内部子弹状态，这里由于子弹碰撞舰队后会有更进一步的状态变更，所以可以看到 _update_bullets 函数的第 100 行有 self.\_check_bullet_alien_collisions() 函数的调用。第 51 行更新模型内部外星人状态，可以看到 _update_aliens 函数有检测舰队是否到达边界的函数（第157行），有检测是否与飞船碰撞的函数（第161行），还有检测是否到达底部的函数（第 164 行）。至此三类部件内在状态都已作相应变更，这对应上面第 2 步。

然后第 54 行在界面上更新显示状态信息变更后的部件，可以看到第 206, 208, 210 行分别更新了三类部件，这对应上面第 3 步。第 45 行的 while 循环即对应上面第 4 步。



当我们新增一个功能时，也要让新增的功能与上面的运转流程相吻合。比如当我们新增 laser 功能时，首先是要构造出 laser. 因为 laser 的位置是依赖 ship 的位置的，所以我们需要把 ai_game 传入到 laser.py 第8 行的构造函数以获取它包含的 ship 的位置信息。另外 \_\_init\_\_  里包含一些 laser 自身的形状颜色位置等信息。那么 laser 包含的成员方法应该有哪些呢？位置变更的方法肯定是要有的，这就是 update 函数。而位置变更后与舰队碰撞时也会改变舰队状态，所以要有 _check_laser_alien_collisions 函数。另外 laser 自身位置变更后也要重新绘制，这就是 draw_laser 函数。可以看到最后一个函数 _update_laser 其实仅仅是调用了 update 和 _check_laser_alien_collisions.

现在需要把 laser 的功能加入到项目里，可以按照上面项目运转的流程来操作。首先实例化 AlienInvasion 时需要再多构建 laser 部件，这就是 alien_invasion.py 的第 35 行，且可以看到有把 self 作为参数传入获取飞船信息。然后流程第 1 步，laser 会对键盘输入作出反应，所以第 67 和 84 行会有相关指令变更。再到流程第 2 步，第 53 行 _update_laser 更新 laser 位置信息并作碰撞检测。然后流程第 3 步，第 209 行更新位置变更后的 laser.



 <font color=red>TODO 1：</font>

按照 laser 的方法，新增一个 guarder 类。目的是给 ship 增加保护罩，比如按键盘 g 键后就在飞船周围增加一个半圆形的保护罩。保护罩的功能是可以防御外星舰队的子弹。

虽然我们的外星舰队目前不支持发射子弹功能，但这并不要紧，相关函数可以为空。外星舰队发射子弹的功能与后续进展关联不大。



新增 guarder 的过程中可以发现我们的 bonus_system 并不是可扩展的。也就是每增加一个功能时，在我们实现了这个类后，我们都需要在 alien_invasion.py 里去做相关方法的联动。这样就并没有对 laser 和 guarder 这样相似的功能做统一的管理。laser 和 guarder 的成员变量除了各自形状颜色外都差不多，而且成员方法更是几乎雷同。都要有位置变更的方法，都要有碰撞后的检测方法，而且都要有重新绘制的方法。那么怎样做到对 laser 和 guarder 统一管理。



 <font color=red>TODO 2：</font>

新增一个 sugar **抽象类**，定义三个方法 update, check_collisions, draw. 让 laser 和 guarder 继承 sugar 并覆盖实现这三个方法。这样 laser 和 guarder 就有了统一的行为模式，而且以后再增加新的功能只要是继承 sugar 也会有统一的行为模式。（抽象类需导入模块 import abc）

抽象类就像是声明了一种规范。好处是在 bonus_system 里可以提前统一处理 sugar. 比如在 bonus_system 要调用某个特定 sugar 的绘制函数，那么这个 sugar 必须要有类似的 draw 函数。但如果每个特定 sugar 的 draw 函数名字都不一样，比如 draw_laser,draw_guarder, 那么在 bonus_system 里就没法提前去处理了。这样就像回到了以前的状态，每增加个功能都要去改代码，这不是我们所希望的。但若是每个功能都继承抽象类 sugar, 那么实现该功能时必须重写绘制函数 draw, 那么在 bonus_system 里可以提前方便的调用 draw 函数绘制任意 sugar, 而无需担心这个特定的 sugar 到底是什么怎么实现的 draw.

虽然我们上面新增了 surgar 抽象类，但似乎没起到作用，别着急现在我们就把它用起来。我们不希望每增加一个功能都在 alien_invasion.py 去做多处改动。当 alien_invasion 自身变大或新功能增多后都会导致越来越难以维护，因为模型耦合性太强了。我们现在要做的就是把 bonus_system 作为桥梁，让 alien_invasion 和 sugar 代表的功能联系起来。在 alien_invasion.py 里只出现 bonus_system 相关的代码而不出现 laser 和 guarder 相关功能的代码，这些功能都通过 bonus_system 接入项目。



 <font color=red>TODO 3：</font>

重构 bonus_system 类，实现上面的功能以及我们之前说过的十秒内随机下落 sugar 和飞船吃到 sugar 后能力维持十秒的功能。第一个十秒下落的功能，我们知道飞船一直都是在向下落的，可以看 alien 的 update 函数就知道了。只是在 bonus_system 里需要增加几处时间计算。在 bonus_system 的构造函数 \_\_init\_\_  里需要有一个程序开始时间 programStartTime = time.time() 成员变量，这个变量在 bonus_system 实例化时就确定了，然后在 bonus_system 类下更新 sugar 位置信息的函数里要再获取下当前时间 currentTime = time.time(), 当 currentTime - programStartTime 大于 9.9 小于 10.1 时（或者随机几秒）就要新降 sugar 了，当然别忘了旧 sugar 的处理。飞船能力维持 10 秒的处理与此类似，需要先记录下飞船吃到 sugar 的时间，然后发射函数里再检测当前时间与吃到时间之差，当差大于 10 秒时，能力就失效（一个布尔变量的开关）。

另外关于随机下落 sugar 的处理，就是下落的 sugar 有个 id 是随机生成的，laser 和 guarder 也有各自的 id, 当飞船吃到 sugar 后，匹配 sugar‘s id 的能力（laser 或 guarder）被激活。可以把每个功能的 id 保存在 bonus_system 的一个数组成员变量里。比如我们还可在 bonus_system 里保存一个 sugar 的数组，比如 sugars = [laser, sugar], 然后凭掉落 id 选中 sugars[id]. 那么因为这个数组里的都是 sugar, 所以可以方便的调用 sugars[id].update 或 sugars[id].draw 等。这就是继承抽象好处的体现。

因为碰撞检测使用了 Sprite 的 groupcollide 函数，所以功能需要继承 Sprite. 又因为要继承 Sugar, 所以就会产生多继承。这里需要注意的是 Sprite 也有名为 update 和 draw 的函数。我不太确定两个父类有重名方法会否导致冲突之类，但不试试怎么知道呢。

关于按键检测，我还没有细致思考是否每个功能 laser 或 guarder 的关联按键都应在构造函数里指定。检测函数是放在 bonus_system 里还是下放到 laser 和 guarder 里，我也还有待考虑。

