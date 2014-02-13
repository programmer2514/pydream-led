from .display import display
import time

class animation():

    def __init__(self):
        self.sprite = [
            [0,0,0,0,0,0,0],
            [0,1,1,0,1,1,0],
            [1,0,0,1,0,0,1],
            [1,0,0,0,0,0,1],
            [0,1,0,0,0,1,0],
            [0,0,1,0,1,0,0],
            [0,0,0,1,0,0,0],
        ]

        self.sign = display()
        self.sign.connect()

    def run(self):
        size = len(self.sprite[0])+1
        # start = 0
        # while start < 21:
        #     self.sign.put_sprite(start,0,self.sprite)
        #     start += size

        start = 21
        while True:
            self.sign.refresh()
            if start < 0:
                start = 21
            else:
                start -= 1

            print start

            self.sign.move_left()
            spot = start
            self.sign.put_sprite(spot-size,0,self.sprite)
            
            while spot < 21:
                self.sign.put_sprite(spot,0,self.sprite)
                spot += size
            time.sleep(0.1)
