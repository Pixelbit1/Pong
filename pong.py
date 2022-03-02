#2.25.2021
import pygame
import random
import time
import sys
import os

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Monospace", 50)
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("Pong")


class player:
    def __init__(self,player):
        self.player = player
        self.y = random.randint(1, 500)
        self.score = 0
        self.width = 15
        self.height = 75
        if self.player == 1:
            self.x = 25
            self.center = [300, 80]
        else:
            self.x = 984
            self.center = [724, 80]
        
        
    def render(self):
        score_text = font.render(str(self.score), False, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.center))
        screen.blit(score_text, score_rect)
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        
    
    def collision(self):
        if self.y < 0:
            self.y = 0
        if self.y > 501:
            self.y = 501
        
class ball:
    def __init__(self):
        self.width = 20
        self.x = 512 - self.width/2
        self.y = 288 - self.width/2
        self.xdirection = random.randint(1, 2)
        self.ydirection = random.randint(1, 2)
        self.timer = 60
        self.frames = 0
        self.move_speed = 3
        
    def move(self):
        if self.timer == 0:
            if self.xdirection == 1:
                self.x += self.move_speed
            else:
                self.x -= self.move_speed
                
            if self.ydirection == 1:
                self.y += self.move_speed
            else:
                self.y -= self.move_speed
                
                
            if self.y < 0:
                self.ydirection = 1
            if self.y > 576 - self.width:
                self.ydirection = 0
                
        else:
            self.timer -= 1
            
        self.frames += 1
        if self.frames % 120 == 0:
            self.move_speed *= 1.1
            
            
    def collision(self):
        if self.x < 0 - self.width or self.x > 1024:
            
            if self.x > 1024:
                player1.score += 1
            else:
                player2.score += 1
                
            self.x = 512 - self.width/2
            self.y = 288 - self.width/2
            self.xdirection = random.randint(1, 2)
            self.ydirection = random.randint(1, 2)
            self.timer = 60
            self.frames = 0
            self.move_speed = 3
            
        
        if player1.x < self.x < player1.x + player1.width:
            if player1.y - self.width < self.y < player1.y + player1.height:
                self.xdirection = 1
                
        if player2.x - self.width < self.x < player2.x + player2.width:
            if player2.y - self.width < self.y < player2.y + player2.height:
                self.xdirection = 0
                
        
            
            
            
    def render(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.width))
    
    
ball = ball()
player1 = player(1)
player2 = player(2)
move_speed = 9
loop = True

while loop:
    
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1024, 576))
   # pygame.draw.rect(screen, (255, 255, 255), (510, 0, 4, 576)) 
    for i in range(69):
        pygame.draw.rect(screen, (255, 255, 255), (510, i * 8 + 15, 4, 4))
    
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            exit()
        
    if pressed_keys[pygame.K_w]:
        player1.y -= move_speed
    if pressed_keys[pygame.K_s]:
        player1.y += move_speed
    if pressed_keys[pygame.K_UP]:
        player2.y -= move_speed
    if pressed_keys[pygame.K_DOWN]:
        player2.y += move_speed
        
    ball.move()
    ball.collision()
    ball.render()
     
    player1.collision()
    player2.collision()
        
    player1.render()
    player2.render()
    pygame.display.flip()
    time.sleep(0.016)
    
exit()
