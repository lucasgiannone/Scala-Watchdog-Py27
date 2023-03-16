import win32gui
import win32con
import time


def runWatchdog():
    while True:
        try:
            countdown = 5
            hwnd = win32gui.FindWindowEx(0, 0, 0, "Scala Player")
            if hwnd:
                tup = win32gui.GetWindowPlacement(hwnd)
                print(tup[1])
                if tup[1] != 3 and tup[1] != 1:
                    print('Scala => maximized')
                    # win32gui.SetForegroundWindow(hwnd)
                    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                time.sleep(countdown)
            else:
                print('Scala => not found')
                time.sleep(countdown)
        except:
            print('Error occurred')
            time.sleep(countdown)


if __name__ == "__main__":
    runWatchdog()
