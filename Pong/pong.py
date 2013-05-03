'''
Created on Mar 23, 2013
@author: Miles Stevenson
Released under the GNU General Public License
'''
import pygame, sys, random


""" Global Variables """
size = width, height = 800, 400
speed = [1,1]
running = True
black = 0, 0, 0

player_scores = (
            pygame.image.load("data/digit_0.png"),pygame.image.load("data/digit_1.png"),
            pygame.image.load("data/digit_2.png"),pygame.image.load("data/digit_3.png"),
            pygame.image.load("data/digit_4.png"),pygame.image.load("data/digit_5.png"),
            pygame.image.load("data/digit_6.png"),pygame.image.load("data/digit_7.png"),
            pygame.image.load("data/digit_8.png"),pygame.image.load("data/digit_9.png")
        )

score_rects = []
for score in player_scores:
    score_rects.append(score.get_rect())

player_count = 0
ai_count = 0

player_score = score_rects[0].move((width/4), 10)
ai_score = score_rects[0].move(width - (width/4), 10)

""" Global Functions: reset_score, update_ai_score, update_player_score, draw_line
                    draw_ai_score, draw_player_score
                    
    The following functions are global, because I'm unsure how to use them in a more
    OOP manner for now. """
def reset_scores():
    global ai_count
    global player_count
    
    player_count = 0
    ai_count = 0
    screen.blit(player_scores[player_count], player_score)
    screen.blit(player_scores[ai_count], ai_score)      

def update_ai_score():
    global ai_count
    
    ai_count = ai_count + 1
    ai_score = score_rects[ai_count]
    
def update_player_score():
    global player_count
    
    player_count = player_count + 1
    player_score = score_rects[player_count]
        
def draw_line():
    screen.blit(split, split_rect) 

def draw_ai_score():
    screen.blit(player_scores[ai_count], ai_score)
        
def draw_player_score():   
    screen.blit(player_scores[player_count], player_score)
    

""" Class: Ball
    Returns: Ball object
    Functions: update, draw, restart_ball, collision """
class Ball:
    
    def __init__(self): 
        
        """ Ball initialization """
        self.bats = (player1.bat_rect, player2.bat_rect)
        self.ball = pygame.image.load("data/ball.png")
        self.ball_rect = self.ball.get_rect(center=(320,15))
    
    def restart_ball(self):
        self.ball_rect = self.ball.get_rect(center=(320,15))
        speed[0] = -speed[0]
      
    def update(self):
        
        #Check for updates in the ball's position, and handle them accordingly
        self.ball_rect = self.ball_rect.move(speed)
        
        if self.ball_rect.right > width:
            update_player_score()
            self.restart_ball()
        if self.ball_rect.left < 0:
            update_ai_score()
            self.restart_ball()          
        if self.ball_rect.top > height or self.ball_rect.bottom < 0:
            speed[1] = -speed[1]
                    
        if (self.ball_rect.midleft <= self.bats[0].midright):
            if (self.collision(self.bats[0])):
                speed[0] = -speed[0]
                
        if (self.ball_rect.midright >= self.bats[1].midleft):
            if (self.collision(self.bats[1])):
                speed[0] = -speed[0]    
        
        if ai_count > 9 or player_count > 9:
            reset_scores()        
        pygame.event.pump()
        
    def draw(self, screen, background):
        
        #Draw the updates we've just made to Ball
        screen.blit(self.ball, self.ball_rect)
            
    def collision(self, target):
        return self.ball_rect.colliderect(target)
        
""" Class: Bat
    Returns: Bat object
    Functions: draw, update, move_up, move_down, return_rect  """
class Bat:
    
    def __init__(self, xpos, ypos, ai):
        self.ai = ai
        self.bat = pygame.image.load("data/paddle.png")
        self.bat_rect = self.bat.get_rect()
        self.bat_rect = self.bat_rect.move(xpos, ypos)
             
        
    def update(self, pressed):
        if self.ai is "False":
            if pressed[pygame.K_UP]:
                self.move_up()
            if pressed[pygame.K_DOWN]:
                self.move_down()
            pygame.event.pump()
        else:
            #Handle AI
            if ball.ball_rect.x >= width/2:
                if ball.ball_rect.y < self.bat_rect.y:
                    self.move_up()
                elif ball.ball_rect.y > self.bat_rect.y:
                    self.move_down()
        
    def draw(self, screen, background):
                
        #Draw what updates we've made to the screen
        screen.blit(self.bat, self.bat_rect)
        
    def move_up(self):
        if self.bat_rect.y > 0:
            if self.ai is "False":
                self.bat_rect.y = self.bat_rect.y - 1
            else:
                self.bat_rect.y = self.bat_rect.y - 1
                self.bat_rect.y = self.bat_rect.y - random.randint(-2,2)
        
    def move_down(self):
        if self.bat_rect.y < (height - self.bat_rect.height):
            if self.ai is "False":
                self.bat_rect.y = self.bat_rect.y + 1
            else:
                self.bat_rect.y = self.bat_rect.y + 1
                self.bat_rect.y = self.bat_rect.y + random.randint(-2,2)

    def return_rect(self): 
        return self.bat_rect    


""" Actual game execution begins here """
            
print("Pong initiated!")       
pygame.init()
pygame.display.set_caption("Pong Clone")
     
""" Initialize the screen """
screen = pygame.display.set_mode(size) #create a graphical window 
    
""" Initialize the background buffer """
background = pygame.display.set_mode(screen.get_size())
background = background.convert()
    
        
player1 = Bat(10, 150, "False")
player2 = Bat(780, 150, "True")
ball = Ball()

split = pygame.image.load("data/dividing-line.png")
split_rect = split.get_rect()
split_rect = split_rect.move(width/2,0)

while running: 
          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                           
    ball.update()
    player1.update(pygame.key.get_pressed())
    player2.update(pygame.key.get_pressed())
            
    screen.blit(background, (0,0))
    
    draw_line()
    draw_player_score() 
    draw_ai_score()       
    ball.draw(screen, background)
    player1.draw(screen,background)
    player2.draw(screen, background)
            
    pygame.display.update()