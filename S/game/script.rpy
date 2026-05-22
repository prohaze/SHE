image gulang = "images/ending_CG/gulang.png"
# image gulang_b = "images/ending_CG/gulang.jpg"
image tuoniao = "images/ending_CG/tuoniao.jpg"
image linjian = "images/ending_CG/linjian.jpg"
image kongwen = "images/ending_CG/kongwen.jpg"
image yinshui = "images/ending_CG/yinshui.png"
image tuichang = "images/ending_CG/tuichang.jpg"
image xiangxi = "images/ending_CG/xiangxi.jpg"
image qingping = "images/ending_CG/qingping.jpg"
image xuyu = "images/ending_CG/xuyu.jpg"
image poxiao = "images/ending_CG/poxiao.jpg"
image feiniao = "images/ending_CG/feiniao.jpg"
# image yinshui_b = "images/ending_CG/yinshui_b.jpg"
# image yinshui_color = "images/ending_CG/yinshui_color.jpg"


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
            
            textbutton "Close":
                xalign 0.5
                action Hide("item_description")

screen items_screen():
    modal True
    # 添加进度显示
    text "Items Found[len(clicked_items)]/4":
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

            textbutton "Close":
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

define s = Character("siu man") #避免每次都打很多字
define n = Character(None, what_italic=True)

label start:

    scene 31 #Emma:需要替换开场图片
    show titletest:
        pos(120,150)
    
    ##show eileen happy #Emma：需要透明底角色立绘，后续替换立绘图

    menu:
        "Start Game":
            style choice_vbox:
                xalign 0.5
                ypos 700
                yanchor 0.5
            jump chapter0
        "Exit Game":
            return

label chapter0:
    show black #替换黑幕布
    image chapter0_title = ParameterizedText(xalign=0.5, yalign=0.45, size=108)
    show chapter0_title "Prologue: The Message"
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
        "Explore the Room":
            call explore_room #call完之后走jump
            jump explore_complete
        "Wait Quietly":
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
    'HR'"Miss Sheh? Mr. Chen is asking for you."
    jump chapter0_2

label after_third_item:
    $ five_item_clicked = False  # 重置标记
    s "It seems the interview is about to start…"
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
        print(f"Money {amount:+} ({reason})，Current: {money}")
    
    def add_social(amount, reason=""):
        global social
        social += amount
        print(f"Social {amount:+} ({reason})，Current: {social}")
    
    def add_mental(amount, reason=""):
        global mental
        mental += amount
        print(f"Mental {amount:+} ({reason})，Current: {mental}")
    
    def add_awakening(amount, reason=""):
        global awakening
        awakening += amount
        print(f"Awakening {amount:+} ({reason})，Current: {awakening}")

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

define c = Character("Chen ")

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
define unknown_woman = Character("？？？", color="#808080")
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
    show chapter1_title "Chapter 1：Onboarding"
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
    "The building smells of air freshener and ambition. You’re 13 minutes early. Everyone is."
    hide she_03_tinysmile_eye onlayer top

    show she_03_tinysmile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "First day on the job. Time to get a feel for the place."
    hide she_03_tinysmile onlayer top

    jump lobby_explore

# ========== 大堂探索 ==========
screen lobby_menu(gate_used, coffee_bought, appearance_checked):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.45
        
        text "Items to Explore – Lobby":
            size 34
            color "#ffffff"
            outlines [ (2, "#000000", 0, 0) ]
        
        if not gate_used:
            textbutton "Turnstile" action Jump("gate_interaction")
        if not coffee_bought:
            textbutton "Coffee Bar" action Jump("coffee_stand")
        if not appearance_checked:
            textbutton "Elevator Door Reflection" action Jump("mirror_check")

label lobby_explore:
    scene lobby with dissolve
    
    if gate_used and coffee_bought and appearance_checked:
        show she_03_tinysmile onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "Still some time left. Might as well look around the office floor."
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
    'Barista'"Hi, what can I get for you?"

    s "Hot latte, please. Thanks."

    show coffee_staff_03_chat with dissolve:
        zoom 0.68
        xpos 690
        ypos 160
    'Barista'"Don’t see you often. New here?"

    s "Yeah, today’s my first day."

    show coffee_staff_02_smile with dissolve:
        zoom 0.68
        xpos 690
        ypos 160
    'Barista'"{i}You‘re wearing your new work skirt. It fits perfectly.{/i}"

    $ money -= 30
    "-30 yuan。【Current balance：[money] yuan】"
    $ coffee_bought = True
    
    jump lobby_explore

# ========== 整理仪容 ==========

label mirror_check:
    scene lobby
    show elevator_reflection with dissolve
    "{i}You‘re wearing your new work skirt. It fits perfectly.{/i}"
    
    $ appearance_checked = True
    
    jump lobby_explore

# ========== 电梯选择 ==========
screen elevator_menu(third_floor, eight_floor, twenty_third_floor):
    style_prefix "choice"
    
    # 临时位置设置
    vbox:
        xalign 0.5
        yalign 0.4
        
        # text ""Explore Office Floor":
        #     outlines [ (2, "#000000", 0, 0) ]
        #     xpos 50 
        
        if not third_floor:
            textbutton "3rd Floor" action Jump("third_floor")
        if not eight_floor:
            textbutton "8th Floor" action Jump("eight_floor")
        if not twenty_third_floor:
            textbutton "23rd Floor" action Jump("twenty_third_floor")

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
    "{i}HR Department...{/i}"
    $ third_floor = True
    jump elevator_choice
            
label eight_floor:
    scene bg eight_floor with dissolve:
        xzoom -1
    "{i}Marketing Department...{/i}"
    $ eight_floor = True
    jump elevator_encounter
            
label twenty_third_floor:
    scene bg twenty_third_floor with dissolve
    "{i}Executive Floor...{/i}"
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
    s"Oh, time’s up. Better get to my desk."
    hide she_03_tinysmile onlayer top
    hide she_07_astonish onlayer top
    
    scene office with fade
    "{i}{cps=10}12th Floor – Design Department{/cps}{/i}"
    "{i}Rows of desks. Beige and gray cubicles. Someone‘s microwaving popcorn — it’s about to burn.{/i}"

# 延续已有定义的角色
define s = Character("Siu Man")
define n = Character(None, what_italic=True)

# 第一章新角色定义
define xiaojin = Character("Siu Gam", color="#FFD700")
define linjie = Character("Ms Lam", color="#808080")
define chen = Character("Chen Wing Yan", color="#4169E1")
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
    "{i}You arrive at your desk and start unpacking your things.{/i}"
    
    show jin_01_happy with moveinright:
        zoom 0.97
        xpos 700
        ypos 150
    xiaojin "Hey! The new girl! Finally, someone who’s not old enough to be my dad. Want coffee? I‘ll tell you which machine’s the best."

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
        "Sure, thanks!":
            $ xiaojin_interest += 1
            jump xiaojin_friendly
            
        "Maybe later. I want to get settled in first.":
            jump xiaojin_neutral
            
        "I brought my own.":
            jump xiaojin_cold

# 选项A：友好路线
label xiaojin_friendly:
    hide she_01_normal_eye_o onlayer top
    show she_05_happy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "I already got one downstairs, but sure — thanks."
    hide she_05_happy onlayer top

    scene tea_room with dissolve
    
    show jin_02_frown with dissolve:
        zoom 0.97
        xpos 700
        ypos 150
    xiaojin "You’re new, so just remember — don‘t cross Mr. Chan. He seems easygoing, but don’t push it. And that woman in HR? Stay on her good side too."
    xiaojin "…Forget it. Just don’t offend anyone. I‘ve been here eight months, and I’m still figuring it out."
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
    s "Give me a sec. I want to organize my desk first."
    
    xiaojin "Sure, no rush. Let me know if you need anything."
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
    s "I brought my own."

    xiaojin "…Haha, cool. I‘ll see you around."
    hide jin_01_happy with moveoutright

    hide she_01_normal_eye onlayer top
    
    jump linjie_encounter

# ========== 林姐登场 ==========

label linjie_encounter:
    scene office_area with fade:
        zoom 0.75
    
    "{i}You continue tidying up your desk.{/i}"
    
    show linjie_00_shade with moveinright:
        zoom 0.92
        xpos 790
        ypos 200
    '？？' "Welcome. The handover documents are in the shared link. There’s a meeting at 10 — don‘t be late."
    hide linjie_00_shade with dissolve
    
    "{i}She walks by. No pause, no glance.{/i}"
    
    menu:
        "Okay, thanks!":
            jump linjie_response_a
            
        "You nod silently.":
            jump linjie_response_b
            
        "Looking forward to the meeting.":
            jump linjie_response_c

# 选项A：积极
label linjie_response_a:
    s "Okay, thanks!"
    
    "{i}Her steps hesitate for a moment, but she doesn’t look back. She keeps walking.{/i}"

    $ linjie_interest += 1
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项B：冷淡
label linjie_response_b:
    "{i}You nod silently.{/i}"
    
    "{i}She doesn‘t seem to notice. She just walks away.{/i}"
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项C：职业（触发隐藏记录）
label linjie_response_c:
    s "Looking forward to the meeting."
    
    show linjie_00_shade with dissolve:
        zoom 0.92
        xpos 790
        ypos 200
    "{i}She pauses, turning just a little.{/i}"
    
    '？？' "Oh, really?"
        
    hide linjie_00_shade with dissolve
    show black with dissolve
    "{i}She’s gone.{/i}"
    
    $ linjie_interest += 1

    
    # 隐藏记录提示（仅开发者可见，玩家看不到）
    # [林姐兴趣度：低但不为零]
    
    jump task_1_3

# ========== 任务1.3：第一个任务 ==========
label task_1_3:
    show meeting_room with fade
    
    "{i}10:00 AM, Conference Room C.{/i}"
    "{i}The fluorescent lights hum. Eight people sit around the table. You‘re at least ten years younger than the youngest one.{/i}"
    
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 681
        ypos 162
    chen "Morning, everyone. Quick update — we’ve secured the new IP project. The client is a major studio. This is our chance to turn things around."
    hide chen_01_normal

    show chen_02_smile_front with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 687
        ypos 162
    chen "Time to let the newcomer shine. Siu Man, you‘ll take the competitor analysis."
    
    menu:
        "Great!":
            $ mental = mental + 2 if 'mental' in globals() else 2
            jump task_response_a
            
        "I’ll do my best.":
            jump task_response_b
            
        "Which specific parts should I break down?":
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

    s "Great!"

    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1342
        ypos 159
    chen "Good to see you motivated. Lam will get you started."

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
    s "I’ll do my best."
    
    chen "Good, if there’s any problems, ask Lam. She‘s very experienced."

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
    s "Which specific parts should I break down?"
    
    show she_02_sweat_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}Someone by the table lets out a soft laugh.{/i}"
    "{i}Not malicious, but… you’re the only one who doesn‘t know.{/i}"

    hide chen_02_smile_front
    show chen_02_smile:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 162
    chen "Good question. Lam will guide you. Just those few top games on the market — art style, progression systems, monetization design… the interesting stuff."
    show chen_03_narroweyes:
        zoom 0.9
        xzoom -1.0
        xpos 1358
        ypos 162
    chen "Don’t worry. I chose you for a reason. I‘ve seen your graduation project — those character designs had real spark."
    hide she_03_tinysmile_eye onlayer top
    hide she_02_sweat_eye onlayer top

    scene black with dissolve
    jump after_task_assignment

# 任务分配后
label after_task_assignment:
    scene meeting_room with fade
    
    "{i}The meeting ends. Everyone packs up and leaves.{/i}"
    
    show linjie_04_frown with dissolve:
        zoom 0.92
        xpos 790
        ypos 200
    
    linjie "He always throws impossible tasks at newbies. Each of those competitor projects took hundreds of people three years. You’re going to break them down alone? You‘ll run yourself into the ground."
    
    menu:
        "Thanks for the reminder. I’ll be careful.":
            jump linjie_after_a
            
        "I can handle it. I’ve analyzed plenty of games back in school.":
            jump linjie_after_b
            
        "Why is it impossible? Isn‘t there an analytical framework?":
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
    s "Thanks for the reminder. I’ll be careful."
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "Mm."
    
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
    s "I can handle it. I’ve analyzed plenty of games back in school."
    
    linjie "…………"
    show linjie_05_interested with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "Alright, I like that. Let me know if you need help."
    
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
    s "Why is it impossible? Isn‘t there an analytical framework?"
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "…That’s how it works on paper. Not always in reality. You’ll see."
    
    hide she_06_surprise_eye onlayer top   
    $ task_assigned = True
    
    jump chapter1_end

# 1.3结束标记
label chapter1_end:
    scene office_area with fade
    
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
        n "So sleepy…"
    if fatigue > 40:
        n "I can’t get this gacha probability curve to add up…"
    if fatigue > 30:
        n "And there’s an early‑morning meeting tomorrow…"
    
    n "But if I can’t finish it… will Mr. Chen think I‘m not good enough?"
    
    "{i}You rest your head on the desk, lost in thought. Then you hear footsteps. You listen closely — they stop.{/i}"
    
    show chen_03_narroweyes with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160
    chen "Still working?I was going through some documents upstairs and noticed your floor’s lights were on."
    
    "{i}He places a cup of coffee on your desk.{/i}"
    
    chen "Here. Americano from the convenience store downstairs. Not sure if it’s to your taste."
    
    menu:
        "Thank you, Mr. Chan.":
            jump overtime_response_a
            
        "You shouldn‘t have.":
            jump overtime_response_b
            
        "I’m almost done.":
            jump overtime_response_c

label overtime_response_a:
    s "Thank you, Mr. Chan."
    chen "Don’t mention it."
    jump chen_conversation

label overtime_response_b:
    s "You shouldn‘t have."
    "{i}Chan Wing Yan smiles but says nothing.{/i}"
    jump chen_conversation

label overtime_response_c:
    s "I’m almost done."
    chen "Pretty efficient, aren‘t you?"
    jump chen_conversation

label chen_conversation:
    "{i}Chan Wing Yan sits on the corner of the desk.{/i}"
    chen "I‘ve seen your resume. Your qualifications are top-tier. You had options. What made you pick this place?"
    show chen_00_body:
        zoom 0.9
        xzoom -1.0
        xpos 1357
        ypos 438
    menu:
        "No one else wanted me.":
            jump chen_honest
            
        "This position is the best match for my professional expertise.":
            jump chen_safe
            
        "I‘m looking for faster career growth.":
            jump chen_ambition

label chen_honest:
    s "No one else wanted me."
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
    "{i}Chan Wing Yan‘s expression softens.{/i}"

    chen "I understand. I began exactly where you are — this same desk, 20 years back. And now…"
    "{i}He gives a vague upward point.{/i}"

    show chen_04_frontsmile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161
    chen "Work hard. Stay till the end. That‘s how you win."
    "{i}He stands up.{/i}"
    
    hide chen_04_frontsmile with dissolve
    chen "Don‘t stay too late. Be careful on your way home."
    chen "…………"
    chen "Actually, I‘m leaving too… Want a ride?"
    jump car_choice

