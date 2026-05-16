# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define config.layers = ['master', 'transient', 'screens', 'interface', 'front'] #显示图层

#成就相关数值
default escape = 0 #【成就：鸵鸟】


#运行python先打包一个字典给screen item_description调取不同描述用
init python:
    item_descriptions = {
        "magazine": "A special issue of Female Leaders, half a page torn out by someone.",
        "computer": "An open Excel spreadsheet showing the salary range for your applied position: starting salary $22,000 for males, $18,000 for females.",
        "smartphone": "A message from Mom: Have you found a job? Your brother needs new shoes.",
        "window": "You gaze at the city, with 135 rejection letters scattered among it."
    }
    item_names = {
        "magazine": "magazine",
        "computer": "computer",
        "smartphone": "smartphone",
        "window": "window"
    }
    item_image = {
        "window": "chapter0_items/window_scenery.png" 
    }

#小曼立绘的淡入淡出，onlayer使用必须用这个控制
transform top_dissolve:
    # 进入
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    
    # 离开 - 关键
    on hide:
        alpha 1.0
        linear 0.25 alpha 0.0

transform item3_left_rotate:
    zoom 0.7
    align(0.5, 1.0)
    rotate 70
    # 快速滑入并旋转
    easein 0.6 align(0.5, 0.9) rotate 0

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
        at transform:
            on idle:
                zoom 0.75
                rotate 80 
                xpos 800
                ypos 850
            on hover:
                zoom 1
                linear 0.4 rotate 20 xpos 750 ypos 550
        idle "chapter0_items/item3_smartphone.png"
        hover "chapter0_items/item3_smartphone_hover.png"

        if not item3_smartphone_clicked: 
            action [
                SetVariable("chapter0_items/item3_smartphone_clicked", True),
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
            idle "chapter0_items/item3_smartphone.png"
            hover "chapter0_items/item3_smartphone_hover.png"
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
label your_label_name:

    "{i}This recruiting season, you sent out 147 resumes. 12 came back as rejections. The rest disappeared without a trace.{/i}"
    "{i}Mom calls every Sunday, asking when you’ll finally find a job and telling you to stop being so picky.\nBut this time… something feels different.{/i}"
    hide she_01_normal_nocard onlayer top
    scene black with fade
    "{i}You enter the waiting room. You’re next.{/i}"
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

#========================

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
                size 28
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        button:
            xsize 600
            ysize 50
            action act2
            
            text opt2:
                size 28
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        # 第二行
        button:
            xsize 600
            ysize 50
            action act3
            
            text opt3:
                size 28
                xalign 0.5
                yalign 0.5
                idle_color "#888888"

        button:
            xsize 600
            ysize 50
            action act4
            
            text opt4:
                size 28
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
    "{i}He stands up to greet you, with a warm smile and perfect posture. He is the kind of person who makes you feel seen the moment you meet him.{/i}"
    show she_01_normal_nocard_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}You sit down, your attention drawn to the arrangement of his office.{/i}"
    hide she_01_normal_nocard onlayer top
    hide she_01_normal_nocard_eye onlayer top
    scene chen_office with fade:
        zoom 1.1
        xalign 0.9
        yalign 0.4
    call screen grid_choice(
        "Which item do you want to examine most?",
        "Bookshelf", "Photo on the Desk",
        "Patterned Coffee Mug", "Floor-to-Ceiling Window",
        Jump("bookshelf"), Jump("family_photo"),
        Jump("coffee_mug"), Jump("french_window")
    )

label bookshelf:
    "{i}There are books on law, business strategy, and a collection of poems by female poets.{/i}"
    window hide
    jump after_menu

label family_photo:
    "{i}It is a family photo, showing his wife and two children. They are all smiling.{/i}"
    window hide
    jump after_menu

label coffee_mug:
    "{i}A chipped coffee mug with the words “World’s Best Dad” printed on it.{/i}"
    window hide
    jump after_menu

label french_window:
    "{i}Standing here, it feels as if the entire city is beneath your feet.{/i}"
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
    c"Siu Man, tell me, why do you want to work here？"

    menu:
        "I need the money.":
            s "I need the money."

        "I admire your company's values.":
            s "I admire your company's values."
            $ add_social(1, "Interview B")

        "I want to prove I can do better than anyone else.":
            s "I want to prove I can do better than anyone else."
            $ add_mental(1, "Interview C")

    c "I see. You know, there’s a contingency that we were like to get someone older, with more experience. But what I see in your resume is... hunger."

    $ show_sequential_thoughts(
        "He looks at your resume.",
        "He looks at your face.",
        "He looks at your hands."
    )

    c "Do you have any questions for me?"

    menu:
        "What are the promotion pathways for females here?":
            s "What are the promotion pathways for females here?"
            show chen_02_smile:
                zoom 0.9
                xzoom -1.0
                xpos 680
                ypos 160 
            c "Good question. We're very progressive here. Half of our middle managers are females... well, one-third actually... there's Ms Lam, she's outstanding."
            hide chen_02_smile
            jump chapter0_3

        "Is there flexible remote work available?":
            s "Is there flexible remote work available?"
            show chen_05_wanwei: 
                zoom 0.9
                xzoom -1.0
                xpos 687
                ypos 161
            c "Good question. Our company actually cares a lot about work-life balance. Flexible remote work is available in principle."
            c "But... to be honest, in the gaming industry—especially for designers, it’s best to be on-site more often in the early stage. Of course, it’s not mandatory. Just a suggestion."
            hide chen_05_wanwei
            jump chapter0_3

        "No, you've covered everything thoroughly.":
            jump chapter0_3

label chapter0_3:
    show chen_03_narroweyes:
        zoom 0.9
        xzoom -1.0
        xpos 680
        ypos 160
    c"Do you have any other questions？"
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
    s"No, thank you."
    c"Then that concludes the interview. It's been a pleasure talking with you."    
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
default coffee_bought = False
#default elevator_floor = 0
default gate_used = False
default appearance_checked = False
default third_floor = False
default eight_floor = False
default twenty_third_floor = False

# 场景定义（占位符图片）
#image bg lobby = "bg_lobby.png"  # 公司大堂
image bg third_floor = "images/chapter1/third_floor.jpg"  # 3楼HR
image bg eight_floor = "images/chapter1/eighth_floor.jpg"  # 8楼市场部
image bg twenty_third_floor = "images/chapter1/twenty_third_floor.jpg"  # 23楼高管层

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
    
    play sound "rope_drop.ogg"
    show office_card at bounce_rotate_in
    show office_card_rope at rotate_in
    #"“哔！”" #改成音效
    
    "{i}Welcome, Siu Man! This is the first time you hear your own name here.{/i}"
    
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
    scene bg third_floor with dissolve:
        zoom 1.5
    "{i}HR部门...{/i}"
    $ third_floor = True
    jump elevator_choice
            
label eight_floor:
    scene bg eight_floor with dissolve:
        xzoom -1
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
    
    show woman_01_normal with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160
    "{i}The elevator doors slide open. A woman in her forties, sharply dressed in a tailored suit, her eyes weary.{/i}"
    
    show woman_02_talk:
        zoom 0.8
        xpos 1350
        ypos 160
    unknown_woman "New here?"
    hide woman_02_talk
    
    show she_05_happy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "First day."
    
    show woman_02_talk:
        zoom 0.8
        xpos 1350
        ypos 160
    unknown_woman "I see."
    show she_05_happy_sweat onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}She stares at you a little too long.{i}"
    unknown_woman "Design department?"

    show she_06_surprise_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_05_happy_sweat onlayer top
    s "Huh, how did you tell?"
    
    unknown_woman "It’s in your eyes. Wonder how long you’ll stick around here."
    
    hide woman_01_normal with dissolve    
    "{i}She gets off at the third floor. You never learn her name.{/i}"
    
    # 剧情继续到下一部分...
    hide she_05_happy onlayer top
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
        zoom 0.75
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
    hide she_03_tinysmile_eye onlayer top
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
        zoom 0.75
    
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
    show meeting_room with fade
    
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
    chen "好问题。林姐会带你。就是市面上那几款头部游戏，美术风格、养成线、付费点设计……那些有趣的东西。"
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
    scene meeting_room with fade
    
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
    
    "{i}You’re back at your desk, staring at the shared folder open on your computer screen.{/i}"
    "{i}Your first task to prove yourself has begun.{/i}"
    
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
    
    "{i}Day 5 at work, 10:47 PM.{/i}"
    "{i}The office feels different at night, quieter, yet the hum of the vending machine grows louder.{/i}"
    
    call mini_game_analysis
    
    $ fatigue = 50
    
    if fatigue > 60:
        n "好想睡觉……"
    if fatigue > 40:
        n "I can’t get this gacha probability curve to add up…"
    if fatigue > 30:
        n "And there’s an early‑morning meeting tomorrow…"
    
    n "但做不完的话，陈总会不会觉得我不行？"
    
    "{i}你趴在桌上想着，耳边传来一阵脚步声。细听时，脚步声停了。{/i}"
    
    show chen_03_narroweyes with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160
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
    show chen_00_body:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 438
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
    
    hide chen_03_narroweyes
    show chen_06_surprise_head:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 162
    chen "…………"
    
    show chen_02_smile_front with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 162
    hide chen_00_body
    hide chen_06_surprise_head
    "{i}陈永仁表情柔和下来。{/i}"

    chen "我懂。我就是从这个位置开始的——就是这张桌子，20年前。现在你看……"
    "{i}他模糊地往上指了指。{/i}"

    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161
    chen "努力工作，留到最后，这就是赢的方法。"
    "{i}他站起来。{/i}"
    
    hide chen_04_frontsmile with dissolve
    chen "别太晚，回家注意安全。"
    chen "…………"
    chen "其实我也要走了……送你一程？"
    jump car_choice

label chen_safe:
    s "这里的岗位和我的专业技能最匹配。"
    show chen_02_smile:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161 
    hide chen_00_body
    chen "嗯，确实。你的拆解能力很强。"
    "{i}他站起来。{/i}"
    hide chen_02_smile
    chen "别太晚，明天还有早会。"
    chen "……其实我也要走了，送你一程？"
    jump car_choice

label chen_ambition:
    s "我想升得快一些。"
    show chen_02_smile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161
    hide chen_00_body
    chen "有野心。我喜欢。"
    "{i}他站起来。{/i}"
    hide chen_02_smile
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
    scene car_inside with fade
    "{i}车内很干净，有淡淡的皮革味。{/i}"
    s "您把我放在711就好，我刚好买个早餐，麻烦您了。"
    chen "没问题。"
    "{i}陈永仁放了一首老歌。你们都没说话。{/i}"
    "{i}他在便利店前停车。{/i}"
    chen "明天见，好好休息。"
    jump task_1_4_end2

label reject_car:
    s "不用，我坐地铁。"
    chen "随你。明天见。"
    hide chen_02_smile_front with moveoutright
    hide chen_03_narroweyes with moveoutright
    "{i}陈永仁走了。{/i}"
    "{i}你看着他离开，胸口有什么东西松开了，不知道为什么。{/i}"
    jump task_1_4_end1

label task_1_4_end1:
    scene office_desk with fade
    "{i}深夜的办公室闪烁的是代码的霓虹。{/i}"
    "{i}电子bug能梦见仿生萤火虫吗？\n在刚来那天所看到的落地窗里，星星亮起，夜幕降临。{/i}"
    jump task_1_5

