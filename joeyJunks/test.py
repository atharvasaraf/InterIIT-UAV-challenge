import sys,tty,termios,cv2,numpy,qrtools,os
class Keyboard:
    """docstring for Keyboard."""


    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return int(ch)

def main():
    while True:
        key = Keyboard()
        print key()
