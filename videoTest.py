'''
Created on Apr 21, 2012

@author: Christian
'''


import pygame
import pygame.examples.sound
from Text import Text
from helpers import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
def playMovie():
    pygame.mixer.quit()
    mov = pygame.movie.Movie('data/videos/RainbowIntro-lowRes.mpg')
    mov.set_display(screen, screen.get_rect())
    
    #pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN))
    #pygame.time.set_timer(pygame.USEREVENT, 1000)
    mov.play()
    while mov.get_busy():
        ev = pygame.event.wait()
        if ev.type == pygame.QUIT:
            break
    if mov.get_busy():
        mov.stop()
    #pygame.time.set_timer(pygame.USEREVENT, 0)

def playMusic():
    pygame.mixer.init()
    s = pygame.mixer.Sound('background.wav')
    print s.get_length()
    chan = s.play()
    while chan.get_busy():
        ev = pygame.event.wait()
        if ev.type == pygame.QUIT:
            break
    if chan.get_busy():
        chan.stop()

def showMessage():
    scrollImage = load_image('scroll.png', (640, 240))
    scroll = pygame.sprite.Sprite()
    scroll.image = scrollImage
    scroll.rect = scrollImage.get_rect()
    scroll.bottom = 480
    
    pygame.font.init()
    f = pygame.font.Font(os.path.join('data', 'fonts', 'ayuma.ttf'), 32)
    textIms = [f.render(m, 1, (0, 0, 0)) for m in "Bennett Bartel\n    Bar".split('\n')]
    for i,im in enumerate(textIms):
        scroll.image.blit(im, (50, 25+32*i))
        pygame.image.save(im, 'img'+str(i)+'.png')
    
    
    screen.blit(scroll.image, (0, 240))
    pygame.display.flip()
    while True:
        ev = pygame.event.wait()
        if ev.type in [pygame.KEYDOWN, pygame.QUIT, pygame.MOUSEBUTTONDOWN]:
            break

def showChangingMessage():
    g = pygame.sprite.RenderUpdates()
    background = load_image('backgroundImage.png', (screen.get_rect().width, screen.get_rect().height))
    screen.blit(background, (0,0))
    t = Text("Foo")
    t.color = (0,255,0)
    t.font = 'data/fonts/ayuma.ttf'
    t.createImage()
    t.rect.topleft = (0,0)
    g.add(t)
    
    i = 1
    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            t.st = str(i)
            i += 1
            t.createImage()
        elif ev.type == pygame.QUIT:
            break
    
        g.clear(screen, background)
        changes = g.draw(screen)
        pygame.display.update(changes)
        pygame.display.flip()
    
showChangingMessage()