import pyautogui

# 禮物圖片位置
buttonPlocation = [
    "hs_photo/01.jpg",
    "hs_photo/02.jpg",
    "hs_photo/03.jpg",
    "hs_photo/04.jpg",
    "hs_photo/05.jpg",
    "hs_photo/06.jpg",
    "hs_photo/07.jpg",
    "hs_photo/08.jpg"]
# 搜尋禮物
for i in range(8):
    buttonPlocation[i] = pyautogui.locateCenterOnScreen(
        buttonPlocation[i], confidence = 0.7 # ,region = () 搜尋範圍 #
    )
for i in range(8):
    print(i, buttonPlocation[i])