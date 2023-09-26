import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) 
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    lst = [pg.transform.rotozoom(kk_img, i, 1.0) for i in range(10)]
    lst += [pg.transform.rotozoom(kk_img, i, 1.0) for i in range(10, 1, -1)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [(1600-(tmr-1600)%3200), 0])
        screen.blit(bg_img2, [1600-(tmr%3200), 0])
        screen.blit(lst[tmr%18], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)
    
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()