# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define config.layers = ['master', 'transient', 'screens', 'interface', 'front'] #显示图层

#成就相关数值
default escape = 0 #【成就：鸵鸟】


#运行python先打包一个字典给screen item_description调取不同描述用
init python:
    item_descriptions = {
        "magazine": "《女性领导者》特刊，有人撕掉了一半页面。",
        "computer": "【Excel表格开着】你应聘岗位的薪资范围：男性起薪22K，女性18K。",
        "smartphone": "妈妈的信息：工作找到了吗？弟弟要买新鞋。",
        "window": "你看着这座城市，135封拒信散落其中。"
    }
    item_names = {
        "magazine": "杂志",
        "computer": "前台电脑",
        "smartphone": "手机",
        "window": "玻璃窗"
    }
    item_image = {
        "window": "chapter0_items/window_scenery.png" 
    }

#小曼立绘的淡入淡出，onlayer使用必须用这个控制
transform top_dissolve:
    # 进入
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    
    # 离开 - 关键
    on hide:
        alpha 1.0
        linear 0.25 alpha 0.0

# 物品描述屏幕，对应imagebutton中的show函数调用的screen_item_descriptions
#！！！重要！原报错写法：用default定义默认的局部变量，无法传递参数
#即：没有在screen中书写明确的参数声明（screen：我需要参数），show调取时screen只有局部变量传递不了存在字典里的参数信息
#修改后：screen（内部具有明确参数声明description），info来自show指定的调用来源item_description
screen item_description(description, name, image): 
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
    modal True
    # 添加进度显示
    text "已发现物品[len(clicked_items)]/4":
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
        at transform:
            zoom 0.35
        xpos 1580
        ypos 830
        idle "chapter0_items/test_01_book_color.png" #彩色
        hover "chapter0_items/test_01_book_colorhover.png" #彩色
        # idle "test_01_book_bw.png" #黑白
        # hover "test_01_book_bwhover.png" #黑白
        # idle "item1_magazine.png" #原像素风
        # hover "item1_magazine_hover.png" #原像素风
        if not item1_magazine_clicked:  #not clicked时才可点击
            action [
                SetVariable("item1_magazine_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "magazine" in clicked_items else clicked_items + ["magazine"]
                ),                
                Show("item_description", description=item_descriptions["magazine"], name=item_names["magazine"], image=None),
                If(
                    len(clicked_items) >= 3,  # 当前是第4个物品（点击前已有3个）
                    true=[
                        SetVariable("five_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            # 已点击状态
            # idle "item1_magazine.png" #原像素风
            # hover "item1_magazine_hover.png" #原像素风
            idle "chapter0_items/test_01_book_bw.png"
            hover "chapter0_items/test_01_book_bwhover.png"
            action Show("item_description", description=item_descriptions["magazine"], name=item_names["magazine"], image=None)
    
    # 物品2 - 前台电脑
    imagebutton:
        at transform:
            zoom 0.45
        xpos 460
        ypos 470
        # idle "chapter0_items/test_02_computer_bw.png" #黑白
        # hover "chapter0_items/test_02_computer_bwhover.png" #黑白
        idle "chapter0_items/test_02_computer_color.png" #彩色
        hover "chapter0_items/test_02_computer_colorhover.png" #彩色
        # idle "item2_computer.png" #原像素风
        # hover "item2_computer_hover.png" #原像素风
        if not item2_computer_clicked:  
            action [
                SetVariable("item2_computer_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "computer" in clicked_items else clicked_items + ["computer"]
                ),
                Show("item_description", description=item_descriptions["computer"], name=item_names["computer"], image=None),
                If(
                    len(clicked_items) >= 3,  # 当前是第4个物品（点击前已有3个）
                    true=[
                        SetVariable("five_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            # idle "chapter0_items/test_02_computer_bw.png" #黑白
            # hover "chapter0_items/test_02_computer_bwhover.png" #黑白
            idle "chapter0_items/test_02_computer_color.png" #彩色
            hover "chapter0_items/test_02_computer_colorhover.png" #彩色        
            # idle "item2_computer.png" #原像素风
            # hover "item2_computer_hover.png" #原像素风
            action Show("item_description", description=item_descriptions["computer"], name=item_names["computer"], image=None)
    
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
                Show("item_description", description=item_descriptions["smartphone"], name=item_names["smartphone"], image=None),                
                If(
                    len(clicked_items) >= 3,
                    true=[
                        SetVariable("five_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            idle "item3_smartphone.png"
            hover "item3_smartphone_hover.png"
            action Show("item_description", description=item_descriptions["smartphone"], name=item_names["smartphone"], image=None)

    # 物品4 - 玻璃窗
    imagebutton:
        at transform:
            zoom 0.9
        xpos 1229
        ypos 59
        idle "chapter0_items/test_03_window_bw.png"
        hover "chapter0_items/test_03_window_bwhover.png"
        if not item4_window_clicked: 
            action [
                SetVariable("item4_window_clicked", True),
                SetVariable("clicked_items", 
                    clicked_items if "window" in clicked_items else clicked_items + ["window"]
                ),
                Show("item_description", description=item_descriptions["window"], name=item_names["window"], image=item_image["window"]),                
                If(
                    len(clicked_items) >= 3,  # 当前是第4个物品（点击前已有3个）
                    true=[
                        SetVariable("five_item_clicked", True),
                        Hide("items_screen")
                    ],
                    false=NullAction()
                )
            ]
        else:
            idle "chapter0_items/test_03_window_bw.png"
            hover "chapter0_items/test_03_window_bwhover.png"
            action Show("item_description", description=item_descriptions["window"], name=item_names["window"], image=item_image["window"])
# 第三个物品点击标记
default five_item_clicked = False

# 物品描述屏幕，添加自动跳转逻辑
screen item_description(description, name, image): 
    modal True
    zorder 120
    
    # 半透明背景
    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        
        vbox:
                       
            text name:
                size 30 color "#ffffff" xalign 0
            null height 30
            
            add Solid("#FFFFFF"):
                xsize 800
                ysize 1
                xalign 0.5
                alpha 0.3  # 30%不透明度
            null height 30 

            add image:
                at transform:
                    zoom 0.3
                xalign 0.5
            null height 40 
            
            text description:
                size 25
                color "#FFFFFF"
                xalign 0.5
            null height 50

            textbutton "关闭":
                at transform:
                    zoom 0.9
                xalign 0.5
                action [
                    Hide("item_description"),
                    If(
                        five_item_clicked,
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
    show black #替换黑幕布
    image chapter0_title = ParameterizedText(xalign=0.5, yalign=0.45, size=108)
    show chapter0_title "序章：音信"
    with fade
    pause 2
    hide chapter0_title
    #with fade 不要这行之后丝滑切换了，迷
    
    scene office_hall
    with fade
    pause 1
    show she_01_normal_nocard onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}这个招聘季投了147份简历, 12封是拒信，其他杳无音讯。{/i}"
    "{i}妈妈每周日打电话问你什么时候能找到工作，别再挑了。\n但这一次……感觉不一样。{/i}"
    hide she_01_normal_nocard onlayer top
    scene black with fade
    "{i}你进入了等待室，下一个就到你了。{/i}"
    jump waiting_room
    
label waiting_room:
    
    scene dengdaishi with fade:
        zoom 1.9
        xalign 0.5
        yalign 0.7
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
    default item4_window_clicked = False

    # 使用列表记录点击的不同物品
    $ clicked_items = []  # 存储被点击过的物品

    show screen items_screen
    
    # 等待跳转
    $ renpy.pause(delay=None, hard=False, predict=False, modal=False)
    return

# 点击第三个物品后跳转到这里
label explore_complete:
    hide screen items_screen
    hide screen item_description
    'HR'"佘小姐？陈总请您进去。"
    jump chapter0_2

label after_third_item:
    $ five_item_clicked = False  # 重置标记
    s "面试好像要开始了？"
    jump explore_complete


default money = 2000
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

#===================2×2选项方阵===================
screen grid_choice(title, opt1, opt2, opt3, opt4, act1, act2, act3, act4):
    modal True
    style_prefix "choice"
    
    # 2×2 按钮网格
    grid 2 2:
        xalign 0.5
        yalign 0.95
        spacing 20
        
        # 第一行
        button :
            xsize 600
            ysize 50
            action act1
            
            text opt1:
                size 32
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        button:
            xsize 600
            ysize 50
            action act2
            
            text opt2:
                size 32
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        # 第二行
        button:
            xsize 600
            ysize 50
            action act3
            
            text opt3:
                size 32
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        button:
            xsize 600
            ysize 50
            action act4
            
            text opt4:
                size 32
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

#=======================

define c = Character("陈永仁")

label chapter0_2:
    scene chen_office with fade:
        zoom 1.3
        xalign 0.9
        yalign 0.4
    show she_01_normal_nocard onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show chen_03_narroweyes with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160
    "{i}他站起来迎接你，温暖的笑容，完美的姿态。他是那种让你立刻感受到自己被看见的人。{/i}"
    show she_01_normal_nocard_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}你坐下了，被他办公室的布置吸引了注意。{/i}"
    hide she_01_normal_nocard onlayer top
    hide she_01_normal_nocard_eye onlayer top
    scene chen_office with fade:
        zoom 1.1
        xalign 0.9
        yalign 0.4
    call screen grid_choice(
        "你最想查看的物品是",
        "书架", "桌上的照片",
        "印有图案的咖啡杯", "落地窗",
        Jump("bookshelf"), Jump("family_photo"),
        Jump("coffee_mug"), Jump("french_window")
    )
label bookshelf:
    "{i}上面摆放着一些法律书籍、商业策略，还有女性诗人的诗集。{/i}"
    window hide
    jump after_menu

label family_photo:
    "{i}是一张全家福，上面有他的妻子、两个孩子，他们都在笑。{/i}"
    window hide
    jump after_menu

label coffee_mug:
    "{i}杯沿有个缺口的咖啡杯，上面印着“世界最佳爸爸”。{/i}"
    window hide
    jump after_menu

label french_window:
    "{i}站在这，仿佛整座城市都在自己的脚下。{/i}"
    window hide
    jump after_menu

label after_menu:
    scene chen_office with fade:
        zoom 1.3
        xalign 0.9
        yalign 0.4
    show chen_03_narroweyes with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 680
        ypos 160
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
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 681
        ypos 162
    c"明白了。你知道吗，我们有过更有经验的候选人。但我在你简历里看到了……渴望。"
    $ show_sequential_thoughts(
        "他在观察你的手。",
        "他在观察你的脸。", 
        "他在看你的简历。"
    )
    pause 1.5
    hide chen_01_normal with dissolve
    hide screen high_notify
    hide screen mid_notify
    hide screen low_notify
    c"有什么问题想问我吗？"
    menu:
        "这里的女性晋升通道怎么样？":
            s"这里的女性晋升通道怎么样？"
            show chen_02_smile:
                zoom 0.9
                xzoom -1.0
                xpos 680
                ypos 160 
            c"好问题。我们这里很进步。中层管理一半是女性……嗯，三分之一吧……有个Linda，她很优秀。"
            hide chen_02_smile
            jump chapter0_3
        "有居家办公的弹性吗？":
            s"有居家办公的弹性吗？"
            show chen_05_wanwei: 
                zoom 0.9
                xzoom -1.0
                xpos 687
                ypos 161
            c"好问题。我们公司其实很重视工作生活的平衡。居家办公原则上支持。"
            c"但……说实话，在游戏这行——尤其是设计师，前期最好多在场。当然，这不是强制，只是建议。"
            hide chen_05_wanwei
            jump chapter0_3
        "没有了，您都介绍得很清楚。":
            jump chapter0_3

label chapter0_3:
    show chen_03_narroweyes:
        zoom 0.9
        xzoom -1.0
        xpos 680
        ypos 160
    c"还有别的问题吗？"
    hide chen_03_narroweyes
    show chen_03_narroweyes:
        zoom 0.9
        xzoom -1.0
        xpos 680
        ypos 160
    show chen_03_narroweyes with move:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160
    show she_01_normal_nocard onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show she_03_tinysmile_nocard onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s"没有了，谢谢您。"
    c"那么面试就到这吧，和你的交流很愉快。"    
    hide she_01_normal_nocard onlayer top
    hide she_03_tinysmile_nocard onlayer top
    scene black with fade
    #show 邮件页面
    jump chapter1




# 第一章：蜜月期（第1-4周）
# 任务1.1：第一天，第一印象

# 角色定义（延续已有定义）
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
#image bg lobby = "bg_lobby.png"  # 公司大堂
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
    image chapter1_title = ParameterizedText(xalign=0.5, yalign=0.45, size=108)
    show chapter1_title "Chapter 1：入职"
    with fade
    pause 2
    hide chapter1_title
    scene lobby with fade
    
    # 开场
    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "大楼里弥漫着空气清新剂和野心。你早到了13分钟。每个人都这样。"
    hide she_03_tinysmile_eye onlayer top

    show she_03_tinysmile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "今天是入职第一天，先看看新环境怎么样。"
    hide she_03_tinysmile onlayer top

    jump lobby_explore

# ========== 大堂探索 ==========
screen lobby_menu(gate_used, coffee_bought, appearance_checked):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.45
        
        text "大堂可探索：":
            size 34
            color "#ffffff"
            outlines [ (2, "#000000", 0, 0) ]
        
        if not gate_used:
            textbutton "闸机" action Jump("gate_interaction")
        if not coffee_bought:
            textbutton "咖啡亭" action Jump("coffee_stand")
        if not appearance_checked:
            textbutton "电梯门倒影" action Jump("mirror_check")

label lobby_explore:
    scene lobby with dissolve
    
    if gate_used and coffee_bought and appearance_checked:
        show she_03_tinysmile onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "还有点时间，去熟悉熟悉办公楼层吧。"
        hide she_03_tinysmile onlayer top
        jump elevator_choice
    
    # 调用自定义位置的菜单
    call screen lobby_menu(gate_used, coffee_bought, appearance_checked)
# ========== 闸机互动 ==========
transform rotate_in:
    # 起始：倒置旋转，透明
    align(0.5, -0.1)
    rotate 30
    alpha 0.0
    
    # 快速滑入并旋转
    easein 0.6 align(0.535, -0.07) rotate -5 alpha 1.0 


transform bounce_rotate_in:
    # 起始：倒置旋转，透明
    align(-0.1, 1.5)
    rotate 120
    alpha 0.0
    
    # 快速滑入并旋转
    easein 0.6 align(0.35, 0.51) rotate 0 alpha 1.0 
    
    # 弹性回弹
    #easeout 0.5 rotate -10
    easein 0.4 align(0.51, 0.505) rotate 10 
    easeout 0.1 rotate 9 

label gate_interaction:
    
    show office_card at bounce_rotate_in
    show office_card_rope at rotate_in
    #"“哔！”" #改成音效
    
    "“欢迎，小曼！”{i}——这是你第一次在这里听到自己的名字{/i}"
    
    $ gate_used = True
    jump lobby_explore

# ========== 咖啡亭 ==========

label coffee_stand:
    scene coffee_stand_test
    # show she_03_tinysmile onlayer top at top_dissolve:
    #         zoom 0.8
    #         xzoom -1.0
    #         xpos -30
    #         ypos 240
    
    show coffee_staff_01_normal with dissolve:
        zoom 0.68
        xpos 690
        ypos 160
    '咖啡店员'"你好，要点什么？"

    s "一杯热拿铁吧，谢谢。"

    show coffee_staff_03_chat with dissolve:
        zoom 0.68
        xpos 690
        ypos 160
    '咖啡店员'"平时没怎么见过你呢，是新来的吗？"

    s "嗯，今天入职。"

    show coffee_staff_02_smile with dissolve:
        zoom 0.68
        xpos 690
        ypos 160
    '咖啡店员'"你的咖啡好了。祝你入职顺利。"

    $ money -= 30
    "-30元。【当前余额：[money]元】"
    $ coffee_bought = True
    
    jump lobby_explore

# ========== 整理仪容 ==========

label mirror_check:
    scene lobby
    show elevator_reflection with dissolve
    "{i}你穿着新买的职业裙，很合身{/i}"
    
    $ appearance_checked = True
    
    jump lobby_explore

# ========== 电梯选择 ==========
screen elevator_menu(third_floor, eight_floor, twenty_third_floor):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.4
        
        # text "探索办公楼层：":
        #     outlines [ (2, "#000000", 0, 0) ]
        #     xpos 50 
        
        if not third_floor:
            textbutton "3楼" action Jump("third_floor")
        if not eight_floor:
            textbutton "8楼" action Jump("eight_floor")
        if not twenty_third_floor:
            textbutton "23楼" action Jump("twenty_third_floor")

label elevator_choice:
    scene black with dissolve
    show elevator with fade:
        zoom 1.15
        align (0.5, 0.5)
    show she_03_tinysmile onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
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
    scene elevator with fade:
        zoom 2.3
        align (0.5, 0.5)
    
    "{i}电梯门打开。一位40多岁的女人，套装干练，眼神疲惫。{/i}"
    
    show woman normal at right
    
    unknown_woman "新来的？"
    
    show she_05_happy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "第一天。"
    
    unknown_woman "啊。"
    
    "{i}她盯着你看的时间有点长。{i}"
    
    unknown_woman "设计部？"

    hide she_05_happy onlayer top
    show she_06_surprise_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "诶，你怎么知道？"
    
    unknown_woman "就那种眼神。不知道你会在这待多久呢？"
    
    hide woman normal with moveoutleft
    
    "{i}她在8楼下电梯。你始终不知道她的名字。{/i}"
    
    # 剧情继续到下一部分...
    hide she_06_surprise_eye onlayer top
    jump elevator_choice

label chapter1_2:
    show she_07_astonish onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s"啊，时间到了，得赶紧去工位。"
    hide she_03_tinysmile onlayer top
    hide she_07_astonish onlayer top
    
    scene office with fade
    "{i}{cps=10}12楼，“设计部”。{/cps}{/i}"
    "{i}一排排办公桌。米色和灰色的隔间。有人在用微波炉热爆米花，快糊了。{/i}"

# 延续已有定义的角色
define s = Character("小曼")
define n = Character(None, what_italic=True)

# 第一章新角色定义
define xiaojin = Character("小金", color="#FFD700")
define linjie = Character("林姐", color="#808080")
define chen = Character("陈永仁", color="#4169E1")
define unknown = Character("???")

# 延续已有变量，新增关系度变量
default xiaojin_interest = 0
default linjie_interest = 0

# 任务相关标记
default task_assigned = False

# 场景图片定义（占位符）
image bg office_floor = "bg_office_floor.png"
# image bg meeting_room = "bg_meeting_room.png"

# ========== 第一章：自我介绍 ==========
label chapter1_self_intro:
    scene office_area with fade: #要替换空一点的办公桌图片
        zoom 2
    
    "{i}你来到工位，正在收拾东西。{/i}"
    
    show jin_01_happy with moveinright:
        zoom 0.97
        xpos 700
        ypos 150
    xiaojin "嘿！新来的美女！终于有个不是我爸年纪的人了。喝咖啡吗？我告诉你哪个机器好。"

    show jin_01_happy with move:
        zoom 0.97
        xpos 1360
        ypos 150

    show she_01_normal_eye_o onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    menu:
        "好啊，谢谢！":
            $ xiaojin_interest += 1
            jump xiaojin_friendly
            
        "等会儿吧，我想先收拾一下。":
            jump xiaojin_neutral
            
        "我自己带了。":
            jump xiaojin_cold

# 选项A：友好路线
label xiaojin_friendly:
    hide she_01_normal_eye_o onlayer top
    show she_05_happy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我在楼下买了一杯了，不过好啊，谢谢你。"
    hide she_05_happy onlayer top

    scene tea_room with dissolve
    
    show jin_02_frown with dissolve:
        zoom 0.97
        xpos 700
        ypos 150

    xiaojin "你刚来，记得别得罪陈总——他挺随和的，但别惹他。还有HR那女的？也别得罪。"
    xiaojin "……算了，谁都别得罪。我来8个月了，还在琢磨。"
    hide jin_02_frown with dissolve
    
    jump linjie_encounter

# 选项B：礼貌路线
label xiaojin_neutral:
    hide she_01_normal_eye_o onlayer top
    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "等一会儿可以吗，我想先收拾一下桌面。"
    
    xiaojin "行，那你先忙，有事找我。"
    hide jin_01_happy with moveoutright

    jump linjie_encounter

# 选项C：疏远路线
label xiaojin_cold:
    hide she_01_normal_eye_o onlayer top
    show she_01_normal_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我自己带了。"

    xiaojin "……哈哈，那行，我就先走了。"
    hide jin_01_happy with moveoutright

    hide she_01_normal_eye onlayer top
    
    jump linjie_encounter

# ========== 林姐登场 ==========

label linjie_encounter:
    scene office_area with fade:
        zoom 2
    
    "{i}你继续整理工位。{/i}"
    
    show linjie_00_shade with moveinright:
        zoom 0.92
        xpos 790
        ypos 200
    '？？' "欢迎。交接文件在共享链接里。10点有个会，别迟到。"
    hide linjie_00_shade with dissolve
    
    "{i}她从你桌边走过，没停步。{/i}"
    
    menu:
        "好的，谢谢！":
            jump linjie_response_a
            
        "默默点头":
            jump linjie_response_b
            
        "期待开会。":
            jump linjie_response_c

# 选项A：积极
label linjie_response_a:
    s "好的，谢谢！"
    
    "{i}她脚步微顿，但没回头，继续走了。{/i}"

    $ linjie_interest += 1
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项B：冷淡
label linjie_response_b:
    "{i}你默默点头。{/i}"
    
    "{i}她似乎没注意到，径直走远了。{/i}"
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项C：职业（触发隐藏记录）
label linjie_response_c:
    s "期待开会。"
    
    show linjie_00_shade with dissolve:
        zoom 0.92
        xpos 790
        ypos 200
    "{i}她停住，微微转身。{/i}"
    
    '？？' "是吗。"
        
    hide linjie_00_shade with dissolve
    show black with dissolve
    "{i}她走了。{/i}"
    
    $ linjie_interest += 1

    
    # 隐藏记录提示（仅开发者可见，玩家看不到）
    # [林姐兴趣度：低但不为零]
    
    jump task_1_3

# ========== 任务1.3：第一个任务 ==========
label task_1_3:
    show meeting_room with fade:
        zoom 1.45
        yalign 0.6
    
    "{i}上午10点，C会议室。{/i}"
    "{i}日光灯嗡嗡响。8个人围坐。你比最年轻的至少小10岁。{/i}"
    
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 681
        ypos 162
    chen "各位早。快速更新——我们拿下了那个新IP项目。对方是大厂，这可是咱们翻身的机会。"
    hide chen_01_normal

    show chen_02_smile_front with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 687
        ypos 162
    chen "给新人一些机会。小曼，你来负责竞品游戏的拆解分析。"
    
    menu:
        "太好了！":
            $ mental = mental + 2 if 'mental' in globals() else 2
            jump task_response_a
            
        "我会尽力的。":
            jump task_response_b
            
        "具体要拆解哪些部分？":
            jump task_response_c

# 选项A：积极
label task_response_a:
    show chen_02_smile_front with move:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160

    show she_05_happy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "太好了！"

    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1342
        ypos 159
    chen "有干劲是好事。林姐会带你入门。"

    hide she_05_happy onlayer top
    
    scene black with dissolve
    jump after_task_assignment

# 选项B：谦虚
label task_response_b:
    show chen_02_smile_front with move:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160

    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我会尽力的。"
    
    chen "嗯，有问题找林姐。她经验很丰富。"

    hide she_03_tinysmile_eye onlayer top

    scene black with dissolve
    jump after_task_assignment

# 选项C：谨慎（特殊剧情）
label task_response_c:
    show chen_02_smile_front with move:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160

    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "具体要拆解哪些部分？"
    
    show she_02_sweat_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}桌边有人轻笑。{/i}"
    "{i}不是恶意，但……只有你不知道。{/i}"

    hide chen_02_smile_front
    show chen_02_smile:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 162
    chen "好问题。林姐会带你。就是市面上那几款头部二次元游戏，美术风格、养成线、付费点设计……那些有趣的东西。"
    show chen_03_narroweyes:
        zoom 0.9
        xzoom -1.0
        xpos 1358
        ypos 162
    chen "别担心，我选你是有理由的。我看过你毕设，那些角色设计很有灵气。"
    hide she_03_tinysmile_eye onlayer top
    hide she_02_sweat_eye onlayer top

    scene black with dissolve
    jump after_task_assignment

# 任务分配后
label after_task_assignment:
    scene meeting_room with fade:
        zoom 1.45
        yalign 0.6
    
    "{i}会议结束，大家都收拾东西离开了。{/i}"
    
    show linjie_04_frown with dissolve:
        zoom 0.92
        xpos 790
        ypos 200
    
    linjie "他总把不可能的任务扔给新人。那几个竞品项目？每个都是几百人的大团队做了三年。你要一个人拆完？别累死自己。"
    
    menu:
        "谢谢提醒，我会注意的。":
            jump linjie_after_a
            
        "我能搞定。在学校我拆过很多游戏。":
            jump linjie_after_b
            
        "为什么不可能？不是有分析框架吗？":
            jump linjie_after_c

# 会后选项A：感激
label linjie_after_a:
    show linjie_04_frown with move:
        zoom 0.92
        xpos 1450
        ypos 200

    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "谢谢提醒，我会注意的。"
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "嗯。"
    
    hide she_03_tinysmile_eye onlayer top
    $ task_assigned = True
    $ linjie_interest += 1
    
    jump chapter1_end

# 会后选项B：自信（林姐认可）
label linjie_after_b:
    show linjie_04_frown with move:
        zoom 0.92
        xpos 1450
        ypos 200

    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我能搞定。在学校我拆过很多游戏。"
    
    linjie "…………"
    show linjie_05_interested with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "行，有骨气。需要帮忙找我。"
    
    hide she_03_tinysmile_eye onlayer top
    $ task_assigned = True
    $ linjie_interest += 1
    
    jump chapter1_end

# 会后选项C：好奇
label linjie_after_c:
    show linjie_04_frown with move:
        zoom 0.92
        xpos 1450
        ypos 200

    show she_06_surprise_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "为什么不可能？不是有分析框架吗？"
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "……框架是框架，执行是执行。你以后会明白的。"
    
    hide she_06_surprise_eye onlayer top   
    $ task_assigned = True
    
    jump chapter1_end

# 1.3结束标记
label chapter1_end:
    scene bg desk_area with fade
    
    "{i}你回到工位，看着电脑屏幕上打开的共享文件夹。{/i}"
    "{i}你证明自己的第一个任务，开始了。{/i}"
    
    # 此处可跳转到下一章节
    # jump chapter1.4
    

# ========== 任务1.4：第一次加班 ==========
# 触发：入职第5天，晚上10:47

default fatigue = 0
default family_pressure = 0
default mother_anger = 0
default car_ride = False
default xiaohongshu_contact = False

label task_1_4:
    scene office_desk with fade
    
    "{i}入职第5天，晚上10:47{/i}"
    "{i}晚上的办公室不一样。更安静。自动售货机的嗡嗡声更响。{/i}"
    
    call mini_game_analysis
    
    $ fatigue = 50
    
    if fatigue > 60:
        n "好想睡觉……"
    if fatigue > 40:
        n "这个抽卡概率曲线怎么算都不对……"
    if fatigue > 30:
        n "明天还要早会……"
    
    n "但做不完的话，陈总会不会觉得我不行？"
    
    "{i}你趴在桌上想着，耳边传来一阵脚步声。细听时，脚步声停了。{/i}"
    
    show chen normal at center with dissolve
    
    chen "还在？我刚才在楼上审方案，看到你们这层灯还亮着。"
    
    "{i}他把一杯咖啡放你桌上。{/i}"
    
    chen "给。楼下便利店的美式，不知道你喝不喝得惯。"
    
    menu:
        "谢谢陈总。":
            jump overtime_response_a
            
        "不用这么客气。":
            jump overtime_response_b
            
        "我快做完了。":
            jump overtime_response_c

label overtime_response_a:
    s "谢谢陈总。"
    chen "别客气。"
    jump chen_conversation

label overtime_response_b:
    s "不用这么客气。"
    "{i}陈永仁笑了笑，没说话。{/i}"
    jump chen_conversation

label overtime_response_c:
    s "我快做完了。"
    chen "效率挺高啊。"
    jump chen_conversation

label chen_conversation:
    "{i}陈永仁坐在桌角。{/i}"
    chen "我看过你简历，你的履历顶尖，你可以去任何地方，为什么选这儿？"
    
    menu:
        "别处都不要我。":
            jump chen_honest
            
        "最适合我的技能":
            jump chen_safe
            
        "我想升得快一些。":
            jump chen_ambition

label chen_honest:
    s "别处都不要我。"
    $ mental = mental + 2 if 'mental' in globals() else 2
    show chen normal at center
    "{i}陈永仁表情柔和下来。{/i}"
    chen "我懂。我就是从这个位置开始的——就是这张桌子，20年前。现在你看……"
    "{i}他模糊地往上指了指。{/i}"
    chen "努力工作，留到最后，这就是赢的方法。"
    "{i}他站起来。{/i}"
    chen "别太晚，回家注意安全。"
    "{i}顿了一下。{/i}"
    chen "其实我也要走了……送你一程？"
    jump car_choice

label chen_safe:
    s "这里的岗位和我的专业技能最匹配。"
    chen "嗯，确实。你的拆解能力很强。"
    "{i}他站起来。{/i}"
    chen "别太晚，明天还有早会。"
    chen "……其实我也要走了，送你一程？"
    jump car_choice

label chen_ambition:
    s "我想升得快一些。"
    "{i}陈永仁笑了。{/i}"
    chen "有野心。我喜欢。"
    "{i}他站起来。{/i}"
    chen "别加班太晚。其实我也要走了……送你一程？"
    jump car_choice

label car_choice:
    menu:
        "好，谢谢。":
            $ car_ride = True
            jump car_scene
            
        "不用，我坐地铁。":
            jump reject_car

label car_scene:
    s "好，谢谢。"
    chen "走吧，车在楼下。"
    scene black with fade
    "{i}车内很干净，有淡淡的皮革味。{/i}"
    "{i}陈永仁放了一首老歌。你们都没说话。{/i}"
    "{i}他在你公寓楼下停车。{/i}"
    chen "明天见，好好休息。"
    jump task_1_4_end

label reject_car:
    s "不用，我坐地铁。"
    chen "随你。明天见。"
    hide chen normal with moveoutright
    "{i}走了。{/i}"
    "{i}你看着他离开，胸口有什么东西松开了，不知道为什么。{/i}"
    jump task_1_4_end

label task_1_4_end:
    scene office_desk with fade
    "{i}任务完成。{/i}"
    #"{i}解锁：深夜办公室探索{/i}"
    jump task_1_5

label mini_game_analysis:
    "{i}你需要完成三款游戏的竞品拆解。{/i}"
    #设置游戏ABC的图片 --> 提示玩家拆解方向
    
    menu:
        "游戏A的核心付费点是？"
        "月卡订阅":
            $ temp_score = 1
        "抽卡保底":
            $ temp_score = 1
        "皮肤直售":
            $ temp_score = 0
    
    menu:
        "游戏B的主要留存机制是？"
        "每日签到":
            $ temp_score += 1
        "社交公会":
            $ temp_score += 1
        "剧情解锁":
            $ temp_score += 0
    
    menu:
        "游戏C的美术风格属于？"
        "写实3D":
            $ temp_score += 0
        "二次元赛璐璐":
            $ temp_score += 1
        "像素复古":
            $ temp_score += 0
    
    if temp_score >= 2:
        "{i}拆解完成。数据已保存。{/i}"
    else:
        "{i}部分数据存疑，但先这样吧。{/i}"
        $ fatigue += 20
    
    return

# ========== 任务1.5：家庭税 ==========
define mom = Character("妈妈")
label task_1_5:
    scene home with fade
    "{i}第2周，周日下午。{/i}"
    
    #增加手机画面，这部分screen可能要重做
    mom "第一个月的工资。什么时候发？"
    
    menu:
        "两周后。":
            jump salary_truth
            
        "快了。":
            jump salary_vague
            
        "问这干嘛？":
            jump salary_defensive

label salary_truth:
    s "两周后。"
    mom "好。你弟弟要换新校服，还有学校旅行要交钱，1200块钱。这钱就你出吧？你现在可是有大工作的人了。"
    jump family_money_choice

label salary_vague:
    s "快了。"
    mom "到底是多快？你弟弟要换新校服，还有学校旅行要交钱，1200块钱。你能出吧？"
    jump family_money_choice

label salary_defensive:
    s "问这干嘛？"
    mom "怎么，翅膀硬了？你弟弟要换新校服，还有学校旅行要交钱，1200块钱。家里手头紧，你帮衬一下怎么了？"
    $ family_pressure += 1
    jump family_money_choice

label family_money_choice:
    menu:
        "好。":
            jump give_money
            
        "那是我一半伙食费。": #不，这里得改，香港一个月1200的房租也太便宜了
            jump argue_start
            
        "沉默":
            jump stay_silent

label give_money:
    s "好。"
    $ money -= 600
    $ family_pressure += 1
    mom "乖。就知道你懂事。弟弟会谢谢你的。"
    "{i}-1200元。当前余额：[money]元{/i}"
    jump task_1_5_end

label stay_silent:
    s "……"
    mom "你不说话是什么意思？算了，等你发工资再说吧。"
    "{i}心头涌现一阵内疚。{/i}"
    $ mental = mental - 1 if 'mental' in globals() else -1
    jump task_1_5_end

label argue_start:
    s "那是我一半吃饭钱。" #同步修改
    mom "我们这么多年白养你的？他是你亲生弟弟，家人帮家人。到时候班上就他一个穿不起鞋，你弟弟得遭人看低的！"
    call argue_minigame
    jump task_1_5_end

label argue_minigame:
    "{i}争吵开始了……{/i}"
    $ mother_anger = 30
    
    menu:
        "我也有我自己的生活……":
            $ mother_anger += 20
        "他的鞋凭什么我负责？我买鞋他穿，我没饭吃他管不管？":
            $ mother_anger += 30
        "我会给，别再这么说了。":
            $ mother_anger += 10
    
    if mother_anger >= 50:
        "{i}妈妈怒气冲冲地挂了电话。{/i}"
        "{i}几天后，她发来消息，像什么都没发生。但你记得。{/i}"
    else:
        "{i}你勉强稳住了局面，保住了钱，但心里空落落的。{/i}"
    
    return

label task_1_5_end:
    "{i}手机随后震动。{/i}"
    '小紫书-你的粉丝'"姐妹，看到你发家里要钱的事了。同款遭遇，你不是一个人。"
    $ xiaohongshu_contact = True
    "{i}新联系人：小紫书姐妹{/i}"
    jump task_1_6

# ========== 任务1.6：不经意的触碰 ==========

label task_1_6:
    scene tea_room with fade
    "{i}第3周，工作日。{/i}"
    "{i}你伸手拿杯子时，有人从你上方伸过手来。{/i}"
    
    show chen normal at center with dissolve
    
    chen "抱歉，我也拿……哦，你也在泡咖啡？"
    "{i}他站得很近。比必要近。{/i}"
    "{i}他拿糖的时候手臂擦过你。{/i}"
    
    menu:
        "观察他的表情":
            "{i}他在笑。{/i}"
            jump touch_reaction
            
        "观察他的手":
            "{i}他的手放在台面上，离你的手只有几寸。{/i}"
            jump touch_reaction
            
        "注意自己的感受":
            jump touch_reaction

label touch_reaction:
    menu:
        "没什么，就是有点挤。":
            jump touch_ignore
            
        "他为什么站这么近？":
            jump touch_alert
            
        "稍微挪开一点":
            jump touch_move

label touch_ignore:
    s "没什么，就是有点挤。"
    "{i}你继续泡咖啡。{/i}"
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label touch_alert:
    s "……"
    "{i}你在心里问自己：他为什么站这么近？{/i}"
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label touch_move:
    "{i}你稍微往旁边挪了一步。{/i}"
    "{i}陈永仁没明显反应。但你一动，他眼神扫了你一下。{/i}"
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label task_1_6_end:
    hide chen normal with moveoutright
    "{i}他走了，你一个人对着茶杯发呆。{/i}"
    
    "{i}手机上林姐发来一条消息{/i}"
    linjie "看到你和陈永仁在茶水间了，注意点。"
    
    menu:
        "什么意思？":
            s "注意什么？"
            linjie "没什么。接完水快回来，有个新的brief发你了。"
            $ linjie_interest += 1
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "没什么事。":
            s "没什么事啊。"
            linjie "……随你。"
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "删除消息":
            "{i}你删掉了这条消息。{/i}"
            $ escape += 1
            scene black with dissolve
            pause 1.0
            jump chapter_2

        "思索":
            s "林姐平常不说这些的，怎么……"
            "{i}你正揣摩这条消息的的意图，斟酌着打下回复，又有新消息发来了。{/i}"
            linjie "接完水快回来，有个新的brief发你了。"
            $ linjie_interest += 1
            scene black with dissolve
            pause 1.0
            jump chapter_2


# 定义变量
default salary_checked = False
default salary_evidence = False
default fitness_video_watched = False
default investigation_unlocked = False
default investigation_skill = 0

# 工资条界面
screen payslip_screen():
    modal True
    
    # 背景遮罩
    add Solid("#000000cc")
    
    # 工资条主体
    frame:
        xalign 0.5
        yalign 0.3
        xsize 500
        ysize 800
        background "#4d4d4d"
        padding (30, 30)
        
        vbox:
            spacing 12

            # 标题
            text"工资条" size 28
            
            null height 20
            
            # 基本信息
            hbox:
                text"姓名："
                text"佘小曼"
            hbox:
                text"部门："
                text"设计部"
            hbox:
                text"日期："
                text"2028年3月"
            
            null height 20
            
            # 工资明细（可点击展开）
            vbox:
                spacing 10
                
                # 基本工资
                hbox:
                    xfill True
                    text"基本工资"
                    text"16,500" xalign 1.0
                
                # 绩效工资（悬停效果）
                button:
                    xfill True
                    action NullAction()
                    background None
                    
                    hbox:
                        xfill True
                        text"绩效调整"xalign -0.07
                        text"0" xalign 1.05
                    
                    # 悬停提示
                    tooltip "无说明"
                    
                    hovered Show("payslip_tooltip", msg="无说明")
                    unhovered Hide("payslip_tooltip")
                
                # 其他项目
                hbox:
                    xfill True
                    text"交通补贴"
                    text"500" xalign 1.0
                
                hbox:
                    xfill True
                    text"餐补"
                    text"500" xalign 1.0
            
            null height 10
            
            # 分隔线
            add Solid("#cccccc") xsize 440 ysize 1
            
            null height 10
            
            # 实发工资（可点击心算对比）
            button:
                xfill True
                action [SetVariable("salary_checked", True), Show("salary_calc")]
                background None
                
                hbox:
                    xfill True
                    text"实发工资" xalign -0.07
                    text"17,500" xalign 1.05
                
                if not salary_checked:
                    text"（开始心算对比）" size 12 xalign 1.03 yalign 0.3
            

            null height 30
            
            # 关闭按钮
            textbutton "关闭":
                xalign 0.5
                action If(salary_checked, 
                    [Hide("payslip_screen"), Jump("call_lin_sister")],
                    [Hide("payslip_screen"), Jump("salary_ignore")])
                background "#3498db"
                padding (30, 10)
                text_color "#ffffff"


# 悬停提示界面
screen payslip_tooltip(msg):
    frame:
        pos (1000, 450)
        background "#2c3e50"
        padding (10, 5)
        
        text msg color "#ffffff" size 20

# 心算弹窗（可选的详细说明）
screen salary_calc():
    modal True
    # 物品描述屏幕，添加自动跳转逻辑

    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50

        vbox:
            xsize 600
            ysize 200

            text"正常应该是：" size 24
            null height 30
            text"16,500 + 2,000 + 500 + 500 = 19,500" size 24 xalign 0.5
            text"↑" size 25 xalign 0.395
            null height 20
            # 分隔线
            add Solid("#cccccc") xsize 600 ysize 1 xalign 0.5
            null height 30
            text"我的绩效调整被扣发了，没有附带任何原因说明。" size 24 xalign 0.5
            null height 50
            textbutton "×":
                xalign 0.5
                yalign 0.55
                xpadding 5
                ypadding 3
                action Hide("salary_calc")
                text_color "#ffffff"
                background "#3498db"


label chapter_2:
    image chapter2_title = ParameterizedText(xalign=0.5, yalign=0.45, size=108)
    show chapter2_title "Chapter 2 裂缝"
    with fade
    pause 2
    hide chapter2_title
    
# 工资条剧情
label payslip_event:
    scene bedroom_night #后期改
    pause 0.5

    s "看看这个月努力的成果吧！" 
    window hide
    
    show screen payslip_screen
    # 等待玩家交互
    $ ui.interact()
    
    # if not salary_checked:
    #     s "数目怎么不太对劲？"
    #     show screen payslip_screen
    #     $ ui.interact()
    
    jump call_lin_sister

label salary_ignore:
    s "有点少啊……"
    s "不过也还可以了，下个月继续努力吧。"
    $ escape += 1
    jump fitness_video_event

# 打电话给林姐
label call_lin_sister:
    scene bg bedroom_night
    with dissolve

    s "数目怎么不太对劲？"
    
    s "怎么会这样……我得找人问明白。"

    "{i}【电话联系人 林姐】 拨号中……{/i}"
    "{i}*……嘟嘟……*{/i}"
    
    s "林姐，不好意思打扰你了——我发现自己的工资条好像不太对？"

    linjie "…………………………"
    
    linjie "你查过男新人的起薪吗？"
    
    s "……什么？"
    
    linjie "小金当初进公司时和你同岗位，问他当时拿多少。"

    "{i}电话挂断了。{/i}"
    "{i}你握着手机，心跳得有点快。{/i}"

    menu:
        "直接问小金":
            jump ask_xiaojin_directly
        
        "不问":
            jump dont_ask_xiaojin
        
        "自己进行调查":
            jump investigate_other_ways

# 选项A：直接问小金
screen clue_unequal_wage:
    modal True
    
    frame:
        xalign 0.5
        yalign 0.45
        xpadding 80
        ypadding 60
 
        vbox:
            xalign 0.5
            yalign 0.5
            text "【线索】阴阳工资" size 28
            null height 30
            add Solid("#cccccc") xsize 600 ysize 1
            null height 30
            text "天与地，阴与阳；她与他，阴与阳" size 24 xalign 0.5
            null height 40
            
            textbutton "收起":
                text_size 24
                xalign 0.5    
                # 关键：使用Return()结束call screen
                action [Hide("clue_unequal_wage"), Return()]

label ask_xiaojin_directly:
    scene bg office_day
    with fade
    
    "{i}第二天午休，你找到了小金。{/i}"
    
    s "小金，能问你个事吗？你当时刚入职的时候起薪是多少？"
    
    show xiaojin awkward
    
    xiaojin "呃……这个……"
    xiaojin "22.5k……公司不让互相问工资来着，你别跟别人说啊。"
    xiaojin "出什么事了，突然说起这个？"
    
    s "我19.5k。"
    
    show xiaojin shocked
    xiaojin "Oh shit……"
    hide xiaojin
    
    # 任务更新界面
    call screen clue_unequal_wage("线索") with dissolve
    
    "{i}获得了线索：阴阳工资{/i}" #加音效：噔噔噔↑
       
    $ salary_evidence = True
    $ investigation_unlocked = True
    $ linjie_interest += 1
    
    jump fitness_video_event

# 选项B：不问
label dont_ask_xiaojin:
    scene bg bedroom_night with dissolve
    
    "{i}等心跳没那么快时，你放下了手机。{/i}"
    
    s "不问，就不会尴尬。不问，就不会惹麻烦。"

    "{i}你起身去洗漱，仿佛什么都没发生。{/i}"
    "{i}涟漪过后，风平浪静。涟漪下有没有更深的漩涡……{/i}"
    "{i}谁知道呢。{/i}"
    $ escape += 1 
    
    jump fitness_video_event

# 选项C：其他方式调查
label investigate_other_ways:
    scene bg bedroom_night
    with dissolve
    
    s "还是先自己查查看吧。"
    
    "【正在浏览】{i}公司招聘网站：公司同岗位的薪资范围{/i}"
    "【正在浏览】{i}内部文档：薪酬制度细则{/i}"
    "【正在浏览】{i}匿名论坛：公司薪资讨论版块{/i}"

    call screen clue_unequal_wage("线索") with dissolve
    "{i}获得了线索：阴阳工资{/i}" #加音效：噔噔噔↑

    $ investigation_unlocked = True
    
    "{i}在调查中你发现很多资料来自和你有相似经历的前辈。{/i}"
    "{i}坏消息，走到这条路上的不止你一个人。{/i}"
    "{i}好消息是，走在这条路上的不止你一个人。{/i}"

    $ investigation_skill += 1
    $ linjie_interest += 1

    jump fitness_video_event

# 健身视频事件
label fitness_video_event:
    scene bg bedroom_night
    with fade
    
    "{i}第6周 周六，晚{/i}"
    "{i}你躺在床上刷手机，但眼皮已经开始打架。{/i}"
    
    #微信消息提示音音效，接手机界面
    show phone_screen_time:
        zoom 1.5
        xalign 0.5
        yalign 0.35#锁屏时间
    s "23:47，竟然已经这么晚了。"

    s "有陈总的消息……"

    hide phone_screen_time
    show phone_pyq with pixellate:
        zoom 1.5
        xalign 0.5
        yalign 0.35
    "{i}【陈总】刚健完身，我发在朋友圈的技巧你可以试试，用来解压很不错。{/i}"
    # show screen phone_notification("陈永仁", "【视频】刚健完身。你可以试试这个，用来解压很好！")
    # with dissolve
        
    menu:
        "看视频":
            jump watch_fitness_video
        
        "忽略视频":
            jump ignore_video
        
        "点赞视频":
            jump reply_thumb_up

# 手机通知界面
# screen phone_notification(sender, msg):
#     frame:
#         xalign 0.5
#         ypos 100
#         xsize 350
#         background "#ffffff"
#         padding (15, 15)
        
#         vbox:
#             spacing 8
            
#             hbox:
#                 text sender bold True
#                 text " 微信" size 12
                
#             text msg size 14
            
#             null height 5
            
#             hbox:
#                 xalign 1.0
#                 text "现在" color "#999999" size 12

# 选项A：看视频
transform rotate_right:
    align(0.5, 0.4)
    rotate 0
    alpha 1.0

    linear 0.8 align(0.5, 0.4) rotate -90 alpha 0.0 

transform chen_video_1:
    on show:
        zoom 1.1
        align (-0.5, 0.5)
        alpha 0.0
        linear 0.8 align(0.5, 0.5) alpha 1.0

    on hide:
        align (0.5, -0.5)
        linear 0.5 align(-0.5, 1.5) alpha 0.0

transform chen_video_2:
    on show:
        zoom 1.1
        align (0.5, -1.0)
        alpha 0.0
        pause 0.8
        linear 1.2 align(0.5, 0.5) alpha 1.0

    on hide:
        align (0.5, -0.5)
        linear 0.5 align(-0.5, 1.5) alpha 0.0

transform chen_video_3:
    on show:
        zoom 1.1
        align (1.5, 0.5)
        alpha 0.0
        pause 1.3
        linear 1.2 align(0.5, 0.5) alpha 1.0

    on hide:
        align (0.5, -0.5)
        linear 0.5 align(10.5, 0.5) alpha 0.0

label watch_fitness_video:
    show phone_pyq at rotate_right #后续改这个
    pause 0.5
    scene black with fade
    show gym_01 at chen_video_1:
        zoom 0.5
    show gym_02 at chen_video_2:
        zoom 0.5
    show gym_03 at chen_video_3:
        zoom 0.5
    # 模拟视频播放界面
    # show screen video_player("chen_fitness")
    # with dissolve

    "30秒。陈永仁在健身房，器械的金属光泽映着他的汗水。"
    
    "他做着标准的动作，肌肉随着呼吸起伏。"
    
    "最后一秒，他突然直视镜头。"
    
    chen "你能跟上吗，小曼？"
    
    "他眨了眨眼。"
    
    "视频结束，黑屏。你的脸也黑了。"
    
    # hide screen video_player
    # with dissolve
    
    # $ fitness_video_watched = True
    
    s "呃…………（有某种不适感在胃里蔓延）"
    
    jump after_video

# 视频播放器界面
screen video_player(video_id):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 640
        ysize 360
        background "#000000"
        
        # 模拟视频内容
        vbox:
            xalign 0.5
            yalign 0.5
            
            if video_id == "chen_fitness":
                text "📹 健身视频播放中..." color "#ffffff" size 20
                null height 20
                text "00:15 / 00:30" color "#ffffff" size 14
                null height 10
                add Solid("#333333") xsize 400 ysize 5
                
                # 进度条
                hbox:
                    add Solid("#07c160") xsize 200 ysize 5
                    add Solid("#555555") xsize 200 ysize 5
        
        # 播放控制
        hbox:
            xalign 0.5
            ypos 320
            spacing 20
            
            text "⏮" color "#ffffff" size 24
            text "⏸" color "#ffffff" size 24
            text "⏭" color "#ffffff" size 24

# 选项B：忽略
label ignore_video:
    scene bg bedroom_night
    with dissolve
    
    "你锁屏，把手机倒扣在床头柜上。"
    
    "11:47。这个时间，这个内容。"
    
    "你的直觉告诉你，有些东西不需要打开。"
    
    "手机又震了一下，但你没有看。"
    
    #选择安全，但错过了观察对方行为模式的机会
    
    jump celebration_drink

# 选项C：回赞
label reply_thumb_up:
    scene bg bedroom_night
    with dissolve
    
    "你回复了一个👍。"
    
    chen "这么晚还没睡？"
      
    "消息秒回。你看着那个正在输入的提示，决定不再回复。"
    
    #保持了表面和平，但对方可能认为这是个信号）
    
    jump celebration_drink

# 视频事件后续
label after_video:
    scene bg_office_floor
    with fade

    "{i}第二天办公室，午餐时。{/i}"
    s "哎，你昨晚看到陈总朋友圈的健身视频没？真有点东西。"
    xiaojin "我好像没看到耶？可能没刷到吧。"
    s "……哦，这样啊。"
    
    jump celebration_drink


# 定义变量
default drink_choice = None  # "beer", "wine", "cocktail", "soft"
default xiaojin_topic = None  # "sport", "work", "love"
default hidden_truth_unlocked = False
default talk_to_xiaojin = False
default sit_with_lin = False
default observe_chen = False
default bar_restroom = False
default bar_menu_choice = False

# 任务2.3：庆功酒
label celebration_drink:
    scene bg bar_night
    with fade
    
    "第7周，His Game项目成功上线。"
    "数据表现超过预期，部门办庆功酒，酒水畅饮，陈永仁买单。所有人都来了。"
    
    # 初始化酒吧场景
    jump bar_interaction

# 酒吧交互界面
screen bar_scene():
    add "bg bar_night"
    
    frame:
        xalign 0.5
        ypos 20
        background "#00000080"
        padding (20, 10)
        text "Nine Bar" size 30 bold True xalign 0.1

    # 1. 酒单（左侧）
    button:
        xpos 100
        ypos 200
        xsize 120
        ysize 150
        background "#8b4513"
        hover_background "#a0522d"
        action Jump("bar_menu_choice")

        vbox:
            xalign 0.5
            yalign 0.5
            text "🍷" size 40 xalign 0.5
            text "酒单" size 16 xalign 0.5
    
    # 2. 小金（大声聊天区域）
    button:
        xpos 300
        ypos 250
        xsize 140
        ysize 120
        background "#2e8b57"
        hover_background "#3cb371"
        #action Jump("talk_to_xiaojin")
        action If(talk_to_xiaojin, Jump("talk_to_xiaojin_again"), Jump("talk_to_xiaojin"))

        vbox:
            xalign 0.5
            yalign 0.5
            text "💬" size 35 xalign 0.5
            text "小金" size 16 xalign 0.5
            text "(大声聊天)" size 12 xalign 0.5
        
    # 3. 林姐（角落卡座）
    button:
        xpos 550
        ypos 180
        xsize 130
        ysize 130
        background "#4a4a4a"
        hover_background "#696969"
        action If(sit_with_lin, Jump("sit_with_lin_again"), Jump("sit_with_lin"))
        
        vbox:
            xalign 0.5
            yalign 0.5
            text "🪑" size 35 xalign 0.5
            text "林姐" size 16 xalign 0.5
            text "(角落卡座)" size 12 xalign 0.5
    
    # 4. 陈永仁（中心位置）
    button:
        xpos 400
        ypos 350
        xsize 140
        ysize 140
        background "#8b0000"
        hover_background "#a52a2a"
        action If(observe_chen, Jump("observe_chen_again"), Jump("observe_chen"))
        
        vbox:
            xalign 0.5
            yalign 0.5
            text "👔" size 40 xalign 0.5
            text "陈永仁" size 16 xalign 0.5
            text "(中心位置)" size 12 xalign 0.5
    
    # 5. 洗手间（逃离）
    button:
        xpos 650
        ypos 100
        xsize 100
        ysize 100
        background "#4682b4"
        hover_background "#5f9ea0"
        action If(bar_restroom, Jump("bar_restroom_again"), Jump("bar_restroom"))
        
        vbox:
            xalign 0.5
            yalign 0.5
            text "🚻" size 30 xalign 0.5
            text "洗手间" size 14 xalign 0.5

# 酒吧交互主循环
label bar_interaction:
    show screen bar_scene
    "酒吧里人声鼎沸。你想做什么？"
    $ ui.interact()

# 检查函数 - 统一检查所有条件
label check_all_bar_conditions:
    if talk_to_xiaojin and sit_with_lin and observe_chen and bar_restroom and bar_menu_choice:
        jump bar_ending
    else:
        jump bar_interaction

# 酒单选择
label bar_menu_choice:
    hide screen bar_scene
    
    menu:
        "你拿起酒单，选择："
        
        "啤酒（轻松）":
            $ drink_choice = "beer"
            "你点了一杯精酿啤酒，泡沫细腻。"
            
        "红酒（正式）":
            $ drink_choice = "wine"
            "红酒在杯中摇晃，颜色深沉。"
            
        "鸡尾酒（冒险）":
            $ drink_choice = "cocktail"
            "五颜六色的液体，不知道里面有什么。"
            
        "软饮（清醒）":
            $ drink_choice = "soft"
            "可乐加冰，气泡刺激着喉咙。你保持清醒。"
    
    $ bar_menu_choice = True
    jump check_all_bar_conditions

# 和小金聊天 - 修复：简化结构，确保变量设置正确
label talk_to_xiaojin:
    hide screen bar_scene
    scene bg bar_table
    
    "小金正在大声说着什么，周围几个人在笑。"
    
    menu:
        "加入话题："
        
        "运动":
            $ xiaojin_topic = "sport"
            xiaojin "你来啦？对了，前几天你问我陈总朋友圈是……"
            s "哦，偶然看到，就打算试试健身。你有没有什么健身经验分享的？"
            xiaojin "有啊！我跟你说，蛋白粉就要选……"
            "{i}他把自己的健身心得倾囊相授，真是个好人。{/i}"
            
        "吐槽工作":
            $ xiaojin_topic = "work"
            s "这个项目真是累死了……"
            xiaojin "对吧！有时候觉得AI取代不了我们，因为根本读不懂甲方七零八落的诉求。"
            "{i}你们一起吐槽了半小时甲方，英雌惜英雄。{/i}"
            
        "恋爱话题":
            $ xiaojin_topic = "love"
            xiaojin "你知道最近隔壁部门小x的男朋友和她冷战不？"
            s "嗯？新瓜，细说。"
            xiaojin "小x和男朋友恋爱挺久了，最近她男朋友求婚，但是小x想这几年多专注在事业，往后推推。"
            xiaojin "她男朋友觉得求婚被拒，正沮丧，等着小x哄中……"
            s "那他可得等等了，小x手上的项目后天才交呢。小x姐，女王。"
            xiaojin "小x姐，女王！"

    # 关键修复：在menu结束后统一设置变量
    $ talk_to_xiaojin = True
    $ xiaojin_interest += 1
    jump check_all_bar_conditions

label talk_to_xiaojin_again:
    "{i}小金还在和其他人聊天，插不进话。{/i}"
    jump check_all_bar_conditions

# 和林姐坐一起（关键剧情）- 关键修复：使用call screen而不是show screen
screen clue_moderec:
    modal True
 
    frame:
        xalign 0.5
        yalign 0.45
        xpadding 80
        ypadding 60
 
        vbox:
            xalign 0.5
            yalign 0.5
            text "【线索】模式识别" size 28
            null height 30
            add Solid("#cccccc") xsize 600 ysize 1
            null height 30
            text "你开始明白，这不是偶然。" size 24 xalign 0.5
            null height 40

            textbutton "收起":
                text_size 24
                xalign 0.5
                # 关键：使用Return()结束call screen
                action [Hide("clue_moderec"), Return()]

label sit_with_lin:
    hide screen bar_scene
    
    scene bg bar_corner
    with dissolve
    
    "{i}角落的卡座，林姐一个人坐在那里，光影在她脸上切割出明与暗。{/i}"
    
    linjie "你做得太好了。好得过头了。"
    s "什么意思？"
    linjie "作为新人，陈永仁很中意你——非常中意。"
    "{i}她晃了晃酒杯，冰块碰撞发出清脆的声响。{/i}"
    linjie "他也这样注意过我，后来就不了。"
    s "……发生了什么？"
    "{i}酒有些辣，林姐长饮一口，好一会儿才说话。{/i}"
    linjie "我老了，对他来说，现在我只是有用。"
    "{i}她没有回答你的问题，像是醉了。{/i}"
    linjie "去别的地方转转吧，别和我一样。"

    scene black
    with dissolve
    pause 1.0

    linjie "哎——"
    linjie "别认为“在他眼里我很特别”。”"
    linjie "你本来就特别。"
    linjie "不是因为他。"
    
    $ sit_with_lin = True
    $ hidden_truth_unlocked = True
    
    # 关键修复：使用call screen而不是show screen + ui.interact()
    call screen clue_moderec
    
    jump check_all_bar_conditions

label sit_with_lin_again:
    linjie "怎么又回来了？让我一个人待会儿，你出去转转吧。"
    jump check_all_bar_conditions

# 观察陈永仁
label observe_chen:
    hide screen bar_scene
    
    show chen_looking_others
    "{i}你站在人群边缘，看着陈永仁。{/i}"
    "{i}他对男同事：拍肩、大笑、讲黄色笑话。{/i}"
    "{i}他对女同事：靠近、倾听、眼神专注。{/i}"
    "{i}他对上级：谦卑、递烟、不时倒酒。{/i}"
    hide chen_looking_others

    show chen_smile
    "{i}他时不时看向你，微笑。{/i}"
    hide chen_smile with dissolve

    "{i}他总能根据不同对象，切换最佳模式。{/i}"
    
    $ observe_chen = True
    $ investigation_skill += 1
    jump check_all_bar_conditions

label observe_chen_again:
    "{i}他还在和人推杯换盏……{/i}"
    jump check_all_bar_conditions

# 洗手间逃离
label bar_restroom:
    hide screen bar_scene
    
    scene bg restroom_mirror
    with fade
    
    "{i}躲进洗手间锁上门，外面的说话声、碰杯声离你远去了。{/i}"
    "{i}你看着镜子里的自己，脸颊微红。{/i}"
    "{i}*嗡* 你的手机屏幕亮了。{/i}"
    "【微信】{i}妈：「你什么时候回家？」{/i}"
    "【微信】{i}闺蜜：「那个项目怎么样了？」{/i}"
    "{i}你深吸一口气，现在你暂时逃离了那个世界。{/i}"
    "{i}但你知道，总得回去，过明天。{/i}"

    $ bar_restroom = True
    jump check_all_bar_conditions

label bar_restroom_again:
    "{i}洗手间有人，先出去吧。{/i}"
    jump check_all_bar_conditions

# 酒吧结束，进入任务2.4
init python:
    def notice_take_ride(msg1, msg2, duration=1):
        renpy.show_screen("notify_1", message=msg1, duration=duration)
        renpy.pause(duration + 0.3)
        
        renpy.show_screen("notify_2", message=msg2, duration=duration)
        renpy.pause(duration + 0.3)  # 等待最后一个消失
#注意1
screen notify_1(message, duration=1):
    
    frame:
        at transform:
            alpha 0.0
            easein 0 alpha 1.0
            pause duration
            easeout 1 alpha 0.0

        background Frame("gui/textbox.png", 40, 40)
        padding (20, 12)
        xalign 0.5
        yalign 0.4
        
        hbox:
            xalign 0.5
            spacing 8
            text message size 28
#注意2
screen notify_2(message, duration=1):
    
    frame:
        at transform:
            alpha 0.0
            easein 0.5 alpha 1.0
            pause duration
            easeout 0.5 alpha 0.0
        
        background Frame("gui/textbox.png", 40, 40)
        padding (20, 12)
        xalign 0.5
        yalign 0.45

        hbox:
            spacing 8
            text message size 28

default car_event = False

label bar_ending:
    hide screen bar_scene
    
    scene balck #bg street_night
    with fade
    
    "{i}夜深了，大家陆续离开。{i}"
    "{i}凉风吹在脸上，路灯是朦胧的，微醺的感觉。{i}"
    
    s "看看地铁时间……"
    s "啊……末班车还有15分钟到，要过去地铁站时间有点紧啊……"
    
    #音效+图片表示：一辆车滑停在身边，车窗降下
    
    show chen car_smile
    
    chen "上车吧，我们顺路。"
    
    if investigation_skill > 1:
        $ notice_take_ride("他怎么知道顺不顺路？", "他问过我住在哪里吗？")
    else:
        pass
    
    menu:
        "你握着手机，心跳在加速。" #音效
        
        "上车":
            $ car_event == True 
            jump get_in_car
        
        "我坐地铁。":
            jump refuse_car_safe
        
        "你怎么知道我住哪？":
            jump question_chen

# 选项A：上车
label get_in_car:
    hide chen
    
    "{i}拉开车门，坐进副驾驶，你感觉到皮革座椅的冰凉，闻到车内淡淡的古龙水味。{/i}"
    
    chen "系好安全带。"

    jump chapter3

# 选项B：安全拒绝
label refuse_car_safe:
    s "不用了，我坐地铁，挺方便的。"
    
    #"陈永仁的笑容没变，手指敲了敲方向盘。"
    
    chen "末班车快没了，你确定？"
    
    s "我赶得上，谢谢陈总。"
    
    "{i}你后退一步，点头致谢。{/i}"
    
    #音效+图片，车开走
    "{i}黑夜里尾灯消失，光线渐暗，但你感到十分心安。{/i}"
    
    jump safe_ending

# 选项C：质问（压力抉择）
label question_chen:
    s "您怎么知道我住在哪？"
    
    chen "HR档案里记着大家的联络地址，我记得自己手底下所有团队成员的信息。"
    chen "这是关心的方式，就像现在问你要不要搭便车一样。"
    chen "怎么样，走吗？"
   
    menu:
        
        "上车":
            "{i}你意识到继续对峙没有意义。{/i}"
            s "……那麻烦您了。"
            #音效：关车门
            $ car_event == True
            jump get_in_car
        
        "仍然拒绝":
            s "我还是坐地铁吧，谢谢您关心。"
            "{i}背后的沉默像浓重的夜色，但你走得坚定无比。{/i}"
            jump safe_ending

# 尴尬拒绝后续
label safe_ending:
    scene bg subway_night
    with fade
    
    "{i}你冲进地铁站。{/i}"
    
    "{i}末班车还有3分钟。你赶上了。{/i}"
    
    "{i}车厢里空荡荡的，你坐在角落，手还在抖。{/i}"
    
    "{i}*嗡* 你的手机在震动：{/i}"
    chen "注意安全。"
    s "……"
    
    jump chapter_2_end

# chapter 2结束，安全支线
label chapter_2_end:
    scene bg bedroom_night
    with fade
    
    "{i}你终于回到家，锁上门。{i}"
    
    if hidden_truth_unlocked:
        "{i}林姐的话在耳边回响：{/i}"
        "{i}「别让他让你觉得自己特别。」{/i}"
        "{i}这一周结束了，His Game成功了。{/i}"
        "{i}但某种游戏，才刚刚开始。{/i}"
        "{i}游戏的一方是陈永仁，但你隐隐感觉自己不是另一方唯一的执棋人。"
    jump chapter4


# chapter 2接chapter 3，上车后续，危险路径
    
# 定义变量
default chapter4_started = False
default last_night_evidence = False  # 昨晚是否有证据
default xiaojin_concern_response = None  # "overtime", "sleep", "silent"
default digital_evidence_count = 0  # 数字证据收集数量
default physical_evidence_found = []  # 发现的实体证据列表
default office_searched = False

# 任务4.1：办公室12楼
label chapter4:
    $ chapter4_started = True
    
    scene bg office_12f
    with fade
    
    "你走进去。一切看起来一样。"
    "每个人表现一样。"
    "你却觉得自己戴着标签。"
    
    # 陈永仁走廊相遇
    show chen_normal at right
    with dissolve
    
    chen "早啊小曼！昨天那个PPT做得真棒。非常专业。"
    
    "昨天微妙的恶意已经从他眼中消失。"
    "没有一丝迹象表明昨晚发生过什么。"
    
    hide chen_normal with dissolve
    
    # 小金关心
    show xiaojin_concerned at left
    with dissolve
    
    xiaojin "嘿，你脸色不好。昨晚熬夜了？"
    
    menu:
        "加班":
            s "嗯，加班。"
            xiaojin "嗐，我也一样。这地方会害死我们。"
            
        "没睡好":
            s "昨晚没睡好。"
            xiaojin "那你中午好好补个觉，休息下。"
            
        "沉默":
            s "…………" 
            #show image你盯着他，嘴唇抿成一条线。
            xiaojin "……呃，看来是熬懵了？我不打扰了，你好好休息。"
    
    hide xiaojin_concerned with dissolve
    
    s "在证据集齐前，我得装作一切如常。"
    
    jump chapter4_evidence_prep

# 任务4.2准备：选择工具
label chapter4_evidence_prep:
    scene bg bedroom_night
    with fade
    
    "今晚，你要行动。"
    "从卧室带什么工具？"
    
    # 工具选择界面
    call screen evidence_tools_select
    
    "你准备好了。"
    jump digital_evidence_phase

# 工具选择界面
screen evidence_tools_select():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background "#2c3e50"
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "选择携带工具" size 28 color "#ffffff" xalign 0.5
            
            grid 2 2:
                spacing 15
                
                # 工具1：备用手机
                button:
                    xsize 200
                    ysize 150
                    background "#34495e"
                    hover_background "#4a6fa5"
                    action [SetVariable("tool_phone", True), Return()]
                    
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "📱" size 40
                        text "备用手机" size 16 color "#ffffff"
                        text "(截屏专用)" size 12 color "#95a5a6"
                
                # 工具2：录音笔
                button:
                    xsize 200
                    ysize 150
                    background "#34495e"
                    hover_background "#4a6fa5"
                    action [SetVariable("tool_recorder", True), Return()]
                    
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "🎙️" size 40
                        text "录音笔" size 16 color "#ffffff"
                        text "(持续录音)" size 12 color "#95a5a6"
                
                # 工具3：微型摄像头
                button:
                    xsize 200
                    ysize 150
                    background "#34495e"
                    hover_background "#4a6fa5"
                    action [SetVariable("tool_camera", True), Return()]
                    
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "📹" size 40
                        text "微型摄像头" size 16 color "#ffffff"
                        text "(隐蔽拍摄)" size 12 color "#95a5a6"
                
                # 工具4：什么都不带
                button:
                    xsize 200
                    ysize 150
                    background "#7f8c8d"
                    hover_background "#95a5a6"
                    action Return()
                    
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "🚫" size 40
                        text "轻装上阵" size 16 color "#ffffff"
                        text "(风险+)" size 12 color "#bdc3c7"

# 第一阶段：数字证据 - 截屏快手小游戏
label digital_evidence_phase:
    scene bg bedroom_night
    with fade
    
    "第一阶段：数字证据。"
    "翻看所有陈永仁的消息。"
    "警告：他可能会撤回。"
    
    "小游戏：截屏快手"
    "每条消息5秒内截屏，否则消失。"
    
    # 7条消息，每条5秒限时
    $ digital_evidence_count = 0
    
    call screen screenshot_game(msg="在吗", timeout=5.0)
    call screen screenshot_game(msg="昨晚的事别多想", timeout=5.0)
    call screen screenshot_game(msg="你很特别", timeout=5.0)
    call screen screenshot_game(msg="我知道你家在哪", timeout=5.0)
    call screen screenshot_game(msg="别告诉林姐", timeout=5.0)
    call screen screenshot_game(msg="下周单独吃饭", timeout=5.0)
    call screen screenshot_game(msg="你逃不掉的", timeout=5.0)
    
    "截屏完成。获得 [digital_evidence_count]/7 条证据。"
    
    if digital_evidence_count >= 5:
        "足够作为数字证据。"
        $ last_night_evidence = True
    else:
        "证据不足……有些消息被撤回了。"
    
    jump physical_evidence_phase

# 截屏小游戏界面
screen screenshot_game(msg, timeout=5.0):
    modal True
    
    default start_time = renpy.get_game_time()
    default captured = False
    
    # 实时检查时间
    timer 0.05 repeat True action If(
        (renpy.get_game_time() - start_time) >= timeout,
        true=[Hide("screenshot_game"), Return()],
        false=NullAction()
    )
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 300
        background "#ffffff"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            # 微信消息样式
            frame:
                background "#95ec69"
                xpadding 15
                ypadding 10
                xalign 0.5
                
                text msg size 18 color "#000000"
            
            null height 30
            
            # 倒计时显示
            $ remaining = max(0, timeout - (renpy.get_game_time() - start_time))
            text "[remaining:.1f]秒" size 24 color "#e74c3c" xalign 0.5
            
            null height 20
            
            # 截屏按钮
            if not captured:
                textbutton "📸 截屏":
                    xalign 0.5
                    xsize 150
                    ysize 50
                    background "#3498db"
                    hover_background "#2980b9"
                    text_color "#ffffff"
                    action [SetScreenVariable("captured", True), 
                            SetVariable("digital_evidence_count", digital_evidence_count + 1),
                            Show("screenshot_flash")]
            else:
                text "✓ 已截屏" color "#27ae60" size 20 xalign 0.5

# 截屏闪光效果
screen screenshot_flash():
    add Solid("#ffffff")
    timer 0.1 action Hide("screenshot_flash")

# 第二阶段：实体证据
label physical_evidence_phase:
    scene bg office_night
    with fade
    
    "第二阶段：实体证据。"
    "陈永仁的办公室。需要他不在时进去。"
    
    # 检查林姐关系
    if linjie_relationship >= 3:
        "林姐愿意帮忙。"
        jump lure_chen_away
    else:
        "林姐关系不足。无法调虎离山。"
        menu:
            "怎么办？"
            "直接闯（高风险）":
                jump direct_break_in
            "放弃实体证据":
                jump chapter4_end

# 调虎离山
label lure_chen_away:
    scene bg office_corridor
    with fade
    
    "林姐拨通电话。"
    
    linjie "陈总，紧急会议，3楼会议室，马上。"
    
    "陈永仁从办公室出来，快步走向电梯。"
    
    show chen_walking at right
    chen "来了。"
    hide chen_walking
    
    "5分钟。计时开始。"
    
    # 5分钟倒计时搜查
    call screen office_search_timer(duration=300.0)  # 5分钟 = 300秒

label office_search_results:
    scene bg chen_office
    with fade
    
    "搜查结束。你发现了："
    
    # 根据点击发现显示结果
    if "archives" in physical_evidence_found:
        "【旧员工档案】最下抽屉"
        "几个女性员工，都在两年内离职。原因不明。"
    
    if "gift" in physical_evidence_found:
        "【礼盒】书柜顶层"
        "昂贵香水——未拆封。收件人：无。"
    
    if "notebook" in physical_evidence_found:
        "【笔记本】文件堆下"
        "名字、日期、备注：「李哭了。处理好了。」"
    
    if "photo" in physical_evidence_found:
        "【照片】书里夹着"
        "陈永仁和年轻女性——不是他妻子。"
    
    $ office_searched = True
    jump chapter4_end

# 办公室搜查界面（限时）
screen office_search_timer(duration):
    modal True
    
    default start_time = renpy.get_game_time()
    default time_left = duration
    
    # 倒计时
    timer 0.1 repeat True action [
        SetScreenVariable("time_left", max(0, duration - (renpy.get_game_time() - start_time))),
        If(time_left <= 0, true=[Hide("office_search_timer"), Jump("office_search_results")], false=NullAction())
    ]
    
    # 背景
    add "bg chen_office"
    
    # 时间显示
    frame:
        xalign 0.5
        ypos 20
        background "#e74c3c"
        padding (20, 10)
        
        $ minutes = int(time_left // 60)
        $ seconds = int(time_left % 60)
        text "剩余时间：[minutes]:[seconds:02d]" size 24 color "#ffffff" xalign 0.5
    
    # 可搜查区域
    # 1. 最下抽屉
    if "archives" not in physical_evidence_found:
        button:
            xpos 200
            ypos 400
            xsize 120
            ysize 80
            background "#8b4513"
            hover_background "#a0522d"
            action [AddToSet("physical_evidence_found", "archives"), Show("evidence_found_popup", msg="发现旧员工档案")]
            
            text "🗄️ 抽屉" size 20 xalign 0.5 yalign 0.5
    
    # 2. 书柜顶层
    if "gift" not in physical_evidence_found:
        button:
            xpos 500
            ypos 150
            xsize 100
            ysize 100
            background "#d4af37"
            hover_background "#f4d03f"
            action [AddToSet("physical_evidence_found", "gift"), Show("evidence_found_popup", msg="发现礼盒")]
            
            text "🎁" size 40 xalign 0.5 yalign 0.5
    
    # 3. 文件堆
    if "notebook" not in physical_evidence_found:
        button:
            xpos 400
            ypos 350
            xsize 150
            ysize 100
            background "#95a5a6"
            hover_background "#bdc3c7"
            action [AddToSet("physical_evidence_found", "notebook"), Show("evidence_found_popup", msg="发现笔记本")]
            
            text "📄 文件堆" size 18 xalign 0.5 yalign 0.5
    
    # 4. 书架上的书
    if "photo" not in physical_evidence_found:
        button:
            xpos 600
            ypos 200
            xsize 80
            ysize 120
            background "#3498db"
            hover_background "#5dade2"
            action [AddToSet("physical_evidence_found", "photo"), Show("evidence_found_popup", msg="发现照片")]
            
            text "📖" size 35 xalign 0.5 yalign 0.5

# 发现证据弹窗
screen evidence_found_popup(msg):
    modal False
    
    frame:
        xalign 0.5
        yalign 0.3
        background "#27ae60"
        padding (30, 20)
        
        text msg size 20 color "#ffffff" xalign 0.5
    
    timer 1.5 action Hide("evidence_found_popup")

# 直接闯入（高风险）
label direct_break_in:
    "你选择直接闯入。"
    "门锁着。"
    
    menu:
        "强行撬锁（可能被发现）":
            $ risk_roll = renpy.random.randint(1, 10)
            if risk_roll <= 3:
                "锁开了。但监控拍到了你。"
                $ investigation_skill -= 2
                call screen office_search_timer(duration=60.0)  # 只有1分钟
            else:
                "撬锁失败！保安正在赶来。"
                jump chapter4_fail
        
        "放弃":
            jump chapter4_end

label chapter4_fail:
    "你被发现了。"
    "陈永仁看着你，笑容意味深长。"
    chen "小曼，你在找什么？"
    jump bad_ending_investigation

label chapter4_end:
    scene bg home_night
    with fade
    
    "第11周结束。"
    
    if digital_evidence_count >= 5 or len(physical_evidence_found) >= 2:
        "你掌握了足够的证据。"
        "下一步：决定如何使用。"
        jump chapter5_decision
    else:
        "证据仍然不足……"
        "你需要更多时间，或者更多勇气。"
        jump chapter5
# 定义 AddToSet 函数（Ren'Py没有内置）
init python:
    def add_to_set(set_name, item):
        if item not in globals()[set_name]:
            globals()[set_name].append(item)
    
    # 注册为屏幕动作可用
    # renpy.add_to_store("AddToSet", add_to_set)

#==========================================
init -1 python:
    import random

    # QTE状态管理
    class QTEState:
        def __init__(self):
            self.push_count = 0
            self.escape_clicked = 0
            self.choices_made = []
            self.boundary_warning = False

    qte_state = QTEState()

# ========== 图像和变换定义 ==========
init -1:
    # 基础按钮
    image qte_button_normal = Frame(Solid("#4A5568"), 10, 10)
    image qte_button_hover = Frame(Solid("#718096"), 10, 10)
    image qte_button_hard = Frame(Solid("#2D3748"), 10, 10)
    image qte_button_blink = Frame(Solid("#E53E3E"), 10, 10)

    # 屏幕抖动变换
    transform screen_shake:
        subpixel True
        parallel:
            xoffset 0
            linear 0.05 xoffset 5
            linear 0.05 xoffset -5
            linear 0.05 xoffset 3
            linear 0.05 xoffset -3
            linear 0.05 xoffset 0
            repeat
        parallel:
            yoffset 0
            linear 0.07 yoffset 3
            linear 0.07 yoffset -3
            linear 0.07 yoffset 5
            linear 0.07 yoffset -5
            linear 0.07 yoffset 0
            repeat

    transform subtle_shake:
        subpixel True
        xoffset 0
        linear 0.1 xoffset 2
        linear 0.1 xoffset -2
        linear 0.1 xoffset 0
        repeat

    transform slide_button:
        subpixel True
        xpos 0.3
        linear 3.0 xpos 0.7
        linear 3.0 xpos 0.3
        repeat

    transform blink_effect:
        alpha 1.0
        linear 0.3 alpha 0.0
        linear 0.3 alpha 1.0
        repeat

    transform appear_disappear:
        alpha 0.0
        pause 1.0
        linear 0.2 alpha 1.0
        pause 0.5
        linear 0.2 alpha 0.0
        pause 0.5
        linear 0.2 alpha 1.0

    transform heartbeat:
        zoom 1.0
        linear 0.3 zoom 1.05
        linear 0.3 zoom 1.0
        repeat

# ========== 屏幕定义 ==========
# image flash = Movie(play="tv_breakdown.av1")


# 第一个QTE：车内边界警报
# default countdown_1 = 10

# screen car_qte_1():
#     modal True

#     add Solid("#1a202c") at screen_shake
#     add "flash"
#     vbox:
#         align (0.5, 0.2)
#         spacing 10

#         text "【边界警报】" at blink_effect:
#             size 40
#             color "#FC8181"
#             xalign 0.5

#         text "系统警告：身体反应机制激活" at subtle_shake:
#             size 20
#             color "#A0AEC0"
#             xalign 0.5
            
#         text "[countdown_1]":
#             align (0.5, 0.5)
#             size 30
#             color "#E53E3E"
#             at blink_effect

#     # vbox:
#     #     align (0.5, 0.35)
#     #     spacing 5
#     #     xsize 700

#     #     text "陈永仁的手从头发移到脸颊：":
#     #         size 22
#     #         color "#E2E8F0"
#     #         xalign 0.5

#     #     text "你真美。有人告诉过你，你工作的时候有多迷人吗？":
#     #         size 22
#     #         color "#E2E8F0"
#     #         xalign 0.5

#     #     text "那么专注，那么……鲜活。":
#     #         size 22
#     #         color "#E2E8F0"
#     #         xalign 0.5

#     # 选项区域
#     hbox:
#         align (0.5, 0.65)
#         spacing 30

#         # A. 躲开 - 滑动按钮
#         button at slide_button:
#             background "qte_button_hard"
#             hover_background "qte_button_hover"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "a"), Return(True)]

#             text "躲开" at subtle_shake:
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16

#         # B. 不说话 - 固定
#         button:
#             background "qte_button_normal"
#             hover_background "qte_button_hover"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "b"), Return(True)]

#             text "不说话":
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16

#         # C. 说"不要" - 闪烁出现
#         button at appear_disappear:
#             background "qte_button_blink"
#             hover_background "qte_button_hover"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "c"), Return(True)]

#             text "说不要":
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16

#     # 倒计时
#     #timer 10.0 action [SetVariable("qte_result", "timeout"), Return(False)]
#     timer 1.0 repeat True action If(countdown_1 > 0, SetScreenVariable("countdown_1", countdown_1 - 1), [SetVariable("qte_result", "timeout"), Return(False)])

default qte_phase = "movie"      # 当前阶段：movie/screen
default qte_cycle = 0          # 当前循环次数（0-3）
default qte_total_cycles = 6     # 总循环次数
default countdown_1 = 5         # 总倒计时
default qte_result = None        # 玩家选择结果

# 定义变换效果
transform screen_shake:
    subpixel True
    xoffset 0
    choice:
        pause 0.05
        xoffset 2
        pause 0.05
        xoffset -2
        pause 0.05
        xoffset 0
    repeat

transform blink_effect:
    alpha 1.0
    linear 0.3 alpha 0.3
    linear 0.3 alpha 1.0
    repeat

transform subtle_shake:
    subpixel True
    xoffset 0
    choice:
        pause 0.1
        xoffset 1
        pause 0.1
        xoffset -1
    repeat

transform shake:
    subpixel True
    xoffset 0
    choice:
        pause 0.1
        xoffset 3
        pause 0.05
        yoffset -3
        pause 0.1
        xoffset -3
        pause 0.05
        yoffset 3
    repeat

transform re_shake:
    subpixel True
    xoffset 0
    alpha 0.3
    choice:
        pause 0.1
        xoffset -3
        pause 0.05
        yoffset 3
        pause 0.1
        xoffset 3
        pause 0.05
        yoffset -3
    repeat

transform slide_button:
    subpixel True
    xoffset -20
    linear 0.5 xoffset 0
    pause 0.5
    linear 0.5 xoffset -20
    repeat

transform appear_disappear:
    alpha 0.0
    pause 0.5
    linear 0.2 alpha 1.0
    pause 0.5
    linear 0.2 alpha 0.0
    repeat


# 带倒计时的QTE screen
screen car_qte_1_timer(duration=1.2):
    modal True
    
    # 背景抖动
    add Solid("#1a202c") at screen_shake
    
    # 倒计时显示
    vbox:
        align (0.5, 0.2)
        spacing 10
        
        text "【边界警报】" at blink_effect:
            size 40
            color "#FC8181"
            xalign 0.5
        
        text "系统警告：干扰协议激活" at subtle_shake:
            size 20
            color "#A0AEC0"
            xalign 0.5
        
        text "[countdown_1]" at blink_effect:
            align (0.5, 0.5)
            size 30
            color "#E53E3E"
    
    # 选项区域
    hbox:
        align (0.5, 0.65)
        spacing 30
        
        # A. 躲开 - 滑动按钮
        button at slide_button:
            background "#e53e3e"
            hover_background "#fc8181"
            xsize 160
            ysize 50
            action [SetVariable("qte_result", "a"), Return(True)]
            
            text "躲开" at subtle_shake:
                align (0.5, 0.5)
                color "#FFFFFF"
                size 16
        
        # B. 不说话 - 固定
        button:
            background "#4a5568"
            hover_background "#718096"
            xsize 160
            ysize 50
            action [SetVariable("qte_result", "b"), Return(True)]
            
            text "不说话":
                align (0.5, 0.5)
                color "#FFFFFF"
                size 16
        
        # C. 说"不要" - 闪烁出现
        button at appear_disappear:
            background "#d69e2e"
            hover_background "#f6e05e"
            xsize 160
            ysize 50
            action [SetVariable("qte_result", "c"), Return(True)]
            
            text "说不要":
                align (0.5, 0.5)
                color "#FFFFFF"
                size 16
    
    # 关键：极短倒计时，时间到自动返回False
    timer duration action Return(False)

# 推开他的QTE
screen push_away_qte():
    modal True

    add Solid("#000000")

    vbox:
        align (0.5, 0.3)
        spacing 20

        text "他在吻你" at heartbeat:
            size 36
            color "#E53E3E"
            xalign 0.5

        text "快速点击鼠标推开他！":
            size 18
            color "#A0AEC0"
            xalign 0.5

        text "（每次点击都比上一次更难）":
            size 18
            color "#A0AEC0"
            xalign 0.5

        text "点击次数: [qte_state.push_count] / 5":
            size 24
            color "#FC8181"
            xalign 0.5

    # 全屏点击区域
    button:
        xfill True
        yfill True
        background Solid("#00000000")
        action [SetVariable("qte_state.push_count", qte_state.push_count + 1), 
                If(qte_state.push_count >= 4, true=[Return(True)], false=NullAction())]

    # 动态难度计时器
    timer (3.0 - qte_state.push_count * 0.4) action [Return(False)]

# 10秒抉择窗口
default countdown = 10

screen final_choice():
    modal True

    add Solid("#1a202c")

    vbox:
        align (0.5, 0.2)
        spacing 15

        text "心跳如鼓" at heartbeat:
            size 32
            color "#FC8181"
            xalign 0.5

        text "他在等":
            size 24
            color "#E2E8F0"
            xalign 0.5

        text "不抱的话，明天会很尴尬":
            size 18
            color "#A0AEC0"
            xalign 0.5

        text "抱了的话，这事就过去了":
            size 18
            color "#A0AEC0"
            xalign 0.5

    text "[countdown]":
        align (0.5, 0.45)
        size 80
        color "#E53E3E"
        at heartbeat

    vbox:
        align (0.5, 0.7)
        spacing 20

        # 拥抱选项
        button:
            background "qte_button_normal"
            hover_background "qte_button_hover"
            xsize 220
            ysize 60
            action [SetVariable("final_choice", "hug"), Return(True)]

            text "拥抱他（场景结束，回家）":
                align (0.5, 0.5)
                color "#FFFFFF"
                size 16

        # 逃跑选项（第5秒出现）
        if countdown <= 5:
            if countdown > 2:
                button at blink_effect:
                    background "qte_button_blink"
                    hover_background "qte_button_hover"
                    xsize 200
                    ysize 60
                    action [SetVariable("final_choice", "escape"), Return(True)]

                    text "推开车门逃跑":
                        align (0.5, 0.5)
                        color "#FFFFFF"
                        size 16
            else:
                button:
                    background "qte_button_blink"
                    hover_background "qte_button_hover"
                    xsize 200
                    ysize 60
                    action [SetVariable("final_choice", "escape"), Return(True)]

                    text "推开车门逃跑":
                        align (0.5, 0.5)
                        color "#FFFFFF"
                        size 16

    timer 1.0 repeat True action If(countdown > 0, SetScreenVariable("countdown", countdown - 1), [SetVariable("final_choice", "timeout"), Return(False)])

# 房间扫描界面
screen room_scan():
    modal True

    add Solid("#2D3748")

    text "房间扫描：点击物品触发思绪":
        align (0.5, 0.1)
        size 28
        color "#E2E8F0"

    # 镜子
    button:
        align (0.2, 0.3)
        xsize 120
        ysize 180
        background Frame(Solid("#718096"), 5, 5)
        hover_background Frame(Solid("#A0AEC0"), 5, 5)
        action [SetVariable("clicked_item", "mirror"), Return(True)]

        text "镜子":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    # 床与小熊
    button:
        align (0.5, 0.3)
        xsize 180
        ysize 120
        background Frame(Solid("#4A5568"), 5, 5)
        hover_background Frame(Solid("#718096"), 5, 5)
        action [SetVariable("clicked_item", "bed"), Return(True)]

        text "床与小熊":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    # 手机
    button:
        align (0.8, 0.3)
        xsize 80
        ysize 140
        background Frame(Solid("#2D3748"), 5, 5)
        hover_background Frame(Solid("#4A5568"), 5, 5)
        action [SetVariable("clicked_item", "phone"), Return(True)]

        text "手机":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    # 淋浴
    button:
        align (0.35, 0.7)
        xsize 100
        ysize 100
        background Frame(Solid("#4299E1"), 5, 5)
        hover_background Frame(Solid("#63B3ED"), 5, 5)
        action [SetVariable("clicked_item", "shower"), Return(True)]

        text "淋浴":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    # 日记
    button:
        align (0.65, 0.7)
        xsize 100
        ysize 130
        background Frame(Solid("#D69E2E"), 5, 5)
        hover_background Frame(Solid("#ECC94B"), 5, 5)
        action [SetVariable("clicked_item", "diary"), Return(True)]

        text "日记":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    textbutton "离开房间":
        align (0.5, 0.95)
        action Return(False)

# ========== 游戏主流程 ==========
label chapter3:

    $ qte_state = QTEState()

    #scene garage with fade

    "车内。夜色。空调开得很低。"

    jump car_xsr

# 主QTE流程控制label
label car_xsr:
    # 初始化
    $ qte_cycle = 0
    $ qte_phase = "movie"
    $ countdown_1 = 10
    
    "【边界警报】系统警告：身体反应机制激活"
    
    # 开始循环
    jump qte_loop

# 循环控制器
label qte_loop:
    # 检查是否完成4次循环或倒计时结束
    if qte_cycle >= qte_total_cycles or countdown_1 <= 0:
        jump qte_result_check
    
    # 根据阶段执行
    if qte_phase == "movie":
        jump qte_movie_phase
    else:
        jump qte_screen_phase

# 影片播放阶段（玩家无法操作）
label qte_movie_phase:
    # 显示影片，不可交互
    play sound "flash.mp3"
    show flash:
            zoom 2
            align(0.5, 0.5)
    #骚扰01
    if qte_cycle == 1:
        show touch

    #骚扰02
    if qte_cycle == 2:
        show black:
            zoom 2
            align(0.5, 0.5)
        image harrassment_02a = ParameterizedText(xalign=0.5, yalign=0.45, size=68, color="#8a1616")
        image harrassment_02b = ParameterizedText(xalign=0.505, yalign=0.454, size=68, color="#b50d0d", bold=True)
        show harrassment_02a "有人告诉过你，\n你工作的时候有多迷人吗？" at re_shake
        show harrassment_02b "有人告诉过你，\n你工作的时候有多迷人吗？" at shake

    #骚扰03
    if qte_cycle ==3:
        scene lean
        image harrassment_03a = ParameterizedText(xalign=0.35, yalign=0.45, size=68, color="#8a1616")
        image harrassment_03b = ParameterizedText(xalign=0.65, yalign=0.55, size=88, color="#8a1616")
        show harrassment_03a "那么专注" at shake
        show harrassment_03b "那么……鲜活！" at shake
        scene black

    
    # 影片播放固定时间（例如1.5秒）
    $ renpy.pause(1, hard=True)  # hard=True 防止点击跳过
    
    # 切换到screen阶段
    $ qte_phase = "screen"
    hide flash
    
    jump qte_loop

# Screen操作阶段（玩家可操作，极短时间）
label qte_screen_phase:
    # 减少倒计时
    $ countdown_1 -= 1
    
    # 显示screen，极短操作时间
    call screen car_qte_1_timer(duration=0.8)
    
    # 检查玩家是否操作
    if _return:
        # 玩家成功操作，结束QTE
        jump qte_success
    else:
        # 玩家未操作，继续循环
        $ qte_cycle += 1
        $ qte_phase = "movie"
        jump qte_loop


# 结果处理
label qte_result_check:
    $ qte_result = ""
    call screen car_qte_1_timer()
    
    if qte_result == "timeout":
        $ qte_result = "b"

    if qte_result == "a":
        "你偏过头，躲开了他的手。"
        "陈永仁笑了笑，收回了手："
        extend "好吧，是我冒昧了。"
        jump car_ending_avoided

    elif qte_result == "b":
        "你沉默着，没有回应。"
        "陈永仁的手停留在你脸上，温度灼人。"
        jump car_continuation

    else:
        $ qte_state.choices_made.append("拒绝")
        s "请别这样。"

        "陈永仁停顿。手还在脸上："
        extend "别哪样？我就是欣赏你。欣赏一个人有错吗？"

        "他凑近："
        extend "我结婚了。你有男朋友。这没什么。就是……欣赏。"

        jump kiss_sequence

label car_continuation:
    "陈永仁的手指在你脸颊上停留了一秒，然后收回。"
    "你知道吗，有时候沉默比说话更有力量。"

    jump kiss_sequence

label kiss_sequence:
    "他吻你。"

    window hide

    $ qte_state.push_count = 0
    $ push_success = False

    while qte_state.push_count < 5:
        call screen push_away_qte()

        if _return:
            $ push_success = True
            jump pushed_away
        else:
            $ qte_state.push_count += 1
            if qte_state.push_count >= 3:
                "你感到无力..."
                window hide

    if not push_success:
        jump kiss_ending_long

label pushed_away:
    window show

    "你推开了他。"
    "陈永仁愣了一下，随即笑了："
    extend "抱歉，是我太冲动了。"

    "他张开双臂："
    extend "来，抱一下。朋友嘛？"

    jump final_decision

label kiss_ending_long:
    window show

    "吻持续了很久。"
    "当你终于能呼吸时，他已经收回了身体，仿佛什么都没发生。"

    "他张开双臂："
    extend "来，抱一下。朋友嘛？"

    jump final_decision

label final_decision:
    $ final_choice = ""
    call screen final_choice()

    if final_choice == "hug" or final_choice == "timeout":
        jump ending_hug
    else:
        jump ending_escape

label ending_hug:
    "你拥抱了他。"
    "他的体温透过衬衫传来，心跳平稳，仿佛刚才的混乱只是错觉。"

    "这就对了，"
    extend "我们就是朋友。"

    "他送你到楼下。你看着他的车尾灯消失在街角。"

    jump room_scene

label ending_escape:
    "你推开车门，踉跄下车，跑向电梯。"

    "身后传来他的声音："
    extend "小曼！等等！听我解释！"

    "你没回头。"

    "电梯门关上的瞬间，你看见他还站在车边，双臂垂落。"

    jump room_scene

label car_ending_avoided:
    "气氛有些尴尬，但他很快恢复了常态。"
    "我送你回去吧。"
    extend "今天确实晚了。"

    "一路上，你们聊着工作，仿佛刚才的触碰从未发生。"

    jump room_scene

label room_scene:
    scene bg room
    with fade

    "你的房间。"
    "门在身后关上，世界突然安静得可怕。"

    $ clicked_item = ""

    while True:
        call screen room_scan()

        if not _return:
            jump game_ending

        if clicked_item == "mirror":
            "你看向镜子。"
            "看起来一样。感觉不一样。"
            "那个女人的脸还是你的，但眼神...像是陌生人的。"

        elif clicked_item == "bed":
            "床头的泰迪熊歪着头看你。"
            "你想躺下。可能再也起不来。"
            "被子还保持着今早你掀开时的形状。"

        elif clicked_item == "phone":
            "8条未读消息。"
            "3条来自陈永仁。"
            "到家了吗？"
            "刚才的事，别多想。"
            "明天见。"

        elif clicked_item == "shower":
            "你需要洗。"
            "需要让水流冲走什么。"
            "但你知道，有些东西冲不掉。"

        elif clicked_item == "diary":
            "你翻开日记。"
            "空白页。"
            "一个字都写不出来。"
            "或者，有太多字，不知道从哪里开始。"

label game_ending:
    if "拒绝" in qte_state.choices_made:
        "你坐在床边，手机亮了又暗。"
        "我拒绝了。"
        extend "我推开了他。"
        "但为什么，心跳还是这么快？"

    elif final_choice == "escape":
        "你逃跑了。"
        "但逃跑之后呢？"
        "明天还要上班。还要见他。还要假装什么都没发生。"

    else:
        "你拥抱了他。"
        "朋友，他这么说的。"
        "但你不知道，朋友之间，会不会有这样的心跳。"

    "窗外，天快亮了。"

    $ ending_text = ""
    if len(qte_state.choices_made) > 0:
        $ ending_text = "关键选择：" + " → ".join(qte_state.choices_made)

    "[ending_text]"

    "《She: 镜中倒影》第一章 - 完"

    return


# ==========================================
# 第五章：抉择（第15周）
# ==========================================

# 定义变量
default chapter5_started = False
default evidence_complete = False
default advice_heard = False

# 路线选择标记
default route_legal = False
default route_hr = False
default route_public = False
default route_leave = False

# 路线条件变量
default lawyer_contacted = False
default courage = 0
default xiaohongshu_fans = 0

# 路线A变量
default police_credibility = 100
default police_report_2 = False

# 路线B变量
default hr_talk_done = False
default department_reorganized = False

# 路线C变量
default post_views = 0
default post_comments = 0
default media_contacted = 0
default lawyer_letter_received = False
default public_pressure = 0

# 路线D变量
default resignation_written = False
default last_day_done = False

# 第五章入口
label chapter5:
    $ chapter5_started = True
    
    scene bg bedroom_night
    with fade
    
    "第15周。周三。凌晨1:17。"
    "你把所有东西摊开在床上。"
    "消息。笔记。报警回执。律师名片。小红书评论。日记。工资条。所有。"
    
    "四条路清晰浮现。"
    
    jump route_selection

# 路线选择界面
screen route_choice_screen():
    modal True
    
    add Solid("#000000CC")
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 50
        background "#2c3e50"
        
        vbox:
            spacing 25
            xalign 0.5
            
            text "第五章：抉择" size 36 color "#ffffff" xalign 0.5
            text "四条路" size 28 color "#bdc3c7" xalign 0.5
            
            null height 20
            
            # 路线A
            button:
                xsize 500
                ysize 80
                background ("#27ae60" if (evidence_complete and lawyer_contacted) else "#7f8c8d")
                hover_background "#2ecc71"
                action [SetVariable("route_legal", True), Return("legal")]
                
                hbox:
                    xfill True
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    
                    text "⚖️" size 30
                    vbox:
                        text "路线A：法律途径" size 20 color "#ffffff"
                        text "条件：证据 + 律师联系" size 14 color "#bdc3c7"
            
            # 路线B
            button:
                xsize 500
                ysize 80
                background ("#3498db" if (evidence_complete and courage > 50) else "#7f8c8d")
                hover_background "#5dade2"
                action [SetVariable("route_hr", True), Return("hr")]
                
                hbox:
                    xfill True
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    
                    text "🏢" size 30
                    vbox:
                        text "路线B：HR内部举报" size 20 color "#ffffff"
                        text "条件：证据 + 勇气 > 50" size 14 color "#bdc3c7"
            
            # 路线C
            button:
                xsize 500
                ysize 80
                background ("#e74c3c" if (evidence_complete and xiaohongshu_fans > 800) else "#7f8c8d")
                hover_background "#ec7063"
                action [SetVariable("route_public", True), Return("public")]
                
                hbox:
                    xfill True
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    
                    text "📱" size 30
                    vbox:
                        text "路线C：公众曝光" size 20 color "#ffffff"
                        text "条件：证据 + 小红书粉丝 > 800" size 14 color "#bdc3c7"
            
            # 路线D
            button:
                xsize 500
                ysize 80
                background ("#f39c12" if (mental < 20) else "#7f8c8d")
                hover_background "#f5b041"
                action [SetVariable("route_leave", True), Return("leave")]
                
                hbox:
                    xfill True
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    
                    text "🚪" size 30
                    vbox:
                        text "路线D：离开" size 20 color "#ffffff"
                        text "条件：心理健康 < 20" size 14 color "#bdc3c7"

label route_selection:
    call screen route_choice_screen
    
    if _return == "legal":
        jump route_a_legal
    elif _return == "hr":
        jump route_b_hr
    elif _return == "public":
        jump route_c_public
    elif _return == "leave":
        jump route_d_leave
    else:
        jump route_selection

# ==========================================
# 路线A：法律途径
# ==========================================

label route_a_legal:
    scene bg bedroom_night
    with fade
    
    "你选择了法律途径。"
    "你相信系统。你相信正义需要程序。"
    
    jump task_5_a_1

label task_5_a_1:
    scene bg police_station
    with fade
    
    "中区警署。下午2:30。"
    
    show police_officer young at center with dissolve
    
    "警官很年轻。他努力显得友善。"
    
    "警官" "佘小姐，请坐。你想补充报案？"
    
    s "是的。我有新的证据。"
    
    hide police_officer young
    jump police_statement_game

screen police_statement_game():
    modal True
    
    default statement_history = []
    default current_question = 0
    default consistency_score = 100
    
    add Solid("#34495e")
    
    frame:
        xalign 0.5
        yalign 0.2
        background "#2c3e50"
        padding (30, 20)
        
        text "陈述一致性: [consistency_score]%" size 24 color "#ffffff" xalign 0.5
        
        if consistency_score < 60:
            text "可信度不足" size 18 color "#e74c3c" xalign 0.5
    
    if current_question == 0:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            background "#ffffff"
            
            vbox:
                spacing 20
                text "Q1: 第一次不当接触发生在什么时候？" size 20 color "#2c3e50"
                
                textbutton "办公室茶水间":
                    action [SetScreenVariable("statement_history", statement_history + ["pantry"]), 
                            SetScreenVariable("current_question", 1)]
                
                textbutton "我不记得了":
                    action [SetScreenVariable("consistency_score", consistency_score - 20),
                            SetScreenVariable("statement_history", statement_history + ["unknown"]), 
                            SetScreenVariable("current_question", 1)]

                if car_event:
                    textbutton "庆功酒后，他送我回家":
                        action [SetScreenVariable("statement_history", statement_history + ["car"]), 
                                SetScreenVariable("current_question", 1)]
                else: 
                    pass
    
    elif current_question == 1:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            background "#ffffff"
            
            vbox:
                spacing 20
                text "Q2: 详细描述当晚他送你回家的经过？" size 20 color "#2c3e50"
                
                if "car" in statement_history:
                    textbutton "他在车里试图吻我，我推开了他":
                        action [SetScreenVariable("current_question", 2)]
                    
                    textbutton "什么都没发生，他只是送我回家":
                        action [SetScreenVariable("consistency_score", consistency_score - 30),
                                SetScreenVariable("current_question", 2)]
                else:
                    textbutton "他说要送我，但我拒绝了":
                        action [SetScreenVariable("consistency_score", consistency_score - 20),
                                SetScreenVariable("current_question", 2)]
                    
                    textbutton "我们去了酒店":
                        action [SetScreenVariable("consistency_score", consistency_score - 40),
                                SetScreenVariable("current_question", 2)]
    
    elif current_question == 2:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 30
            background "#ffffff"
            
            vbox:
                spacing 20
                text "Q3: 为什么现在才来报案？" size 20 color "#2c3e50"
                
                textbutton "我需要时间收集证据":
                    action [Return(80)]
                
                textbutton "我害怕":
                    action [Return(60)]
                
                textbutton "我不知道这算不算犯罪":
                    action [Return(40)]

label police_statement_game:
    call screen police_statement_game
    
    $ police_credibility = _return
    
    jump police_result

label police_result:
    scene bg police_station
    with fade
    
    show police_officer young at center
    
    "警官" "好的，佘小姐。我们会调查。"
    
    "{i}翻译：什么都不会发生。{/i}"
    
    hide police_officer young with dissolve
    
    scene bg bedroom_night
    with fade
    
    "{i}3周后。{/i}"
    
    "【短信通知】"
    "「经调查，证据不足，不予立案。」"
    
    $ police_report_2 = True
    
    "新物品：【报警回执单2号】"
    "又一张盖着公章的纸。又一段被程序终结的正义。"
    
    jump chapter5_ending

# ==========================================
# 路线B：HR内部举报
# ==========================================

label route_b_hr:
    scene bg bedroom_night
    with fade
    
    "你选择了内部渠道。"
    "你相信公司会保护自己人。你相信规则之内能解决。"
    
    jump task_5_b_1

label task_5_b_1:
    scene bg hr_office
    with fade
    
    "HR总监办公室。3楼。"
    
    show hr_director at center with dissolve
    
    'HR总监' "佘小姐，请坐。这事很严重，你明白吗？"
    'HR总监' "指控一位高级经理……我们需要非常谨慎。"
    
    menu:
        "回应："
        
        "我不是指控，我是举报。":
            s "我不是指控，我是举报。这是两回事。"
            'HR总监' "……措辞的区别。继续。"
            
        "我有证据。":
            s "我有证据。工资差异记录。聊天记录。证人。"
            'HR总监' "请出示。"
            $ courage += 10
            
        "我要留记录。":
            s "我要这次谈话有记录。邮件抄送，或者会议纪要。"
            'HR总监' "……当然。这是标准流程。"
            $ courage += 5
    
    "你把证据摊在桌上。"
    
    'HR总监' "明白了。我们会内部调查。有结果通知你。"
    
    hide hr_director with dissolve
    
    scene black
    with fade
    
    "{i}2周后。{/i}"
    
    scene bg hr_office
    with fade
    
    show hr_director at center
    
    'HR总监' "调查结束。无充分证据证明不当行为。"
    'HR总监' "但已提醒陈经理注意职业边界。"
    
    s "……就这样？"
    
    'HR总监' "佘小姐，我建议你关注自己的职业发展。"
    'HR总监'"对了，部门重组的通知你收到了吗？"
    
    hide hr_director with dissolve
    
    $ department_reorganized = True
    
    scene bg remote_office
    with fade
    
    "偏远办公室。独自一人。没团队。"
    "你的工位对着墙。没有窗。"
    
    jump chapter5_ending

# ==========================================
# 路线C：公众曝光
# ==========================================

label route_c_public:
    scene bg bedroom_night
    with fade
    
    "你选择了公众。"
    "你相信声音。你相信众目睽睽之下，真相无法被掩埋。"
    
    jump task_5_c_1

screen xiaohongshu_post():
    modal True
    
    default disclosure_level = "medium"
    default selected_evidence = []
    default post_title = ""
    
    add Solid("#ffffff")
    
    frame:
        xalign 0.5
        yalign 0.1
        background "#ff2442"
        xsize 800
        ysize 60
        padding (20, 10)
        
        text "小红书" size 24 color "#ffffff" xalign 0.5
    
    frame:
        xalign 0.5
        yalign 0.55
        xsize 800
        ysize 600
        background "#f8f8f8"
        padding (30, 30)
        
        vbox:
            spacing 20
            
            hbox:
                spacing 10
                text "标题：" size 18 color "#333333"
                
                textbutton (post_title if post_title else "点击输入标题..."):
                    xsize 600
                    ysize 40
                    background "#ffffff"
                    text_size 16
                    text_color ("#333333" if post_title else "#999999")
                    action Show("post_title_input")
            
            null height 20
            
            text "披露程度：" size 18 color "#333333"
            
            hbox:
                spacing 15
                
                textbutton "隐去细节":
                    action SetScreenVariable("disclosure_level", "low")
                    background ("#ff2442" if disclosure_level == "low" else "#dddddd")
                
                textbutton "部分实名":
                    action SetScreenVariable("disclosure_level", "medium")
                    background ("#ff2442" if disclosure_level == "medium" else "#dddddd")
                
                textbutton "完全公开":
                    action SetScreenVariable("disclosure_level", "high")
                    background ("#ff2442" if disclosure_level == "high" else "#dddddd")
            
            null height 20
            
            text "附带证据：" size 18 color "#333333"
            
            grid 2 2:
                spacing 10
                
                textbutton "工资差异记录":
                    action ToggleScreenVariable("selected_evidence", "salary")
                    background ("#ff2442" if "salary" in selected_evidence else "#dddddd")
                    xsize 200
                    ysize 50
                
                textbutton "聊天记录截图":
                    action ToggleScreenVariable("selected_evidence", "chat")
                    background ("#ff2442" if "chat" in selected_evidence else "#dddddd")
                    xsize 200
                    ysize 50
                
                textbutton "报警回执":
                    action ToggleScreenVariable("selected_evidence", "police")
                    background ("#ff2442" if "police" in selected_evidence else "#dddddd")
                    xsize 200
                    ysize 50
                
                textbutton "证人证言":
                    action ToggleScreenVariable("selected_evidence", "witness")
                    background ("#ff2442" if "witness" in selected_evidence else "#dddddd")
                    xsize 200
                    ysize 50
            
            null height 30
            
            textbutton "发布":
                xalign 0.5
                xsize 200
                ysize 50
                background "#ff2442"
                text_size 20
                text_color "#ffffff"
                action [Return({"disclosure": disclosure_level, "evidence": selected_evidence, "title": post_title})]

screen post_title_input():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        background "#ffffff"
        
        vbox:
            spacing 15
            
            text "输入标题：" size 20
            
            textbutton "在游戏公司被性骚扰，我决定说出来":
                action [SetScreenVariable("post_title", "在游戏公司被性骚扰，我决定说出来"), Hide("post_title_input")]
            
            textbutton "关于某游戏公司高管，一些必须讲的事":
                action [SetScreenVariable("post_title", "关于某游戏公司高管，一些必须讲的事"), Hide("post_title_input")]
            
            textbutton "22k vs 19.5k，不只是工资":
                action [SetScreenVariable("post_title", "22k vs 19.5k，不只是工资"), Hide("post_title_input")]
            
            textbutton "取消":
                action Hide("post_title_input")
                xalign 0.5

label task_5_c_1:
    call screen xiaohongshu_post
    
    $ post_result = _return
    
    scene bg bedroom_night
    with fade
    
    "帖子发出。"
    
    $ post_views = 90000
    $ post_comments = 7000
    $ media_contacted = 2
    
    "24小时。"
    "9万浏览量。"
    "7000多条评论。"
    "2家媒体联系。"
    
    "{i}反噬。{/i}"
    
    "她就是想要钱。"
    "为什么不早说？"
    "他是个好人，她在毁他。"
    
    $ public_pressure = 50
    $ mental -= 30
    
    "压力+[public_pressure]。睡眠-80%。"
    
    "但……"
    
    "【私信】姐妹，我也经历过。谢谢你敢说。"
    "【私信】我在这家公司3年了，一直不敢说。"
    "【私信】你不是一个人。"
    
    "你不再是一个人。"
    
    jump chapter5_ending

# ==========================================
# 路线D：离开
# ==========================================

label route_d_leave:
    scene bg bedroom_night
    with fade
    
    "你选择了离开。"
    "有时候，活下去比赢更重要。"
    
    jump task_5_d_1

screen resignation_letter():
    modal True
    
    default reason_choice = ""
    
    add Solid("#f5f5f5")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 600
        background "#ffffff"
        padding (60, 60)
        
        vbox:
            spacing 30
            
            text "辞职信" size 28 color "#333333" xalign 0.5
            
            null height 20
            
            text "尊敬的HR：" size 16 color "#333333"
            text "    我申请辞去设计部职位，最后工作日为两周后。" size 16 color "#333333"
            
            null height 30
            
            text "辞职理由：" size 16 color "#333333" bold True
            
            vbox:
                spacing 15
                
                button:
                    xfill True
                    ysize 50
                    background ("#e8e8e8" if reason_choice == "personal" else "#ffffff")
                    hover_background "#f0f0f0"
                    action SetScreenVariable("reason_choice", "personal")
                    
                    text "A. 个人原因" size 16 color "#333333" xalign 0.5
                
                button:
                    xfill True
                    ysize 50
                    background ("#e8e8e8" if reason_choice == "blank" else "#ffffff")
                    hover_background "#f0f0f0"
                    action SetScreenVariable("reason_choice", "blank")
                    
                    text "B. 不填" size 16 color "#333333" xalign 0.5
                
                button:
                    xfill True
                    ysize 50
                    background ("#e8e8e8" if reason_choice == "truth" else "#ffffff")
                    hover_background "#f0f0f0"
                    action SetScreenVariable("reason_choice", "truth")
                    
                    text "C. 真相（即使什么也改变不了）" size 16 color "#333333" xalign 0.5
            
            null height 40
            
            text "申请人：佘小曼" size 16 color "#333333" xalign 1.0
            text "日期：2028年4月15日" size 16 color "#333333" xalign 1.0
            
            null height 30
            
            textbutton "提交":
                xalign 0.5
                xsize 150
                ysize 45
                background ("#cccccc" if reason_choice == "" else "#27ae60")
                text_size 18
                text_color "#ffffff"
                action [Return(reason_choice)]

label task_5_d_1:
    call screen resignation_letter
    
    $ resignation_reason = _return
    
    scene bg bedroom_night
    with fade
    
    if resignation_reason == "personal":
        "你写了'个人原因'。最安全的答案。最沉默的答案。"
    elif resignation_reason == "blank":
        "你留了一栏空白。有时候，空白比文字更响亮。"
    elif resignation_reason == "truth":
        "你写下了真相。每一个字都像是从骨头上刮下来的。"
        "即使什么也改变不了。"
    
    $ resignation_written = True
    
    jump last_day

label last_day:
    scene bg office_floor
    with fade
    
    "最后一天。"
    
    show xiaojin at left with dissolve
    
    xiaojin "……真的要走了？"
    
    s "嗯。"
    
    xiaojin "这地方配不上你。但也……别太拼了，好吗？"
    
    hide xiaojin with moveoutleft
    
    show linjie at right with moveinright
    
    "林姐走过来。她看着你，很久。"
    "然后她抱了你。"
    "{i}她第一次碰你。{/i}"
    
    linjie "我撑了3年。你4个月。"
    linjie "你比我强。"
    
    hide linjie with dissolve
    
    scene bg building_exterior
    with fade
    
    "你走出去。"
    "大楼从外面看一样。永远一样。"
    "已经有人坐在你工位上了。"
    
    $ last_day_done = True
    
    jump chapter5_ending

# ==========================================
# 第五章结局
# ==========================================

label chapter5_ending:
    scene bg bedroom_night
    with fade
    
    "第五章结束。"
    
    if route_legal:
        "你选择了法律。程序走完了，正义还在路上。"
    elif route_hr:
        "你选择了内部。系统保护了系统，你学会了墙的颜色。"
    elif route_public:
        "你选择了公众。声音很吵，但至少有人听见了。"
    elif route_leave:
        "你选择了离开。活着走出去，本身就是一种胜利。"
    
    "《She: 镜中倒影》第五章 - 完"
    
    return