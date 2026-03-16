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

# 延续已有定义的角色
define s = Character("小曼")
define n = Character(None, what_italic=True)

# 第一章新角色定义
define xiaojin = Character("小金", color="#FFD700")
define linjie = Character("林姐", color="#808080")
define chen = Character("陈永仁", color="#4169E1")
define unknown = Character("???", color="#808080")

# 延续已有变量，新增关系度变量
default xiaojin_rel = 0
default linjie_interest = 0

# 任务相关标记
default task_assigned = False

# 场景图片定义（占位符）
image bg office_floor = "bg_office_floor.png"
image bg pantry = "bg_pantry.png"
image bg meeting_room = "bg_meeting_room.png"
image bg desk_area = "bg_desk_area.png"

# 角色立绘（占位符）
image xiaojin normal = "xiaojin_normal.png"
image xiaojin whisper = "xiaojin_whisper.png"
image linjie normal = "linjie_normal.png"
image linjie stop = "linjie_stop.png"

# ========== 第一章：自我介绍 ==========

label chapter1_self_intro:
    scene bg office_floor with fade
    
    "{i}你来到工位，正在收拾东西。{/i}"
    
    show xiaojin normal at right with moveinright
    
    xiaojin "嘿！新来的美女！终于有个不是我爸年纪的人了。喝咖啡吗？我告诉你哪个机器好。"
    
    menu:
        "好啊，谢谢！":
            $ xiaojin_rel += 1
            jump xiaojin_friendly
            
        "等会儿吧，我想先收拾一下。":
            jump xiaojin_neutral
            
        "我自己带了。":
            jump xiaojin_cold

# 选项A：友好路线
label xiaojin_friendly:
    hide xiaojin normal
    scene bg pantry with dissolve
    
    show xiaojin whisper at center
    
    xiaojin "悄悄话——别得罪陈总。他挺随和的，但别惹他。还有HR那女的？也别得罪。"
    
    xiaojin "算了，谁都别得罪。我来8个月了，还在琢磨。"
    
    hide xiaojin whisper with moveoutleft
    
    jump linjie_encounter

# 选项B：礼貌路线
label xiaojin_neutral:
    hide xiaojin normal with moveoutright
    
    xiaojin "行，那你先忙，有事找我。"
    
    jump linjie_encounter

# 选项C：疏远路线
label xiaojin_cold:
    hide xiaojin normal
    
    xiaojin "哦……挺独立的啊。"
    
    hide xiaojin normal with moveoutright
    
    jump linjie_encounter

# ========== 林姐登场 ==========

label linjie_encounter:
    scene bg desk_area with fade
    
    "{i}你继续整理工位。{/i}"
    
    show linjie normal at left with moveinleft
    
    linjie "欢迎。文件在共享链接里。10点开会，别迟到。"
    
    "{i}她从你桌边走过，没停步，头也不回。{/i}"
    
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
    
    "{i}林姐脚步微顿，但没回头，继续走了。{/i}"
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项B：冷淡
label linjie_response_b:
    "{i}你默默点头。{/i}"
    
    "{i}林姐似乎没注意到，径直走远了。{/i}"
    
    hide linjie normal with moveoutleft
    
    jump task_1_3

# 选项C：职业（触发隐藏记录）
label linjie_response_c:
    s "期待开会。"
    
    show linjie stop at left
    
    "{i}她停住。微微转身。{/i}"
    
    linjie "是吗。"
    
    "{i}走了。{/i}"
    
    $ linjie_interest = 1
    
    hide linjie stop with moveoutleft
    
    # 隐藏记录提示（仅开发者可见，玩家看不到）
    # [林姐兴趣度：低但不为零]
    
    jump task_1_3

# ========== 任务1.3：第一个任务 ==========

label task_1_3:
    scene bg meeting_room with fade
    
    "{i}上午10点，C会议室。{/i}"
    "{i}日光灯嗡嗡响。8个人围坐。你比最年轻的至少小10岁。{/i}"
    
    show chen normal at center with dissolve
    
    chen "各位早。快速更新——我们拿下了那个新IP项目。对方是大厂，这可是咱们翻身的机会。"
    
    "{i}他环顾四周，目光落在你身上。{/i}"
    
    chen "新人有机会。小曼，你来负责竞品游戏的拆解分析。"
    
    menu:
        "太好了！":
            $ mental = mental + 2 if 'mental' in globals() else 2
            jump task_response_a
            
        "我尽力。":
            jump task_response_b
            
        "具体要拆解哪些部分？":
            jump task_response_c

# 选项A：积极
label task_response_a:
    s "太好了！"
    
    chen "有干劲是好事。林姐会带你入门。"
    
    jump after_task_assignment

# 选项B：谦虚
label task_response_b:
    s "我尽力。"
    
    chen "嗯，有问题找林姐。她经验很丰富。"
    
    jump after_task_assignment

