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
                        Hide("item_description"),
                        Return()
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
                        Hide("item_description"), 
                        Return()
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
                        Hide("item_description"),
                        Return()
                    ],
                    false=NullAction()
                )
            ]
        else:
            idle "item3_smartphone.png"
            hover "item3_smartphone_hover.png"
            action Show("item_description", description=item_descriptions["smartphone"], name=item_names["smartphone"])



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
    #default bear_clicked = False
    #default item4_seen = False
    #default item5_seen = False
    #$ clicked_count = 0

    # 使用列表记录点击的不同物品
    $ clicked_items = []  # 存储被点击过的物品

    show screen items_screen
    
    # 等待跳转
    $ renpy.pause(delay=None, hard=False, predict=False, modal=False)
    s"面试好像要开始了？"
    return

label explore_complete:
    hide screen items_screen
    hide screen item_description
    scene 31 # scene可以把textbox遮掉
    with fade
    pause 1.0
    'HR'"佘小姐？陈总请您进去。"
    jump chapter0_2

#----------------------------------------

#screen items_screen_0.2():
    # # 物品1 - 书架
    # imagebutton:
    #     xpos 1200
    #     ypos 200
    #     idle "item0.21_book.png"
    #     #hover "item0.21_book_hover.png"
    #     if not item0.21_book_clicked:  #not clicked时才可点击
    #         Show("item_description", description="法律书籍、商业策略，还有……女性诗人的诗集"), 



#数值初始值
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
default elevator_floor = 0
default gate_used = False
default appearance_checked = False

# 场景定义（占位符图片）
image bg lobby = "bg_lobby.png"  # 公司大堂
image bg elevator = "bg_elevator.png"  # 电梯内部
image bg hr_floor = "bg_hr_floor.png"  # 3楼HR
image bg marketing_floor = "bg_marketing_floor.png"  # 8楼市场部
image bg your_floor = "bg_your_floor.png"  # 12楼你的部门（设计部）
image bg executive_floor = "bg_executive_floor.png"  # 23楼高管层
image bg coffee_stand = "bg_coffee_stand.png"  # 咖啡亭

# 角色立绘（占位符）
image woman normal = "woman_normal.png"

# ========== 第一章入口 ==========

label chapter1:
    scene bg lobby with fade
    
    # 开场
    "大楼里弥漫着空气清新剂和野心。你早到了13分钟。每个人都这样。"
    
    jump lobby_explore

# ========== 大堂探索 ==========

label lobby_explore:
    scene bg lobby
    
    # 检查是否三个内容都已探索
    if gate_used and coffee_bought and appearance_checked:
        "该去上班了。"
        jump elevator_choice
    
    menu:
        "大堂可探索："
        
        "闸机 - 刷工牌" if not gate_used:
            jump gate_interaction
            
        "咖啡亭 - 买咖啡" if not coffee_bought:
            jump coffee_stand
            
        "电梯门倒影 - 整理仪容" if not appearance_checked:
            jump mirror_check

# ========== 闸机互动 ==========

label gate_interaction:
    scene bg lobby
    
    "哔！"
    
    "欢迎，小曼——第一次在这里听到自己的名字"
    
    $ gate_used = True
    
    jump lobby_explore

# ========== 咖啡亭 ==========

label coffee_stand:
    scene bg coffee_stand
    
    "咖啡师很帅，他也发现了你这位新来的美女"
    
    $ money -= 30
    
    "-30元。当前余额：[money]元"
    
    $ coffee_bought = True
    
    jump lobby_explore

# ========== 整理仪容 ==========

label mirror_check:
    scene bg lobby
    
    "你穿着新买的职业裙，很合身"
    
    $ appearance_checked = True
    
    jump lobby_explore

# ========== 电梯选择 ==========

label elevator_choice:
    scene bg elevator
    
    menu:
        "选择楼层："
        
        "3楼：HR":
            $ elevator_floor = 3
            scene bg hr_floor with dissolve
            "HR部门..."
            jump elevator_encounter
            
        "8楼：市场部":
            $ elevator_floor = 8
            scene bg marketing_floor with dissolve
            "市场部..."
            jump elevator_encounter
            
        "12楼：你的部门":
            $ elevator_floor = 12
            scene bg your_floor with dissolve
            "设计部..."
            jump elevator_encounter
            
        "23楼：高管层":
            $ elevator_floor = 23
            scene bg executive_floor with dissolve
            "高管层..."
            jump elevator_encounter

# ========== 电梯随机遭遇 ==========

label elevator_encounter:
    scene bg elevator with fade
    
    "电梯门打开。一位40多岁的女人，套装干练，眼神疲惫。"
    
    show woman normal at center
    
    unknown_woman "新来的？"
    
    s "第一天。"
    
    unknown_woman "啊。"
    
    "她盯着你看的时间有点长。"
    
    unknown_woman "设计部？"
    
    s "怎么知道？"
    
    unknown_woman "就那种眼神。不知道你会在这待多久呢？"
    
    hide woman normal with moveoutleft
    
    "她在8楼下电梯。你始终不知道她的名字。"
    
    # 剧情继续到下一部分...
    return      