import sys
from PIL import Image, ImageFilter

def convertImg(imgName):
    try:
        img = Image.open(imgName)
        print("檔案格式: ") # 設定第二層問題
        print("1. -toPNG")
        print("2. -toJPG")
        print("3. -toTIFF")
        print("4. -toPDF")
        print("5. -toBMP")
        print("6. -toEPS")
        print("7. -toGIF")
        op1 = input("您想進行的操作: ") 
        if op1 == "1":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'png' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "2":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'jpg' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "3":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'tiff' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "4":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'pdf' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "5":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'bmp' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "6":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'eps' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
        if op1 == "7":
            dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
            newImgName = imgName[:dotIndex] + 'gif' # 設定新檔名
            convertImg.save(newImgName) # 儲存檔案
    except FileNotFoundError as fnfe:
        print(fnfe)

def resizeImg(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size) # 查看原始檔案大小
        newWidth = int(input("new width: ")) # 輸入寬度
        ratio = float(newWidth) / img.size[0] # ratio新的取比例 #[0]取寬
        newHeight = int(img.size[1] * ratio) # 用比例換算高
        resizedImg = img.resize((newWidth, newHeight), Image.BILINEAR) # 被放大或所小後的影像, 後面是演算法
        print("new image size: ", resizedImg.size) # 顯示新的大小
        dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
        newImgName = imgName[:dotIndex] + "_resized" + imgName[dotIndex:] # 設定新檔名
        resizedImg.save(newImgName) # 儲存檔案
        print("Resized image is saved as ", newImgName, "\n") # 顯示儲存訊息和檔名
    except FileNotFoundError as fnfe:
        print(fnfe)

def rotateImg(imgName):
    try:
        img = Image.open(imgName)
        print("旋轉選項: ") # 設定第二層問題
        print("1. 左右翻轉")
        print("2. 上下翻轉")
        print("3. 旋轉 90 度")
        print("4. 旋轉 180 度")
        print("5. 旋轉 270 度")
        print("6. other")
        op1 = input("您想進行的操作: ") 
        if op1 == "1":
            newIm = img.transpose(Image.FLIP_LEFT_RIGHT) # 左右翻轉
            str1 = "_flip_LR"
        if op1 == "2":
            newIm = img.transpose(Image.FLIP_TOP_BOTTOM) # 上下翻轉
            str1 = "_flip_TB"
        if op1 == "3":
            newIm = img.transpose(Image.ROTATE_90) # 旋轉 90 度
            str1 = "_rotate_90"
        if op1 == "4":
            newIm = img.transpose(Image.ROTATE_180) # 旋轉 180 度
            str1 = "_rotate_180"
        if op1 == "5":
            newIm = img.transpose(Image.ROTATE_270) # 旋轉 270 度
            str1 = "_rotate_270"
        if op1 == "6":
            rotDegree = float(input("Rotate degree: ")) # 旋轉輸入的角度
            newIm = img.rotate(rotDegree) # 和transpose不同的是如果用rotate會有邊邊被cut掉
            str1 = "_rotate_" + str(rotDegree)
        dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:] # 設定新檔名
        newIm.save(newImgName) # 儲存檔案
        print("Rotated img is saved as ", newImgName, "\n") # 顯示儲存訊息和檔名
    except FileNotFoundError as fnfe:
        print(fnfe)

def genThumbnail(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size) # 查看原始檔案大小
        newWidth, newHeight = map(int, input("請輸入縮圖尺寸: ").split()) # 使用者輸入新的縮圖大小
        img.thumbnail((newWidth, newHeight)) # 套用新大小
        dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
        newImgName = imgName[:dotIndex] + "_thumbnail" + imgName[dotIndex:] # 設定新檔名
        img.save(newImgName) # 儲存檔案
        print("Thumbnail image is saved as ", newImgName, "\n") # 顯示儲存訊息和檔名
    except FileNotFoundError as fnfe:
        print(fnfe)

def applyFilter(imgName):
    try:
        im = Image.open(imgName)
        print("濾鏡選項: ") # 設定第二層問題
        print("1. 模糊 (BLUR)")
        print("2. 輪廓 (CONTOUR)")
        print("3. 細節增強 (DETAIL)")
        print("4. 邊緣增強 (EDGE_ENHANCE)")
        print("5. 深度邊緣增強 (EDGE_ENHANCE_MORE)")
        print("6. 浮雕效果 (EMBOSS)")
        print("7. 邊緣訊息 (FIND_EDGES)")
        print("8. 平滑效果 (SMOOTH)")
        print("9. 深度平滑效果 (SMOOTH_MORE)")
        print("A. 銳利化效果 (SHARPEN)")
        op1 = input("選擇要套用的濾鏡: ") 
        if op1 == "1":
            newImg = im.filter(ImageFilter.BLUR) # 模糊 (BLUR)
            str1 = "_BLUR"
        if op1 == "2":
            newImg = im.filter(ImageFilter.CONTOUR) # 輪廓 (CONTOUR)
            str1 = "_CONTOUR"
        if op1 == "3":
            newImg = im.filter(ImageFilter.DETAIL) # 細節增強 (DETAIL)
            str1 = "_DETAIL"
        if op1 == "4":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE) # 邊緣增強 (EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE"
        if op1 == "5":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE_MORE) # 深度邊緣增強 (EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE"
        if op1 == "6":
            newImg = im.filter(ImageFilter.EMBOSS) # 浮雕效果 (EMBOSS)
            str1 = "_EMBOSS"
        if op1 == "7":
            newImg = im.filter(ImageFilter.FIND_EDGES) # 邊緣訊息 (FIND_EDGES)
            str1 = "_FIND_EDGES" 
        if op1 == "8":
            newImg = im.filter(ImageFilter.SMOOTH) # 平滑效果 (SMOOTH)
            str1 = "_SMOOTH"
        if op1 == "9":
            newImg = im.filter(ImageFilter.SMOOTH_MORE) # 深度平滑效果 (SMOOTH_MORE)
            str1 = "_SMOOTH_MORE"
        if op1 == "A":
            newImg = im.filter(ImageFilter.SHARPEN) # 銳利化效果 (SHARPEN)
            str1 = "_SHARPEN"
        dotIndex = imgName.index(".") # 尋找.jpg或.jepg的.
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:] # 設定新檔名
        newImg.save(newImgName) # 儲存檔案
        print("Filtered image is saved as ", newImgName, "\n") # 顯示儲存訊息和檔名
    except FileNotFoundError as fnfe:
        print(fnfe)

def showMenu(): # 設定第一層問題
    print("====================")
    print("1: 張單影像格式轉換")
    print("2: 張單影像旋轉")
    print("3: 張單影像等比例縮放")
    print("4: 張單影像縮圖製作")
    print("5: 張單影像濾鏡套用")
    print("0: 結束")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        while True: # 無限循環
            showMenu()
            op = input("選擇功能: ")
            if op == "1":
                convertImg(sys.argv[1])
            elif op == "2":
                rotateImg(sys.argv[1])
            elif op == "3":
                resizeImg(sys.argv[1])
            elif op == "4":
                genThumbnail(sys.argv[1])
            elif op == "5":
                applyFilter(sys.argv[1])
            elif op == "0":
                print("bye bye～～～")
                break # 終止迴圈
    else:
        print("Error...!")