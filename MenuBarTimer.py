import rumps
import time
import os
'''
Antonio Leon
02/13/2024
Menu Bar Timer
'''

class TimerApp(rumps.App):
    def __init__(self):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        icon_path = os.path.join(script_directory, "sandClock.png")
        super(TimerApp, self).__init__("Timer", icon=icon_path)
        self.timer = rumps.Timer(self.update_timer, 1)
        self.start_time = time.time()
        self.menu = ["10 Minutes", "15 Minutes", "20 Minutes", "Stop"]

    def update_timer(self, sender):
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.duration - elapsed_time)
        minutes = int(remaining_time / 60)
        seconds = int(remaining_time % 60)
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        self.title = time_str

        if remaining_time == 0:
            self.timer.stop()
            rumps.notification(title='Timer Expired', subtitle='Time is up!', message='Your timer has finished!')
    
    @rumps.clicked("10 Minutes")
    def start_10_min_timer(self, _):
        self.start_timer(10 * 60)

    @rumps.clicked("15 Minutes")
    def start_15_min_timer(self, _):
        self.start_timer(15 * 60)
        
    @rumps.clicked("20 Minutes")
    def start_20_min_timer(self, _):
        self.start_timer(20 * 60)

    @rumps.clicked("Stop")
    def stop_timer(self, _):
        self.timer.stop()

    def start_timer(self, duration):
        self.duration = duration
        self.start_time = time.time()
        self.timer.start()

if __name__ == '__main__':
    app = TimerApp()
    app.run()
    