label chen_safe:
    s "This position is the best match for my professional expertise."
    show chen_02_smile:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161 
    hide chen_00_body
    chen "Yeah, you really do. Your analytical skills are impressive."
    "{i}He stands up.{/i}"
    hide chen_02_smile
    chen "Don‘t stay too late. There’s an early meeting tomorrow."
    chen "Actually, I‘m leaving too… Want a ride?"
    jump car_choice

label chen_ambition:
    s "I‘m looking for faster career growth."
    show chen_02_smile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 161
    hide chen_00_body
    chen "Ambitious. I like that."
    "{i}He stands up.{/i}"
    hide chen_02_smile
    chen "Don’t work too late. Actually, I‘m leaving too… Want a ride?"
    jump car_choice

label car_choice:
    menu:
        "Alright, thank you.":
            $ car_ride = True
            jump car_scene
            
        "No thanks, I’ll take the subway.":
            jump reject_car

label car_scene:
    s "Alright, thank you."
    chen "Let's go. The car's downstairs."
    scene car_inside with fade
    "{i}The car is clean, with a faint scent of leather.{/i}"
    s "You can just drop me at the the convenience store. I need to grab some breakfast anyway. Sorry to bother you."
    chen "No problem"
    "{i}Chan Wing Yan puts on an old song. Neither of you speaks.{/i}"
    "{i}He stops the car in front of the convenience store.{/i}"
    chen "See you tomorrow. Get some rest."
    jump task_1_4_end2

label reject_car:
    s "No thanks, I’ll take the subway."
    chen "Suit yourself. See you tomorrow."
    hide chen_02_smile_front with moveoutright
    hide chen_03_narroweyes with moveoutright
    "{i}Chan Wing Yan leaves.{/i}"
    "{i}You watch him leave, and something in your chest unclenches. You don't know why.{/i}"
    jump task_1_4_end1

label task_1_4_end1:
    scene office_desk with fade
    "{i}The late office flickers with the neon of code.{/i}"
    "{i}Do electronic bugs dream of bionic fireflies?\nIn the floor-to-ceiling window you saw on your first day, stars ignite, and night falls.{/i}"
    jump task_1_5

label task_1_4_end2:
    scene home with fade
    "{i}You get home, tidy up a bit, and lie down. Soon you're asleep.{/i}"
    "{i}In dreams, the late office flickers with code's cold neon.{/i}"
    "{i}Do electronic bugs dream of bionic fireflies?\nIn the floor-to-ceiling window you saw on your first day, stars ignite, and night falls.{/i}"
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
        "{i}Not all the data looks right, but let‘s leave it for the moment.{/i}"
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
    "{i}The phone buzzes a moment later.{/i}"
    'PurpleNote: Your Follower'"Girl, I saw your post about your family asking for money. Same boat. You’re not alone."
    $ xiaohongshu_contact = True
    "{i}New contact: Xiaozishu Sis{/i}"
    jump task_1_6

# ========== 任务1.6：不经意的触碰 ==========
transform shock:
    linear 0.2 xoffset 10 yoffset -10
    linear 0.1 xoffset -10 yoffset 10
    linear 0.2 xoffset 0 yoffset 0
label task_1_6:
    scene tea_room with fade
    "{i}Week 3. A workday.{/i}"
    show she_05_happy_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "Coffee, yay~ 🎵~"
    hide she_05_happy_nobag onlayer top
    show she_06_surprise_eye_nobag onlayer top at shock:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}Someone reaches over from above you.{/i}"
    
    show chen_06_surprise with dissolve:
        zoom 0.9
        xzoom -1
        xpos 1358
        ypos 162
    chen "Sorry, just grabbing a sugar cube…"
    show chen_04_frontsmile:
        zoom 0.9
        xzoom -1
        xpos 1350
        ypos 161
    chen "Oh, you‘re making coffee too?"
    "{i}He stands very close. His arm brushes against you as he reaches for the sugar.{/i}"
    
    menu:
        "Watch his expression":
            "{i}He’s smiling.{/i}"
            jump touch_reaction
            
        "Look at his hand":
            "{i}His hand rests on the counter, just inches from yours.{/i}"
            jump touch_reaction
            
        "Notice your own feelings":
            jump touch_reaction

label touch_reaction:
    menu:
        "Nothing, it‘s just a bit crowded.":
            jump touch_ignore
            
        "Why is he standing so close?":
            jump touch_alert
            
        "Move away slightly":
            jump touch_move

label touch_ignore:
    show she_03_tinysmile_eye_nobag onlayer top with dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_06_surprise_eye_nobag onlayer top
    s "Yeah, a cup of coffee in the morning helps me wake up."
    hide chen_06_surprise
    chen "You’ve been doing great work. And by the way, your breakdown analysis was excellent. I knew I was right about you."
    jump task_1_6_a

label touch_alert:
    s "……"
    s "Haha, yeah."
    show she_02_sweat_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "{i}Why is he standing so close?{/i}"
    hide chen_06_surprise
    show chen_02_smile_front with dissolve:
        zoom 0.9
        xzoom -1
        xpos 1358
        ypos 162
    chen "You’ve been doing great work. And by the way, your breakdown analysis was excellent. I knew I was right about you."
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
    s "Yeah, a cup of coffee helps me focus at work."
    show chen_04_glance:
        zoom 0.9
        xzoom -1
        xpos 1350
        ypos 161
    "{i}Chan Wing Yan doesn‘t react noticeably. But the moment you move, his eyes flick toward you.{/i}"
    hide chen_04_glance
    chen "You’ve been doing great work. And by the way, your breakdown analysis was excellent. I knew I was right about you."
    jump task_1_6_bc

label task_1_6_a:
    chen "I’ll head off now. Keep up the good work."
    hide chen_04_frontsmile with moveoutright
    hide chen_02_smile_front with moveoutright
    jump task_1_6_end

label task_1_6_bc:
    chen "I’ll head off now. Keep up the good work."
    hide chen_04_frontsmile with moveoutright
    hide chen_02_smile_front with moveoutright
    "{i}He leaves. The steam from the coffee cup rises slowly.{/i}"
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
    hide she_06_surprise_eye_nobag onlayer top
    play sound "phone_vibration.mp3" #替换短版
    show linjie_wx_lockscreen with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    show linjie_wx_0 with dissolve: 
        zoom 1.4
        align (0.5, 0.45)
        pause 1.0
    linjie "I saw you and Chan in the break room. Be careful."
    
    menu:
        "What do you mean?":
            show linjie_wx_a1:
                zoom 1.4
                align (0.5, 0.45)
            s "Be careful? For what?"
            show linjie_wx_a2:
                zoom 1.4
                align (0.5, 0.45)
            linjie "Nothing. Just grab your water and come back. I sent you a new brief."
            show linjie_wx_a3:
                zoom 1.4
                align (0.5, 0.45)
            $ linjie_interest += 1
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "Nothing happened.":
            show linjie_wx_b1:
                zoom 1.4
                align (0.5, 0.45)
            s "Nothing happened."
            show linjie_wx_b2:
                zoom 1.4
                align (0.5, 0.45)
            linjie "…Suit yourself."
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2
            
        "Message deleted.":
            show linjie_wx_c1:
                zoom 1.4
                align (0.5, 0.45)
            "{i}Message deleted.{/i}"
            $ escape += 1
            # hide she_01_normal_eye_o_nobag onlayer top
            scene black with dissolve
            pause 1.0
            jump chapter_2

        "Think it over":
            s "Lam doesn‘t usually say things like this. Why…"
            "{i}You’re mulling over the intent behind this message, carefully typing out a reply, when another message arrives.{/i}"
            show linjie_wx_d1:
                zoom 1.4
                align (0.5, 0.45)
            linjie "Come back soon after you grab your water. I sent you a new brief."
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
                    text"(Start calculating in your head)" size 12 xalign 1.03 yalign 0.3
            

            null height 30
            
            # 关闭按钮
            textbutton "Close":
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

            text"The correct amount should be:" size 24
            null height 30
            text"16,500 + 2,000 + 500 + 500 = 19,500" size 24 xalign 0.5
            text"↑" size 25 xalign 0.395
            null height 20
            # 分隔线
            add Solid("#cccccc") xsize 600 ysize 1 xalign 0.5
            null height 30
            text"My performance adjustment pay was withheld, with no explanation attached." size 24 xalign 0.5
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
    show chapter2_title "Chapter 2 Cracks"
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
            
            textbutton "Close":
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
    
    "{i}【Clue】 Yin‑Yang Wage Divide{/i}" #加音效：噔噔噔↑

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

    $ salary_evidence = True
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

    show pyq at shock:
        zoom 1.5
        xalign 0.5
        yalign 0.35
    s "呃…………" #（有某种不适感在胃里蔓延）
    
    $ fitness_video_watched = True

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
        
        textbutton "beer": 
            action [Hide("drink_menu"), Jump("beer")]
        textbutton "wine": 
            action [Hide("drink_menu"), Jump("wine")]
        textbutton "cocktail": 
            action [Hide("drink_menu"), Jump("cocktail")]
        textbutton "soda": 
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

            textbutton "Close":
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
        $ notice_take_ride("How did he know if it was on his way? ", "Did he ask me where I lived?")
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
    jump she_ending_gulang
        
        
define bella = Character("Bella", color="#fff5bc")

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
    show she_17_sad onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    s "林姐，我……"
    s "昨天晚上庆功宴结束，陈总说要送我回家。"
    
    hide linjie_01_normal
    show linjie_07_shock at shock:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "!"

    s "……我有点东西丢在车上了，不知道陈总是不是把东西放在办公室里，我想去看看。"
    s "不知道是不是只有我丢了东西，如果可能，我想替大家把失物带回来。"
    s "……即使无法弥补曾经那个空缺，也多少能在今后有个心安。"
    show she_17_sad_smile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "你愿意帮帮我吗？"
    hide she_17_sad onlayer top
    
    # 两人对视
    # 调虎离山
    show linjie_06_bar_closeeyes:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "………………"
    hide linjie_07_shock

    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    show she_06_surprise_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    linjie "……我这里还有些文件要处理，先走了。"
    
    hide she_06_surprise_eye_nobag onlayer top

    # 小曼失落
    scene office_desk with fade
    show she_13_sigh2 onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}回到工位上，你继续想着搜证的办法。{/i}"

    # 脚步声音效

    show she_01_normal_eye_o_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "哎？"
    hide she_13_sigh2 onlayer top

    "{i}林姐从你旁边快速走过，她手机里传来微信电话的声音。{/i}"
    "{i}她走过时刻意看了你一眼。{/i}"
    linjie "陈总吗，这里有个甲方的视觉需求我需要找您确认一下，需要在11楼会议室放映，您现在有别的日程吗。"
    linjie "了解，最多耽误您5分钟行吗？"
    linjie "好的，我准备好设备了。"
    "{i}你从工位上看到陈永仁从办公室出来，快步走向电梯。{/i}"

    show she_17_sad_smile onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_01_normal_eye_o_nobag onlayer top
    s "那么，我也该走了。"
    hide she_17_sad_smile onlayer top

jump cyro_office_start

label linjie_refuse_help:
    scene corridor with fade
    show she_17_sad onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    s "林姐，我……"
    s "昨天晚上庆功宴结束，陈总说要送我回家。"

    hide linjie_01_normal
    show linjie_07_shock at shock:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "!"

    s "……我想找证据争一个结果，不管是好是坏"
    s "听你昨天的话，我觉得你是明白的。我计划今天去陈总办公室试试，你能帮我吗？"

    show linjie_06_bar_closeeyes:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "…………"
    hide linjie_07_shock
    
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    show she_06_surprise_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    linjie "佘小姐，昨晚我喝多了，你说的这些我不太记得。"
    linjie "如果昨天和你大吐苦水，说了太多我走到今天的诸多不易，给你造成困扰了，是我失态。"
    linjie "不好意思，我手上还有工作，不能奉陪。"
    hide linjie_06_bar_closeeyes
    hide she_17_sad onlayer top
    
    #林姐走开
    hide linjie_01_normal
    scene black
    linjie "但无论如何，希望你今后顺利。"

    s "……"
    show she_17_sad_smile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "谢谢。"
    hide she_06_surprise_eye_nobag onlayer top
    hide she_17_sad_smile onlayer top
    
    show office_desk with dissolve
    s "{i}林姐拒绝了，接下来怎么办呢？{/i}"
    menu:
        "自己搜查":
            s "趁陈永仁不在时抓紧时间进办公室找找看吧。"
            jump cyro_break_in
        "找别的办法":
            s "再想想别的办法吧。"
            jump encounter_bella

label encounter_bella:
    
    scene corridor with fade
    show she_14_deepthink_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}你在走回自己工位的路上想着其他办法，没注意迎面走来的人。{/i}"
    jump bella

label encounter_bella_leave_safe: #从办公室搜查成功离开跳转
    
    scene corridor with fade
    show she_14_deepthink_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}你在走回自己工位的路上平复紧张的心情，没注意迎面走来的人。{/i}"
    jump bella

label bella:
    show bella_00_shade with vpunch:
        zoom 0.95
        xpos 1450
        ypos 230
    hide she_14_deepthink_card onlayer top
    show she_07_astonish_nobag onlayer top at shock:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 230
    '???' "哎哎哎！"
    s "！"
    show bella_04_file_fall:
        zoom 0.95
        xpos 1450
        ypos 230
    "{i}文件撒了{/i}"
    s "不好意思我在想别的事，我帮你……"
    hide she_07_astonish_nobag onlayer top
    
    #转场
    scene black with fade

    show she_03_tinysmile_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "你看顺序对吗？"
    show bella_01_happy with dissolve:
        zoom 0.95
        xpos 1450
        ypos 230
    '???' "哦没事，陈总要得不急，我等会儿整整，谢谢前辈！"

    show she_01_normal_eye_o_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "找陈总？你……实习生？"
    hide she_03_tinysmile_eye_nobag onlayer top

    show bella_05_shuanglang:
        zoom 0.95
        xpos 1450
        ypos 230
    bella "对的！我是Bella，现在是实习生。"
    extend "不过陈总最近经常派我干活，我觉得我有很大可能转正！"
    show she_17_sad_smile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "哦……那加油啊。"
    hide she_01_normal_eye_o_nobag onlayer top
    hide she_17_sad_smile onlayer top

    jump week13_lawyer_evidence_check

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

    # "Search Complete"
    # "Evidence Collected: 4"
               
    hide screen cyro_office_timer

    scene black

    if found_evidence > 0:
        "{i}You take photos of all clues you have found, put everything back in place, and slip out before Chan Wing Yan returns.{/i}"
        jump encounter_bella_leave_safe
    else:
        "{i}没有找到证据，但该走了{/i}"
    jump week13_lawyer_evidence_check

