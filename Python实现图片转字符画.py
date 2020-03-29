# -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 构建命令行输入参数处理ArgumentParser实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int, default = 80)
parser.add_argument('--height',type = int, default = 80)

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file

# 输出字符画的宽度
WIDTH = args.width

# 输出字符画的高度
HEIGHT = args.height

# 输出字符画的路径
OUTPUT = args.output

# 定义字符画所使用的的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# RGB值转字符函数
def get_char(r,g,b,alpha=256):

	# 判断alpha值
	if alpha == 0:
		return ' '

	# 获取字符集的长度，这里为70
	length = len(ascii_char)

	# 将RGB值转为灰度值gray，灰度值范围为0-255
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

	# 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上

	unit = (256.0 + 1)/length

    # 返回灰度值对应的字符
	return ascii_char[int(gray/unit)]

# 图片处理
if __name__ == '__main__':
	
	# 打开并调整图片的宽和高
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	# 初始化输出的字符串
	txt = " "

	# 遍历图片中的每一行
	for i in range(HEIGHT):
		# 遍历该行的每一列
		for j in range(WIDTH):
			# 将(j,i)坐标的RGB像素转为字符后添加到txt字符串
			txt += get_char(*im.getpixel((j,i)))
		# 遍历完一行后需要增加换行符
		txt += '\n'

	# 输出到屏幕
	print(txt)

	# 字符画输出到文件
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open("output.txt",'w') as f:
			f.write(txt)
