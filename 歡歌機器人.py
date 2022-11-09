import pyautogui
import time

pyautogui.FAILSAFE = True
time_secs = 480*60 # 偵測時間(秒鐘)
print("可以開始撿紅包")

end_time = time.time() + time_secs

# 圖源
buttonA6 = './imageOfHappySong/buttonA6.jpg' # 紅包按鈕
buttonA7 = './imageOfHappySong/buttonA7.jpg' # 抽火箭按鈕
buttonB = './imageOfHappySong/buttonB.jpg' # 領取紅包按鈕




while(time.time() < end_time):
    # 偵測紅包
    button1location = pyautogui.locateOnScreen(
        buttonA6, confidence=0.7, region=(480, 0, 500, 540))
    if(button1location != None):
        pyautogui.click(button1location.left+button1location.width/2, button1location.top+button1location.height-20)
        print(button1location)

        # 領取紅包
        time.sleep(0.05)
        pyautogui.click(744, 534) # 領取
        time.sleep(0.1)
        pyautogui.click(50, 540) # 關閉視窗
        print("紅包")

    # 偵測火箭
    else:
        button1location = pyautogui.locateOnScreen(buttonA7, confidence=0.7, region=(480, 360, 500, 480))
        if(button1location != None):
            pyautogui.click(button1location) # 抽
            print(button1location)
            pyautogui.click(50, 540) # 關閉視窗
            print("火箭")

    time_remaining = end_time - time.time()
    hours, mins = divmod(time_remaining, 3600) 
    mins, secs = divmod(mins, 3600)
    timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
    print("\r"+timeformat, end="" )