# ============================================================
# 时间耗尽
# ============================================================

label cyro_office_time_up:

    $ cyro_office_time_left = 0

    hide screen cyro_office_timer

    "时间到了。"

    "门外传来脚步声。"
    
    # 脚步声停在身后，小曼回头
    
    chen "看看，这是谁呀？"
    scene black with fade
    show chen_08_horrible with dissolve:
        zoom 2.0 xalign 0.45 ypos -600
        linear 1.5 zoom 2.0 xalign 0.45 ypos -500
        linear 0.1 zoom 7 xalign 0.65 ypos -800
    pause 1.5
    jump she_ending_gulang_or_songbie

    return


label she_ending_gulang_or_songbie:
    if she_friend_full():
        jump she_ending_songbie
    else:
        jump she_ending_gulang

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
    xoffset -250
    linear 0.5 xoffset -50
    pause 0.3
    linear 0.6 xoffset -250
    pause 0.3

transform appear_disappear:
    alpha 1.0
    pause 0.5
    linear 0.3 alpha 0
    pause 0.5
    linear 0.3 alpha 1.0
    repeat


transform push_button_shake:
    xoffset 0 yoffset 0
    linear 0.3 xoffset -100 yoffset -20
    linear 0.2 xoffset 110 yoffset 40 
    linear 0.4 xoffset -120 yoffset 30
    linear 0.3 xoffset 80 yoffset -50
    repeat

# 带倒计时的QTE screen
# screen car_qte_1_timer(duration=1.2):
#    modal True
    
    #     # 倒计时显示
#     vbox:
#         align (0.5, 0.2)
#         spacing 10
        
#         text "【Boundary Alert】" at blink_effect:
#             size 40
#             color "#FC8181"
#             xalign 0.5
        
#         text "【Boundary Warning】System Warning: Interference protocol activated" at subtle_shake:
#             size 20
#             color "#A0AEC0"
#             xalign 0.5
        
#         text "[countdown_1]" at blink_effect:
#             align (0.5, 0.5)
#             size 30
#             color "#E53E3E"
    
#     # 选项区域
#     hbox:
#         align (0.5, 0.65)
#         spacing 30
        
#         # A. 躲开 - 滑动按钮
#         button at slide_button:
#             background "#e53e3e"
#             hover_background "#fc8181"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "a"), Return(True)]
#            
#             text "Dodge" at subtle_shake:
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16
        
#         # B. 不说话 - 固定
#         button:
#             background "#4a5568"
#             hover_background "#718096"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "b"), Return(True)]
#             
#             text "Stay silent":
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16
        
#         # C. 说"不要" - 闪烁出现
#         button at appear_disappear:
#             background "#d69e2e"
#             hover_background "#f6e05e"
#             xsize 160
#             ysize 50
#             action [SetVariable("qte_result", "c"), Return(True)]
            
#             text "Say stop":
#                 align (0.5, 0.5)
#                 color "#FFFFFF"
#                 size 16
    
#     # 关键：极短倒计时，时间到自动返回False
#     timer duration action Return(False)

# ========== 游戏主流程 ==========
label chapter3:

    $ qte_state = QTEState()

    "车内。夜色。空调开得很低。"

    scene black with fade
    pause 1.0
    show expression Movie(play="videos/xsr_anime.webm", size=(1920, 1080)) as xsr_anime at truecenter
    with dissolve
    $ renpy.pause(11.55, hard=True)
    hide xsr_anime with fade

    jump car_xsr

# 主QTE流程控制label
label car_xsr:
    # 初始化
    $ qte_cycle = 0
    $ qte_phase = "movie"
    $ countdown_1 = 10
     
    # 开始循环
    jump qte_loop

