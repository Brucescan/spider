import ddddocr

# 免费的
'''
使用过程中可能会出现的问题
1、python在3.9以下
2、在运行过程中，底部出现报错dll的问题，安装一下c++环境
3、在运行过程中，顶部出现PIL的问题，安装pillow模块，如果当前模块已安装还出现，版本过高，需要卸载重新安装指定的pillow
'''
# 对ddddocr进行实例化
ocr = ddddocr.DdddOcr()
# 读取文件
with open('yzm.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

print(res)