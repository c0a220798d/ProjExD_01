import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    # bg_lst = [bg_img, bg2_img] 
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk2_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    lst = [kk_img, kk2_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [1600-x, 0])
        screen.blit(lst[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(1000)
    
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()