# 性骚扰QTE计时条
screen qte_choice_timer_5(question, time_limit=2.5):
    modal True
    
    # 使用 persistent 或外部变量来跟踪，避免 screen 重置
    default start_time = renpy.get_game_runtime()
    default local_time_left = time_limit
    
    # 关键：只更新倒计时，不重置 start_time
    timer 0.05 repeat True action [
        SetScreenVariable("local_time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
        If(
            local_time_left <= 0,
            true=[
                Return("timeout")  # 返回超时，由 label 处理后续
            ],
            false=NullAction()
        )
    ]
    
    $ progress = local_time_left / time_limit if time_limit > 0 else 0
# screen qte_choice_timer_5(question, time_limit=1.5):
#     modal True
    
#     default start_time = renpy.get_game_runtime()
#     default time_left = time_limit
    
#     timer 0.05 repeat True action [
#         SetScreenVariable("time_left", max(0, time_limit - (renpy.get_game_runtime() - start_time))),
#         If(time_left <= 0, true=[Hide("qte_choice_timer_5"), 
#             SetScreenVariable("qte_cycle", qte_cycle + 1),
#             SetScreenVariable("qte_phase", "movie"),
#             Text("abced")
#             Jump("qte_loop")], false=NullAction())
#     ]
    
#     $ progress = time_left / time_limit
    

    # 选项区域
    hbox:
        align (0.5, 0.65)
        spacing 30
        
        # A. 躲开 - 滑动按钮
        imagebutton at slide_button:
            idle "circle_button1"
            action [SetVariable("qte_result", "a"), Return()]

        # B. 不说话 - 固定
        imagebutton:
            idle "circle_button2"
            xoffset -100
            yoffset 200
            action [SetVariable("qte_result", "b"), Return()]
        
        # C. 说"不要" - 闪烁出现
        imagebutton at appear_disappear:
            idle "circle_button3"
            xoffset -100
            yoffset 200
            action [SetVariable("qte_result", "c"), Return()]

    
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
        text "[local_time_left:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"



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
    show expression Movie(play="videos/tv_breakdown.webm", size=(1920, 1080)) as flash_video at truecenter
    
    # 播放固定时间（1秒）
    $ renpy.pause(1.0, hard=True)
    
    # 隐藏视频
    hide flash_video

    if qte_cycle == 0:
        scene black
        image harrassment_01 = ParameterizedText(xalign=0.5, yalign=0.45, size=168, color="#ffffff")
        show harrassment_01 "What? What's happening?" at shake

    #骚扰01
    if qte_cycle == 1:
        scene xsr_1

    #骚扰02
    if qte_cycle == 2:
        scene xsr_2
        image harrassment_02a = ParameterizedText(xalign=0.5, yalign=0.45, size=168, color="#8a1616")
        image harrassment_02b = ParameterizedText(xalign=0.505, yalign=0.454, size=168, color="#b50d0d", bold=True)
        show harrassment_02a "Run Run Run!!!!!!" at re_shake
        show harrassment_02b "Run Run Run!!!!!!" at shake

    #骚扰03
    if qte_cycle ==3:
        show xsr_3 at heartbeat
        image harrassment_03a = ParameterizedText(xalign=0.35, yalign=0.45, size=100, color="#8a1616")
        image harrassment_03b = ParameterizedText(xalign=0.65, yalign=0.55, size=100, color="#8a1616")
        show harrassment_03a "GET OUT OF THE CAR" at shake
        show harrassment_03b "HELP HELP HELP HELP" at shake
        scene xsr_qte
    
    # 切换到screen阶段
    $ qte_phase = "screen"
    # hide flash
    
    jump qte_loop

# Screen操作阶段（玩家可操作，极短时间）
label qte_screen_phase:
    # 减少倒计时
    $ countdown_1 -= 1

    # 关键：使用 call screen 获取返回值
    call screen qte_choice_timer_5("做出反应！", time_limit=2.5)
    
    # _return后的值现在可能是 "a", "b", "c", 或 "timeout"
    if _return == "timeout":
        # 超时未选择，默认走 "b"（沉默）
        $ qte_result = "b"
        $ qte_cycle += 1
        $ qte_phase = "movie"
        jump qte_loop
    else:
        # 玩家做出了选择，那abc都可能
        scene black with dissolve
        jump qte_result_check


# 结果处理
label qte_result_check:

    if qte_result == "timeout":
        $ qte_result = "b"

    if qte_result == "a":
        jump car_run

    elif qte_result == "b":
        scene xsr_3 with vpunch
        $ escape += 1
        "{i}看着你沉默的反应，陈永仁离你更近。{/i}"
        "{i}他的手在你脸上摩挲，随后顺势向下，手指扫过你的颌骨。{/i}"
        jump car_continuation

    else:
        # $ qte_state.choices_made.append("拒绝")
        scene car_inside with dissolve
        s "陈总，您自重。"

        "{i}陈永仁的手微微一顿。{/i}"
        chen "别哪样？我就是欣赏你。欣赏一个人有错吗？"

        "{i}他挑起你的一缕头发，凑近嗅闻：{/i}"
        chen "就是……欣赏。"

        jump kiss_sequence

label car_continuation:
    "{i}他抬起你的下巴端详着你。{/i}"
    chen "工作的时候那么有冲劲，现在倒是很青涩。"
    chen "真是不错的反应。"
    chen "让人想知道更多……"
    "{i}他要吻你。{/i}" with vpunch

    jump kiss_sequence

# =========================
# 呕呕呕推开他的QTE
# =========================

screen push_away_qte (time_limit_2 = 8):
    modal True
    
    # 使用 persistent 或外部变量来跟踪，避免 screen 重置
    default start_time_2 = renpy.get_game_runtime()
    default local_time_left_2 = time_limit_2
    
    # 关键：只更新倒计时，不重置 start_time
    timer 0.05 repeat True action [
        SetScreenVariable("local_time_left_2", max(0, time_limit_2 - (renpy.get_game_runtime() - start_time_2))),
        If(
            local_time_left_2 <= 0,
            true=[
                Jump("kiss_ending_long")  # 返回超时，由 label 处理后续
            ],
            false=NullAction()
        )
    ]
    
    $ progress = local_time_left_2 / time_limit_2 if time_limit_2 > 0 else 0

    add "#000000CC"


    vbox:
        align (0.5, 0.3)
        spacing 20

        text "推开他！":
            size 24
            color "#FC8181"
            xalign 0.5
        text "[qte_state.push_count] / 10":
            size 24
            color "#FC8181"
            xalign 0.5

    imagebutton at push_button_shake:
        idle "circle_button"
        hover "circle_button_press"
        align(0.5, 0.5)
        action [SetVariable("qte_state.push_count", qte_state.push_count + 1), #play sound "ding" #记得加音效
                If(qte_state.push_count >= 10, true=Jump("pushed_away"), false=NullAction())]

    # 动态难度计时器
    # timer (3.0 - qte_state.push_count * 0.4) action [Return(False)]
    
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
        text "[local_time_left_2:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"


# 10秒抉择窗口
default final_choice = ""

screen final_choice(time_limit_3 = 10):
    modal True
    
    # 使用 persistent 或外部变量来跟踪，避免 screen 重置
    default start_time_3 = renpy.get_game_runtime()
    default local_time_left_3 = time_limit_3
    
    # 关键：只更新倒计时，不重置 start_time
    timer 0.05 repeat True action [
        SetScreenVariable("local_time_left_3", max(0, time_limit_3 - (renpy.get_game_runtime() - start_time_3))),
        If(
            local_time_left_3 <= 0,
            true=[
                Return("hug")  # 返回超时，由 label 处理后续
            ],
            false=NullAction()
        )
    ]
    
    $ progress = local_time_left_3 / time_limit_3 if time_limit_3 > 0 else 0

    vbox:

        # 拥抱选项
        imagebutton:
            idle "circle_button4"
            hover "circle_button4_press"
            xpos 860
            ypos 550
            action [SetVariable("final_choice", "hug"), Return("hug")] # action (play sound"ding") #记得加音效

        # 逃跑选项（第5秒出现）
        if local_time_left_3 < 6:
            imagebutton at appear_disappear:
                idle "circle_button5"
                hover "circle_button5_press"
                xpos 860
                ypos 600
                action [SetVariable("final_choice", "escape"), Return("escape")] # action (play sound"ding") #记得加音效
        else:
            pass

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
        text "[local_time_left_3:.1f]":
            xalign 0.5
            yalign 0.55
            size 18
            color "#000000"

label kiss_sequence:
    scene lean_notext at vpunch
    $ qte_state.push_count = 0

    # while qte_state.push_count < 5:
    call screen push_away_qte()

label pushed_away:
    scene car_inside with dissolve
    "你推开了他。"
    "陈永仁愣了一下:"
    chen "呵呵，是我会错意了吗。"

    chen "是不能接受进展这么快？啊，我明白了。"
    chen "那来抱一下。朋友嘛？"

    jump final_decision

label kiss_ending_long:
    s "使不出力"
    s "不要"
    s "{cps=50}不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要不要{/cps}"
    # $ has_kiss_evidence = True

    scene black with fade
    $renpy.pause(1.5, hard=True)
    "{i}吻持续了很久。{/i}"
    "{i}当你终于能呼吸时，他已经收回了身体，仿佛什么都没发生。{/i}"
    "{i}你想吐。{/i}"
    extend "\n{i}{cps=2}你想吐。{/cps}{/i}"
    "{i}站在房门口时，你根本不记得自己是怎么到家的。{/i}"
    # extend "\n{i}{cps=12}你想吐你想吐你想吐你想吐你想吐。{/cps}{/i}"

    jump room_scene

label final_decision:

    $ final_choice = ""
    $ show_sequential_thoughts(
        "What I should do?",
        "He's looking.",
        "Maybe a hug can fix everything..."
    )
    call screen final_choice()

    if final_choice == "hug":
        $ escape += 1
        jump ending_hug
    else:
        jump ending_escape

label ending_hug:
    # $ has_hug_evidence = True
    scene black with dissolve
    
    "{i}你麻木地拥抱了他。{/i}"
    "{i}感觉到他手臂的挤压。{/i}"
    chen "这就对了，"
    extend "慢慢来。哈哈哈。"

    scene car_outside
    "{i}车停下的时候他给你解开安全带。{/i}"
    chen "明天见，小曼，今晚很愉快。"
    "{i}你看着他的车尾灯消失在街角。{/i}"
    "{i}{cps=2}你想吐。{/cps}"
    extend "\n{i}{cps=12}你想吐你想吐你想吐你想吐你想吐。{/cps}{/i}"
    scene black with fade

    jump room_scene

label ending_escape:
    "{i}你找到了安全带卡扣，但却没办法控制手指的颤抖。{/i}"
    "#这里记得加音效"
    # play sound "kada" # 记得加音效
    # "{i}不停地尝试后安全带终于解开了{/i}"
    scene street with dissolve
    "{i}你推开车门，踉跄下车，跑向大路。{/i}"
    scene black with fade
    jump room_scene


label car_run:
    "{i}你找到了安全带卡扣，手指止不住地颤抖。{/i}"
    "{i}你没有停止尝试。{/i}"
    "#这里记得加音效"
    # play sound "kada" # 记得加音效
    scene street with dissolve
    "{i}你推开车门，踉跄下车，跑向大路。{/i}"
    chen "小曼！小曼————"
    "{i}你没有回头。{/i}"
    scene black with fade

# ------------------------
# 回家解离情绪

screen room_scan():
    modal True

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

    textbutton "Sleep":
        background Frame("gui/textbox.png")
        padding (180, 0)
        hover_background Frame("blue_textbox")
        align (0.5, 0.85)
        text_color "#888888"
        text_hover_color "#ffffff"
        action Return(False)

label room_scene:
    "{i}站在房门口时，你根本不记得自己是怎么到家的。{/i}"
    scene home with dissolve
    "{i}门在身后关上，世界突然安静得可怕。{/i}"

    $ clicked_item = ""

    while True:
        call screen room_scan()

        if not _return:
            jump game_sleep

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

label game_sleep:
    
    # if "拒绝" in qte_state.choices_made:
    #     "你坐在床边，手机亮了又暗。"
    #     "我拒绝了。"
    #     extend "我推开了他。"
    #     "但为什么，心跳还是这么快？"
    
    if escape >= 4:
        "{i}快睡吧……快睡吧……{/i}"
        "{i}醒来之后一切都会变好的，{/i}"
        extend "{i}{cps=3}一切，都会{/cps}{/i}"
        extend "{b}{i}{cps=3}变好的。{/cps}{/i}{/b}"
        jump tuoniao

    else:
        if final_choice == "escape":
            "{i}你逃跑了。{/i}"
            "{i}但逃跑之后呢？{/i}"
        else:
            "{i}温热的躯体与触感。{/i}"
            extend "{i}却像濡湿阴凉的软体动物爬过的黏腻。{/i}"
            s "{cps=10}…………………………………………………………{/cps}"

        "{i}该睡了，但今晚又该如何做个好梦？{/i}"  # ← 改为8空格缩进

    jump chapter4

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
default route_public = False
default route_leave = False

# # 路线条件变量
# default lawyer_contacted = False
default courage = 0
# default xiaohongshu_fans = 0

# # 路线A变量
default police_credibility = 100
# default police_report_2 = False

# 路线B变量
default hr_talk_done = False
default department_reorganized = False

# 路线C变量
default post_views = 0
default post_comments = 0
default media_contacted = 0
default lawyer_letter_received = False
default public_pressure = 0

# ==========================================
# 小红书发帖：证据联动变量
# ==========================================

default xhs_selected_evidence = []
default xhs_post_title = ""


init python:

    def get_xhs_available_evidence():
        items = []

        # 1. 工资差异记录：不是性骚扰直接证据，可触发歪结局
        if salary_evidence:
            items.append({
                "id": "salary",
                "label": "工资差异记录",
                "related": False
            })

        # 2. 上车经历
        if car_event:
            items.append({
                "id": "car",
                "label": "上车经历",
                "related": True
            })

        # 3. 旧员工档案
        if cyro_office_found_files:
            items.append({
                "id": "files",
                "label": "旧员工档案",
                "related": True
            })

        # 4. 未拆封香水礼盒
        if cyro_office_found_perfume:
            items.append({
                "id": "perfume",
                "label": "未拆封香水礼盒",
                "related": True
            })

        # 5. 夹在书里的照片
        if cyro_office_found_photo:
            items.append({
                "id": "photo",
                "label": "夹在书里的照片",
                "related": True
            })

        # 6. 黑色笔记本
        if cyro_office_found_notebook:
            items.append({
                "id": "notebook",
                "label": "黑色笔记本",
                "related": True
            })

        return items


    def chunk_list(items, size):
        return [items[i:i + size] for i in range(0, len(items), size)]


    def xhs_toggle_evidence(evidence_id):
        global xhs_selected_evidence

        if evidence_id in xhs_selected_evidence:
            xhs_selected_evidence.remove(evidence_id)
        else:
            xhs_selected_evidence.append(evidence_id)

        renpy.restart_interaction()


    def make_xhs_post_body(selected_ids):
        all_items = get_xhs_available_evidence()
        label_map = {item["id"]: item["label"] for item in all_items}

        selected_labels = []

        for evidence_id in selected_ids:
            if evidence_id in label_map:
                selected_labels.append(label_map[evidence_id])

        if len(selected_labels) == 0:
            if len(all_items) == 0:
                return "I didn't leave any evidence. But that doesn't mean nothing happened. It's just that this time, I don't want to pretend nothing happened."
            else:
                return "I have some materials, but I haven't decided which part to release yet."

        return "I've sorted " + str(len(selected_labels)) + "pieces of material:" + "、".join(selected_labels) + "I know this path will be difficult, but I don't want to remain silent any longer."


    def xhs_only_unrelated_evidence(selected_ids):
        all_items = get_xhs_available_evidence()
        related_map = {item["id"]: item["related"] for item in all_items}

        if len(selected_ids) == 0:
            return False

        for evidence_id in selected_ids:
            if related_map.get(evidence_id, False):
                return False

        return True

# 路线D变量
default resignation_written = False
default last_day_done = False

default disclosure_level = "medium"

# 第五章入口
# ----------------------
# label chapter5:
#     $ chapter5_started = True
    
#     scene bg bedroom_night
#     with fade
    
#     "第15周。周三。凌晨1:17。"
#     "你把所有东西摊开在床上。"
#     "曾经的报警回执、日记、工资条、小红书评论……"
#     "还有一张收藏了很久的律师名片。"
    
#     jump week13_lawyer_evidence_check


# ==========================================
# 第五章前置：律师证据审查
# 放置位置：label chapter5 后面，screen route_choice_screen 前面
# ==========================================

define zhao_lawyer = Character("Lawyer Zhao")

# 如果前面已经定义过这些 default，重复 default 不会重置已存在存档里的值
default evidence_count = 0

default has_message_evidence = False # 健身视频
default has_car_xsr_experience = False # 性骚扰场景
# default has_hug_evidence = False # 联动完成
# default has_kiss_evidence = False # 联动完成


# default has_audio_evidence = False
# default has_photo_or_video_evidence = False
# default has_witness_evidence = False
# default has_other_victim_evidence = False
# default has_company_complaint_evidence = False
# default has_medical_or_psychological_evidence = False
# default has_retaliation_evidence = False

# 避免你 route_choice_screen 里 xiaohongshu_fans 未定义时报错
default xiaohongshu_fans = 0


label week13_lawyer_evidence_check:

    # ----------------------
    # 自动整理已有证据
    # ----------------------

    $ evidence_count = 0

    # 办公室搜证数量
    if found_evidence > 0:
        $ evidence_count += found_evidence # 这里把办公室四个都算了，不用多写
        # $ has_photo_or_video_evidence = True
        # $ has_other_victim_evidence = True

    # # 工资差异证据
    # if salary_evidence:
    #     $ evidence_count += 1
    #     $ has_company_complaint_evidence = True

    # 车内经历
    if car_event:
        $ evidence_count += 1
        $ has_car_xsr_experience = True
        $ has_kiss_evidence = True

    # # 林姐线索 / 模式识别
    # if hidden_truth_unlocked:
    #     $ evidence_count += 1
    #     $ has_witness_evidence = True
    #     $ has_other_victim_evidence = True

    # # 小红书联系 / 其他受害者线索
    # if xiaohongshu_contact:
    #     $ evidence_count += 1
    #     $ has_other_victim_evidence = True

    # 如果玩家看过陈永仁深夜健身视频，算作一条模糊数字证据
    if fitness_video_watched:
        $ evidence_count += 1
        $ has_message_evidence = True

    # 如果没有专门设置录音/医疗/报复证据，保持 False

    # ----------------------
    # 正式剧情
    # ----------------------

    scene cafe with fade

    "第13周。中环某咖啡馆。"
    show she_01_normal_nocard_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show lawyer_01_normal:
        zoom 0.76
        xpos 1450
        ypos 240
    zhao_lawyer "给我看看你有的。"

    show she_01_normal_eye_nocard onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_01_normal_nocard_eye onlayer top
    # ----------------------
    # 证据数量 check
    # ----------------------

    if evidence_count == 0:
        show lawyer_02_surprise:
            zoom 0.76
            xpos 1450
            ypos 240
        zhao_lawyer "没有证据？"
        zhao_lawyer "法律判断要以证据为基础做出。"
        extend "没有证据难立案，难证明，也容易被反过来质疑。"
        show lawyer_01_normal:
            zoom 0.76
            xpos 1450
            ypos 240
        zhao_lawyer "你经历的痛苦是真的，我明白。"
        zhao_lawyer "但法律要看的，是能不能把痛苦变成证据。"
        zhao_lawyer "不过别灰心。媒体、民众舆论也能让不公被看见。"
        zhao_lawyer "但这条路也险。很多人把舆论当做武器，最后却失去了对它的控制。"
        zhao_lawyer "你可能会被陌生人审判，受到各种中伤。"
        zhao_lawyer "佘女士，要想清楚啊。"
        hide she_01_normal_eye_nocard onlayer top
        jump chapter5_route_selection

    elif evidence_count <= 3:

        zhao_lawyer "证据太少，还不能形成完整链条。"
        zhao_lawyer "它们能证明你不舒服，但不一定能证明他做了什么。"
        zhao_lawyer "对方可以说是误会、玩笑，或者你们关系本来就不错。"

    else:

        zhao_lawyer "材料不少，但法律看的是关键证据。"
        zhao_lawyer "如果没有直接证明，他仍然有解释空间。"

    # ----------------------
    # 证据类型 check
    # ----------------------

    zhao_lawyer "我逐项看。"

    if has_message_evidence:

        zhao_lawyer "聊天记录能证明联系。"
        zhao_lawyer "但如果内容不够明确，他可以说是关心、玩笑，或者普通同事互动。"

    if has_car_xsr_experience:

        zhao_lawyer "车里的事最严重，也最难证明。"
        zhao_lawyer "没有监控、录音、证人，你最多能证明你上过车。"
        zhao_lawyer "但车里具体发生了什么，法律上还需要更直接的材料。"

    if cyro_office_found_files:
        
        zhao_lawyer "这些档案的记录不能直接表明她们离职的原因是陈永仁的性骚扰。"

    if cyro_office_found_perfume: 

        zhao_lawyer "没有贺卡指明收礼人，香水礼盒可以送给任何人。"
        zhao_lawyer "就算收礼方的身份明确了，陈永仁也可以辩驳说这是正常社交。"

    if cyro_office_found_notebook:
        zhao_lawyer "记录语焉不详，甚至没有明确的姓名指向，很难作为证据。"

    if cyro_office_found_photo:
        zhao_lawyer "这张照片拍到的动作倒是很亲密，但是很难达到性骚扰的判定标准。"
        zhao_lawyer "而且这上面的人不是你……"

    # if has_hug_evidence:

    #     zhao_lawyer "拥抱可以被他说成普通安慰。"
    #     zhao_lawyer "尤其在你们存在上下级关系时，他会把它包装成关心。"

    # if has_kiss_evidence:

    #     zhao_lawyer "吻更严重。"
    #     zhao_lawyer "但如果没有证人、录像、录音，他可以否认，也可以说你同意了。"
    #     zhao_lawyer "这就是这类案件最残酷的地方。"

    # if has_audio_evidence:

    #     zhao_lawyer "录音有用。"
    #     zhao_lawyer "但如果内容模糊，或者没有清楚指向具体行为，他仍然可以解释成别的事。"

    # if has_photo_or_video_evidence:

    #     zhao_lawyer "照片和视频要看有没有拍到关键动作。"
    #     zhao_lawyer "如果只是同框、同行、同处一个空间，只能证明你们在一起。"

    # if has_witness_evidence:

    #     zhao_lawyer "证人有用。"
    #     zhao_lawyer "但如果她只是听你转述，只能算辅助。"
    #     zhao_lawyer "如果她亲眼见过、亲耳听过，证明力会强很多。"

    # if has_other_victim_evidence:

    #     zhao_lawyer "其他受害者能证明他可能有行为模式。"
    #     zhao_lawyer "但它不能直接证明他对你做过什么。"
    #     zhao_lawyer "法律会把这两件事分开看。"

    # if has_company_complaint_evidence:

    #     zhao_lawyer "投诉记录能证明你反映过。"
    #     zhao_lawyer "但它不一定能证明他做过。"
    #     zhao_lawyer "公司也可能说，他们已经按流程处理。"

    # if has_medical_or_psychological_evidence:

    #     zhao_lawyer "医疗或心理记录能证明你受到了伤害。"
    #     zhao_lawyer "但它不一定证明伤害是谁造成的。"

    # if has_retaliation_evidence:

    #     zhao_lawyer "打击报复材料可以走公司责任。"
    #     zhao_lawyer "但你要证明它和投诉之间有明确关联。"

    # ----------------------
    # 总结
    # ----------------------

    zhao_lawyer "这些证据无法形成强力的证据链，打官司胜诉很难。"

    s "没有其他反抗的可能了吗？"

    zhao_lawyer "法律之外，还有人情。"

    zhao_lawyer "媒体、民众舆论也能让不公被看见。"

    zhao_lawyer "但这条路也险。很多人把舆论当做武器，最后却失去了对它的控制。"
    zhao_lawyer "你可能会被陌生人审判，受到各种中伤。"

    "{i}赵律师把证据放回桌上。{/i}"
        
    zhao_lawyer "佘女士，要想清楚啊。"
    hide lawyer_01_normal with dissolve

    hide she_01_normal_eye_nocard onlayer top

    # $ lawyer_contacted = True

    # if evidence_count > 0:
    #     $ evidence_complete = True
    # else:
    #     $ evidence_complete = False

    jump chapter5_route_selection

# ----------------------
# 第五章路线选择标签（改名避免冲突）
# ----------------------
label chapter5_route_selection:

    scene home

    call screen she_final_route_screen

    $ result = _return

    if result == "legal":
        jump she_route_legal

    elif result == "hr":
        jump she_route_hr

    elif result == "public":
        jump she_route_public

    elif result == "linjie":
        jump she_route_linjie



# ==========================================
# 小红书发帖界面
# ==========================================
screen xiaozishu_post():
    modal True

    add Solid("#f6f2fb")

    $ available_evidence = get_xhs_available_evidence()
    $ evidence_rows = chunk_list(available_evidence, 2)
    $ post_body = make_xhs_post_body(xhs_selected_evidence)

    # 主卡片
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 720
        background "#ffffff"
        padding (48, 38)

        vbox:
            spacing 22

            # 顶部
            frame:
                xfill True
                ysize 58
                background "#7b3fb2"
                padding (20, 10)

                text "xiaozishu":
                    size 24
                    color "#ffffff"
                    xalign 0.5
                    yalign 0.5

            null height 8

            # 标题
            hbox:
                spacing 18
                yalign 0.5

                text "Title":
                    size 18
                    color "#333333"
                    yalign 0.5

                textbutton (xhs_post_title if xhs_post_title else "Click to enter a title..."):
                    xsize 660
                    ysize 46
                    background "#f3edf8"
                    hover_background "#eadcf5"
                    text_size 18
                    text_color ("#333333" if xhs_post_title else "#9b8aaa")
                    text_hover_color "#333333"
                    action Show("post_title_input")

            # 披露程度
            text "Level of disclosure:":
                size 18
                color "#333333"

            hbox:
                spacing 12

                textbutton "隐去细节":
                    xsize 180
                    ysize 48
                    background ("#7b3fb2" if disclosure_level == "low" else "#eee6f5")
                    hover_background "#9b62c9"
                    text_size 18
                    text_color ("#ffffff" if disclosure_level == "low" else "#6b3a91")
                    text_hover_color "#ffffff"
                    action SetVariable("disclosure_level", "low")

                textbutton "部分实名":
                    xsize 180
                    ysize 48
                    background ("#7b3fb2" if disclosure_level == "medium" else "#eee6f5")
                    hover_background "#9b62c9"
                    text_size 18
                    text_color ("#ffffff" if disclosure_level == "medium" else "#6b3a91")
                    text_hover_color "#ffffff"
                    action SetVariable("disclosure_level", "medium")

                textbutton "完全公开":
                    xsize 180
                    ysize 48
                    background ("#7b3fb2" if disclosure_level == "high" else "#eee6f5")
                    hover_background "#9b62c9"
                    text_size 18
                    text_color ("#ffffff" if disclosure_level == "high" else "#6b3a91")
                    text_hover_color "#ffffff"
                    action SetVariable("disclosure_level", "high")

            # 附带证据
            text "附带证据：":
                size 18
                color "#333333"

            if len(available_evidence) == 0:

                frame:
                    xsize 760
                    ysize 50
                    background "#f3edf8"
                    padding (18, 10)

                    text "暂无可附带证据":
                        size 18
                        color "#9b8aaa"
                        yalign 0.5

            else:

                vbox:
                    spacing 12

                    for row in evidence_rows:

                        hbox:
                            spacing 12

                            for ev in row:

                                textbutton ev["label"]:
                                    xsize 330
                                    ysize 48
                                    background ("#7b3fb2" if ev["id"] in xhs_selected_evidence else "#eee6f5")
                                    hover_background "#9b62c9"
                                    text_size 18
                                    text_color ("#ffffff" if ev["id"] in xhs_selected_evidence else "#6b3a91")
                                    text_hover_color "#ffffff"
                                    action Function(xhs_toggle_evidence, ev["id"])

            # 发布内容
            text "Release content:":
                size 18
                color "#333333"

            frame:
                xsize 800
                ysize 145
                background "#f8f4fb"
                padding (20, 16)

                text post_body:
                    size 18
                    color "#333333"
                    xmaximum 760

            null height 4

            textbutton "发布":
                xalign 0.5
                xsize 240
                ysize 52
                background "#7b3fb2"
                hover_background "#9b62c9"
                text_size 18
                text_color "#ffffff"
                text_hover_color "#ffffff"
                action Return({
                    "evidence": xhs_selected_evidence,
                    "title": xhs_post_title,
                    "body": post_body
                })


# ==========================================
# 标题选择界面
# ==========================================
screen post_title_input():
    modal True

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        background "#ffffff"
        padding (38, 34)

        vbox:
            spacing 18

            text "选择标题":
                size 22
                color "#333333"
                xalign 0.5

            textbutton "在游戏公司被性骚扰，我决定说出来":
                xsize 600
                ysize 48
                background "#f3edf8"
                hover_background "#7b3fb2"
                text_size 18
                text_color "#333333"
                text_hover_color "#ffffff"
                action [
                    SetVariable("xhs_post_title", "在游戏公司被性骚扰，我决定说出来"),
                    Hide("post_title_input")
                ]

            textbutton "关于某游戏公司高管，一些必须讲的事":
                xsize 600
                ysize 48
                background "#f3edf8"
                hover_background "#7b3fb2"
                text_size 18
                text_color "#333333"
                text_hover_color "#ffffff"
                action [
                    SetVariable("xhs_post_title", "关于某游戏公司高管，一些必须讲的事"),
                    Hide("post_title_input")
                ]

            textbutton "22k vs 19.5k，不只是工资":
                xsize 600
                ysize 48
                background "#f3edf8"
                hover_background "#7b3fb2"
                text_size 18
                text_color "#333333"
                text_hover_color "#ffffff"
                action [
                    SetVariable("xhs_post_title", "22k vs 19.5k，不只是工资"),
                    Hide("post_title_input")
                ]

            null height 6

            textbutton "取消":
                xalign 0.5
                xsize 180
                ysize 44
                background "#eee6f5"
                hover_background "#7b3fb2"
                text_size 18
                text_color "#6b3a91"
                text_hover_color "#ffffff"
                action Hide("post_title_input")



# ==========================================
# SHE 新结局区
# ==========================================

label ending_a_empty_document:
    # A-1【空文】

    scene bg police_station
    with fade

    "{i}You submit the evidence photos you found.{/i}"
    "{i}The officer looks through the materials you provided.{/i}"

    if not car_ride:
        "Police Officer" "The people in these materials don’t look like you..."
        s "These are other coworkers he harassed."
        "Police Officer" "Miss Sheh, under our law, whoever makes a claim must provide evidence. But you cannot provide evidence on someone else’s behalf."
        s "..."
        "Police Officer" "...This is the receipt for your report. We’ll notify you if there is any progress."
        s "Did you look at the chat records, workplace recordings, and coworker testimonies I submitted?"
        "Police Officer" "We have received all the materials. We’ll process and investigate according to procedure. You may go."
    else:
        "Police Officer" "Alright, Miss Sheh. We’ve received your statement and materials."
        s "Will the case be filed?"
        "Police Officer" "We’ll process and investigate according to procedure. You may go."

    scene black
    with fade

    "{i}Three weeks later:{/i}"
    "{i}Insufficient evidence. Case not accepted.{/i}"

    $ unlock_cg("kongwen")  # 解锁"空文"CG

    # CG：空文
    # scene cg_empty_document with fade
    # "{i}A blank document. A report that never became a case.{/i}"
    $ unlock_cg("kongwen")

    jump ending_common


label ending_b_water:
    # B-1【饮水】

    scene black
    with fade

    "{i}File: Transfer Notice. Chan Wing Yan’s signature is on it.{/i}"
    "{i}You reported Chan Wing Yan to the company for sexual harassment.{/i}"
    "{i}Without enough evidence, the company does not accept your report.{/i}"
    "{i}Chan Wing Yan finds out about it. You are transferred somewhere else.{/i}"

    scene office_desk
    with fade

    s "My new desk is still on the same floor as the design department. Just very far away."
    s "The water dispenser becomes my only colleague. It doesn’t talk, but at least it doesn’t touch me."
    s "The edge of the office. The edge of the work."
    s "If there’s one good thing, I guess drinking water has become easier."

    "{i}You take a sip of water.{/i}"

    "{i}Across the room, you see two people enter another pantry one after another.{/i}"

    s "Contact: Bella. I saw Chan Wing Yan enter the pantry with you. Be careful."

    s "The water temperature is just right."

    "{i}In the corner near the pantry, a folding chair becomes your new workstation.{/i}"
    "{i}Administrative scraps pile up in front of you: printing meeting notes, sticking receipts, sorting reimbursement forms, checking delivery lists.{/i}"
    "{i}Your original desk has long been moved to the farthest corner of the office.{/i}"
    "{i}All permissions for core projects have been removed from your computer.{/i}"
    "{i}No real work emails come anymore.{/i}"

    $ unlock_cg("yinshui")

    # CG：饮水
    # scene cg_water with fade
    $ unlock_cg("yinshui")

    jump ending_common


label ending_c_exit:
    # C-1【退场】

    scene bg hr_office
    with fade

    s "May I ask, is the company here to deal with this matter, or to deal with me?"
    s "If it’s not the former, there’s no need to continue."
    s "There is no reason to stay in a place like this."
    s "I resign."

    scene black
    with fade

    # 桌面收拾干净，桌上只有背包和亮着的手机
    # scene cg_clean_desk_phone with fade

    "{i}Your Xiaozishu post stops at 423 comments. The heat has long faded.{/i}"
    "{i}The latest comment, posted two days ago, says: “Another clout chaser.”{/i}"

    "{i}Comment: Is there any evidence? I’ve been reading for ages.{/i}"
    "{i}Comment: Hugs to the poster. Sexual harassment is really hard to collect evidence for. Sigh.{/i}"
    "{i}Comment: I don’t know the full story, so I won’t comment.{/i}"
    "{i}Comment: No pictures, no truth. Just account farming.{/i}"

    "{i}You turn off your phone.{/i}"

    $ unlock_cg("tuichang")

    # CG：退场
    # scene cg_exit with fade
    $ unlock_cg("tuichang")

    jump ending_common


label ending_d_mutual_respect:
    # D-1【相惜】

    scene tea_room
    with fade

    s "Ms. Lam, sorry to bother you again... I found a lawyer—"
    s "But the lawyer said that because I didn’t get in the car at the time, I neither experienced actual assault nor left direct evidence."
    s "And the photos and materials I collected involve other people. I’m not the person directly involved..."
    s "So there’s almost no chance of winning."

    s "But when I saw those photos and files, I realized so many brilliant women should have stood somewhere higher."
    s "Because of Chan Wing Yan, they faded instead."

    s "I... I wanted to ask whether you would be willing to be the one to stand up and sue Chan Wing Yan."

    linjie "Miss Sheh, did something I once said give you the wrong signal?"

    linjie "You want to be a savior. You have ambition. But have you thought about this?"
    linjie "You are standing in front of someone who actually went through it, asking her to reopen that memory for something you did not truly experience yourself."

    linjie "You didn’t really go through it, so you don’t understand..."

    linjie "...Forget it."
    linjie "I still have work to do. Excuse me."

    s "I’m sorry... I crossed a line."

    linjie "..."

    linjie "I don’t regret what I said after drinking that night."
    linjie "But I also hope you can understand this."
    linjie "Before a wound heals, no matter how thick the scab becomes, tearing it off will still draw blood."

    s "...I’ll remember that."

    "{i}Ms. Lam turns to leave.{/i}"

    s "Ms. Lam, I’m sorry. And thank you..."
    s "Also, I hope work goes well for you!"

    s "That’s not empty small talk! Uh, I know that in a company, after certain things happen, work can become difficult—uh, no, that’s not what I mean..."
    s "I just mean... I hope things go smoothly for you. I hope everything gets better."

    scene elevator
    with fade

    "{i}The elevator doors close.{/i}"

    linjie "I heard you."
    linjie "You too. I hope things go smoothly for you too."

    $ unlock_cg("xiangxi")

    # CG：相惜
    # scene cg_mutual_respect with fade
    $ unlock_cg("xiangxi")

    jump ending_common


label ending_b_whisper:
    # B-2【絮语】

    scene bg hr_office
    with fade

    s "I want to report Chan Wing Yan for sexual harassment. All the evidence is here."

    'HR' "Leave the materials here. You may go."

    "{i}She keeps her head down, still working on her own tasks.{/i}"

    s "Aren’t you going to look at the evidence?"

    'HR' "...New here?"

    "{i}She glances at you, then picks up the materials and slowly browses through them.{/i}"

    'HR' "...Given the current situation, I suggest you don’t waste your effort."

    s "Isn’t this enough evidence? Even if it isn’t, he has hurt enough people."

    "{i}She does not answer.{/i}"

    'HR' "..."
    'HR' "Fine. I can submit this for you. Go back and wait for notice."

    scene black
    with fade

    scene office_area
    with fade

    "{i}File: Transfer Notice. Chan Wing Yan’s signature is on it.{/i}"

    "{i}You are about to leave your current desk.{/i}"

    chen "Ah, perfect timing. Bella, you can sit here."

    "{i}Bella looks at you with surprise. While Chan Wing Yan isn’t paying attention, she quietly greets you with her eyes.{/i}"

    chen "So many capable newcomers these days. You have to cultivate them properly."

    "{i}Chan Wing Yan leaves after saying that. You follow behind him.{/i}"

    scene black
    with fade

    "{i}Corridor.{/i}"

    chen "It took me more than ten years to get from a newcomer to this position."
    chen "How to get promoted, how to swallow grievances—I know all of it too well."
    chen "In recent years, I’ve seen more and more talented newcomers. I like them very much."
    chen "Sometimes a few leave, and I do feel it’s a pity."
    chen "But thankfully, there are always more newcomers."

    "{i}He stops talking and enters his office. Your elevator arrives too.{/i}"

    "{i}Your phone vibrates.{/i}"

    chen "A few days in, and you think you can bring me down with a few photos. Too young."

    "{i}You are about to take a screenshot.{/i}"

    "{i}Chan Wing Yan recalled a message.{/i}"

    chen "Siu Man, wish you a bright future."

    scene black
    with fade

    'HR' "I wouldn’t call that smart."
    'HR' "But I would call it brave."

    $ unlock_cg("xuyu")

    # CG：絮语
    # scene cg_whisper with fade
    $ unlock_cg("xuyu")

    jump ending_common


label ending_common:
    scene black
    with fade

    "{i}SHE{/i}"
    "{i}THE END{/i}"
    $ renpy.full_restart()
    return

# ==========================================
# SHE 完整结局系统 V2
# 全部新增 label，避免和旧 label 重名
# ==========================================

default she_last_route = ""
default she_public_result = ""
default she_public_selected_evidence = []


init python:

    def she_evidence_count():
        count = 0

        if cyro_office_found_files:
            count += 1

        if cyro_office_found_perfume:
            count += 1

        if cyro_office_found_photo:
            count += 1

        if cyro_office_found_notebook:
            count += 1

        return count


    def she_has_full_evidence():
        return she_evidence_count() >= 4


    def she_friend_full():
        return linjie_interest >= 2 or xiaojin_interest >= 1


    def she_only_unrelated_evidence(selected_ids):
        if len(selected_ids) == 0:
            return False

        related_ids = ["car", "files", "perfume", "photo", "notebook"]

        for evidence_id in selected_ids:
            if evidence_id in related_ids:
                return False

        return True


# ==========================================
# 最终路线选择界面
# 证据 < 4：法律 / 内部举报 / 小紫书 / 找林姐
# 证据 = 4：法律 / 内部举报 / 小紫书
# ==========================================

screen she_final_route_screen():

    modal True

    add Solid("#000000CC")

    $ e_count = she_evidence_count()

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        background "#ffffff"
        padding (50, 42)

        vbox:
            spacing 22

            text "Back home, you look at the materials you've organized.":
                size 24
                color "#333333"
                xalign 0.5

            text "current evidence: [e_count]/4":
                size 18
                color "#7b3fb2"
                xalign 0.5

            null height 10

            textbutton "law":
                xsize 620
                ysize 54
                background "#eee6f5"
                hover_background "#7b3fb2"
                text_size 20
                text_color "#6b3a91"
                text_hover_color "#ffffff"
                action Return("legal")

            textbutton "Internal reporting":
                xsize 620
                ysize 54
                background "#eee6f5"
                hover_background "#7b3fb2"
                text_size 20
                text_color "#6b3a91"
                text_hover_color "#ffffff"
                action Return("hr")

            textbutton "Purple Note":
                xsize 620
                ysize 54
                background "#eee6f5"
                hover_background "#7b3fb2"
                text_size 20
                text_color "#6b3a91"
                text_hover_color "#ffffff"
                action Return("public")

            if e_count < 4:

                textbutton "Looking for Lam":
                    xsize 620
                    ysize 54
                    background "#eee6f5"
                    hover_background "#7b3fb2"
                    text_size 20
                    text_color "#6b3a91"
                    text_hover_color "#ffffff"
                    action Return("linjie")


# ==========================================
# 路线分发
# ==========================================

label she_route_legal:

    $ she_last_route = "legal"

    if she_has_full_evidence():
        jump she_ending_a3_poxiao

    elif she_evidence_count() > 0:
        jump she_ending_a1_kongwen_easter

    else:
        jump she_ending_a1_kongwen


label she_route_hr:

    $ she_last_route = "hr"

    if she_has_full_evidence():
        jump she_ending_b3_feiniao

    elif she_evidence_count() > 0:
        jump she_ending_b2_xuyu

    else:
        jump she_ending_b1_yinshui


label she_route_public:

    $ she_last_route = "public"

    if she_has_full_evidence():
        $ disclosure_level = "high"
        jump she_ending_c3_qingyun

    call screen xiaozishu_post

    $ post_result = _return
    $ she_public_selected_evidence = post_result["evidence"]

    if disclosure_level == "high":
        jump she_bad_end_public

    elif she_only_unrelated_evidence(she_public_selected_evidence):
        jump she_ending_manyou

    elif she_evidence_count() == 0 and car_event:
        jump she_ending_c2_qingping_no_evidence

    elif she_evidence_count() == 0 and not car_event:
        jump she_ending_c1_tuichang

    else:
        jump she_ending_c2_qingping_with_evidence


label she_route_linjie:

    $ she_last_route = "linjie"

    if she_evidence_count() == 0 and not car_event:
        jump she_ending_d1_xiangxi

    elif she_evidence_count() == 0 and car_event:
        jump she_ending_d2_lijian # 0证，上车

    elif she_evidence_count() > 0 and she_evidence_count() < 4 and not car_event:
        jump she_ending_d2_lijian # 不上车，后续注意台词无车上性骚扰

    else: 
        jump she_ending_d2_lijian # 上车


# ==========================================
# 完全公开中转
# ==========================================

label she_bad_end_public:

    scene home_laptop with fade

    "真实姓名、公司信息、聊天截图、所有细节一起被发了出去。"

    "帖子发出。"

    "24小时。"
    "9万浏览量。"
    "7000多条评论。"
    "2家媒体联系。"

    "{i}反噬。{/i}"

    "她就是想要钱。"
    "为什么不早说？"
    "他是个好人，她在毁他。"

    # 后面补充：公司发现了帖子
    "但……"

    show totally_expose with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    "【私信】姐妹，我也经历过。谢谢你敢说。"
    "【私信】我在这家公司3年了，一直不敢说。"
    "【私信】你不是一个人。"

    "你不再是一个人。"

    if she_friend_full():
        jump she_ending_songbie
    else:
        jump she_ending_gulang


# ==========================================
# A-1【空文】
# 无证据走法律
# ==========================================

label she_ending_a1_kongwen:

    scene police_station with fade # 补插图
    show she_01_normal_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    if not car_event:
        
        show police_01_normal with dissolve:
            zoom 0.92
            xpos 1400
            ypos 180
        '值班民警' "您好，您举报陈永仁性骚扰，有什么证据吗？"

        show she_01_normal_eye_o onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "This is the Moments post he sent me. Also, my coworkers have experienced his harassment too."
        hide she_01_normal_eye onlayer top

        '值班民警' "佘小姐，这个朋友圈并没有达到性骚扰的标准。"
        '值班民警' "另外，我们的法律是“谁主张，谁举证”。但是你不可以代为举证。"

        show she_09_unhappy_bag onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "…………"
        hide she_01_normal_eye_o onlayer top

        '值班民警' "我们理解您的心情，但是我们也需要靠证据办事。"
        '值班民警' "这是受理回执，有进展会通知您。"
        hide she_09_unhappy_bag onlayer top

    else:
        show police_01_normal with dissolve:
            zoom 0.92
            xpos 1400
            ypos 180
        '值班民警' "您说车里发生了性骚扰行为，有录音、录像或者第三人在场吗？"

        show she_02_sweat_eye onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "没有。"
        
        '值班民警' "那目前只能先登记。是否立案，还需要进一步判断。"
        
        show she_09_unhappy_bag onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "………………"
        hide she_01_normal_eye onlayer top
        hide she_09_unhappy_bag onlayer top

    scene reports with fade

    "{i}3周后。{/i}"
    "证据不足，不予立案。"

    show kongwen with fade
    "CG: Blank Document"

    $ unlock_cg("kongwen")

    jump she_ending_common


# ==========================================
# A-1【空文】彩蛋
# 有证据但不够，走法律
# ==========================================

label she_ending_a1_kongwen_easter:

    scene police_station with fade
    show she_01_normal_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show police_01_normal:
        zoom 0.92
        xpos 1400
        ypos 180

    if not car_event:
        
        '值班民警' "这些材料里出现的人不像你啊。"

        show she_01_normal_eye_o onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "这些是他骚扰的其他同事。"

        '值班民警' "佘小姐，我们的法律是“谁主张，谁举证”。"
        '值班民警' "你不可以代为举证。"

        show she_09_unhappy_bag onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "…………"
        hide she_01_normal_eye onlayer top
        hide she_01_normal_eye_o onlayer top

        '值班民警' "这是受理回执，有进展会通知你。"
        hide she_09_unhappy_bag

    else:
        '值班民警' "材料我们收到了。"
        '值班民警' "这些材料里出现的人不像你啊。"

        show she_01_normal_eye_o onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "这些是他骚扰的其他同事。"
        hide she_01_normal_eye_o onlayer top

        '值班民警' "佘小姐，我们的法律是“谁主张，谁举证”。"
        '值班民警' "你不可以代为举证。"

        show she_15_unflinched_card onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "I also suffered his harassment in his car!"
        '值班民警' "但车里的关键事实仍然缺少直接证据。"

        show she_09_unhappy_bag onlayer top:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        s "…………"
        hide she_15_unflinched_card onlayer top
        hide she_01_normal_eye onlayer top
  
        '值班民警' "这是受理回执，有进展会通知你。"
        hide she_09_unhappy_bag onlayer top
        
    scene report with fade
    "3周后。"

    "证据不足，不予立案。"

    show kongwen with fade
    "解锁结局：空文"

    $ unlock_cg("kongwen")

    scene black with dissolve
    $renpy.pause(1.5, hard=True)
    
    # 空文彩蛋
    scene office_desk with fade
    show she_13_sigh2 onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "好受打击，但还是得干活，继续找线索。"
    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我一定要让陈永仁付出代价！"
    hide she_13_sigh2 onlayer top

    "{i}你正要继续工作，却看到陈永仁把Bella单独叫进办公室。{/i}"
    show she_15_unflinched_card onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "？我得去看看。"
    hide she_14_deepthink onlayer top
    hide she_15_unflinched_card onlayer top

    scene corridor with fade
    
    show linjie_01_normal:
        zoom 0.92
        xpos 1450
        ypos 200
    show she_06_surprise_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}你到办公室门口正要进去，发现林姐也在。{/i}"
    "{i}你正要进门，林姐拦住了你。{/i}"
    
    show she_02_sweat_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "不是林姐，Bella 刚刚……"

    linjie "你在这儿等着。"
    hide linjie_01_normal with dissolve

    "{i}林姐进去提起了有关其他深度项目的话题，把实习生 Bella 支走了。{/i}"

    show bella_03_frown with dissolve:
        zoom 0.95
        xpos 1450
        ypos 230
    bella "……？"
    show she_13_sigh3 onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show she_17_sad onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "……小心点啊。"
    hide she_02_sweat_eye_nobag onlayer top
    hide she_13_sigh3 onlayer top

    show bella_04_file_fall with dissolve:
        zoom 0.95
        xpos 1450
        ypos 230
    'Bella' "啊？……哦。"
    hide bella_03_frown
    
    "{i}看 Bella 的表情从迷茫到若有所思，你放心了，回到工位上。{/i}"
    scene office_desk with fade
    hide she_17_sad onlayer top
    
    show linjie_kongwen_1 with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    "【微信】林姐：你很勇敢。"
    "【微信】林姐：那么我也该更进一步了。"

    show linjie_kongwen_2 with dissolve:
        zoom 1.4
        align (0.5, 0.45)

    scene black with fade

    jump she_ending_common