# 选项C：谨慎（特殊剧情）
label task_response_c:
    s "具体要拆解哪些部分？"
    
    "{i}桌边有人轻笑。不是恶意，但……只有你不知道。{/i}"
    
    chen "好问题。林姐会带你。就是市面上那几款头部二次元游戏，美术风格、养成线、付费点设计……那些有趣的东西。"
    
    chen "别担心，我选你是有理由的。我看过你毕设，那个角色设计很有灵气。"
    
    jump after_task_assignment

# 任务分配后
label after_task_assignment:
    hide chen normal with dissolve
    
    "{i}会议结束，你收拾东西准备离开。{/i}"
    
    show linjie normal at right with moveinright
    
    linjie "他总把不可能的任务扔给新人。那几个竞品项目？每个都是几百人的大团队做了三年。你要一个人拆完？别累死自己。"
    
    menu:
        "谢谢提醒，我会注意的。":
            jump linjie_after_a
            
        "我能搞定。在学校我拆过很多游戏。":
            jump linjie_after_b
            
        "为什么是不可能？不是有分析框架吗？":
            jump linjie_after_c

# 会后选项A：感激
label linjie_after_a:
    s "谢谢提醒，我会注意的。"
    
    linjie "嗯。"
    
    hide linjie normal with moveoutright
    
    $ task_assigned = True
    
    jump chapter1_end

# 会后选项B：自信（林姐认可）
label linjie_after_b:
    s "我能搞定。在学校我拆过很多游戏。"
    
    show linjie normal at right
    
    "{i}林姐看了你一眼。{/i}"
    
    linjie "行，有骨气。需要帮忙找我。"
    
    hide linjie normal with moveoutright
    
    $ task_assigned = True
    $ linjie_interest += 1
    
    jump chapter1_end

# 会后选项C：好奇
label linjie_after_c:
    s "为什么是不可能？不是有分析框架吗？"
    
    linjie "……框架是框架，执行是执行。你以后会明白的。"
    
    hide linjie normal with moveoutright
    
    $ task_assigned = True
    
    jump chapter1_end

# 1.3结束标记
label chapter1_end:
    scene bg desk_area with fade
    
    "{i}你回到工位，看着电脑屏幕上打开的共享文件夹。{/i}"
    "{i}第一个任务，开始了。{/i}"
    
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
    scene bg night_office with fade
    
    "{i}入职第5天，晚上10:47{/i}"
    "{i}晚上的办公室不一样。更安静。自动售货机的嗡嗡声更响。{/i}"
    "{i}你以为只有你一个人……{/i}"
    
    call mini_game_analysis
    
    $ fatigue = 50
    
    if fatigue > 60:
        n "好想睡觉……"
    if fatigue > 40:
        n "这个抽卡概率曲线怎么算都不对……"
    if fatigue > 30:
        n "明天还要早会……"
    
    n "但做不完的话，陈总会不会觉得我不行？"
    
    "{i}键盘声停了。你听到脚步声。抬头。{/i}"
    
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
    chen "你知道吗，我看过你简历。你的履历顶尖。你可以去任何地方。为什么选这儿？"
    
    menu:
        "别处都不要我。":
            jump chen_honest
            
        "最适合我的技能。":
            jump chen_safe
            
        "我想升得快。":
            jump chen_ambition

label chen_honest:
    s "别处都不要我。"
    $ mental = mental + 2 if 'mental' in globals() else 2
    show chen normal at center
    "{i}陈永仁表情柔和下来。{/i}"
    chen "我懂。我就是从这个位置开始的。真的，就是这张桌子。20年前。现在你看。"
    "{i}他模糊地往上指了指。{/i}"
    chen "努力工作。留到最后。这就是赢的方法。"
    "{i}他站起来。{/i}"
    chen "别太晚。回家注意安全。"
    "{i}顿了一下。{/i}"
    chen "其实我也要走了。送你一程？"
    jump car_choice

label chen_safe:
    s "最适合我的技能。"
    chen "嗯，确实。你的拆解能力很强。"
    "{i}他站起来。{/i}"
    chen "别太晚，明天还有早会。其实我也要走了，送你一程？"
    jump car_choice

label chen_ambition:
    s "我想升得快。"
    "{i}陈永仁笑了。{/i}"
    chen "有野心。我喜欢。"
    "{i}他站起来。{/i}"
    chen "别太晚。其实我也要走了，送你一程？"
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
    chen "明天见。好好休息。"
    jump task_1_4_end

label reject_car:
    s "不用，我坐地铁。"
    chen "随你。明天见。"
    hide chen normal with moveoutright
    "{i}走了。{/i}"
    "{i}你看着他离开。胸口有什么东西松开了。不知道为什么。{/i}"
    jump task_1_4_end

label task_1_4_end:
    scene bg night_office with fade
    "{i}任务完成。{/i}"
    "{i}解锁：深夜办公室探索{/i}"
    "{i}项目进度加5{/i}"
    jump task_1_5

label mini_game_analysis:
    "{i}你需要完成三款游戏的竞品拆解。{/i}"
    
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

