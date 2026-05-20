# gallery.rpy - CG画廊系统（带分页 + 跨周目持久化解锁）
# 使用方法：
#   1. 放入 game/ 文件夹
#   2. 在剧情中调用 $ unlock_cg("gulang") 解锁
#   3. 用 ShowMenu("gallery") 打开画廊

################################################################################
# 配置区
################################################################################

# CG列表（按显示顺序排列）
define cg_list = [
    {"id": "gulang", "title": "孤狼"},
    {"id": "gulang_b", "title": "孤狼·B"},
    {"id": "tuoniao", "title": "鸵鸟"},
    {"id": "linjian", "title": "林间"},
    {"id": "kongwen", "title": "空文"},
    {"id": "yinshui", "title": "饮水"},
    {"id": "tuichang", "title": "退场"},
    {"id": "xiangxi", "title": "相惜"},
    {"id": "qingping", "title": "青萍"},
    {"id": "xuyu", "title": "絮语"},
    {"id": "poxiao", "title": "破晓"},
    {"id": "feiniao", "title": "飞鸟"},
    {"id": "yinshui_b", "title": "饮水·B"},
    {"id": "yinshui_color", "title": "饮水·彩"},
]

# 每页显示数量（3列 x 2行 = 6张）
define CG_PER_PAGE = 6

# 当前页码（从0开始）—— 这个不用跨周目保存，用普通 default
default gallery_page = 0

################################################################################
# 持久化解锁状态（跨周目保存）
################################################################################

# 在 init -1 python 里初始化 persistent.cg_unlocked（只执行一次）
init -1 python:
    import math
    
    # 如果 persistent 里没有 cg_unlocked，创建一个全 False 的字典
    if not hasattr(persistent, 'cg_unlocked') or persistent.cg_unlocked is None:
        persistent.cg_unlocked = {
            "gulang": False,
            "gulang_b": False,
            "tuoniao": False,
            "linjian": False,
            "kongwen": False,
            "yinshui": False,
            "tuichang": False,
            "xiangxi": False,
            "qingping": False,
            "xuyu": False,
            "poxiao": False,
            "feiniao": False,
            "yinshui_b": False,
            "yinshui_color": False,
        }
    
    # 检查是否有新增的 CG（后续扩展用）
    all_cg_ids = ["gulang", "gulang_b", "tuoniao", "linjian", "kongwen", 
                  "yinshui", "tuichang", "xiangxi", "qingping", "xuyu", 
                  "poxiao", "feiniao", "yinshui_b", "yinshui_color"]
    for cg_id in all_cg_ids:
        if cg_id not in persistent.cg_unlocked:
            persistent.cg_unlocked[cg_id] = False

################################################################################
# 解锁函数（必须在 init python 之后定义，才能访问 persistent）
################################################################################

init python:
    def unlock_cg(cg_id):
        """
        解锁指定CG（跨周目永久保存）
        调用方式：$ unlock_cg("gulang")
        """
        if cg_id in persistent.cg_unlocked:
            persistent.cg_unlocked[cg_id] = True
            # 可选：显示解锁提示
            # renpy.notify("CG 已解锁：" + cg_id)
        else:
            # 如果传入不存在的ID，打印警告（开发时排查用）
            renpy.log("警告：尝试解锁不存在的CG '" + cg_id + "'")
    
    def get_total_pages():
        """计算总页数"""
        return int(math.ceil(len(cg_list) / float(CG_PER_PAGE)))
    
    def get_page_cgs(page):
        """获取指定页的CG数据列表"""
        start = page * CG_PER_PAGE
        end = start + CG_PER_PAGE
        return cg_list[start:end]
    
    def get_cg_title(cg_id):
        """根据ID获取CG标题"""
        for item in cg_list:
            if item["id"] == cg_id:
                return item["title"]
        return "未知CG"
    
    def reset_all_cg():
        """重置所有CG解锁状态（调试用）"""
        for key in persistent.cg_unlocked:
            persistent.cg_unlocked[key] = False
        renpy.notify("所有CG已重置")

################################################################################
# 画廊主界面
################################################################################

# gallery.rpy - CG画廊系统（带分页 + 跨周目持久化解锁 + 修复缩略图溢出）

# ... 前面所有代码不变，直到 screen gallery() ...

