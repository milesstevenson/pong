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
    Functions: update """
class Ball:
    
    def __init__(self): 
        
        """ Ball initialization """
        self.ball = pygame.image.load("data/ball.png") #load our ball image
        self.ball_rect = self.ball.get_rect(center=(320,15)) #set the ball rectangle position to be at (320, 15)
      
    def update(self):
        
        #Check for updates in the ball's position, and handle them accordingly
        self.ball_rect = self.ball_rect.move(speed) #change the position of the ball
        if self.ball_rect.right > width or self.ball_rect.left < 0:
            speed[0] = -speed[0]
        if self.ball_rect.top > height or self.ball_rect.bottom < 0:
            speed[1] = -speed[1]

        
    def draw(self, screen, background):
        
        #Draw the updates we've just made to Ball
        screen.blit(self.ball, self.ball_rect) #draw the image of the ball onto our ball_rect
        
""" Class: Bat
    Functions:  """
class Bat:
    
    def __init__(self):
        
        #Our initialization of the Bat class
        self.position = [20,150]
        self.bat = pygame.image.load("data/bat.png")
        self.bat_rect = self.bat.get_rect()
        self.bat_rect = self.bat_rect.move(self.position) #set the ball rectangle position to be at (320, 15)
        
        
    def watchActivity(self, event):
        
        #get the collection of keys pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            print("Big pooper!")
            self.position[1] = self.position[1] - 1
            self.bat_rect.move(self.position)
        #if event.key == pygame.KEYUP:
         #   print("Little pooper!")
          #  self.position[1] = self.position[1] + 1
           # self.bat_rect.move(self.position)
        
    def draw(self, screen, background):
                
        #Draw what updates we've made to the screen
        screen.blit(self.bat, self.bat_rect)

""" Class: Play
    Functions: Play """
class Pong():
    
    def __init__(self):
        
        print("Pong initiated!")
    
    def Play(self):
            
        pygame.init() #initialize all modules from pygame
        pygame.display.set_caption("Pong Clone")
    
        """ Initialize the screen """
        screen = pygame.display.set_mode(size) #create a graphical window 
    
        """ Initialize the background buffer """
        background = pygame.display.set_mode(screen.get_size())
        background = background.convert()
    
        ball = Ball()
        player1 = Bat()
    
        while running:
            #print("Cursor position:", pygame.mouse.get_pos())
        
            for event in pygame.event.get():
                player1.watchActivity(event)
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #screen.fill(black)   
            ball.update()
            
            screen.blit(background, (0,0))
            
            ball.draw(screen, background)
            player1.draw(screen,background)
            
            pygame.display.update()
        
def main():
    Game = Pong()
    Game.Play()
    
if __name__ == '__main__': main()
    #pass