label task_1_4_end2:
    scene home with fade
    "{i}回到家，你简单收拾后便躺下，很快就睡着了。{/i}"
    "{i}梦里，深夜的办公室闪烁的是代码的霓虹。{/i}"
    "{i}电子bug能梦见仿生萤火虫吗？\n在刚来那天所看到的落地窗里，星星亮起，夜幕降临。{/i}"
    jump task_1_5

label mini_game_analysis:
    "{i}You need to finish competitive analysis for these games.{/i}"
    #设置游戏ABC的图片 --> 提示玩家拆解方向
    
    show game_wzry:
        xpos 544
        ypos 123
    menu:
        "What is the core monetization driver of this game?"
        "VIP Privileges":
            $ temp_score = 1
            hide game_wzry
        "Gacha Pity Mechanic":
            $ temp_score = 0
            hide game_wzry
        "Paid Skins":
            $ temp_score = 1
            hide game_wzry
    
    # menu:
    #     "游戏B的主要留存机制是？"
    #     "每日签到":
    #         $ temp_score += 1
    #     "社交公会":
    #         $ temp_score += 1
    #     "剧情解锁":
    #         $ temp_score += 0
    
    show game_elden_ring:
        xpos 544
        ypos 123
    menu:
        "What art style does this game adopt?"
        "Realistic 3D":
            $ temp_score += 1
            hide game_elden_ring
        "Anime Cel‑shaded":
            $ temp_score += 0
            hide game_elden_ring
        "Retro Pixel Art":
            $ temp_score += 0
            hide game_elden_ring
    
    show game_srcx:
        xpos 544
        ypos 123
    menu:
        "Which genre does this game belong to?"
        "Single‑player Role‑Playing":
            $ temp_score += 0
            hide game_srcx
        "Two‑Player Co‑op Puzzle":
            $ temp_score += 1
            hide game_srcx
        "Multiplayer Competitive Shooter":
            $ temp_score += 0
            hide game_srcx

    if temp_score >= 3:
        "{i}Analysis complete. Data saved.{/i}"
    else:
        "{i}部分数据存疑，但先这样吧。{/i}"
        $ fatigue += 20
    
    return

# ========== 任务1.5：家庭税 ==========
define mom = Character("Mom")

label task_1_5:
    scene home with fade
    "{i}Week 2, Sunday afternoon.{/i}"
    window hide
    
    #消息音效
    play sound "wx_voice_call.mp3"
    show mom_phonecall with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    pause 1.5
    hide mom_phonecall with fade
    jump salary_qte

default quarrel_time_limit = 3.0    # 总时间（秒）
default quarrel_time_left = 3.0     # 剩余时间
default quarrel_answered = False    # 是否已回答

