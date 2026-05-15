# ========== 1. 定义图片 ==========
# 原始CG（结局大图）
image endingGuLang = "images/endingGuLang.png"
image endingChuNiao = "images/endingChuNiao.png"
image endingSongBie = "images/endingSongbie.png"
image endingKongWen = "images/endingKongWen.png"
image endingYinShui = "images/endingYinShui.png"
image endingTuiChang = "images/endingTuiChang.png"
image endingXiangXi = "images/endingXiangXi.png"
image endingQingPing = "images/endingQingPing.png"
image endingLiJian = "images/endingLiJian.png"
image endingXuYu = "images/endingXuYu.png"
image endingPoXiao = "images/endingPoXiao.png"
image endingFeiNiao = "images/endingFeiNiao.png"
image endingLangChao = "images/endingLangChao.png"
# 命名格式为 image ending+“结局拼音” = ...

# 缩略图
image thumb_endingGuLang = "images/thumb_endingGuLang.png"
image thumb_endingChuNiao = "images/thumb_endingChuNiao.png"
image thumb_endingSongBie = "images/thumb_endingSongBie.png"
image thumb_endingKongWen = "images/thumb_endingKongWen.png"
image thumb_endingYinShui = "images/thumb_endingYinShui.png"
image thumb_endingTuiChang = "images/thumb_endingTuiChang.png"
image thumb_endingXiangXi = "images/thumb_endingXiangXi.png"
image thumb_endingQingPing = "images/thumb_endingQingPing.png"
image thumb_endingLiJian = "images/thumb_endingLiJian.png"
image thumb_endingXuYu = "images/thumb_endingXuYu.png"
image thumb_endingPoXiao = "images/thumb_endingPoXiao.png"
image thumb_endingFeiNiao = "images/thumb_endingFeiNiao.png"
image thumb_endingLangChao = "images/thumb_endingLangChao.png"

# 未解锁占位图
image lock = "images/lock.png"

# ========== 2. 持久化记录变量 ==========
# 这个列表会永久保存已解锁的结局ID，不会随读档消失。应该不用改这个。
default persistent.unlocked_endings = []

# ========== 3. 解锁函数 ==========
init python:
    def unlock_ending(ending_id):
        if ending_id not in persistent.unlocked_endings:
            persistent.unlocked_endings.append(ending_id)
            # 可选：立即保存，防止强退丢失。也不用管这个。
            renpy.save_persistent()

# ========== 4.  条件检查  ==========
#用来解锁cg
#init python:
#    def check_endingGuLang():
#    if 数值1 and 数值2 and 数值3：
#    unlock_ending("endingGuLang")

# ========== 5. 画廊主界面 ==========
screen gallery():
    tag menu
    add "gui/overlay/main_menu.png"   # 画廊背景图，可以换

#以下是画廊滚轴功能

    # 使用 vpgrid（垂直可滚动网格）来放置所有按钮
    vpgrid:
        # 布局参数：每行显示 3 个按钮（可以改成 4 或 2）
        cols 3
        # 每个格子之间的间距（水平、垂直）
        spacing 20
        # 整个网格区域的左上角位置和大小（占满大部分屏幕）
        xalign 0.5
        yalign 0.5
        xsize 800   # 网格区域的宽度（根据实际分辨率调整）
        ysize 600   # 网格区域的高度（超出这个高度就会出滚动条）
        # 让网格内容居中显示
        draggable True      # 允许鼠标拖拽滚动
        mousewheel True     # 允许鼠标滚轮滚动

        # ----- 下面就是咱所有的 CG 按钮，按顺序一个一个写 -----
        # 结局1
        if "endingGuLang" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingGuLang"
                action Show("display_cg", cg_image="endingGuLang")
        else:
            imagebutton:
                idle "lock"
                action NullAction()

        # 结局2
        if "endingChuNiao" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingChuNiao"
                action Show("display_cg", cg_image="endingChuNiao")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            

        # 结局3
        if "endingSongBie" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingSongBie"
                action Show("display_cg", cg_image="endingSongBie")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局4
        if "endingKongWen" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_engdingKongWen"
                action Show("display_cg", cg_image="endingKongWen")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局5
        if "endingYinShui" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingYinShui"
                action Show("display_cg", cg_image="endingYinShui")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局6
        if "endingTuiChang" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingTuiChang"
                action Show("display_cg", cg_image="endingTuiChang")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局7
        if "endingXiangXi" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingXiangXi"
                action Show("display_cg", cg_image="endingXiangXi")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局8
        if "endingQingPing" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingQingPing"
                action Show("display_cg", cg_image="endingQingPing")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局9
        if "endingLiJian" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingLiJian"
                action Show("display_cg", cg_image="endingLiJian")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局10
        if "endingXuYu" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingXuYu"
                action Show("display_cg", cg_image="endingXuYu")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局11
        if "endingPoXiao" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingPoXiao"
                action Show("display_cg", cg_image="endingPoXiao")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
        # 结局12
        if "endingFeiNiao" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingFeiNiao"
                action Show("display_cg", cg_image="endingFeiNiao")
        else:
            imagebutton:
                idle "lock"
                action NullAction()
            
         # 结局13
        if "endingLangChao" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_endingLangChao"
                action Show("display_cg", cg_image="endingLangChao")
        else:
            imagebutton:
                idle "lock"
                action NullAction()

        # 结局3、结局4……继续往下加，有多少加多少
        # 例如：
        # if "ending3" in persistent.unlocked_endings:
        #     imagebutton:
        #         idle "thumb_ending3"
        #         action Show("display_cg", cg_image="ending3")
        # else:
        #     imagebutton:
        #         idle "lock"
        #         action NullAction()

        # 注意：vpgrid 会自动换行，不需要手动算行数

    # 返回按钮（放在滚动区域外面，固定在底部）
    textbutton "返回":
        action Return()
        xalign 0.5
        yalign 0.95

# ========== 5. 全屏显示CG的界面 ==========
screen display_cg(cg_image):
    modal True
    add cg_image
    imagebutton:
        idle "gui/return.png"   # 后面可以换成自定义的返回图标
        action Hide("display_cg")
        xalign 0.95
        yalign 0.95