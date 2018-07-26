#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont
import random

# 打开图片
im = Image.open('test.jpg')

# 生成随机数字
msgNum = str(random.randint(1, 99))

# 编辑图片，添加红色随机数字
w, h = im.size
wDraw = 0.7 * w
hDraw = 0.00001 * w
font = ImageFont.truetype('/System/Library/Fonts/Avenir.ttc', 180)
draw = ImageDraw.Draw(im)
draw.text((wDraw, hDraw), msgNum, font=font, fill=(255, 33, 33))

# 生成图片
im.save('1_msg.png', 'jpeg')
print("完成！")