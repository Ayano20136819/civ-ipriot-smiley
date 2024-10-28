import time
from smiley import Smiley

class Sick(Smiley):
    def __init__(self):
        super().__init__(complexion=self.GREEN)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
                Draws the mouth feature on a smiley
                """
        mouth = [42, 43, 44, 45, 51, 52]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 17, 18, 13, 21 ,22]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion
            self.pixels[pixel] = eyes