# ==========================================
# B-1【饮水】
# 无证据内部举报
# ==========================================
label she_ending_b1_yinshui:

    scene black with fade

    "{i}文件：调岗通知，上面有陈永仁的签字。{/i}"

    "你向公司举报陈永仁性骚扰。"

    "因为没有证据，公司并未接受你的举报。"

    "举报的消息被陈永仁知道，你被调岗去了别的地方。"

    scene new_office_desk with fade

    show she_01_normal_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "新工位和设计部还在同一层，只是离得很远。"
    s "饮水机成了我唯一的同事，它不会说话，不过也不会对我动手动脚。"

    show she_05_happy_sweat_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "办公区的最边缘，工作内容也是最边缘。"
    hide she_01_normal_eye_nobag onlayer top

    show she_14_thinking onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "好处的话……"
    hide she_05_happy_sweat_nobag onlayer top

    show she_03_tinysmile_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "大概是喝水变得容易了吧。"
    hide she_14_thinking onlayer top

    show she_06_surprise_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}对面另外一个茶水间先后进去了两个人。{/i}"
    hide she_03_tinysmile_eye_nobag onlayer top
    pause 0.5
    hide she_06_surprise_eye_nobag onlayer top
    
    show bella_yinshui with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    s "【联系人-Bella】我看到陈永仁和你一起在茶水间，注意点。"

    show she_drink_water onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    pause 1.5
    show she_03_tinysmile_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    pause 0.2
    hide she_drink_water onlayer top
    s "水温刚好。"
    hide she_03_tinysmile_eye_nobag onlayer top

    scene yinshui with fade

    "如人饮水，冷暖自知。"
    "解锁结局：饮水"
    $ unlock_cg("yinshui")

    jump she_ending_common

