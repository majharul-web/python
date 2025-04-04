import pyautogui

def make_pyramid(height):
    pyramid = ""
    for i in range(1, height + 1):
        pyramid += '#' * i + '\n' 
  
    # print(pyramid)
    pyautogui.write(pyramid)  

height = int(input("Enter the height of pyramid: "))
make_pyramid(height)
