# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。



#运行python先打包一个字典给screen item_description调取不同描述用
init python:
    item_descriptions = {
        "magazine": "《女性领导者》特刊，有人撕掉了一半页面。",
        "computer": "【Excel表格开着】你应聘岗位的薪资范围：男性起薪22K，女性18K。",
        "smartphone": "妈妈的信息：工作拿到了吗？弟弟要买新鞋。"
    }
    item_names = {
        "magazine": "杂志",
        "computer": "前台电脑",
        "smartphone": "手机"
    }

# 物品描述屏幕，对应imagebutton中的show函数调用的screen_item_descriptions
#！！！重要！原报错写法：用default定义默认的局部变量，无法传递参数
#即：没有在screen中书写明确的参数声明（screen：我需要参数），show调取时screen只有局部变量传递不了存在字典里的参数信息
#修改后：screen（内部具有明确参数声明description），info来自show指定的调用来源item_description
screen item_description(description, name): 
    #default description = ""
    modal True
    zorder 100
    
    # 半透明背景
    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        
        vbox:
                       
            text name:
                size 28 color "#ffffff" xalign 0
            null height 30
            
            add Solid("#FFFFFF"):
                xsize 800
                ysize 1
                xalign 0.5
                alpha 0.3  # 30%不透明度
            null height 30

            text description:
                size 24
                color "#FFFFFF"
                xalign 0.5
            null height 50
            
            textbutton "关闭":
                xalign 0.5
                action Hide("item_description")

