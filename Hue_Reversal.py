# 色相反転させるプログラム
# import 関係
from PIL import Image

# 画像の読み込みとオープン
img = Image.open("./画像パス")　#ここは適宜調整お願いします。
img.show()

# RGB に変換
rgb_img = img.convert('RGB')

# 画像サイズを取得
size = rgb_img.size

# 取得したサイズと同じ空のイメージを新規に作成
img2 = Image.new('RGB', size)

# 反転画像の作成
for x in range(size[0]):
    for y in range(size[1]):
        r, g, b = rgb_img.getpixel((x, y))

        # 反転処理
        r = 255 - r
        g = 255 - g
        b = 255 - b

        img2.putpixel((x, y), (r, g, b, 0))

# 反転画像を開く
img2.show()
