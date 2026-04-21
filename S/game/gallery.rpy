# ========== 1. 定义图片 ==========
# 原始CG（结局大图）
image ending1 = "images/ending1.png"
image ending2 = "images/ending2.png"
# 如果有更多结局，继续写 image ending3 = ...

# 缩略图
image thumb_ending1 = "images/thumb_ending1.png"
image thumb_ending2 = "images/thumb_ending2.png"

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

# ========== 4. 画廊主界面 ==========
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
        xsize 800   # 网格区域的宽度（根据你的分辨率调整）
        ysize 600   # 网格区域的高度（超出这个高度就会出滚动条）
        # 让网格内容居中显示
        draggable True      # 允许鼠标拖拽滚动
        mousewheel True     # 允许鼠标滚轮滚动

        # ----- 下面就是咱所有的 CG 按钮，按顺序一个一个写 -----
        # 结局1
        if "ending1" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_ending1"
                action Show("display_cg", cg_image="ending1")
        else:
            imagebutton:
                idle "lock"
                action NullAction()

        # 结局2
        if "ending2" in persistent.unlocked_endings:
            imagebutton:
                idle "thumb_ending2"
                action Show("display_cg", cg_image="ending2")
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