# ==========================================
# C-1【退场】
# 无证据、没上车，小紫书
# ==========================================

label she_ending_c1_tuichang:

    scene home_laptop with fade

    "{i}你把自己的经历和猜测发上网，希望大家关注职场性骚扰问题。{/i}"

    "{i}公司好像发现了这个帖子，你被人事约谈了。{/i}"

    scene hr_office with dissolve

    show she_15_idea_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "冒昧问一下，公司是想来处理这件事，还是来处理我？"

    s "如果不是前者的话，不用说了。"

    s "这样的地方没有待下去的必要。"
    
    show she_15_unflinched onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "我辞职。"
    hide she_15_idea_card onlayer top
    hide she_15_unflinched onlayer top

    scene pack_up with fade
    "{i}桌面收拾干净了，桌上只有一个背包和一个屏幕亮着的手机。{/i}"
    "{i}你的小紫书帖子评论总数停在423条，热度早就掉了。{/i}"
    "{i}最新一条评论是：又一个蹭热度的。{/i}"

    scene tuichang with fade

    "解锁结局：退场"

    $ unlock_cg("tuichang")

    jump she_ending_common

# ==========================================
# D-1【相惜】
# 找林姐，但自己不是当事人
# ==========================================

label she_ending_d1_xiangxi:

    scene corridor with fade
    show she_17_sad onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    s "林姐，不好意思又打扰你……我找律师了。"
    s "但是律师说我当时没有上车，既没有实际遭遇侵害，也没有留下证据。"
    s "其他收集的材料照片，我并不是当事人。几乎没有胜算。"

    show she_09_unhappy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "可是我看到那些照片和档案，好多惊才绝艳的前辈本应该站在更高的位置，却因为陈永仁黯淡下去了。"
    hide she_09_unhappy onlayer top
    s "我、我想问问你，愿意成为站出来起诉陈永仁的人吗。"

    show linjie_04_frown with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "佘小姐，是我曾经对你说的话释放了一些错误的信号吗？"
    show she_06_surprise_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    linjie "你想做救世主，有野心。"
    linjie "但是你想过吗，站在亲历者面前诉说你没有经历过这件事，需要亲历者重新再现那段记忆。"

    show linjie_08_tolerate:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "你没有真正经历过，你根本……"
    linjie "…………"

    show linjie_06_bar_closeeyes with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "……算了。"
    hide linjie_08_tolerate

    hide linjie_06_bar_closeeyes
    linjie "我还有工作事宜，失陪。"
    show linjie_09_back with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200

    hide she_06_surprise_eye_nobag onlayer top
    s "对不起……是我冒犯。"

    linjie "我不后悔酒后说的那番话。"
    # hide linjie_09_back with dissolve # 模拟转身
    linjie "但也希望你能理解，一个伤口愈合前，它的痂不管有多么厚，撕下来都是血淋淋的。"

    s "……我记住了。"
    hide linjie_00_shade with dissolve
    "{i}林姐走向电梯。{/i}"

    show she_17_sad_smile onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240    
    s "嗯，林姐，对不起，还有谢谢你。"
    hide she_17_sad onlayer top

    show she_03_tinysmile_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "以及祝你工作顺利！"
    show she_05_sohappy_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "不是没营养的客套，就是希望你顺利，一切都好。"
    hide she_03_tinysmile_eye_nobag onlayer top
    hide she_05_sohappy_nobag onlayer top

    "{i}电梯门关上了。{/i}"
    hide she_05_happy_nobag onlayer top

    scene elevator with fade
    show linjie_06_bar_closeeyes:
        zoom 0.92
        xpos 1450
        ypos 200
    linjie "我听到了。你也顺利。"
    
    scene xiangxi with fade

    "解锁结局：相惜"

    $ unlock_cg("xiangxi")

    jump she_ending_common


