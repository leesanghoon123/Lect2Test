import game_framework
from pico2d import *
import  random
import game_world

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 150
        self.frame = random.randint(0, 7)
        self.image = load_image('bird100x100x14.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Bird() for i in range(5)]


running = True;
while running:
    handle_events()

    for Bird in team:
        Bird.update()

    clear_canvas()
    for Bird in team:
        Bird.draw()
    update_canvas()

    delay(0.05)

close_canvas()
