import winsound
import time

while True :
    t=900
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
        
    duration = 1100  # milliseconds
    freq = 900  # Hz
    winsound.Beep(freq, duration)