screen items_screen():
    # 添加进度显示
    text "已发现物品[len(clicked_items)]/3":
        xalign 0.95
        yalign 0.05
        size 36
        color "#ffffff"
        outlines [ (2, "#000000", 0, 0) ]  # 添加黑色描边
    # vbox:
    #     xalign 0.5
    #     yalign 0.5
    #     text "进度: [len(clicked_items)]/3" size 24 color "#FFD700"

    # 物品1 - 杂志
    imagebutton:
        xpos 1200
        ypos 200
        idle "item1_magazine.png"
        hover "item1_magazine_hover.png"
        if not item1_magazine_clicked:  #not clicked时才可点击
            action [
                SetVariable("item1_magazine_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "magazine" in clicked_items else clicked_items + ["magazine"]
                ),                
                Show("item_description", description=item_descriptions["magazine"], name=item_names["magazine"]),
                If(
                    len(clicked_items) >= 2,  # 当前是第3个物品（点击前已有2个）
                    true=[
                        SetVariable("third_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            # 已点击状态
            idle "item1_magazine.png" 
            hover "item1_magazine_hover.png"
            action Show("item_description", description=item_descriptions["magazine"], name=item_names["magazine"])
    
    # 物品2 - 前台电脑
    imagebutton:
        xpos 400
        ypos 200
        idle "item2_computer.png"
        hover "item2_computer_hover.png"
        if not item2_computer_clicked:  
            action [
                SetVariable("item2_computer_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "computer" in clicked_items else clicked_items + ["computer"]
                ),
                Show("item_description", description=item_descriptions["computer"], name=item_names["computer"]),
                If(
                    len(clicked_items) >= 2,  # 当前是第3个物品（点击前已有2个）
                    true=[
                        SetVariable("third_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            idle "item2_computer.png"
            hover "item2_computer_hover.png"
            action Show("item_description", description=item_descriptions["computer"], name=item_names["computer"])
    
    # 物品3 - 手机
    imagebutton:
        xpos 100
        ypos 200
        idle "item3_smartphone.png"
        hover "item3_smartphone_hover.png"
        if not item3_smartphone_clicked: 
            action [
                SetVariable("item3_smartphone_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "smartphone" in clicked_items else clicked_items + ["smartphone"]
                ),
                Show("item_description", description=item_descriptions["smartphone"], name=item_names["smartphone"]),                
                If(
                    len(clicked_items) >= 2,  # 当前是第3个物品（点击前已有2个）
                    true=[
                        SetVariable("third_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            idle "item3_smartphone.png"
            hover "item3_smartphone_hover.png"
            action Show("item_description", description=item_descriptions["smartphone"], name=item_names["smartphone"])

# 第三个物品点击标记
default third_item_clicked = False

# 物品描述屏幕，添加自动跳转逻辑
screen item_description(description, name): 
    modal True
    zorder 100
    
    # 半透明背景
    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        
        vbox:
                       
            text name:
                size 28 color "#ffffff" xalign 0
            null height 30
            
            add Solid("#FFFFFF"):
                xsize 800
                ysize 1
                xalign 0.5
                alpha 0.3  # 30%不透明度
            null height 30

            text description:
                size 24
                color "#FFFFFF"
                xalign 0.5
            null height 50
            
            textbutton "关闭":
                xalign 0.5
                action [
                    Hide("item_description"),
                    If(
                        third_item_clicked,
                        true=Jump("after_third_item"),
                        false=NullAction()
                    )
                ]

#-----------------------------------------------

define s = Character("小曼") #避免每次都打很多字
define n = Character(None, what_italic=True)

label start:

    scene 31 #Emma:需要替换开场图片
    show titletest:
        pos(120,150)
    
    ##show eileen happy #Emma：需要透明底角色立绘，后续替换立绘图

    menu:
        "开始游戏":
            style choice_vbox:
                xalign 0.5
                ypos 700
                yanchor 0.5
            jump chapter0
        "退出游戏":
            return

label chapter0:
    show garage #替换黑幕布

    image chapter0_title = ParameterizedText(xalign=0.5, yalign=0.45, size=108)
    show chapter0_title "序章：入职"
    with fade
    pause 2
    hide chapter0_title
    #with fade 不要这行之后丝滑切换了，迷
    
    scene 31
    with fade
    pause 1
    "{i}你投了147份简历, 12封是拒信。{/i}"
    "{i}妈妈每周日打电话问你什么时候别挑了。但这一次……感觉不一样。{/i}"
    "{i}你进入了等待室，下一个就到你了。{/i}"
    jump waiting_room
    
label waiting_room:
    
    scene garage #替换为办公室图片

    menu:
        "探索房间":
            call explore_room #call完之后走jump
            jump explore_complete
        "安静等待":
            jump explore_complete

label explore_room:
    # 初始化点击状态
    default item1_magazine_clicked = False
    default item2_computer_clicked = False
    default item3_smartphone_clicked = False

    # 使用列表记录点击的不同物品
    $ clicked_items = []  # 存储被点击过的物品

    show screen items_screen
    
    # 等待跳转
    $ renpy.pause(delay=None, hard=False, predict=False, modal=False)
    return

label explore_complete:
    hide screen items_screen
    hide screen item_description
    scene 31 # scene可以把textbox遮掉
    with fade
    pause 1.0
    'HR'"佘小姐？陈总请您进去。"
    jump chapter0_2

# 点击第三个物品后跳转到这里
label after_third_item:
    $ third_item_clicked = False  # 重置标记
    s "面试好像要开始了？"
    jump explore_complete

default money = 800
default social = 0
default mental = 0
default awakening = 0
init python:
    #数值系统
    def add_money(amount, reason=""):
        global money
        money += amount
        print(f"金钱 {amount:+} ({reason})，当前: {money}")
    
    def add_social(amount, reason=""):
        global social
        social += amount
        print(f"社交 {amount:+} ({reason})，当前: {social}")
    
    def add_mental(amount, reason=""):
        global mental
        mental += amount
        print(f"精神 {amount:+} ({reason})，当前: {mental}")
    
    def add_awakening(amount, reason=""):
        global awakening
        awakening += amount
        print(f"觉醒 {amount:+} ({reason})，当前: {awakening}")

    #陈永仁到处乱看的提示            
    def show_sequential_thoughts(high_msg, mid_msg, low_msg, interval=0.5, duration=1.5):
        # 瀑布式先后提示弹出消失（高中低，已折叠）
        renpy.show_screen("high_notify", message=high_msg, duration=duration)
        renpy.pause(interval)
        
        renpy.show_screen("mid_notify", message=mid_msg, duration=duration)
        renpy.pause(interval)
        
        renpy.show_screen("low_notify", message=low_msg, duration=duration)
        renpy.pause(duration + 0.3)  # 等待最后一个消失

# 高
screen high_notify(message, duration=1):
    zorder 100
    
    frame:
        at transform:
            alpha 0.0
            easein 1 alpha 1.0
            pause duration
            easeout 2 alpha 0.0
        
        background Frame("gui/textbox.png", 10, 10)
        padding (100, 12)
        xalign 0.1
        yalign 0.1  # 高位置：10%
        hbox:
            spacing 8
            text message size 30

# 中
screen mid_notify(message, duration=1):
    zorder 100
    
    frame:
        at transform:
            alpha 0.0
            pause 1
            easein 1.5 alpha 1.0
            pause duration
            easeout 1.5 alpha 0.0
        
        background Frame("gui/textbox.png", 10, 10)
        padding (100, 12)
        xalign 0.9
        yalign 0.3  # 中位置：30%
        
        hbox:
            spacing 8
            text message size 30

# 低
screen low_notify(message, duration=1):
    zorder 100
    
    frame:
        at transform:
            alpha 0.0
            pause 1.5
            easein 1.5 alpha 1.0
            pause duration
            easeout 1.5 alpha 0.0
        
        background Frame("gui/textbox.png", 10, 10)
        padding (100, 12)
        xalign 0.2
        yalign 0.5 
        
        hbox:
            spacing 8
            text message size 30

define c = Character("陈永仁")

label chapter0_2:
    "{i}他站起来迎接你，温暖的笑容，完美的姿态。他是那种让你立刻感受到自己被看见的人。{/i}"
    "{i}你坐下了，被他办公桌上的东西吸引了注意。{/i}"
    menu:
        "书架":
            "上面摆放着一些法律书籍、商业策略，还有女性诗人的诗集。"
        "桌上的照片":
            "是一张全家福，上面有他的妻子、两个孩子，他们都在笑。"
        "印有图案的咖啡杯":
            "“世界最佳爸爸”——杯沿有缺口。"
        "落地窗":
            "站在这能看见整座城市。"
    jump after_menu

label after_menu:
    c"小曼，告诉我，你为什么想来这里工作？"
    menu:
        "我需要钱。":
            s"我需要钱。"
        "我欣赏贵公司的价值观。":
            s"我欣赏贵公司的价值观。"
            $ add_social(1, "面试B")
        "我想证明我能比任何人做得更好。":
            s"我想证明我能比任何人做得更好。"
            $ add_mental(1, "面试C")
    c"明白了。你知道吗，我们有过更有经验的候选人。但我在你简历里看到了……渴望。"
    $ show_sequential_thoughts(
        "他在观察你的手。",
        "他在观察你的脸。", 
        "他在看你的简历。"
    )
    pause 3
    c"有什么问题想问我吗？"
    menu:
        "这里的女性晋升通道怎么样？":
            s"这里的女性晋升通道怎么样？"
            "{i}陈永仁笑了。{/i}"
            c"好问题。我们这里很进步。中层管理一半是女性……嗯，三分之一吧……有个Linda，她很优秀。"
            jump chapter0_3
        "有居家办公的弹性吗？":
            s"有居家办公的弹性吗？"
            "{i}陈笑容依旧，但眼神变得认真起来{/i}"
            c"好问题。我们公司其实很重视工作生活的平衡。居家办公原则上支持。"
            c"但……说实话，在游戏这行——尤其是设计师，前期最好多在场。当然，这不是强制，只是建议。"
            jump chapter0_3
        "没有了，您都介绍得很清楚。":
            jump chapter0_3

label chapter0_3:
    c"还有别的问题吗？"
    s"没有了，谢谢您。"
    c"那么面试就到这吧，和你的交流很愉快。"

    scene black
    #show 邮件页面




# 第一章：蜜月期（第1-4周）
# 任务1.1：第一天，第一印象

# 角色定义（延续已有定义）
define s = Character("小曼")  # 已定义，延续使用
define unknown_woman = Character("陌生女人", color="#808080")
define narrator = Character(None, what_italic=True)

# 变量定义（延续已有default变量）
# money已在前面定义为default money = 800
default coffee_bought = False
#default elevator_floor = 0
default gate_used = False
default appearance_checked = False
default third_floor = False
default eight_floor = False
default twenty_third_floor = False

# 场景定义（占位符图片）
image bg lobby = "bg_lobby.png"  # 公司大堂
image bg elevator = "bg_elevator.png"  # 电梯内部
image bg coffee_stand = "bg_coffee_stand.png"  # 咖啡亭
image bg third_floor = "bg_hr_floor.png"  # 3楼HR
image bg eight_floor = "bg_marketing_floor.png"  # 8楼市场部
image bg your_floor = "bg_your_floor.png"  # 12楼你的部门（设计部）
image bg twenty_third_floor = "bg_executive_floor.png"  # 23楼高管层

# 角色立绘（占位符）
image woman normal = "woman_normal.png"

# ========== 第一章入口 ==========

label chapter1:
    scene bg lobby with fade
    
    # 开场
    "大楼里弥漫着空气清新剂和野心。你早到了13分钟。每个人都这样。"
    
    jump lobby_explore

# ========== 大堂探索 ==========
screen lobby_menu(gate_used, coffee_bought, appearance_checked):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.35
        
        text "大堂可探索："
        
        if not gate_used:
            textbutton "闸机 - 刷工牌" action Jump("gate_interaction")
        if not coffee_bought:
            textbutton "咖啡亭 - 买咖啡" action Jump("coffee_stand")
        if not appearance_checked:
            textbutton "电梯门倒影 - 整理仪容" action Jump("mirror_check")

label lobby_explore:
    scene bg lobby
    
    if gate_used and coffee_bought and appearance_checked:
        s"还有点时间，去熟悉熟悉办公楼层吧。"
        jump elevator_choice
    
    # 调用自定义位置的菜单
    call screen lobby_menu(gate_used, coffee_bought, appearance_checked)
# ========== 闸机互动 ==========

label gate_interaction:
    scene bg lobby
    
    "“哔！”"
    
    "“欢迎，小曼！”{i}——这是你第一次在这里听到自己的名字{/i}"
    
    $ gate_used = True
    
    jump lobby_explore

# ========== 咖啡亭 ==========

label coffee_stand:
    scene bg coffee_stand
    
    "{i}咖啡师很帅，他也发现了你这位新来的美女{/i}"
    
    $ money -= 30
    
    "-30元。【当前余额：[money]元】"
    
    $ coffee_bought = True
    
    jump lobby_explore

# ========== 整理仪容 ==========

label mirror_check:
    scene bg lobby
    
    "{i}你穿着新买的职业裙，很合身{/i}"
    
    $ appearance_checked = True
    
    jump lobby_explore

# ========== 电梯选择 ==========
screen elevator_menu(third_floor, eight_floor, twenty_third_floor):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.35
        
        text "探索办公楼层："
        
        if not third_floor:
            textbutton "3楼" action Jump("third_floor")
        if not eight_floor:
            textbutton "8楼" action Jump("eight_floor")
        if not twenty_third_floor:
            textbutton "23楼" action Jump("twenty_third_floor")

label elevator_choice:
    scene bg elevator
    
    if third_floor and eight_floor and twenty_third_floor:
        jump chapter1_2
    call screen elevator_menu(third_floor, eight_floor, twenty_third_floor)


        
label third_floor:
    scene bg third_floor with dissolve
    "{i}HR部门...{/i}"
    $ third_floor = True
    jump elevator_choice
            
label eight_floor:
    scene bg eight_floor with dissolve
    "{i}市场部...{/i}"
    $ eight_floor = True
    jump elevator_encounter
            
label twenty_third_floor:
    scene bg twenty_third_floor with dissolve
    "{i}高管层...{/i}"
    $ twenty_third_floor = True
    jump elevator_choice

# ========== 电梯随机遭遇 ==========

label elevator_encounter:
    scene bg elevator with fade
    
    "{i}电梯门打开。一位40多岁的女人，套装干练，眼神疲惫。{/i}"
    
    show woman normal at center
    
    unknown_woman "新来的？"
    
    s "第一天。"
    
    unknown_woman "啊。"
    
    "{i}她盯着你看的时间有点长。{i}"
    
    unknown_woman "设计部？"
    
    s "诶，你怎么知道？"
    
    unknown_woman "就那种眼神。不知道你会在这待多久呢？"
    
    hide woman normal with moveoutleft
    
    "{i}她在8楼下电梯。你始终不知道她的名字。{/i}"
    
    # 剧情继续到下一部分...
    jump elevator_choice

label chapter1_2:
    s"啊，时间到了，得赶紧去工位。"
    scene bg your floor with fade
    "{i}来到12楼，门牌标着“设计部”。{/i}"
    "{i}一排排办公桌。米色和灰色的隔间。有人在用微波炉热爆米花，快糊了。{/i}"