screen gallery():
    tag menu
    modal True
    
    add Solid("#1a1a2e")
    
    frame:
        background None
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40  # ← 增大整体间距（原来是30）
            
            # 标题
            text "CG 画廊" size 48 color "#fff" xalign 0.5
            
            # 页码显示
            $ total_pages = get_total_pages()
            text "第 [gallery_page + 1] / [total_pages] 页" size 20 color "#aaa" xalign 0.5
            
            # CG 网格 - 关键修改区域
            grid 3 2:
                xalign 0.5
                spacing 40  # ← 增大格子间距（原来是25）
                
                $ page_cgs = get_page_cgs(gallery_page)
                
                for i in range(CG_PER_PAGE):
                    if i < len(page_cgs):
                        $ cg_item = page_cgs[i]
                        $ cg_id = cg_item["id"]
                        $ cg_title = cg_item["title"]
                        
                        vbox:
                            xalign 0.5
                            spacing 12  # ← 增大标题和图间距（原来是8）
                            
                            # === 关键修改：固定尺寸容器 + 图片自适应填充 ===
                            button:
                                xsize 280  # ← 固定宽度（原来是300）
                                ysize 180  # ← 固定高度（原来是200）
                                padding (0, 0)  # 去掉内边距，让图片顶满
                                
                                if persistent.cg_unlocked.get(cg_id, False):
                                    background Solid("#2a2a3e")
                                    hover_background Solid("#3a3a5e")
                                    action Show("cg_viewer", cg=cg_id)
                                    
                                    # 方案A：图片填满容器，保持比例裁切边缘（推荐）
                                    add cg_id:
                                        xysize (280, 180)  # 强制容器尺寸
                                        fit "cover"        # 填满容器，裁切多余部分（类似CSS background-size: cover）
                                        xalign 0.5
                                        yalign 0.5
                                    
                                    # 方案B（备用）：如果想完整显示图片，用 fit "contain" 代替
                                    # 但会有黑边，所以不推荐
                                    
                                else:
                                    # 未锁定状态
                                    background Solid("#1a1a2e")
                                    text "???" size 36 color "#555" xalign 0.5 yalign 0.5
                            
                            # 标题区域 - 固定高度防止文字跳动
                            frame:
                                background None
                                xsize 280  # 和按钮同宽
                                ysize 30   # 固定高度
                                padding (0, 0)
                                
                                if persistent.cg_unlocked.get(cg_id, False):
                                    text cg_title size 18 color "#ddd" xalign 0.5 yalign 0.5
                                else:
                                    text "未解锁" size 18 color "#555" xalign 0.5 yalign 0.5
                    else:
                        # 空白填充 - 和格子尺寸一致
                        null width 280 height 210  # 180图+30标题
            
            # 翻页控制按钮
            hbox:
                xalign 0.5
                spacing 40
                
                textbutton "上一页":
                    text_size 22
                    action SetVariable("gallery_page", max(0, gallery_page - 1))
                    sensitive gallery_page > 0
                
                textbutton "返回":
                    text_size 22
                    action Return()
                
                textbutton "下一页":
                    text_size 22
                    action SetVariable("gallery_page", min(total_pages - 1, gallery_page + 1))
                    sensitive gallery_page < total_pages - 1

################################################################################
# CG 大图查看界面
################################################################################

screen cg_viewer(cg):
    modal True
    zorder 200
    
    # 黑色背景
    add Solid("#000")
    
    # 查找标题
    $ cg_title = get_cg_title(cg)
    
    # 显示大图
    frame:
        background None
        xfill True
        yfill True
        
        add cg:
            xalign 0.5
            yalign 0.5
            xysize (config.screen_width, config.screen_height)
            fit "contain"
    
    # 标题
    text "[cg_title]" size 32 color "#fff" xalign 0.5 ypos 40 outlines [(2, "#000", 0, 0)]
    
    # 关闭提示
    text "点击任意位置或按 ESC / 空格 / 回车 关闭" size 16 color "#888" xalign 0.5 yalign 0.98
    
    # 多种关闭方式
    key "K_ESCAPE" action Hide("cg_viewer")
    key "K_SPACE" action Hide("cg_viewer")
    key "K_RETURN" action Hide("cg_viewer")
    key "K_KP_ENTER" action Hide("cg_viewer")
    
    # 点击屏幕关闭
    button:
        xfill True
        yfill True
        action Hide("cg_viewer")
        background None