# ==========================================
# B-2【絮语】
# 有证据但不足，内部举报
# ==========================================
label she_ending_b2_xuyu:

    scene hr_office with fade

    show she_15_unflinched_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    # s "我要举报陈永仁性骚扰，所有证据都在这里。"
    s "I'm reporting Chen Yongren for sexual harassment.  All the materials here."

    'HR' "材料放这儿，你可以走了。"

    # "她低头干着手头的工作。"
    "She bowed her head and looked at the work in hand."

    show she_01_normal_eye_o_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    # s "您不看看证据吗？"
    s "Don't you check the evidence?"
    hide she_15_unflinched_card onlayer top

    'HR' "……新来的？"

    # "她匆匆抬头瞥了你一眼，拿起你提交的材料浏览起来。"
    "She glances up at you briefly, then picks up the documents you submitted and skims through them."
    # "她始终没有抬头，你看不清她的面容。"
    "She didn't looked up. You couldn't see her face clearly."

    'HR' "现在的情况，我建议你不要做无用功。"

    show she_15_idea_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    # s "这些证据不够多吗？但是他伤害的人够多了。"
    s "Isn't this evidence enough? But he has hurt enough people."
    hide she_01_normal_eye_o_nobag onlayer top

    'HR' "……"
    'HR' "行，我可以帮你提交，回去等通知吧。"

    hide she_15_idea_card onlayer top

    # 被调岗
    scene office_area with fade

    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    "{i}文件：调岗通知，上面有陈永仁的签字。{/i}"
    s "……………………"
    "你正要离开现在的工位。"

    show she_06_surprise_eye onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_14_deepthink onlayer top

    show chen_02_smile with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1349
        ypos 161
    # chen "哎，刚好，Bella 你坐这里吧。"
    chen "Perfect, Bella, take a seat here."

    # "Bella惊喜地看了你一眼，趁陈永仁不注意，悄悄用眼神和你打了个招呼。"
    "Bella shoots you a surprised glance. While Chen Yongren isn't looking, she quietly greets you with her eyes."

    show she_15_unflinched_card onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_06_surprise_eye onlayer top
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    # chen "有能力的新人真多啊，要好好深耕啊。"
    chen "So many talented new faces these days. You ought to put in solid work."
    
    hide she_15_unflinched_card onlayer top

    # 陈永仁嘚瑟
    scene corridor with fade
    # "你走在他的后面。"
    "You walk behind him."
    show she_15_unflinched_bag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    
    show chen_01_normal with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 162
    # chen "从新人走到这个位置十几年，想要晋升怎么做、遇到委屈怎么忍，我可太清楚了。"
    chen "It took me over a decade to get to this position as a newcomer. I know exactly how to get promoted, and how to endure all the grievances."

    show chen_03_narroweyes with dissolve:
        zoom 0.9
        xzoom -1.0
        xpos 1350
        ypos 160
    # chen "最近几年看有才的新人是越来越多，太喜欢她们了。偶尔走了几个，也会觉得可惜。"
    chen "I've seen more and more gifted newcomers these past few years. I'm quite fond of them. I even feel regretful whenever a few leave."
    hide chen_01_normal

    show chen_05_wanwei:
        zoom 0.9
        xzoom -1.0
        xpos 1356
        ypos 162
    # chen "不过还好，新人还多着呢。"
    chen "But it's fine, there are always plenty of new ones."
    hide chen_03_narroweyes

    scene black with dissolve
    hide she_15_unflinched_bag onlayer top
    # "他没再继续说话，进了办公室，你的电梯也到了。"
    "He falls silent and walks into the office. Your elevator arrives right then."
    
    # 陈永仁挑衅
    scene elevator

    play sound "phone_vibration"

    show chen_xuyu_1 with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    # chen "进来几天，凭几张照片就想扳倒我，太嫩了。"
    chen "Only been here a few days, and you think you can take me down with just a few photos. Still far too naive."

    # "你正想截图。"
    "You reach out to take a screenshot."

    show chen_xuyu_2:
        zoom 1.4
        align (0.5, 0.45)
    # "陈永仁撤回了一条消息。"
    "Chen Yongren revoked a message."
    hide chen_xuyu_1

    show chen_xuyu_3:
        zoom 1.4
        align (0.5, 0.45)
    # chen "小曼，前程似锦啊。"
    chen "Xiaoman, wish you a bright future ahead."
    hide chen_xuyu_2
    hide chen_xuyu_3 with dissolve

    show she_14_think onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    # s "这就是无用功的意思吗？"
    s "Is this what it means to be futile effort?"
    hide she_14_think onlayer top

    scene xuyu with dissolve
    # "是蛊惑，还是示警？"
    "Is this manipulation, or a warning?"
    # "解锁结局：絮语"
    "Ending Unlocked: Whispers"

    $ unlock_cg("xuyu")

    jump she_ending_common


# ==========================================
# C-2【青萍】无证据，上车
# ==========================================

label she_ending_c2_qingping_no_evidence:

    scene home_laptop with fade

    "没有找到有效的证据，你决定把自己的经历放上网，让其他女性警惕起来。"
    show she_01_normal_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "我是刚进公司的新员工……"
    s "在项目完成的一次部门聚餐结束后，男上司提出送我回家。"
    s "在我上车后，他对我实施了骚扰行为。"

    "{i}在你写下这些文字的时候，那些不愿想起的回忆又向你涌来。{/i}"
    hide she_01_normal_eye_nobag onlayer top

    "{i}封闭的空间。{/i}"
    "{i}解不开的安全带。{/i}"
    "{i}拉扯你的思绪和手臂。{/i}"
    "{i}你被束缚得喘不过气。{/i}"
    show she_15_unflinched_card onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "{i}我要写，我就要写！{/i}"
    s "{i}陈永仁不止一个，但一个陈永仁就能祸害一百个。{/i}"
    s "{i}受害人不止我一个，但一个我或许能帮助一百个。{/i}"

    "{i}一个小时过去，你整理好了帖子，发布。{/i}"

    hide she_15_unflinched_card onlayer top

    s "【置顶】希望广大姐妹擦亮眼睛，保护自己。写下这些的时候我很折磨，但也希望有相似经历的姐妹，在能够接受的范围内，不要停止发声。"

    "评论：有没有证据啊，看半天了。"
    "评论：摸摸博主，性骚扰真的很难搜证，唉。"
    "评论：未知全貌，不予置评。"
    "评论：没图没真相，起号的。"

    show she_08_guilt onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    s "{i}唉……难道没有留下证据，就是没有留下伤害吗？{/i}"
    hide she_08_guilt onlayer top

    "【新评论：楼上怎么说话呢，没证据就是没有留下伤害吗？】"
    "【新评论：不是所有人在被侵权的那一刻都有空架好摄像机。】"
    "【新评论：谢谢博主，这是我第一次感觉我的遭遇不是因为我做错了事。】"
    show she_03_tinysmile_eye_nobag onlayer top:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    "小曼微笑。"
    hide she_03_tinysmile_eye_nobag onlayer top

    scene qingping with fade
    "解锁结局：青萍"

    $ unlock_cg("qingping")

    jump she_ending_common


# ==========================================
# C-2【青萍】有证据但不足
# ==========================================

label she_ending_c2_qingping_with_evidence:

    scene home_laptop with fade

    "在给材料进行隐私处理之后，你把自己搜集的证据和搜证经历放上网，让其他女性警惕起来。"

    s "我是刚进公司的新员工……"

    if car_event:

        s "在项目完成的一次部门聚餐结束后，男上司提出送我回家。"

        s "我上了他的车，这之后他在车内对我实施性骚扰。"

    else:

        s "在项目完成的一次部门聚餐结束后，男上司提出送我回家。"

        s "我拒绝了上车，但这之后我发觉不对劲，开始关注他的行为。"

    s "以儒雅面貌示人的人，未必是好人。希望广大姐妹擦亮眼睛，保护自己。"

    "一个小时过去，你整理好了帖子，发布。"

    s "【置顶】希望遭遇这些的姐妹好起来。我在收集的材料中看到你们都曾惊才绝艳，愿你们也能在往后熠熠生辉。"

    "帖子发出后，浏览量逐渐攀升。"

    "200。"
    "3000。"
    "15000。"
    "80000+。"

    play sound "wx_voice_call"
    show linjie_qingping with moveinbottom:
        zoom 1.4
        align (0.5, 0.45)
    "林姐电话打了进来。"

    linjie "看帖呢？"

    s "诶？！林姐你怎么知道？"

    linjie "快别傻乐了，我还知道这是你写的。赶紧把头像换了吧，主页暴露隐私的地方也隐藏下。"

    linjie "下次干这种事记得换小号，或者至少换个 IP。"

    s "哦哦哦，我马上换！谢谢林姐！"

    linjie "这事你办得谈不上聪明。"

    s "……嘿嘿。"

    linjie "但称得上勇敢。"

    s "不过，既然林姐你刷到了，是不是也留言了？"

    linjie "哼，我可不像你就差把名字挂脸上了，慢慢找吧。"
    hide linjie_qingping with dissolve

    "【评论：其实我也遇到了……但当时快要职级评定了，我不敢说。】"
    "【评论：我也是。】"
    "【评论：我也是，只敢和朋友说。博主好勇敢。】"
    "【评论：还有没有证据啊，看半天了没个露脸的。】"
    "【评论：图都不敢放全，P 的吧。】"
    "【新评论：我最近也遇到了一样的事情，我明天就举报那个老色胚！】"
    "【新评论：你举报那我也举报。】"
    "【新评论：我有点顾虑，但我明天准备提醒新来的小实习生注意点。】"

    '小曼' "找不到林姐，不过——"

    '小曼' "发现了新的希望。"

    scene qingping with fade
    "解锁结局：青萍"
    $ unlock_cg("qingping")

    jump she_ending_common


# ==========================================
# D-2【利剑】
# 找林姐之后，继续留下收集证据
# ==========================================

label she_ending_d2_lijian:

    scene tea_room with fade

    if she_evidence_count() == 0 and car_event:
        show she_17_sad onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        show linjie_01_normal with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        '小曼' "林姐，不好意思又打扰你……我找律师了。"
        '小曼' "但是律师说，我没有留下被骚扰的证据，几乎没有胜算。"
        '小曼' "我、我想问问你，愿意成为站出来起诉陈永仁的人吗。"

        show linjie_04_frown with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        '林姐' "佘小姐，你想做救世主，有野心。但是你回忆过那个时刻吗？"
        show she_06_surprise_eye_nobag onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '林姐' "难受吗？是不是恨不得大脑完全不记得这段记忆？"
        hide linjie_01_normal

        show she_09_unhappy onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '小曼' "……对不起，我应该将心比心。"
        hide she_06_surprise_eye_nobag onlayer top

        show linjie_06_bar_notlikeme with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        '林姐' "道歉我收下了。不过走到今天，我没那么脆弱。还有工作事宜，失陪。"
        hide linjie_04_frown
        hide linjie_06_bar_notlikeme with dissolve

        show she_01_normal_eye_o_nobag onlayer top with vpunch:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '小曼' "林姐！"
        '小曼' "我们还能反抗吗？"
        hide she_09_unhappy onlayer top

        show linjie_06_bar_closeeyes with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        linjie "…………"

    elif she_evidence_count() > 0 and she_evidence_count() < 4 and linjie_interest > 2:
        show she_17_sad onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        show linjie_01_normal with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        "林姐，不好意思又打扰你……我找律师了。"
        if car_event:
            '小曼' "但是律师说，我没有留下被骚扰的证据，几乎没有胜算。"
        if not car_event:
            '小曼' "律师说，证据不够，而且在收集的材料里我不是当事人。几乎没有胜算。"
            '小曼' "可是我看到那些照片和档案，好多惊才绝艳的前辈本应该站在更高的位置，却因为陈永仁黯淡下去了。"
        '小曼' "我、我想问问你……"
        '小曼' "我想问问你，你最近过得好吗？"
        '小曼' "以前过得好吗，以后也会过得好吗？"

        show linjie_06_bar:
            zoom 0.92
            xpos 1450
            ypos 200
        pause 1.0
        show linjie_06_bar_closeeyes with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        '林姐' "……"
        hide linjie_06_bar
    else:
        pass

    
    hide linjie_06_bar_closeeyes
    '林姐' "小曼，have a good day。"
    hide linjie_01_normal with dissolve

    '小曼' "我没问，但我觉得我做对了。"
    hide she_17_sad onlayer top
    hide she_01_normal_eye_o_nobag onlayer top

    scene office with fade

    show she_01_normal_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    '小曼' "我留下来继续收集更多证据。"
    hide she_01_normal_eye_nobag onlayer top

    "这件事比想象中困难。"
    "陈永仁看你没上车，对你有所警觉，继续骚扰你，试探你是否有反抗倾向。"
    "你因为要留在公司里，只能极力隐忍。"
    "他看你像是要留在这里工作，好像找到了你的弱点。"
    "几个月里，你要防他骚扰你，还要防他骚扰更多的她。"

    "你的防备让陈永仁没法得手，他把你调去了部门边缘。"

    scene new_office_desk with fade

    show she_13_sigh3 onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    '小曼' "这就是林姐每天面对的吗。"
    show she_17_sad onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    hide she_13_sigh3 onlayer top
    '小曼' "只是过了几个月我就有点撑不住了，她却走过了好几年。"
    hide she_17_sad onlayer top

    scene linjie_reflection with fade
    "屏幕反光里出现林姐的脸。"

    show she_06_surprise_eye_nobag onlayer top at shock:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    '小曼' "！"

    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    '林姐' "你今天把工位搬回去，等会儿会有项目文件发你。"

    show she_06_surprise_eye_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    '小曼' "诶？"
    pause 0.5
    hide she_06_surprise_eye_nobag onlayer top

    scene office_desk with fade

    "你把办公用品放在原来的工位上，发现办公室东西都换了。"

    show she_01_normal_eye_o_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240
    '小曼' "今天陈总……不在？"

    show jin_01_happy with dissolve:
        zoom 0.95
        xpos 1360
        ypos 150
    '小金' "办公室易主啦！现在是林总掌管我们的生杀大权。"
    show jin_01_happy with dissolve:
        zoom 0.95
        xpos 1360
        ypos 150
        linear 0.5 xpos 1000 ypos 150 
    show bella_01_happy with dissolve:
        zoom 0.93
        xpos 1400
        ypos 230
    'Bella' "呜呜终于可以不用穿长袖长裤严防死守了，这几个月闷死我了！"
    show she_05_happy_nobag onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    show jin_01_happy with dissolve:
        zoom 0.95
        xpos 1000
        ypos 150
        linear 0.3 xpos 850 ypos 150
    show bella_01_happy with dissolve:
        zoom 0.93
        xpos 1400
        ypos 230
        linear 0.2 xpos 1150 ypos 230
    hide she_01_normal_eye_o_nobag onlayer top
    show linjie_05_interested with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200
    '林姐' "聚在门口不干活，要造反？"

    '小金' "老大我马上走，马上走！"
    'Bella' "嘿嘿，我也走。"

    hide jin_01_happy with dissolve
    hide bella_01_happy with dissolve
    "小金和 Bella 作鸟兽散。"

    if linjie_interest < 3:
        show she_05_sohappy_nobag onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '小曼' "我是要造反的，不过，好像已经成功了？"
        hide she_05_happy_nobag onlayer top
        show linjie_02_smile with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200

    else:
        '林姐' "你呢？"

        show she_05_happy_sweat_nobag onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '小曼' "哈哈我也走。"

        show linjie_02_smile with dissolve:
            zoom 0.92
            xpos 1450
            ypos 200
        '林姐' "去吧，have a nice day。"

        show she_05_sohappy_nobag onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240
        '小曼' "老大，祝你有 many many nice days！"
        hide she_05_happy_sweat_nobag onlayer top
        hide she_05_happy_nobag onlayer top
        hide she_05_sohappy_nobag onlayer top

    scene linjian with fade

    "解锁结局：利剑"
    $ unlock_cg("linjian")

    jump she_ending_common


