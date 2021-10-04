from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x,y
    global side
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
           x = event.x    
           y = KPU_HEIGHT -1 - event.y            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
c, d = 0, 0
frame = 0
side = 100
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.clip_draw(0, 0, 100, 100, x, y)

    if x != c and y != d:
        character.clip_draw(frame * 100, 100, 100, 100, c, d)
        c += 1 and c<x
        d += 1 and d<y       
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




