'''
Created on Mar 23, 2013
@author: Miles Stevenson
Released under the GNU General Public License
'''
import pygame, sys

size = width, height = 700, 400
speed = [1,1]
down = [0,1]
up = [0,-1]
running = True
black = 0, 0, 0

""" Class: Ball
    Returns: Ball object
    Functions: update, draw """
class Ball:
    
    def __init__(self): 
        
        """ Ball initialization """
        self.ball = pygame.image.load("data/ball.png")
        self.ball_rect = self.ball.get_rect(center=(320,15))
      
    def update(self):
        
        #Check for updates in the ball's position, and handle them accordingly
        self.ball_rect = self.ball_rect.move(speed)
        if self.ball_rect.right > width or self.ball_rect.left < 0:
            speed[0] = -speed[0]
        if self.ball_rect.top > height or self.ball_rect.bottom < 0:
            speed[1] = -speed[1]
        pygame.event.pump()

        
    def draw(self, screen, background):
        
        #Draw the updates we've just made to Ball
        screen.blit(self.ball, self.ball_rect)
        
""" Class: Bat
    Returns: Bat object
    Functions: draw, move_up, move_down  """
class Bat:
    
    def __init__(self):
        
        #Our initialization of the Bat class
        self.position = [20,150]
        self.bat = pygame.image.load("data/bat.png")
        self.bat_rect = self.bat.get_rect()
        self.bat_rect = self.bat_rect.move(self.position)
        self.state = "still"
        
        
    def update(self, pressed):
        pygame.event.pump()
        #print("In Watch Activity")
        
    def draw(self, screen, background):
                
        #Draw what updates we've made to the screen
        screen.blit(self.bat, self.bat_rect)
        
    def move_up(self):
        #self.state = "moveup"
        if self.bat_rect.y > 0:
            self.bat_rect.y = self.bat_rect.y - 1
        
    def move_down(self):
        if self.bat_rect.y < (height - self.bat_rect.height):
            self.bat_rect.y = self.bat_rect.y + 1

""" Class: Pong
    Returns: Pong object
    Functions: play """
class Pong():
    
    def __init__(self):
        
        print("Pong initiated!")
    
    def play(self):
            
        pygame.init()
        pygame.display.set_caption("Pong Clone")
    
        """ Initialize the screen """
        screen = pygame.display.set_mode(size) #create a graphical window 
    
        """ Initialize the background buffer """
        background = pygame.display.set_mode(screen.get_size())
        background = background.convert()
    
        ball = Ball()
        player = Bat()
    
        while running:
            
            print("Cursor position:", pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                """ BAD, BAD, NOT GOOD!!
                    BAD, BAD!
                    BAD!
                elif event.type == pygame.KEYUP:
                    player.state = "still"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.move_up()
                    if event.key == pygame.K_DOWN:
                        player.move_down()"""
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player.move_up()
            if pressed[pygame.K_DOWN]:
                player.move_down()
            else:
                player.state = "still"
                
            ball.update()
            player.update(pressed)
            
            screen.blit(background, (0,0))
            
            ball.draw(screen, background)
            player.draw(screen,background)
            
            pygame.display.update()
        
def main():
    Game = Pong()
    Game.play()
    
if __name__ == '__main__': main()
    #pass