screen qte_choice_timer(question, time_limit=3.0):
    modal True
    
    default start_time = renpy.get_game_runtime()
    default time_left = time_limit
    
    timer 0.05 repeat True action [
        SetScreenVariable("time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
        If(time_left <= 0, true=[Hide("qte_choice_timer"), Jump("qte_timeout")], false=NullAction())
    ]
    
    $ progress = time_left / time_limit
    
    # 警告色：时间少于30%变红
    $ bg_pulse = 0.1 if progress < 0.3 else 0.0
    
    # 背景闪烁警告
    if progress < 0.3:
        add Solid("#ff000010") at transform:
            alpha 0.0
            block:
                linear 0.2 alpha 0.3
                linear 0.2 alpha 0.0
                repeat
    
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 30
        
        textbutton "In two weeks.":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer"), Jump("salary_truth")]
        
        textbutton "Soon.": 
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer"), Jump("salary_vague")]
        
        textbutton "Why do you ask?":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer"), Jump("salary_defensive")]
    
    # ===== 底部倒计时条 =====
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -40
        xsize 1400
        ysize 25
        background "#1a1a1a"
        
        # 内部进度条
        add "white_time_bar":
            xalign 0.5
            xsize int(1400 * progress)
            ysize 15
        
        # 时间文字
        text "[time_left:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"
            
label salary_qte:
    show mother_02_smallmouth:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "Your first month's salary. When will it be paid?"
    
    # 调用 QTE 选择题
    call screen qte_choice_timer(
        question="",
        time_limit=3.0
    )
    
    # 这里不会执行，因为 screen 直接 jump 了
    return

# 各选项结果
label salary_truth:
    s "In two weeks."
    show mother_03_unhappy:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "Good. Your brother needs a new school uniform, and there’s a school trip fee—1,200 yuan. You’ll pay for it, right? You have a big job now."
    jump family_money_choice

label salary_vague:
    s "Soon."
    show mother_03_unhappy:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "How soon exactly? Your brother needs a new school uniform and to pay for his school trip—1,200 yuan. Can you pay for that?"
    jump family_money_choice

label salary_defensive:
    s "Why are you asking?"
    show mother_01_bigmouth:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "What, you think you’re all grown up now? Your brother needs a new school uniform, and there’s a school trip fee—1,200 yuan. Money is tight at home. What’s wrong with helping out?"
    jump family_money_choice

# 超时未选择
label qte_timeout:
    s "..."
    mom "Why aren’t you saying anything?"
    mom "Your brother needs a new school uniform, and there’s a school trip fee—1,200 yuan. You’ll pay for it, right? You have a big job now."
    jump family_money_choice

# QTE第二题
screen qte_choice_timer_2(question, time_limit=5.0):
    modal True
    
    default start_time = renpy.get_game_runtime()
    default time_left = time_limit
    
    timer 0.05 repeat True action [
        SetScreenVariable("time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
        If(time_left <= 0, true=[Hide("qte_choice_timer_2"), Jump("stay_silent")], false=NullAction())
    ]
    
    $ progress = time_left / time_limit
    
    # 警告色：时间少于30%变红
    $ bg_pulse = 0.1 if progress < 0.3 else 0.0
    
    # 背景闪烁警告
    if progress < 0.3:
        add Solid("#ff000010") at transform:
            alpha 0.0
            block:
                linear 0.2 alpha 0.3
                linear 0.2 alpha 0.0
                repeat
    
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 30
        
        textbutton "Fine.":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_2"), Jump("give_money")]
        
        textbutton "That’s half my food budget.": 
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_2"), Jump("angry_game")]
        
        textbutton "(Stay silent)":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_2"), Jump("stay_silent")]
    
    # ===== 底部倒计时条 =====
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -40
        xsize 1400
        ysize 25
        background "#1a1a1a"
        
        # 内部进度条
        add "white_time_bar":
            xalign 0.5
            xsize int(1400 * progress)
            ysize 15
        
        # 时间文字
        text "[time_left:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"

label family_money_choice:
    # 调用 QTE 选择题
    # 前面回答有mom不同的问题了：mom "怎么，翅膀硬了？你弟弟要换新校服，还有学校旅行要交钱，1200块钱。家里手头紧，你帮衬一下怎么了？"
    call screen qte_choice_timer_2(
        question="",
        time_limit=5.0
    )
    return

label give_money:
    s "Fine."
    $ money -= 1200
    show mother_04_smile with dissolve:
        zoom 0.83
        xpos 1360
        ypos 260
    hide mother_02_smallmouth
    hide mother_03_unhappy
    mom "Good girl. I knew you were sensible. Your brother will thank you."
    hide mother_04_smile with dissolve
    "{i}-1,200 yuan. Current balance: [money] yuan{/i}"
    jump family_tax_end

label angry_game:
    s "That’s half my food budget!"
    $ mother_anger += 2
    jump argue_continue

label stay_silent:
    s "..."
    show mother_03_unhappy:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "What is that silence supposed to mean?"
    show mother_02_smallmouth:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "Have you forgotten how I scrimped and saved to raise you?"
    $ mother_anger += 1
    jump stay_silent_continue #考虑到有保守派会沉默避免冲突但不是真的不抗争，设置沉默意图的二次验证

# QTE第三题
screen qte_choice_timer_3(question, time_limit=3.0):
    modal True
    
    default start_time = renpy.get_game_runtime()
    default time_left = time_limit
    
    timer 0.05 repeat True action [
        SetScreenVariable("time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
        If(time_left <= 0, true=[Hide("qte_choice_timer_3"), Jump("silent_guilt")], false=NullAction())
    ]
    
    $ progress = time_left / time_limit
    
    # 警告色：时间少于30%变红
    $ bg_pulse = 0.1 if progress < 0.3 else 0.0
    
    # 背景闪烁警告
    if progress < 0.3:
        add Solid("#ff000010") at transform:
            alpha 0.0
            block:
                linear 0.2 alpha 0.3
                linear 0.2 alpha 0.0
                repeat
    
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 30
        
        textbutton "(Keep silent)":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_3"), Jump("silent_guilt")]
        
        textbutton "(Question her back)": 
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_3"), Jump("silent_argue")]

    # ===== 底部倒计时条 =====
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -40
        xsize 1400
        ysize 25
        background "#1a1a1a"
        
        # 内部进度条
        add "white_time_bar":
            xalign 0.5
            xsize int(1400 * progress)
            ysize 15
        
        # 时间文字
        text "[time_left:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"

label stay_silent_continue:
    call screen qte_choice_timer_3(
        question="",
        time_limit=3.0
    )
    return

label silent_guilt:
    s "{i}A wave of guilt rises in your chest.{/i}"
    s "I’ll give you the money. Please stop saying things like that."
    $ money -= 1200
    show mother_04_smile with dissolve:
        zoom 0.83
        xpos 1360
        ypos 260
    hide mother_02_smallmouth
    hide mother_03_unhappy
    mom "Good girl. I knew you were sensible. Your brother will thank you."
    hide mother_04_smile with dissolve
    "{i}-1,200 yuan. Current balance: [money] yuan{/i}"
    # $ mental = mental - 1 if 'mental' in globals() else -1
    jump family_tax_end

label silent_argue:
    s "So now you’re forcing me to scrimp and save to support my younger brother?"
    $ mother_anger += 1
    jump argue_continue

# QTE第四题
screen qte_choice_timer_4(question, time_limit=5.0):
    modal True
    
    default start_time = renpy.get_game_runtime()
    default time_left = time_limit
    
    timer 0.05 repeat True action [
        SetScreenVariable("time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
        If(time_left <= 0, true=[Hide("qte_choice_timer_4"), Jump("silent_guilt")], false=NullAction())
    ]
    
    $ progress = time_left / time_limit
    
    # 警告色：时间少于30%变红
    $ bg_pulse = 0.1 if progress < 0.3 else 0.0
    
    # 背景闪烁警告
    if progress < 0.3:
        add Solid("#ff000010") at transform:
            alpha 0.0
            block:
                linear 0.2 alpha 0.3
                linear 0.2 alpha 0.0
                repeat
    
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 30
        
        textbutton "I have my own life too...":
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_4"), Jump("angry_game_own_life")]
        
        textbutton "Why am I responsible for his shoes?": 
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_4"), Jump("angry_game_unresponsible")]

        textbutton "(Stay silent)": 
            xalign 0.5
            background Frame("gui/textbox.png")
            hover_background Frame("blue_textbox")
            padding (180, 0)
            text_color "#888888"
            text_hover_color "#ffffff"
            action [Hide("qte_choice_timer_4"), Jump("angry_game_calculation")]

    # ===== 底部倒计时条 =====
    frame:
        xalign 0.5
        yalign 1.0
        yoffset -40
        xsize 1400
        ysize 25
        background "#1a1a1a"
        
        # 内部进度条
        add "white_time_bar":
            xalign 0.5
            xsize int(1400 * progress)
            ysize 15
        
        # 时间文字
        text "[time_left:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"

label argue_continue:
    show mother_05_soangry:
        zoom 0.83
        xpos 1360
        ypos 260
    mom "Did we raise you all these years for nothing? He’s your own brother. If he’s the only one in class who can’t afford new shoes, people will look down on him!"
    mom "Besides, if you help your brother now, he’ll help you in the future. How is that a loss?"
    show mother_03_unhappy with dissolve:
        zoom 0.83
        xpos 1360
        ypos 260
    hide mother_05_soangry with dissolve
    mom "We’re all family, aren’t we? When your father and I paid for your education, we didn’t keep score like this."
    call screen qte_choice_timer_4(
        question="",
        time_limit=5.0
    )
    return
    jump angry_game_calculation

label angry_game_own_life:
    $ mother_anger += 1
    jump angry_game_calculation

label angry_game_unresponsible:
    $ mother_anger += 2
    jump angry_game_calculation

label angry_game_calculation:    
    if mother_anger >= 3:
        show mother_06_sosoangry:
            zoom 0.83
            xpos 1360
            ypos 260
        mom "How did I raise such an ungrateful child!"
        hide mother_01_bigmouth
        hide mother_02_smallmouth
        hide mother_03_unhappy
        hide mother_05_soangry
        hide mother_06_sosoangry with dissolve
        "{i}Mom hangs up in a fury.{/i}"
        "{i}A few days later, she sends you a message as if nothing happened. But you remember.{/i}"
        jump family_tax_end
    else:
        mom "Forget it. You can’t squeeze out a single word after half an hour. We’ll talk when you get paid."
        hide mother_01_bigmouth
        hide mother_02_smallmouth
        hide mother_03_unhappy with dissolve
        "{i}You barely manage to hold things together and keep the money, but your chest feels hollow.{/i}"
        jump family_tax_end

label family_tax_end:
    "{i}手机随后震动。{/i}"
    '小紫书 你的粉丝'"姐妹，看到你发家里要钱的事了。同款遭遇，你不是一个人。"
    $ xiaohongshu_contact = True
    "{i}新联系人：小紫书姐妹{/i}"
    jump task_1_6

# ========== 任务1.6：不经意的触碰 ==========
transform shock:
    linear 0.2 xoffset 10 yoffset -10
    linear 0.1 xoffset -10 yoffset 10
    linear 0.2 xoffset 0 yoffset 0
label task_1_6:
    scene tea_room with fade
    "{i}第3周，工作日。{/i}"
    show she_05_happy_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "咖啡，嘿嘿🎵~"
    hide she_05_happy_nobag onlayer top
    show she_06_surprise_eye_nobag onlayer top at shock:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}有人从你上方伸过手来。{/i}"
    
    show chen_06_surprise with dissolve:
        zoom 0.9
        xzoom -1
        xpos 1358
        ypos 162
    chen "抱歉，我拿一下方糖……"
    show chen_04_frontsmile:
        zoom 0.9
        xzoom -1
        xpos 1350
        ypos 161
    chen "哦，你也在泡咖啡？"
    "{i}他站得很近，拿糖的时候手臂擦过你。{/i}"
    
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
    show she_03_tinysmile_eye_nobag onlayer top with dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_06_surprise_eye_nobag onlayer top
    s "是的，早上喝一杯咖啡比较精神"
    hide chen_06_surprise
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_a

label touch_alert:
    s "……"
    s "哈哈，是。"
    show she_02_sweat_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "{i}他为什么站这么近？{/i}"
    hide chen_06_surprise
    show chen_02_smile_front with dissolve:
        zoom 0.9
        xzoom -1
        xpos 1358
        ypos 162
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    hide chen_04_frontsmile
    jump task_1_6_bc

label touch_move:
    hide chen_06_surprise
    hide she_06_surprise_eye_nobag onlayer top
    show she_01_normal_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
        linear 0.6 xpos -50 ypos 240
    s "是，喝一杯咖啡工作起来比较精神"
    show chen_04_glance:
        zoom 0.9
        xzoom -1
        xpos 1350
        ypos 161
    "{i}陈永仁没明显反应。但你一动，他眼神扫了你一下。{/i}"
    hide chen_04_glance
    chen "你工作完成得很好。顺便说一句，拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_bc

label task_1_6_a:
    chen "我先走了，工作加油。"
    hide chen_04_frontsmile with moveoutright
    hide chen_02_smile_front with moveoutright
    jump task_1_6_end

label task_1_6_bc:
    chen "我先走了，工作加油。"
    hide chen_04_frontsmile with moveoutright
    hide chen_02_smile_front with moveoutright
    "{i}他走了，咖啡杯的热气缓缓蒸腾着。{/i}"
    jump task_1_6_end

label task_1_6_end:
    # show she_01_normal_eye_o_nobag onlayer top at top_dissolve:
    #     zoom 0.8
    #     xzoom -1.0
    #     xpos -30
    #     ypos 240
    hide she_01_normal_eye_nobag onlayer top
    hide she_02_sweat_eye_nobag onlayer top
    hide she_03_tinysmile_eye_nobag onlayer top
    hide she_09_unhappy onlayer top
    play sound "phone_vibration.mp3" #替换短版
    show linjie_wx_lockscreen with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    show linjie_wx_0 with dissolve: 
        zoom 1.4
        align (0.5, 0.45)
        pause 1.0
    linjie "看到你和陈永仁在茶水间了，注意点。"
    
    menu:
        "什么意思？":
            show linjie_wx_a1:
                zoom 1.4
                align (0.5, 0.45)
            s "注意什么？"
            show linjie_wx_a2:
                zoom 1.4
                align (0.5, 0.45)
            linjie "没什么。接完水快回来，有个新的brief发你了。"
            show linjie_wx_a3:
                zoom 1.4
                align (0.5, 0.45)
            $ linjie_interest += 1
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "没什么事。":
            show linjie_wx_b1:
                zoom 1.4
                align (0.5, 0.45)
            s "没什么事啊。"
            show linjie_wx_b2:
                zoom 1.4
                align (0.5, 0.45)
            linjie "……随你。"
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "删除消息":
            show linjie_wx_c1:
                zoom 1.4
                align (0.5, 0.45)
            "{i}消息已删除。{/i}"
            $ escape += 1
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2

        "思索":
            s "林姐平常不说这些的，怎么……"
            "{i}你正揣摩这条消息的的意图，斟酌着打下回复，又有新消息发来了。{/i}"
            show linjie_wx_d1:
                zoom 1.4
                align (0.5, 0.45)
            linjie "接完水快回来，有个新的brief发你了。"
            show linjie_wx_d2:
                zoom 1.4
                align (0.5, 0.45)
            $ linjie_interest += 1
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 2.0
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
            text"Payslip" size 28
            
            null height 20
            
            # 基本信息
            hbox:
                text"Name:"
                text"SHEH Siu Man"
            hbox:
                text"Department:"
                text"Design Dept."
            hbox:
                text"Date:"
                text"March 2028"
            
            null height 20
            
            # 工资明细（可点击展开）
            vbox:
                spacing 10
                
                # 基本工资
                hbox:
                    xfill True
                    text"Basic Salary"
                    text"16,500" xalign 1.0
                
                # 绩效工资（悬停效果）
                button:
                    xfill True
                    action NullAction()
                    background None
                    
                    hbox:
                        xfill True
                        text"Performance Adjustment"xalign -0.07
                        text"0" xalign 1.05
                    
                    # 悬停提示
                    tooltip "无说明"
                    
                    hovered Show("payslip_tooltip", msg="无说明")
                    unhovered Hide("payslip_tooltip")
                
                # 其他项目
                hbox:
                    xfill True
                    text"Transportation Allowance"
                    text"500" xalign 1.0
                
                hbox:
                    xfill True
                    text"Meal Allowance"
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
                    text"Net Pay" xalign -0.07
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
    scene home_ceiling #后期改
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
    scene home_ceiling
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
            text "【Clue】 Yin‑Yang Wage Divide" size 28
            null height 30
            add Solid("#cccccc") xsize 600 ysize 1
            null height 30
            text "Sky and earth, shade and glow; her and him, split below." size 24 xalign 0.5
            null height 40
            
            textbutton "收起":
                text_size 24
                xalign 0.5    
                # 关键：使用Return()结束call screen
                action [Hide("clue_unequal_wage"), Return()]

label ask_xiaojin_directly:
    scene office with fade
    
    "{i}The next day during lunch break, you find Siu Gam.{/i}"
    
    show she_01_normal_eye_o_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "Siu Gam, can I ask you something? What was your starting salary when you first joined the company?"
    
    show jin_03_awkward with dissolve:
        zoom 0.97
        xpos 1360
        ypos 150
    xiaojin "Uh… well…"
    xiaojin "22.5k… The company forbids us from discussing salaries with each other. Don’t tell anyone, okay?"
    show jin_04_question:
        zoom 0.97
        xpos 1360
        ypos 150
    xiaojin "Why are you bringing this up all of a sudden?"
    
    s "I get 19.5k."
    
    show jin_05_shocked:
        zoom 0.97
        xpos 1360
        ypos 150
    xiaojin "Oh shit……"
    hide she_01_normal_eye_o_nobag onlayer top at top_dissolve
    scene black    
    # 任务更新界面
    play sound "clue.ogg"
    call screen clue_unequal_wage("线索") with dissolve
    
    "{i}[Clue] Yin‑Yang Wage Divide{/i}" #加音效：噔噔噔↑

    $ salary_evidence = True
    $ investigation_unlocked = True
    $ linjie_interest += 1
    
    jump fitness_video_event

# 选项B：不问
label dont_ask_xiaojin:
    scene home_ceiling with dissolve
    
    "{i}等心跳没那么快时，你放下了手机。{/i}"
    
    s "不问，就不会尴尬。不问，就不会惹麻烦。"

    "{i}你起身去洗漱，仿佛什么都没发生。{/i}"
    "{i}涟漪过后，风平浪静。涟漪下有没有更深的漩涡……{/i}"
    "{i}谁知道呢。{/i}"
    $ escape += 1 
    
    jump fitness_video_event

# 选项C：其他方式调查
label investigate_other_ways:
    scene home_laptop with dissolve
    s "还是先自己查查看吧。"
    "【正在浏览】{i}公司招聘网站：公司同岗位的薪资范围{/i}"
    "【正在浏览】{i}内部文档：薪酬制度细则{/i}"
    "【正在浏览】{i}匿名论坛：公司薪资讨论版块{/i}"

    play sound "clue.ogg"
    call screen clue_unequal_wage("线索") with dissolve
    "{i}获得了线索：阴阳工资{/i}" #加音效：噔噔噔↑

    $ investigation_unlocked = True
    
    "{i}在调查中，你发现很多资料来自和你有相似经历的前辈。{/i}"
    "{i}坏消息，走到这条路上的不止你一个人。{/i}"
    "{i}好消息是，走在这条路上的不止你一个人。{/i}"

    $ investigation_skill += 1
    $ linjie_interest += 1

    jump fitness_video_event

# 健身视频事件
label fitness_video_event:
    scene home_ceiling with fade
    
    "{i}Week 6, Saturday night.{/i}"
    "{i}You lie in bed scrolling through your phone, but your eyelids are already getting heavy.{/i}"
    
    show lockscreen with moveinbottom:
        zoom 1.5
        xalign 0.5
        yalign 0.35 #锁屏时间

    s "23:55. I can't believe it's already this late."

    s "A message from Chan Wing Yan...?"

    hide lockscreen
    show pyq with dissolve:
        zoom 1.5
        xalign 0.5
        yalign 0.35

    "{i}Chan Wing Yan: Just finished working out. You can try the techniques I posted on Moments. They’re great for relieving stress.{/i}"

    menu:
        "Watch the video":
            jump watch_fitness_video
        
        "Ignore the video":
            jump ignore_video
        
        "Like the video":
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
    show pyq at rotate_right #后续改这个
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

    "Thirty seconds. Chan is at the gym, the metallic sheen of the equipment glinting off his sweat."
    "He performs precise movements, his muscles rising and falling with each breath."
    "On the final second, he suddenly stares straight into the camera."
    
    hide gym_02
    hide gym_03
    show gym_01:
        linear 0.4 zoom 1.55 xpos 2180 ypos 1430
        linear 0.1 zoom 1.5 xpos 2130 ypos 1400
    chen "Can you keep up, Siu Man?"
    
    scene black with fade
    "视频结束，黑屏。你的脸也黑了。"
    show home_ceiling with fade
    # hide screen video_player
    # with dissolve
    
    # $ fitness_video_watched = True
    show pyq at shock:
        zoom 1.5
        xalign 0.5
        yalign 0.35
    s "呃…………" #（有某种不适感在胃里蔓延）
    
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
    
    "{i}你锁屏，把手机倒扣在床头柜上。{/i}"
    "{i}23:55。这个时间，这个内容。{/i}"
    "{i}直觉告诉你，有些东西不需要打开。{/i}"
    "{i}手机又震了一下，但你没有看。{/i}"
    
    #选择安全，但错过了观察对方行为模式的机会
    
    jump celebration_drink

# 选项C：回赞
label reply_thumb_up:
    scene bg bedroom_night
    with dissolve
    
    "{i}你没看视频，敷衍了一个赞。{/i}"
    "{i}【微信】陈总：这么晚还没睡？{/i}"
    "{i}消息秒回。你看着那个正在输入的提示，决定不再回复。{/i}"
    #保持了表面和平，但对方可能认为这是个信号）
    
    jump celebration_drink

# 视频事件后续
label after_video:
    scene office with fade

    "{i}第二天办公室，午餐时。{/i}"
    show she_03_tinysmile_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "哎，你昨晚看到陈总朋友圈的健身视频没？有点东西。"
    show jin_02_frown with dissolve:
        zoom 0.97
        xpos 1360
        ypos 150
    xiaojin "我好像没看到耶？可能没刷到吧。"
    show she_05_happy_sweat_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "……哦，这样啊。"
    hide she_03_tinysmile_eye_nobag onlayer top
    hide she_05_happy_sweat_nobag onlayer top
    hide jin_02_frown with dissolve
    
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
    scene bar_outside with fade
    
    "第7周，His Game项目成功上线。"
    "数据表现超过预期，部门办庆功酒，酒水畅饮，陈永仁买单。所有人都来了。"

    jump bar_interaction

# 酒吧交互界面
# 箭头跳动特效
transform heartbeat_bar1: #上下跳
        linear 0.6 zoom 0.9 yoffset 2
        linear 0.6 zoom 0.9 yoffset -2
        repeat
transform heartbeat_bar2: #左右跳
        linear 0.6 zoom 0.9 xoffset 2
        linear 0.6 zoom 0.9 xoffset -2
        repeat
transform arrow_style_ud:
        on idle:
            heartbeat_bar1
        on hover:
            zoom 1.05 
transform arrow_style_lr:
        on idle:
            heartbeat_bar2
        on hover:
            zoom 1.05 

# 初始化酒吧场景
# 本场景bgm循环播放
screen bar_scene():

    # 1. 酒单（左侧）
    imagebutton at arrow_style_ud:
        xpos 440
        ypos 330
        idle "arrow_down"
        hover "arrow_down"
        action [Hide("bar_scene", fade), Jump("bar_menu_choice")]
    
    # 2. 小金（大声聊天区域）
    imagebutton at arrow_style_lr:
        align(0.01, 0.5)
        idle "arrow_left"
        hover "arrow_left"
        action If(talk_to_xiaojin, [Hide("bar_scene", fade), Jump("talk_to_xiaojin_again")], 
            [Hide("bar_scene", fade), Jump("talk_to_xiaojin")]
            )
        
    # 3. 林姐（角落卡座）
    imagebutton at arrow_style_ud:
        align (0.5, 0.05)
        idle "arrow_up"
        hover "arrow_up"
        action If(sit_with_lin, [Hide("bar_scene", fade), Jump("sit_with_lin_again")], 
            [Hide("bar_scene", fade), Jump("sit_with_lin")]
            )

    # 4. 陈永仁（中心位置）
    imagebutton at arrow_style_lr:
        align (0.99, 0.5)
        idle "arrow_right"
        hover "arrow_right"
        action If(observe_chen, Jump("observe_chen_again"), Jump("observe_chen"))
    
    # 5. 洗手间（逃离）
    imagebutton at arrow_style_ud:
        align (0.5, 0.95)
        idle "arrow_down"
        hover "arrow_down"
        action If(bar_restroom, Jump("bar_restroom_again"), Jump("bar_restroom"))

# 酒吧交互主循环
label bar_interaction:
    scene bar_inside with fade
    show screen bar_scene with dissolve
    pause 0.3
    "{i}酒吧里人声鼎沸。你想做什么？{/i}"
    $ ui.interact()

# 检查函数 - 统一检查所有条件
label check_all_bar_conditions:
    if talk_to_xiaojin and sit_with_lin and observe_chen and bar_restroom and bar_menu_choice:
        jump bar_ending
    else:
        jump bar_interaction

# 酒单选择
screen drink_menu:
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.6
        
        textbutton "啤酒": 
            action [Hide("drink_menu"), Jump("beer")]
        textbutton "红酒": 
            action [Hide("drink_menu"), Jump("wine")]
        textbutton "鸡尾酒": 
            action [Hide("drink_menu"), Jump("cocktail")]
        textbutton "汽水": 
            action [Hide("drink_menu"), Jump("soda")]

label bar_menu_choice:
    hide screen bar_scene
    scene bar_drinkmenu

    show screen drink_menu
    $ ui.interact()
    
    # jump check_all_bar_conditions

# 和小金聊天 - 修复：简化结构，确保变量设置正确
label talk_to_xiaojin:
    hide screen bar_scene
    scene bar_counter
    
    "{i}小金正在大声说着什么，周围几个人在笑。{/i}"
    "{i}和他聊点什么呢？{/i}"
    menu:
        
        "运动":
            $ xiaojin_topic = "sport"
            show she_03_tinysmile_eye_nobag onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            show jin_drunk:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "你来啦？"
            
            show jin_04_question:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "对了，前几天你问我陈总朋友圈是……"

            show she_05_happy_nobag onlayer top:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            hide she_03_tinysmile_eye_nobag onlayer top
            s "哦，偶然看到，就打算试试健身。你有没有什么健身经验分享的？"
            
            hide jin_04_question with dissolve
            xiaojin "有啊！我跟你说，蛋白粉就要选……"
            hide she_05_happy_nobag onlayer top
            scene black with dissolve
            "{i}他把自己的健身心得倾囊相授，真是个好人。{/i}"
            
        "吐槽工作":
            $ xiaojin_topic = "work"
            show she_10_tired onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "我来了……这个项目真是累死了……"
            show jin_02_frown with dissolve:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "对吧！有时候觉得AI取代不了我们，因为根本读不懂甲方七零八落的诉求。"
            "{i}你们一起吐槽了半小时甲方，英雌惜英雄。{/i}"
            hide she_10_tired onlayer top
            hide jin_02_frown with dissolve
            scene black with dissolve
            
        "恋爱话题":
            $ xiaojin_topic = "love"
            show jin_02_frown:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "你知道最近隔壁部门小x的男朋友和她冷战不？"
            show she_11_interest onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "嗯？新瓜，细说！"
            xiaojin "小x和男朋友恋爱挺久了，最近她男朋友求婚，但是小x想这几年多专注在事业，往后推推。"
            xiaojin "她男朋友觉得求婚被拒，正沮丧，等着小x哄中……"
            show she_05_sohappy_nobag onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "那他可得等等了，小x手上的项目后天才交呢。小x姐，女王。"
            hide she_11_interest onlayer top
            show jin_drunk:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "小x姐，女王！"
            hide she_05_sohappy_nobag onlayer top
            scene black with dissolve
    # 关键修复：在menu结束后统一设置变量
    $ talk_to_xiaojin = True
    $ xiaojin_interest += 1
    hide jin_drunk with dissolve
    jump check_all_bar_conditions

label talk_to_xiaojin_again:
    hide screen bar_scene
    show bar_counter
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
    scene bar_booth with dissolve
    
    "{i}角落的卡座，林姐一个人坐在那里，光影在她脸上切割出明与暗。{/i}"
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "你做得太好了。好得过头了。"
    show she_01_normal_eye_o_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "什么意思？"
    show linjie_04_frown:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "作为新人，陈永仁很中意你——非常中意。"
    "{i}她晃了晃酒杯，冰块碰撞发出清脆的声响。{/i}"
    show linjie_06_bar_closeeyes with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "他也这样注意过我，后来就不了。"
    s "……发生了什么？"
    "{i}酒有些辣，林姐长饮一口，好一会儿才说话。{/i}"
    show linjie_06_bar with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "我老了，对他来说，现在我只是有用。"
    "{i}她没有回答你的问题，像是醉了。{/i}"
    show linjie_06_bar_notlikeme:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "去别的地方转转吧，别和我一样。"
    hide she_01_normal_eye_o_nobag onlayer top

    scene black with dissolve
    pause 1.0

    #这里加脚步声或者其他音效，表现小曼转身林姐追上来叫住她
    linjie "哎——" with vpunch
    show bar_booth

    show linjie_03_delicate:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "别认为“在他眼里我很特别”。"
    show linjie_02_smile:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "你本来就特别。"
    linjie "不是因为他。"
    hide linjie_03_delicate
    hide linjie_02_smile with dissolve
    
    $ sit_with_lin = True
    $ hidden_truth_unlocked = True
    
    # 关键修复：使用call screen而不是show screen + ui.interact()
    play sound "clue.ogg"
    call screen clue_moderec
    
    jump check_all_bar_conditions

label sit_with_lin_again:
    hide screen bar_scene
    show bar_booth
    linjie "怎么又回来了？让我一个人待会儿，你出去转转吧。"
    jump check_all_bar_conditions

# 观察陈永仁
label observe_chen:
    hide screen bar_scene
    show bar_chen with fade
    
    show chen_02_smile with dissolve:
        zoom 0.9
        xzoom 1.0
        xpos 690
        ypos 162
    "{i}你站在人群边缘，看着陈永仁。{/i}"
    "{i}他对男同事：拍肩、大笑、讲黄色笑话。{/i}"
    "{i}他对女同事：靠近、倾听、眼神专注。{/i}"
    "{i}他对上级：谦卑、递烟、不时倒酒。{/i}"
    hide chen_02_smile

    show chen_06_surprise:
        zoom 0.9
        xzoom 1.0
        xpos 683
        ypos 162 
    "{i}他发现你在不远处……{/i}"
    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom 1.0
        xpos 688
        ypos 161
    hide chen_06_surprise
    "{i}于是看向你，微笑。{/i}"

    "{i}他总能根据不同对象，切换最佳模式。{/i}"
    hide chen_04_frontsmile
    
    $ observe_chen = True
    $ investigation_skill += 1
    jump check_all_bar_conditions

label observe_chen_again:
    hide screen bar_scene
    show bar_chen with dissolve
    "{i}他还在和人推杯换盏……{/i}"
    jump check_all_bar_conditions

# 洗手间逃离
label bar_restroom:
    hide screen bar_scene
    
    scene restroom with fade
    
    "{i}躲进洗手间锁上门，外面的说话声、碰杯声都远去了。{/i}"
    "{i}镜子里的人脸颊微红。{/i}"
    play sound "phone vibration.mp3"
    pause 1.0
    show restroom_wx with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    "【微信】{i}妈：「你什么时候回家？」{/i}"
    "【微信】{i}闺蜜：「那个项目怎么样了？」{/i}"
    hide restroom_wx with dissolve
    "{i}你深吸一口气，现在你暂时逃离了那个世界。{/i}"
    "{i}但你知道，总得回去，过明天。{/i}"

    $ bar_restroom = True
    jump check_all_bar_conditions

label bar_restroom_again:
    hide screen bar_scene
    show restroom with dissolve
    "{i}洗手间有人，先出去吧。{/i}"
    jump check_all_bar_conditions

# 酒单选酒
label beer:

    $ drink_choice = "beer"
    $ bar_menu_choice = True
    "{i}一杯精酿啤酒，泡沫细腻。{/i}"
    "{i}人生得意须尽欢，此刻的泡沫托起你所有的轻盈。{/i}"
    hide screen drink_menu
    jump check_all_bar_conditions

label wine:
    $ drink_choice = "wine"
    $ bar_menu_choice = True
    "{i}红酒在杯中摇晃，颜色深沉。{/i}"
    "{i}葡萄美酒夜光杯，敬那个在深夜依然一往无前的自己。{/i}"
    hide screen drink_menu
    jump check_all_bar_conditions

label cocktail:
    $ drink_choice = "cocktail"
    $ bar_menu_choice = True
    "{i}五颜六色的液体，不知道里面有什么。{/i}"
    "{i}彩虹沉入杯底，等你打捞。每一口都是未知，每一步都是风景。{/i}"
    hide screen drink_menu
    jump check_all_bar_conditions

label soda:
    $ drink_choice = "soda"
    $ bar_menu_choice = True
    "{i}可乐加冰，气泡刺激着喉咙。{/i}"
    "{i}众人皆醉我独醒。猛兽总是独行，牛羊才成群结队。{/i}"
    hide screen drink_menu
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
    
    scene street with fade
    
    "{i}夜深了，大家陆续离开。{i}"
    "{i}凉风吹在脸上，路灯是朦胧的，微醺的感觉。{i}"
    
    s "看看地铁时间……"
    s "啊……末班车还有15分钟到，要过去地铁站时间有点紧啊……"
    
    #音效+图片表示：一辆车滑停在身边，车窗降下
    scene car
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    chen "上车吧，我们顺路。"
    
    if investigation_skill > 1:
        $ notice_take_ride("他怎么知道顺不顺路？", "他问过我住在哪里吗？")
    else:
        pass
    
    "{i}要上车吗？{/i}"
    menu:
        #音效：心跳
        
        "上车":
            "那谢谢陈总了。"
            $ car_event = True 
            jump get_in_car
        
        "我坐地铁。":
            jump refuse_car_safe
        
        "你怎么知道我住哪？":
            jump question_chen

# 选项A：上车
label get_in_car:
    #要开车门的音效
    scene car_inside with fade
    "{i}拉开车门，坐进副驾驶，你感觉到皮革座椅的冰凉，闻到车内淡淡的古龙水味。{/i}"
    chen "系好安全带。"
    jump chapter3

# 选项B：安全拒绝
label refuse_car_safe:
    show she_03_tinysmile_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "不用了，我坐地铁，挺方便的。"
    
    show chen_05_wanwei with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1356
        ypos 162
    chen "末班车快没了，你确定？"
    
    s "我赶得上，谢谢陈总。"
    
    "{i}你后退一步，点头致谢。{/i}"
    
    #音效+图片，车开走
    scene street with dissolve
    "{i}黑夜里尾灯消失，光线渐暗，但你感到十分心安。{/i}"
    hide she_03_tinysmile_eye onlayer top

    jump safe_ending

# 选项C：质问（压力抉择）
label question_chen:
    show she_02_sweat_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "您怎么知道我住在哪？"
    show chen_00_body:
        zoom 0.9
        xzoom -1.0
        xpos 1356
        ypos 438
    hide chen_01_normal

    show chen_02_smile:
        zoom 0.9
        xzoom -1.0
        xpos 1349
        ypos 161
    chen "HR档案里记着大家的联络地址，我记得自己手底下所有团队成员的信息。"
    
    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1349
        ypos 162
    hide chen_02_smile with dissolve
    chen "这是关心的方式，就像现在问你要不要搭便车一样。"
    show chen_04_glance with dissolve:
        zoom 0.9
        xzoom -1
        xpos 1350
        ypos 161
    chen "怎么样，走吗？"
   
    menu:
        
        "上车":
            show she_01_normal_eye onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            "{i}你意识到继续对峙没有意义。{/i}"
            hide she_01_normal_eye onlayer top
            s "……那麻烦您了。"
            hide she_02_sweat_eye onlayer top
            scene black with dissolve
            #音效：关车门
            $ car_event = True
            jump get_in_car
        
        "仍然拒绝":
            show she_01_normal_eye onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "我还是坐地铁吧，谢谢您关心。"
            hide she_02_sweat_eye onlayer top
            hide she_01_normal_eye onlayer top
            scene black with fade
            "{i}背后的沉默像浓重的夜色，但你走得坚定无比。{/i}"
            jump safe_ending

# 尴尬拒绝后续
label safe_ending:
    scene subway_station with fade
    show she_12_breathe onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}你冲进地铁站。{/i}"
    
    show she_05_happy_sweat onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "末班车还有3分钟。赶上了！"
    hide she_12_breathe onlayer top
    hide she_05_happy_sweat onlayer top
    
    scene subway_inside with fade
    "{i}车厢里空荡荡的，你坐在角落，剧烈喘息。{/i}"
    
    play sound "phone vibration.mp3"
    pause 1.0
    show chen_wx_lockscreen with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    pause 1.0
    chen "注意安全。"
    s "……"
    hide chen_wx_lockscreen with dissolve
    
    jump chapter_2_end

# chapter 2结束，安全支线
label chapter_2_end:
    scene black with dissolve
    pause 1.0 
    
    "{i}你终于回到家，锁上门。{i}"
    show she_13_sigh onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    pause 1.0
    scene home with fade
    hide she_13_sigh onlayer top
    show she_14_think onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "……"
    if hidden_truth_unlocked:
        "{i}放下包，靠在门上，林姐的话在耳边回响：{/i}"
        "{i}「别认为“他”让你觉得自己特别。」{/i}"
        "{i}这一周结束了，His Game成功了。{/i}"
        show she_15_unflinched onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        "{i}但某种游戏，才刚刚开始。{/i}"
        "{i}游戏的一方是陈永仁，但你隐隐感觉自己不是另一方唯一的执棋人。"
        hide she_15_unflinched onlayer top
    hide she_14_think onlayer top
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
    
    scene office with fade
    
    "{i}设计部的人与物，九点准时刷新在这里。一切看起来和往常一样。{/i}"

    # 陈永仁走廊相遇
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    chen "早啊小曼！昨天休息得还好吧。"
    
    show she_02_sweat_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "……啊，陈总早。"

    hide chen_01_normal with dissolve
    show she_09_unhappy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}那种语气、那种压力——昨天微妙的一切都已经从他身上消失。{/i}"
    hide she_02_sweat_eye_nobag onlayer top
    s "如果我都无法抓住那一丝恶意，又怎么证明给其他人。"
    hide chen_normal with dissolve
    
    # 小金关心
    show jin_04_question with dissolve:
        zoom 0.97
        xpos 1360
        ypos 150
    show she_01_normal_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    xiaojin "嘿，你脸色不太好。昨晚失眠了？"
    hide she_09_unhappy onlayer top

    menu:
        "借口搪塞":
            show she_05_happy_sweat_nobag onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "嗯，宿醉头晕，没睡好。"
            show jin_02_frown:
                zoom 0.97
                xpos 1360
                ypos 150
            xiaojin "嗐，我也一样，早知道少喝点了"
            hide jin_02_frown with dissolve
            hide she_05_happy_sweat_nobag onlayer top

        "沉默":
            s "…………" 
            xiaojin "……呃，看来是困懵了？你中午好好补个觉，我不打扰了。"
            hide jin_04_question with dissolve
             
        "求助小金":
            show she_15_unflinched_card onlayer top at top_dissolve:
                zoom 0.8
                xzoom -1.0
                xpos -30
                ypos 240
            s "陈总有问题。"
            s "你愿意跟我一起揭发他吗？"
            hide she_01_normal_eye_nobag onlayer top
            jump search_fail

    hide she_01_normal_eye_nobag onlayer top
    scene black with fade
    s "现在得先搜集证据。"
    s "在证据集齐前，要装作一切如常。"
    
    jump harrassment_evidence

label search_fail:
    show jin_03_awkward:
        zoom 0.97
        xpos 1360
        ypos 150
    xiaojin "呃……小曼"
    hide jin_04_question
    hide jin_03_awkward
    show she_16_shocked onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_15_unflinched_card onlayer top
    show chen_04_frontsmile with vpunch:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    chen "哈哈大家聊什么呢，我也来听听。"
    show chen_04_glance with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    chen "一个好上司，可要记得自己手底下所有团队成员的信息，包括聊天喜好……"
    chen "对吗，小曼？"
    hide she_16_shocked onlayer top
    scene black with fade
    show chen_08_horrible with dissolve:
        zoom 2.0 xalign 0.45 ypos -600
        linear 1.5 zoom 2.0 xalign 0.45 ypos -500
        linear 0.1 zoom 7 xalign 0.65 ypos -800
    pause 1.5
    jump ending_gulang
        
        


# 实体证据搜证
label harrassment_evidence:
    scene home with fade
    
    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "{i}陈永仁如果性骚扰女同事，总有引诱对方营造假象的一段时间。{/i}"
    s "{i}看他的全家福照片，他已经结婚了，那他不太可能把用来经营其他女性社交关系的东西放在家……{/i}"
    s "{i}也许，他的办公室是一个突破口。{/i}"
    show she_14_think onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "{i}陈永仁下班后办公室会上锁，如果要进去搜查，只有上班的这段时间。怎么才能在不打草惊蛇的情况下进去找证据呢……{/i}"
    hide she_14_deepthink onlayer top
    show she_15_idea onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "……等等"
    hide she_14_think onlayer top
    hide she_15_idea onlayer top

    # 检查林姐关系
    if linjie_interest >= 3:
        jump linjie_help
    else:
        jump linjie_refuse_help
        

label linjie_help:
    scene corridor with fade
    s "林姐，我……"
    s "昨天晚上庆功宴结束，陈总要送我回家。"

    linjie "!"

    s "……我有点东西丢在车上了，不知道陈总是不是把东西放在办公室里，我想去看看。"
    s "不知道是不是只有我丢了东西，如果可能，我想替大家把失物带回来。"
    s "……即使无法弥补曾经那个空缺，也多少能在今后有个心安。"
    s "你愿意帮帮我吗？"
    
    # 两人对视
    # 调虎离山
    
    linjie "………………"
    linjie "……我这里还有些文件要处理，先走了。"

    # 小曼失落
    scene office_desk with fade
    "{i}回到工位上，你继续想着搜证的办法。{/i}"
    # 脚步声音效
    s "哎？"
    "{i}林姐从你旁边快速走过，她手机里传来微信电话的声音。{/i}"
    linjie "陈总吗，这里有个甲方的视觉需求我需要找您确认一下，需要在11楼会议室放映，您现在有别的日程吗。"
    linjie "了解，最多耽误您5分钟行吗？"
    linjie "好的，我准备好设备了。"
    "{i}你从工位上看到陈永仁从办公室出来，快步走向电梯。{/i}"
jump cyro_office_start

label linjie_refuse_help:
    s "林姐，我……"
    s "昨天晚上庆功宴结束，陈总要送我回家。"

    linjie "!"

    s "……我想找证据争一个结果，不管是好是坏"
    s "听你昨天的话，我觉得你是明白的。我计划今天去陈总办公室试试，你能帮我吗？"

    linjie "佘小姐，昨晚我喝多了，你说的这些我不太记得。"
    linjie "如果昨天和你大吐苦水，说了太多我走到今天的诸多不易，给你造成困扰了，是我失态。"
    linjie "不好意思，我手上还有工作，不能奉陪。"
    #林姐走开
    scene black
    linjie "但无论如何，希望你今后顺利。"

    s "……"
    s "谢谢。"
    
    show office_desk with dissolve
    s "{i}林姐拒绝了，接下来怎么办呢？{/i}"
    menu:
        "自己搜查":
            s "趁陈永仁不在时抓紧时间进办公室找找看吧。"
            jump cyro_break_in
        "找别的办法":
            s "再想想别的办法吧。"
            jump chapter4_end

    # # 5分钟倒计时搜查
    # call screen cyro_office_timer(duration=300.0)  # 5分钟 = 300秒

# 陈永仁办公室：5分钟搜查
# 复制到 game/cyro_office_search.rpy 即可
# ============================================================


# ---------- 全局变量：全部加 cyro_office_ 前缀，避免和其他 default 冲突 ----------

default cyro_office_time_left = 300

default cyro_office_found_files = False
default cyro_office_found_perfume = False
default cyro_office_found_notebook = False
default cyro_office_found_photo = False
default found_evidence = 0

init python:

    def cyro_office_format_time(seconds):
        seconds = max(0, int(seconds))
        m = seconds // 60
        s = seconds % 60
        return "%02d:%02d" % (m, s)

    def cyro_office_mark(name, found):
        if found:
            return "✓ " + name
            found_evidence += 1
        return name

# ============================================================
# 倒计时 Screen：四个搜查场景都会共用这个倒计时
# ============================================================

screen cyro_office_timer():

    zorder 100

    frame:
        xalign 0.97
        yalign 0.04
        padding (22, 12)

        text "[cyro_office_format_time(cyro_office_time_left)]":
            size 42
            color "#FFFFFF"
            bold True

    timer 1.0 repeat True action If(
        cyro_office_time_left > 1,
        SetVariable("cyro_office_time_left", cyro_office_time_left - 1),
        [
            SetVariable("cyro_office_time_left", 0),
            Hide("cyro_office_timer"),
            Jump("cyro_office_time_up")
        ]
    )

# ============================================================
# 办公室搜查地图
# ============================================================

# 退出房间的询问screen
screen cyro_leave_office: 
    modal True
    zorder 120
    
    # 半透明背景
    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        
        vbox:
                       
            text "Leave the room now?":
                size 35 color "#ffffff" xalign 0.5
            null height 30
            
            add Solid("#FFFFFF"):
                xsize 800
                ysize 1
                xalign 0.5
                alpha 0.3  # 30%不透明度

            textbutton "End Search":
                xsize 200
                ysize 50
                align(0.55, 0.5)
                action [Hide("cyro_leave_office"), Jump("cyro_search_leave_safe")]
            textbutton "Continue Search":
                xsize 200
                ysize 50
                align(0.55, 0.7)
                action [Hide("cyro_leave_office")]
# 办公室搜证地图
screen cyro_office_map():

    modal True
    
    # 线索点击区域设置，focus_mask
    button:
        xysize(400, 200)
        background Frame (Transform ("images/chapter4/touming_1.png", xysize=(400, 200)))
        focus_mask True
        xpos 1220
        ypos 480
        # action [Hide("bar_scene", fade), Jump("bar_menu_choice")]
        action [Jump("cyro_office_drawer")]
    button:
        xysize(190, 160)
        background Frame (Transform ("images/chapter4/touming_2.png", xysize=(190, 160)))
        focus_mask True
        xpos 460
        ypos 150
        action [Jump("cyro_office_bookshelf")]
    button:
        xysize(200, 90)
        background Frame (Transform ("images/chapter4/touming_3.png", xysize=(200, 90)))
        focus_mask True
        xpos 900
        ypos 610
        action [Jump("cyro_office_photo")]
    button:
        xysize(250, 115)
        background Frame (Transform ("images/chapter4/touming_4.png", xysize=(250, 115)))
        focus_mask True
        xpos 530
        ypos 600
        action [Jump("cyro_office_desk")]
    # textbutton "[cyro_office_mark('最下层抽屉', cyro_office_found_files)]":
    #     xsize 500
    #     ysize 120
    #     action Return("drawer")

    # textbutton "[cyro_office_mark('书柜顶层礼盒', cyro_office_found_perfume)]":
    #     xsize 500
    #     ysize 120
    #     action Return("bookshelf")

    # textbutton "[cyro_office_mark('文件堆下的笔记本', cyro_office_found_notebook)]":
    #     xsize 500
    #     ysize 120
    #     action Return("desk")

    # textbutton "[cyro_office_mark('照片书', cyro_office_found_photo)]":
    #     xsize 500
    #     ysize 120
    #     action Return("photo")
    # 手动退出键
    imagebutton at arrow_style_ud:
        align (0.5, 0.95)
        idle "arrow_down"
        hover "arrow_down"
        action [Show ("cyro_leave_office")]


# ============================================================
# 进入办公室搜查
# ============================================================
# 直接闯门，时间短
label cyro_break_in:

    $ cyro_office_time_left = 60

    $ cyro_office_found_files = False
    $ cyro_office_found_perfume = False
    $ cyro_office_found_notebook = False
    $ cyro_office_found_photo = False
    
    show screen cyro_office_timer
    scene black

    # 推门音效
    "{i}趁陈永仁去洗手间的空档，你溜进了他的办公室。{/i}"
    s "只有1分钟，必须在他回来之前，找到能证明他性骚扰员工的证据。"
    jump cyro_office_search

# 林姐帮忙，时间长
label cyro_office_start:

    $ cyro_office_time_left = 300

    $ cyro_office_found_files = False
    $ cyro_office_found_perfume = False
    $ cyro_office_found_notebook = False
    $ cyro_office_found_photo = False
    
    show screen cyro_office_timer
    scene black

    # 推门音效
    s "最多只有五分钟。"
    s "必须在他回来之前，找到能证明他性骚扰员工的证据。"
    jump cyro_office_search


# ============================================================
# 搜查主循环
# ============================================================

label cyro_office_search:
    scene chen_office_clue

    # 倒计时结束跳转
    if cyro_office_time_left <= 0:
        jump cyro_office_time_up

    # 正常有时间时执行
    # 所以要在map里面设置场景切换箭头，主循环（主screen 1个线索image button + 3个副screen）

    $ renpy.call_screen("cyro_office_map")
    # $ ui.interact()
    # $ cyro_office_choice = renpy.call_screen("cyro_office_map")

    # if cyro_office_choice == "drawer":
    #     jump cyro_office_drawer

    # elif cyro_office_choice == "bookshelf":
    #     jump cyro_office_bookshelf

    # elif cyro_office_choice == "desk":
    #     jump cyro_office_desk

    # elif cyro_office_choice == "photo":
    #     jump cyro_office_photo

    # elif cyro_office_choice == "finish":
    #     jump cyro_office_complete

    # jump cyro_office_search


# ============================================================
# 场景一：最下层抽屉
# ============================================================

label cyro_office_drawer:

    if not cyro_office_found_files:
        $ cyro_office_found_files = True
        $ found_evidence += 1
        show clue_01_files with fade
        
        "You squat down and pull open the bottom drawer of the desk."

        "It is heavier than you expected."

        "At the back lies a stack of old employee files."

        "You skim through them quickly."

        "They contain records of several female staff members."

        "Oddly enough, all of them resigned one after another within two years."

        "Their reasons for leaving are briefly noted:"

        "Personal reason."

        "Yet each file has been folded separately, as if repeatedly checked by someone."

    else:

        "最下层抽屉已经搜查过了。"

jump cyro_office_search_check


# ============================================================
# 场景二：书柜顶层礼盒
# ============================================================

label cyro_office_bookshelf:

    if not cyro_office_found_perfume:
        $ cyro_office_found_perfume = True
        $ found_evidence += 1

        show clue_02_bookshelf with fade
        "You walk over to the bookshelf."

        "A box sits on the top shelf."

        show clue_02_perfume with dissolve
        "You stand on tiptoes and take it down."

        "Inside the box is a bottle of expensive perfume,"

        "still in its original packaging,"

        "unopened."

        "This is nothing like regular office supplies."

        "It looks more like a gift meant for someone."

    else:

        "书柜顶层你已经搜查过了。"

        "那个未拆封的香水礼盒仍然显得格外突兀。"

jump cyro_office_search_check


# ============================================================
# 场景三：照片
# ============================================================

label cyro_office_photo:

    if not cyro_office_found_photo:

        $ cyro_office_found_photo = True
        $ found_evidence += 1

        show clue_03_photo with fade
        "On the desk lies the notebook Chan Wing Yan uses to jot down trivial matters."

        s "Paperless record‑keeping is standard now. Why is he still so fond of writing things down? Stacked up like this. Is this mid‑life nostalgia?"
        s "Huh?"

        show clue_03_photo_open with dissolve
        "As you flip to the middle, a photo slips out."

        "It shows Chan Wing Yan standing close to a young woman."

        "She is not his wife."

        "No name is written on the back of the photo,"

        "only a date."

        s " …So he marks to mask."

    else:

        "You have searched the photo album."

        "The photo remains tucked between the pages."

jump cyro_office_search_check


# ============================================================
# 场景四：笔记本
# ============================================================

label cyro_office_desk:

    if not cyro_office_found_notebook:

        $ cyro_office_found_notebook = True
        $ found_evidence += 1

        show clue_04_notebook with fade
        "Papers pile up on the desk, with a black notebook tucked underneath."

        "You open the notebook."

        "It is filled with names, dates, and short notes,"

        "scrawled in messy handwriting."

        "One line makes you freeze."

        "Lee cried. Handled."

        "There is a lack of context for this line."

        "Yet it is precisely the lack that makes it deeply unsettling."

    else:

        "You have searched through the stacks of documents."

        "The handwriting in that black notebook still makes you uneasy."

jump cyro_office_search_check


# ============================================================
# 每次搜查后的判断
# ============================================================

label cyro_office_search_check:
    if cyro_office_found_files and cyro_office_found_perfume and cyro_office_found_notebook and cyro_office_found_photo:

        "You have searched all four key locations."
        jump cyro_search_leave_safe

    else:
        jump cyro_office_search

label cyro_search_leave_safe:

    "Search Complete"
    "Evidence Collected: 4"
               
    hide screen cyro_office_timer

    scene black

    if found_evidence > 0:
        "{i}You take photos of all clues you have found, put everything back in place, and slip out before Chan Wing Yan returns.{/i}"
    else:
        "{i}没有找到证据，但该走了{/i}"
jump chapter5


# ============================================================
# 时间耗尽
# ============================================================

label cyro_office_time_up:

    $ cyro_office_time_left = 0

    hide screen cyro_office_timer

    "时间到了。"

    "门外传来脚步声。"
    
    # 脚步声停在身后，小曼回头
    
    chen "……这是谁呀？"
    scene black with fade
    show chen_08_horrible with dissolve:
        zoom 2.0 xalign 0.45 ypos -600
        linear 1.5 zoom 2.0 xalign 0.45 ypos -500
        linear 0.1 zoom 7 xalign 0.65 ypos -800
    pause 1.5
    jump ending_gulang

    return










# label office_search_results:
#     scene bg chen_office
#     with fade
    
#     "搜查结束。你发现了："
    
#     # 根据点击发现显示结果
#     if "archives" in physical_evidence_found:
#         "【旧员工档案】最下抽屉"
#         "几个女性员工，都在两年内离职。原因不明。"
    
#     if "gift" in physical_evidence_found:
#         "【礼盒】书柜顶层"
#         "昂贵香水——未拆封。收件人：无。"
    
#     if "notebook" in physical_evidence_found:
#         "【笔记本】文件堆下"
#         "名字、日期、备注：「李哭了。处理好了。」"
    
#     if "photo" in physical_evidence_found:
#         "【照片】书里夹着"
#         "陈永仁和年轻女性——不是他妻子。"
    
#     $ office_searched = True
#     jump chapter4_end

# # 办公室搜查界面（限时）
# screen office_search_timer(duration):
#     modal True
    
#     default start_time = renpy.get_game_runtime()
#     default time_left = duration
    
#     # 倒计时
#     timer 0.1 repeat True action [
#         SetScreenVariable("time_left", max(0, duration - (renpy.get_game_runtime() - start_time))),
#         If(time_left <= 0, true=[Hide("office_search_timer"), Jump("office_search_results")], false=NullAction())
#     ]
    
#     # 背景
#     add "bg chen_office"
    
#     # 时间显示
#     frame:
#         xalign 0.5
#         ypos 20
#         background "#e74c3c"
#         padding (20, 10)
        
#         $ minutes = int(time_left // 60)
#         $ seconds = int(time_left % 60)
#         text "剩余时间：[minutes]:[seconds:02d]" size 24 color "#ffffff" xalign 0.5
    
#     # 可搜查区域
#     # 1. 最下抽屉
#     if "archives" not in physical_evidence_found:
#         button:
#             xpos 200
#             ypos 400
#             xsize 120
#             ysize 80
#             background "#8b4513"
#             hover_background "#a0522d"
#             action [AddToSet("physical_evidence_found", "archives"), Show("evidence_found_popup", msg="发现旧员工档案")]
            
#             text "🗄️ 抽屉" size 20 xalign 0.5 yalign 0.5
    
#     # 2. 书柜顶层
#     if "gift" not in physical_evidence_found:
#         button:
#             xpos 500
#             ypos 150
#             xsize 100
#             ysize 100
#             background "#d4af37"
#             hover_background "#f4d03f"
#             action [AddToSet("physical_evidence_found", "gift"), Show("evidence_found_popup", msg="发现礼盒")]
            
#             text "🎁" size 40 xalign 0.5 yalign 0.5
    
#     # 3. 文件堆
#     if "notebook" not in physical_evidence_found:
#         button:
#             xpos 400
#             ypos 350
#             xsize 150
#             ysize 100
#             background "#95a5a6"
#             hover_background "#bdc3c7"
#             action [AddToSet("physical_evidence_found", "notebook"), Show("evidence_found_popup", msg="发现笔记本")]
            
#             text "📄 文件堆" size 18 xalign 0.5 yalign 0.5
    
#     # 4. 书架上的书
#     if "photo" not in physical_evidence_found:
#         button:
#             xpos 600
#             ypos 200
#             xsize 80
#             ysize 120
#             background "#3498db"
#             hover_background "#5dade2"
#             action [AddToSet("physical_evidence_found", "photo"), Show("evidence_found_popup", msg="发现照片")]
            
#             text "📖" size 35 xalign 0.5 yalign 0.5

# # 发现证据弹窗
# screen evidence_found_popup(msg):
#     modal False
    
#     frame:
#         xalign 0.5
#         yalign 0.3
#         background "#27ae60"
#         padding (30, 20)
        
#         text msg size 20 color "#ffffff" xalign 0.5
    
#     timer 1.5 action Hide("evidence_found_popup")

# 直接闯入（高风险）
# label direct_break_in:
#     "你选择直接闯入。"
    # menu:
    #     "强行撬锁（可能被发现）":
    #         $ risk_roll = renpy.random.randint(1, 10)
    #         if risk_roll <= 3:
    #             "锁开了。但监控拍到了你。"
    #             $ investigation_skill -= 2
    #             call screen office_search_timer(duration=60.0)  # 只有1分钟
#             else:
#                 "撬锁失败！保安正在赶来。"
#                 jump chapter4_fail
        
#         "放弃":
#             jump chapter4_end

# label chapter4_fail:
#     "你被发现了。"
#     "陈永仁看着你，笑容意味深长。"
#     chen "小曼，你在找什么？"
#     jump bad_ending_investigation

# label chapter4_end:
#     scene bg home_night
#     with fade
    
#     "第11周结束。"
    
#     if digital_evidence_count >= 5 or len(physical_evidence_found) >= 2:
#         "你掌握了足够的证据。"
#         "下一步：决定如何使用。"
#         jump chapter5_decision
#     else:
#         "证据仍然不足……"
#         "你需要更多时间，或者更多勇气。"
#         jump chapter5
# # 定义 AddToSet 函数（Ren'Py没有内置）
# init python:
#     def add_to_set(set_name, item):
#         if item not in globals()[set_name]:
#             globals()[set_name].append(item)
    
#     # 注册为屏幕动作可用
#     # renpy.add_to_store("AddToSet", add_to_set)

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
    
    # 倒计时显示
    vbox:
        align (0.5, 0.2)
        spacing 10
        
        text "【Boundary Alert】" at blink_effect:
            size 40
            color "#FC8181"
            xalign 0.5
        
        text "【Boundary Warning】System Warning: Interference protocol activated" at subtle_shake:
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
            
            text "Dodge" at subtle_shake:
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
            
            text "Stay silent":
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
            
            text "Say stop":
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

    text "Room Scan: Click on items to trigger thoughts:":
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

        text "Mirror":
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

        text "Bed & Teddy Bear":
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

        text "Phone":
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

        text "Shower":
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

        text "Diary":
            align (0.5, 0.5)
            size 20
            color "#FFFFFF"

    textbutton "Leave the Room":
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
    
    "【Boundary Warning】System Warning: Interference protocol activated"
    
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
    show expression Movie(play="videos/tv_breakdown.webm", size=(1960, 1080)) as flash_video at truecenter
    
    # 播放固定时间（1秒）
    $ renpy.pause(1.0, hard=True)
    
    # 隐藏视频
    hide flash_video
    #骚扰01
    if qte_cycle == 1:
        show touch

    #骚扰02
    if qte_cycle == 2:
        scene black
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
    # $ renpy.pause(1, hard=True)  # hard=True 防止点击跳过
    
    # 切换到screen阶段
    $ qte_phase = "screen"
    # hide flash
    
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
        jump car_ending_avoided
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
    "The atmosphere turns awkward, yet he regains his composure quickly."
    "Let me walk you back."
    extend "It’s really late today."

    "Along the way, you talk about work, as if the earlier touch never happened."

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
            "You look into the mirror."
            "You look the same, but feel different."
            "The face in the glass is still yours, yet the eyes… belong to a stranger."

        elif clicked_item == "bed":
            "The teddy bear by the bed tilts its head at you."
            "You want to lie down, and maybe never get up again."
            "The quilt still holds the shape you left when you pulled it back this morning."

        elif clicked_item == "phone":
            "8 unread messages"
            "3 from Chan Wing Yan"
            "Have you gotten home?"
            "About what happened earlier, don’t overthink it."
            "See you tomorrow."

        elif clicked_item == "shower":
            "You need to wash."
            "You need the running water to wash something away."
            "But you know some things can never be rinsed off."

        elif clicked_item == "diary":
            "You open your diary."
            "Blank pages."
            "Not a single word can be written."
            "Or rather, there are too many words, and you don’t know where to start."

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

    return


# ==========================================
# 第五章：抉择（第15周）
# ==========================================

# # 定义变量
# default chapter5_started = False
default evidence_complete = False
# default advice_heard = False

# # 路线选择标记
default route_legal = False
default route_hr = False
# default route_public = False
# default route_leave = False

# # 路线条件变量
default lawyer_contacted = False
default courage = 0
# default xiaohongshu_fans = 0

# # 路线A变量
default police_credibility = 100
# default police_report_2 = False

# # 路线B变量
# default hr_talk_done = False
# default department_reorganized = False

# # 路线C变量
# default post_views = 0
# default post_comments = 0
# default media_contacted = 0
# default lawyer_letter_received = False
# default public_pressure = 0

# # 路线D变量
# default resignation_written = False
# default last_day_done = False

default disclosure_level = "medium"

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
    
    # default disclosure_level = "medium"
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
                    action SetVariable("disclosure_level", "low")
                    
                    background ("#ff2442" if disclosure_level == "low" else "#dddddd")
                
                textbutton "部分实名":
                    action SetVariable("disclosure_level", "medium")
                    
                    background ("#ff2442" if disclosure_level == "medium" else "#dddddd")
                
                textbutton "完全公开":
                    action SetVariable("disclosure_level", "high")
                   
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
                # action [Return({"disclosure": disclosure_level, "evidence": selected_evidence, "title": post_title})]
                action [Return({"evidence": selected_evidence, "title": post_title})]

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
    
    "压力+[public_pressure]。睡眠-80%%。"
    
    "但……"
    
    "【私信】姐妹，我也经历过。谢谢你敢说。"
    "【私信】我在这家公司3年了，一直不敢说。"
    "【私信】你不是一个人。"
    
    "你不再是一个人。"

    # 改：不要碧莲结局判定
    if linjie_interest >=2 and xiaojin_interest >= 1 and disclosure_level == "high":
        jump route_c_she_scene
    else:
            jump chapter5_ending
    
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

label ending_gulang:
    "结局：孤狼"
    return

# ==========================================
# 标题选择界面
# ==========================================
screen post_title_input():
    modal True

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 620
        background "#ffffff"
        padding (36, 32)

        vbox:
            spacing 18

            text "选择标题" size 24 color "#333333" xalign 0.5

            textbutton "在游戏公司被性骚扰，我决定说出来":
                xsize 540
                ysize 46
                background "#f2f2f2"
                hover_background "#8e44ad"
                text_size 17
                text_color "#333333"
                text_hover_color "#ffffff"
                action [SetScreenVariable("post_title", "在游戏公司被性骚扰，我决定说出来"), Hide("post_title_input")]

            textbutton "关于某游戏公司高管，一些必须讲的事":
                xsize 540
                ysize 46
                background "#f2f2f2"
                hover_background "#8e44ad"
                text_size 17
                text_color "#333333"
                text_hover_color "#ffffff"
                action [SetScreenVariable("post_title", "关于某游戏公司高管，一些必须讲的事"), Hide("post_title_input")]

            textbutton "22k vs 19.5k，不只是工资":
                xsize 540
                ysize 46
                background "#f2f2f2"
                hover_background "#8e44ad"
                text_size 17
                text_color "#333333"
                text_hover_color "#ffffff"
                action [SetScreenVariable("post_title", "22k vs 19.5k，不只是工资"), Hide("post_title_input")]

            textbutton "取消":
                xalign 0.5
                xsize 160
                ysize 42
                background "#dddddd"
                hover_background "#bbbbbb"
                text_size 16
                text_color "#333333"
                action Hide("post_title_input")


# ==========================================
# 发帖后剧情判断
# ==========================================
label route_c_she_scene:

    # $ disclosure_choice = post_result.get("disclosure", "medium")

    # if disclosure_choice == "high":
    #     jump bad_end_public
    # else:
        scene bg company_street_evening
        with fade

        "黄昏的公司路口，晚风微凉，夕阳把地面染成暖橘色，路边行道树随风轻晃。"

        "小曼抱着装满个人物品的纸箱，站在路口，指尖微微收紧，望着公司方向轻轻叹了口气，转头看向身旁两人。"

        s "就到这里吧，麻烦你们还特意下来送我。"

        linjie "傻孩子，跟我们还说这些。这段时间辛苦你了，别把所有事都憋在心里。"

        xiaojin "曼姐，以后不管遇到什么事，都别自己扛着，我们都在。"

        "林姐轻轻开口，哼起《送别》的旋律，小金随即轻声附和，小曼垂眸，也慢慢跟着哼唱。"

        "三人合唱（声音轻柔，满是离愁）：长亭外，古道边，芳草碧连天……"

        s "……我们同唱芳草天。"

        "林姐与小金对视一眼，没有打断，依旧顺着旋律继续唱，晚风将歌声轻轻吹散。"

        "三人合唱：晚风拂柳笛声残，夕阳山外山。"

        s "我走啦，你们回去吧。"

        linjie "照顾好自己，常联系。"

        xiaojin "对，有事随时说！"

        "小曼转身，脚步平稳地向前走去，夕阳将她的影子拉长，林姐和小金站在原地，静静望着她的背影，直到渐渐远去。"

        jump chapter5_ending

#     #1. 酒单（左侧）
#     button:
#         xpos 100
#         ypos 200
#         xsize 120
#         ysize 150
#         background "#8b4513"
#         hover_background "#a0522d"
#         action Jump("bar_menu_choice")

#         vbox:
#             xalign 0.5
#             yalign 0.5
#             text "🍷" size 40 xalign 0.5
#             text "酒单" size 16 xalign 0.5
    
#     # 2. 小金（大声聊天区域）
#     button:
#         xpos 300
#         ypos 250
#         xsize 140
#         ysize 120
#         background "#2e8b57"
#         hover_background "#3cb371"
#         #action Jump("talk_to_xiaojin")
#         action If(talk_to_xiaojin, Jump("talk_to_xiaojin_again"), Jump("talk_to_xiaojin"))

#         vbox:
#             xalign 0.5
#             yalign 0.5
#             text "💬" size 35 xalign 0.5
#             text "小金" size 16 xalign 0.5
#             text "(大声聊天)" size 12 xalign 0.5
        
#     # 3. 林姐（角落卡座）
#     button:
#         xpos 550
#         ypos 180
#         xsize 130
#         ysize 130
#         background "#4a4a4a"
#         hover_background "#696969"
#         action If(sit_with_lin, Jump("sit_with_lin_again"), Jump("sit_with_lin"))
        
#         vbox:
#             xalign 0.5
#             yalign 0.5
#             text "🪑" size 35 xalign 0.5
#             text "林姐" size 16 xalign 0.5
#             text "(角落卡座)" size 12 xalign 0.5
    
#     # 4. 陈永仁（中心位置）
#     button:
#         xpos 400
#         ypos 350
#         xsize 140
#         ysize 140
#         background "#8b0000"
#         hover_background "#a52a2a"
#         action If(observe_chen, Jump("observe_chen_again"), Jump("observe_chen"))
        
#         vbox:
#             xalign 0.5
#             yalign 0.5
#             text "👔" size 40 xalign 0.5
#             text "陈永仁" size 16 xalign 0.5
#             text "(中心位置)" size 12 xalign 0.5
    
#     # 5. 洗手间（逃离）
#     button:
#         xpos 650
#         ypos 100
#         xsize 100
#         ysize 100
#         background "#4682b4"
#         hover_background "#5f9ea0"
#         action If(bar_restroom, Jump("bar_restroom_again"), Jump("bar_restroom"))
        
#         vbox:
#             xalign 0.5
#             yalign 0.5
#             text "🚻" size 30 xalign 0.5
#             text "洗手间" size 14 xalign 0.5


# 任务4.2准备：选择工具
# label chapter4_evidence_prep:
#     scene bg bedroom_night
#     with fade
    
#     "今晚，你要行动。"
#     "从卧室带什么工具？"
    
#     # 工具选择界面
#     call screen evidence_tools_select
    
#     "你准备好了。"
#     jump digital_evidence_phase

# # 工具选择界面
# screen evidence_tools_select():
#     modal True
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xpadding 50
#         ypadding 40
#         background "#2c3e50"
        
#         vbox:
#             spacing 20
#             xalign 0.5
            
#             text "选择携带工具" size 28 color "#ffffff" xalign 0.5
            
#             grid 2 2:
#                 spacing 15
                
#                 # 工具1：备用手机
#                 button:
#                     xsize 200
#                     ysize 150
#                     background "#34495e"
#                     hover_background "#4a6fa5"
#                     action [SetVariable("tool_phone", True), Return()]
                    
#                     vbox:
#                         xalign 0.5
#                         yalign 0.5
#                         text "📱" size 40
#                         text "备用手机" size 16 color "#ffffff"
#                         text "(截屏专用)" size 12 color "#95a5a6"
                
#                 # 工具2：录音笔
#                 button:
#                     xsize 200
#                     ysize 150
#                     background "#34495e"
#                     hover_background "#4a6fa5"
#                     action [SetVariable("tool_recorder", True), Return()]
                    
#                     vbox:
#                         xalign 0.5
#                         yalign 0.5
#                         text "🎙️" size 40
#                         text "录音笔" size 16 color "#ffffff"
#                         text "(持续录音)" size 12 color "#95a5a6"
                
#                 # 工具3：微型摄像头
#                 button:
#                     xsize 200
#                     ysize 150
#                     background "#34495e"
#                     hover_background "#4a6fa5"
#                     action [SetVariable("tool_camera", True), Return()]
                    
#                     vbox:
#                         xalign 0.5
#                         yalign 0.5
#                         text "📹" size 40
#                         text "微型摄像头" size 16 color "#ffffff"
#                         text "(隐蔽拍摄)" size 12 color "#95a5a6"
                
#                 # 工具4：什么都不带
#                 button:
#                     xsize 200
#                     ysize 150
#                     background "#7f8c8d"
#                     hover_background "#95a5a6"
#                     action Return()
                    
#                     vbox:
#                         xalign 0.5
#                         yalign 0.5
#                         text "🚫" size 40
#                         text "轻装上阵" size 16 color "#ffffff"
#                         text "(风险+)" size 12 color "#bdc3c7"

# # 第一阶段：数字证据 - 截屏快手小游戏
# label digital_evidence_phase:
#     scene bg bedroom_night
#     with fade
    
#     "第一阶段：数字证据。"
#     "翻看所有陈永仁的消息。"
#     "警告：他可能会撤回。"
    
#     "小游戏：截屏快手"
#     "每条消息5秒内截屏，否则消失。"
    
#     # 7条消息，每条5秒限时
#     $ digital_evidence_count = 0
    
#     call screen screenshot_game(msg="在吗", timeout=5.0)
#     call screen screenshot_game(msg="昨晚的事别多想", timeout=5.0)
#     call screen screenshot_game(msg="你很特别", timeout=5.0)
#     call screen screenshot_game(msg="我知道你家在哪", timeout=5.0)
#     call screen screenshot_game(msg="别告诉林姐", timeout=5.0)
#     call screen screenshot_game(msg="下周单独吃饭", timeout=5.0)
#     call screen screenshot_game(msg="你逃不掉的", timeout=5.0)
    
#     "截屏完成。获得 [digital_evidence_count]/7 条证据。"
    
#     if digital_evidence_count >= 5:
#         "足够作为数字证据。"
#         $ last_night_evidence = True
#     else:
#         "证据不足……有些消息被撤回了。"
    
#     jump physical_evidence_phase

# # 截屏小游戏界面
# screen screenshot_game(msg, timeout=5.0):
#     modal True
    
#     default start_time = renpy.get_game_time()
#     default captured = False
    
#     # 实时检查时间
#     timer 0.05 repeat True action If(
#         (renpy.get_game_time() - start_time) >= timeout,
#         true=[Hide("screenshot_game"), Return()],
#         false=NullAction()
#     )
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xsize 400
#         ysize 300
#         background "#ffffff"
        
#         vbox:
#             xalign 0.5
#             yalign 0.5
#             spacing 20
            
#             # 微信消息样式
#             frame:
#                 background "#95ec69"
#                 xpadding 15
#                 ypadding 10
#                 xalign 0.5
                
#                 text msg size 18 color "#000000"
            
#             null height 30
            
#             # 倒计时显示
#             $ remaining = max(0, timeout - (renpy.get_game_time() - start_time))
#             text "[remaining:.1f]秒" size 24 color "#e74c3c" xalign 0.5
            
#             null height 20
            
#             # 截屏按钮
#             if not captured:
#                 textbutton "📸 截屏":
#                     xalign 0.5
#                     xsize 150
#                     ysize 50
#                     background "#3498db"
#                     hover_background "#2980b9"
#                     text_color "#ffffff"
#                     action [SetScreenVariable("captured", True), 
#                             SetVariable("digital_evidence_count", digital_evidence_count + 1),
#                             Show("screenshot_flash")]
#             else:
#                 text "✓ 已截屏" color "#27ae60" size 20 xalign 0.5

# # 截屏闪光效果
# screen screenshot_flash():
#     add Solid("#ffffff")
#     timer 0.1 action Hide("screenshot_flash")