label task_1_5:
    scene bg home with fade
    "{i}第2周，周日下午。{/i}"
    
    "妈妈发来消息：第一个月的工资。什么时候发？"
    
    menu:
        "两周后。":
            jump salary_truth
            
        "快了。":
            jump salary_vague
            
        "问这干嘛？":
            jump salary_defensive

label salary_truth:
    s "两周后。"
    "妈妈：好。弟弟要换校服。还有学校旅行。500块。你能出吧？你现在可是有大工作的人了。"
    jump family_money_choice

label salary_vague:
    s "快了。"
    "妈妈：到底是多快？弟弟要换校服，还有学校旅行。500块，你能出吧？"
    jump family_money_choice

label salary_defensive:
    s "问这干嘛？"
    "妈妈：怎么，翅膀硬了？弟弟要换校服，还有学校旅行。500块，家里现在紧，你帮衬一下怎么了？"
    $ family_pressure += 1
    jump family_money_choice

label family_money_choice:
    menu:
        "好。":
            jump give_money
            
        "那是我一半房租。":
            jump argue_start
            
        "……":
            jump stay_silent

label give_money:
    s "好。"
    $ money -= 500
    $ family_pressure += 1
    "妈妈：乖。就知道你懂事。弟弟会谢谢你的。"
    "{i}-500元。当前余额：[money]元{/i}"
    jump task_1_5_end

label stay_silent:
    s "……"
    "妈妈：你不说话是什么意思？算了，等你发工资再说吧。"
    "{i}内疚感涌上来。{/i}"
    $ mental = mental - 1 if 'mental' in globals() else -1
    jump task_1_5_end

label argue_start:
    s "那是我一半房租。"
    "妈妈：你以为我们白养你的？这么多年？弟弟是你亲弟弟。家人帮家人。你想让他成为唯一一个穿不起鞋的孩子？"
    call argue_minigame
    jump task_1_5_end

label argue_minigame:
    "{i}争吵开始了……{/i}"
    $ mother_anger = 30
    
    menu:
        "（选择回应）"
        "我也有自己的生活":
            $ mother_anger += 20
        "弟弟的鞋凭什么我负责":
            $ mother_anger += 30
        "我会给，但请别这样说话":
            $ mother_anger += 10
    
    if mother_anger >= 50:
        "{i}妈妈怒气冲冲地挂了电话。{/i}"
        "{i}几天后，她发来消息，像什么都没发生。但你记得。{/i}"
    else:
        "{i}你勉强稳住了局面，保住了钱，但心里空落落的。{/i}"
    
    return

label task_1_5_end:
    "{i}手机随后震动。{/i}"
    "小红书陌生人：姐妹，看到你发家里要钱的事了。同款遭遇。你不是一个人。"
    $ xiaohongshu_contact = True
    "{i}新联系人：小红书姐妹{/i}"
    jump task_1_6

# ========== 任务1.6：不经意的触碰 ==========

label task_1_6:
    scene bg pantry with fade
    "{i}第3周，工作日。{/i}"
    "{i}你伸手拿杯子时，有人从你上方伸过手来。{/i}"
    
    show chen normal at center with dissolve
    
    chen "抱歉，我也拿……哦，你在泡咖啡？我也是。"
    "{i}他站得很近。比必要近。{/i}"
    "{i}他拿糖的时候手臂擦过你。{/i}"
    
    menu:
        "观察他的表情":
            "{i}他在笑。正常的笑。{/i}"
            jump touch_reaction
            
        "观察他的手":
            "{i}他的手放在台面上，离你的手只有几寸。{/i}"
            jump touch_reaction
            
        "注意自己的感受":
            jump touch_reaction

label touch_reaction:
    menu:
        "没什么，就是挤。":
            jump touch_ignore
            
        "他为什么站这么近？":
            jump touch_alert
            
        "稍微挪开一点":
            jump touch_move

label touch_ignore:
    s "没什么，就是挤。"
    "{i}你继续泡咖啡。{/i}"
    chen "你做得很好，顺便说一句。拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label touch_alert:
    s "……"
    "{i}你在心里问自己：他为什么站这么近？{/i}"
    chen "你做得很好，顺便说一句。拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label touch_move:
    "{i}你稍微往旁边挪了一步。{/i}"
    "{i}陈永仁没明显反应。但你一动，他眼神扫了你一下。就那么一下。{/i}"
    chen "你做得很好，顺便说一句。拆解分析很棒。我就知道我没看错你。"
    jump task_1_6_end

label task_1_6_end:
    hide chen normal with moveoutright
    "{i}他走了。你一个人对着茶杯发呆。{/i}"
    
    "林姐发来消息：看到你在茶水间和陈永仁了。小心点。"
    
    menu:
        "小心什么？":
            s "小心什么？"
            "林姐：没什么。自己注意分寸。"
            
        "没什么事。":
            s "没什么事。"
            "林姐：……随你。"
            
        "删除消息":
            "{i}你删掉了这条消息。{/i}"
    
    "{i}第一章结束。{/i}" 