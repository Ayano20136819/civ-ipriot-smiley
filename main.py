"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time
from sad import Sad
from happy import Happy
from angry import Angry
from sick import Sick
from smiley import Smiley

def main():

    happy = Happy()
    happy.show()
    time.sleep(1)
    happy.blink()
    print(happy.my_complexion)

    sadly = Sad()
    sadly.show()
    time.sleep(1)
    sadly.blink()
    print(sadly.my_complexion)

    angry = Angry()
    angry.show()

    #sick = Sick()
    #sick.show()

    #smile = Smiley()
    #smile.show()



if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