# ==========================================
# A-3【破晓】
# 证据完整，法律
# ==========================================

label she_ending_a3_poxiao:

    scene bg bedroom_night
    with fade

    hide she_14_deepthink onlayer top
    hide she_14_think onlayer top
    hide she_09_unhappy onlayer top
    hide she_15_unflinched onlayer top

    "在给材料进行隐私处理之后，你把自己搜集的证据和搜证经历放上网，让其他女性警惕起来。"

    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "我是佘小曼，几个月前刚进公司的新员工。"

    s "在项目完成的一次部门聚餐结束后，男上司陈永仁提出送我回家。"

    if car_event:

        hide she_14_deepthink onlayer top

        show she_09_unhappy onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240

        s "我上了他的车，这之后他在车内对我实施性骚扰。"

        s "这段记忆对我来说很痛苦，但我知道如果我忍气吞声，以后都将活在对自己无能为力的质疑里。"

        s "我决定反抗，之后我找到了他骚扰其他前辈的资料。"

        hide she_09_unhappy onlayer top

    else:

        hide she_14_deepthink onlayer top

        show she_14_think onlayer top at top_dissolve:
            zoom 0.8
            xzoom -1.0
            xpos -30
            ypos 240

        s "我拒绝了上车，但这之后我发觉不对劲，开始关注他的行为。"

        s "之后我找到了他骚扰其他前辈的资料。"

        hide she_14_think onlayer top

    show she_15_unflinched onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "我已经寻求法律手段维权，虽然很难，但我们的处境已经很暗，任何一丝可能都代表一线光亮。"

    hide she_15_unflinched onlayer top

    "把所有证据填写完毕，你直接发布了。"

    "贴文一经发布就获得了极高热度。"

    "【高赞评论：不要温和地走入那个良夜。】"
    "【高赞评论：博主记得说一声开庭时间啊，我要去支持你！】"
    "【最高点赞：博主姓 She 这个巧合真是……she is me，怎么能不支持。】"

    "多家媒体后台私信联系你。"

    scene bg court_outside
    with fade

    hide she_14_deepthink onlayer top
    hide she_14_think onlayer top
    hide she_09_unhappy onlayer top
    hide she_15_unflinched onlayer top

    # 旁白，不显示小曼
    "开庭当天，你出现在法院大门外，门口有很多人。"

    "加油哦。"
    "你真的很勇敢，吾辈楷模。"
    "英雌！"

    show linjie_01_normal with dissolve:
        zoom 0.92
        xpos 1450
        ypos 200

    '林姐' "这么多年拼到这个位置全靠理智决策，但今天我也抛弃理智地希望你赢。"

    hide linjie_01_normal with dissolve

    show woman_01_normal with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160

    '???' "我也是。去吧，给那个良夜一点颜色看看。"

    hide woman_01_normal with dissolve

    scene bg court_outside
    with fade

    hide she_14_deepthink onlayer top
    hide she_14_think onlayer top
    hide she_09_unhappy onlayer top
    hide she_15_unflinched onlayer top

    # 旁白，不显示小曼
    "下发判决结果那天来了，你听完判决走出法院。"

    # 记者提问，小曼入场
    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    '记者1' "佘女士，你现在是什么感觉？感觉值得吗？"

    '记者2' "现在 SheIsMe 词条爆火，你被称作反性骚扰吹哨人，你怎么看？"

    hide she_14_deepthink onlayer top

    show she_09_unhappy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "从判决结果看，我输了。"

    s "但现在那么多的性骚扰者被曝光，职场性别议题被带到大众面前。"

    s "大家现在也不仅仅凭借结果定义这件事为失败，这大概就是意义。"

    s "至于吹哨人，不敢当啦。好多位前辈在我之前就默默奋斗着呢。"

    s "可能抗争的办法不同，但是我们奋斗的目标是一样的。"

    hide she_09_unhappy onlayer top

    show she_15_unflinched onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    s "我想这就是“women”，不仅是女性，也是“我们”本身。"

    hide she_15_unflinched onlayer top

    scene poxiao with fade
    "解锁结局：破晓"
    $ unlock_cg("poxiao")

    jump she_ending_common


# ==========================================
# B-3【飞鸟】
# 证据完整，内部举报
# ==========================================

label she_ending_b3_feiniao:

    scene bg hr_office
    with fade

    hide she_14_deepthink onlayer top
    hide she_14_think onlayer top
    hide she_09_unhappy onlayer top
    hide she_15_unflinched onlayer top
    hide she_17_sad onlayer top
    hide she_17_sad_smile onlayer top

    show she_15_unflinched onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    '小曼' "我要举报陈永仁性骚扰，所有证据都在这里。"

    hide she_15_unflinched onlayer top

    show woman_01_normal with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160

    "HR 在看小曼给的证据。之后她抬起头，小曼发现这是之前在电梯遇到的陌生女人。"

    hide woman_01_normal with dissolve

    show woman_02_talk with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160

    '???' "这些东西你没发在别的地方吧。"

    show she_14_deepthink onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    '小曼' "……"

    hide she_14_deepthink onlayer top

    'HR' "公司看重声誉，要是泄露出去了，我们也很难办。你要是还想在这干，就小心点。"

    'HR' "把事情闹太大，关注度就上去了。公众盯着这里的一言一行，公司都不好作反应。"

    'HR' "明白我的意思吗？"

    hide woman_02_talk with dissolve

    show woman_01_normal with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160

    "小曼发觉了她威胁一样的提醒。"

    hide woman_01_normal with dissolve

    show woman_02_talk with dissolve:
        zoom 0.8
        xpos 1350
        ypos 160

    'HR' "文件有点多，你的材料可能明后天交上去。你可以走了。"

    hide woman_02_talk with dissolve

    show she_09_unhappy onlayer top at top_dissolve:
        zoom 0.8
        xzoom -1.0
        xpos -30
        ypos 240

    "小曼遂按照指示发帖闹大。"

    hide she_09_unhappy onlayer top

    scene bg bedroom_night
    with fade

    "在给材料里除了陈永仁的人像进行隐私处理之后，你把自己搜集的证据和搜证经历放上网。"

    '小曼' "我是佘小曼，几个月前刚进某游戏公司的新员工。"

    '小曼' "在项目完成的一次部门聚餐结束后，男上司提出送我回家。"

    if car_event:

        '小曼' "我上了他的车，这之后他在车内对我实施性骚扰。"

        '小曼' "这段记忆对我来说很痛苦，但我知道如果我忍气吞声，以后都将活在对自己无能为力的质疑下。"

        '小曼' "我决定反抗，之后我找到了他骚扰其他前辈的资料。"

    else:

        '小曼' "我拒绝了上车，但这之后我发觉不对劲，开始关注他的行为。"

        '小曼' "之后我找到了他骚扰其他前辈的资料。"

    '小曼' "我决定把这件事曝光出来，虽然很难说最后是这件事被处理还是我被处理。"

    '小曼' "但我们的处境已经很暗，任何一丝可能都代表一线光亮。"

    '小曼' "我想要试试看。"

    "把所有证据填写完毕，你直接发布了。"

    "贴文一经发布就获得了极高热度。"

    "【高赞评论：大家多多关注这件事情啊，只有够多的眼睛盯着，公司才不敢轻举妄动。】"
    "【高赞评论：这个男的叫陈永仁，公司是某游戏公司。】"
    "【最高点赞：博主姓 She 这个巧合真是……she is me，怎么能不支持。】"

    "多家媒体后台私信联系你。"

    "网上情况持续发酵，大家建立 #SheIsMe 词条说出职场性骚扰或性别歧视问题。"

    "公司信息和陈永仁的劣迹被扒出。"

    "【评论：小曼，我也是曾经被他性骚扰的一员。如果你需要帮助，请联系我，我愿意和你站在一起。】"
    "【评论：我是那个笔记本里被语焉不详提到的李。希望我的亲身经历能给各位在职的姐妹提个醒。】"
    "【评论：我是新来的实习生，也遇到了陈永仁。但我很幸运，部门里有两位前辈都在保护我。】"

    scene bg company_street_evening
    with fade

    "陈永仁上班时被媒体记者抓到采访，引起一些骚乱。"

    '记者1' "您好，您是陈永仁先生吗？昨天网络上有关于您性骚扰女员工的事件，您是否承认？"

    '记者2' "据社媒上目前现身的受害者发言，您多次性骚扰员工。公司内部是否有包庇行为？"

    '陈永仁' "你们是？"

    "上班时间快到了，人群逐渐聚集驻足围观。"

    "公司内部今天谈论的话题都是陈永仁被记者围堵。"

    '职员1' "最近不是在升职考核吗？这下他过不了了吧。"

    '职员2' "这要还能顺利晋升，公司得被喷死。"

    '职员3' "公司还是先关注舆情吧。"

    "公司的举动被网民盯着，对陈永仁做了延迟升职的处理。"

    "同时为了降低大众关注度，让他近期居家办公。"

    scene chen_office
    with fade

    '小曼' "{i}那天面试的时候，站在这里感觉自己被重重地压着。现在……{/i}"

    "现在这间办公室不再是陈永仁的了。"

    "香水、档案和其他旧迹都被清除。"

    "这间房间迎来了新生。"

    "还有新的主人。"

    '???' "办公室就你一个？你们林总呢？"

    '小曼' "林总出去了，文件由我来转交就好。"

    '小曼' "诶？您……"

    '???' "怎么，不是前几天还见过，不认识了？"

    '小曼' "是太认识了，您的耳饰很少见，但我总感觉在公司之外看到过……"

    '小曼' "！"

    '???' "想起来了？我还给你投了60块的推流呢。没想到帖子本身就很有关注度了。"

    '???' "很高兴认识你，小曼。"

    "她向你伸出手。"

    '小曼' "我也是。"








    "解锁结局：飞鸟"
    $ unlock_cg("feiniao")

    jump she_ending_b3_feiniao

# ==========================================
# C-3【青云】
# 证据完整，小紫书自动全部公开
# 与飞鸟合并
# ==========================================

# label she_ending_c3_qingyun:

    

#     # "CG：青云 / 飞鸟"
#     # $ unlock_cg("feiniao")

#     jump she_ending_common


# ==========================================
# 非主线【送别】
# 完全曝光且林姐、小金兴趣值满足
# ==========================================

label she_ending_songbie:

    scene bg company_street_evening
    with fade

    "暴露后，不知何时传出了你做的拆解方案抄袭的消息，你被公司解雇了。"

    "解雇那天，你在楼下，发现陈永仁在落地窗看你。"

    "他没看见公司大门口的遮雨檐挡住了你身边的人。"

    if linjie_interest >= 2 and xiaojin_interest < 1:

        '林姐' "我尽量跟人事那边说，不让你履历上落黑点。之后要推荐信就联系我。"

        '小曼' "好……林姐，谢谢你。"

    elif xiaojin_interest >= 1 and linjie_interest < 2:

        '小金' "小曼……我都知道了，我会努力给留下的女同事们帮忙的。"

        '小金' "陈永仁真不是人！"

        '小曼' "不是人！"

    else:

        '林姐' "我尽量跟人事那边说，不让你履历上落黑点。之后要推荐信就联系我。"

        '小金' "小曼……我都知道了，我会努力给留下的女同事们帮忙的。"

        '小曼' "好……谢谢你们。"

        '小金' "陈永仁真不是人。"

        '林姐' "嗯。"

        '小金' "事已至此，唱首歌送送你——长亭外，古道边……"

        '小曼' "芳草天……"

        '林姐' "不是芳草碧连天吗，怎么……"

        '林姐' "哦。"

    "CG：送别"
    $ unlock_cg("songbie")

    jump she_ending_common


# ==========================================
# 非主线【鸵鸟】
# 可在你想放弃/沉默时 jump 这里
# ==========================================

label she_ending_tuoniao:

    scene bg bedroom_night
    with fade

    "你把手机扣在床头。"

    "通知还在震动。"

    "世界像一只手，把你往被子里按。"

    '小曼' "睡一觉吧。"

    '小曼' "一切，都会好的。"

    "CG：鸵鸟"
    $ unlock_cg("tuoniao")

    jump she_ending_common


# ==========================================
# 非主线【孤狼】
# 完全曝光但没有同伴、搜查暴露没有同伴
# ==========================================

label she_ending_gulang:

    scene office_hall with fade

    "暴露后，不知何时传出了你做的拆解方案抄袭的消息，你被公司解雇了。"

    "你一个人抱着纸箱站在公司门口。"

    "陈永仁站在落地窗后，看着你。"

    "没有人从楼里走出来。"

    "没有人叫住你。"

    scene gulang with fade
    "没有同伴的日子里，一只狼要小心啊。"

    "解锁结局：孤狼"
    $ unlock_cg("gulang")

    jump she_ending_common


# ==========================================
# 非主线【漫游】
# 选了和性骚扰无关的证据
# ==========================================

label she_ending_manyou:

    scene bg bedroom_night
    with fade

    "你把知道的信息全部填了上去，一键发布。"

    "【评论：这到底在说什么。】"
    "【评论：没看懂。】"
    "【评论：是被骚扰还是工资太少？】"
    "【评论：疑似工资太少编炸裂事件博眼球，散了散了。】"

    "你看着屏幕，手指僵在半空。"

    "你说了很多。"

    "但最重要的那件事，反而被淹没了。"

    "CG文案：一案一诉，保持专注。"

    "CG：漫游"

    jump she_ending_common


# ==========================================
# SHE V2 统一收束
# ==========================================

label she_ending_common:

    scene black
    with fade

    "{i}SHE{/i}"
    "{i}THE END{/i}"

    return


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