import pygame
import pygame.locals

class jugador(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left = (100,200)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

def main():
    import pygame

    pygame.init()
    pantalla = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('NASA International Space Apps Challenge')
    salir = False
    reloj1 =  pygame.time.Clock()
    imagen1 = pygame.image.load('eagle.png').convert_alpha()
    imagenfondo = pygame.image.load('luna1.jpg').convert_alpha()
    astonauta = pygame.image.load('Armstrong.png').convert_alpha()
    pygame.mixer.music.load('despegue.mp3')
    aterriza = pygame.mixer.Sound('apolo10.wav')
    
#variables aux
    jugador1 = jugador(imagen1)
    vx,vy = 0,0
    velocidad = 20
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada = False,False,False,False
    rectangulo = pygame.Rect(490,550,100,50)
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = imagen1
    sprite1.rect = imagen1.get_rect()
    sprite1.rect.top = 0
    sprite1.rect.left = 0
    pygame.mixer.music.play(1)
    
#Loop Principal(Dar movimiento a la nave)
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = True
                    vx =- velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = True
                    vx = velocidad
                if event.key == pygame.K_UP:
                    upsigueapretada = True
                    vy =- velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada = True
                    vy = velocidad
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = False
                    if rightsigueapretada: vx = velocidad
                    else: vx = 0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = False
                    if leftsigueapretada: vx =- velocidad
                    else: vx = 0
                if event.key == pygame.K_UP:
                    upsigueapretada = False
                    if downsigueapretada: vy = velocidad
                    else: vy =- 0
                if event.key == pygame.K_DOWN:
                    downsigueapretada = False
                    if upsigueapretada: vy =- velocidad
                    else: vy = 0
#Las colisiones
            oldx = sprite1.rect.left
            sprite1.rect.move_ip(vx,vy)
            if sprite1.rect.colliderect(rectangulo):
                velocidad = 0
                pygame.mixer.music.stop()
                aterriza.play()
                jugador1.imagen = astonauta

            reloj1.tick(60)
            jugador1.mover(vx,vy)
            pantalla.blit(imagenfondo,(0,0))
            pygame.draw.rect(pantalla,(80,70,70),rectangulo)
            jugador1.update(pantalla)
            pygame.display.update()
            

main()
