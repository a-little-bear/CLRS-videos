from manim import *

class Video_not_found(Scene):
    def construct(self):
        text = Tex("Video not found.")
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))