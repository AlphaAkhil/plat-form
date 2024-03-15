import pygame 
from pygame.locals import*
import numpy as np
import os


#------------------------------------------------------------------------------
# boxRow,boxCol= map(int,input("Enter number of row and color: ").split())
# BLOCKSIZE = 30




#-----------------------variable-----------------------------------------------------
#width, and height of window
WIDTH,HEIGHT =(500,500)
BGCOLOR = (0,0,0) ##background color
COLOR = (244,244,244) #needed color
PATH = "assetes/greenZone/Objects/Bushes"



platFormArr =np.zeros(100).reshape(10,10)
print(platFormArr)

platFormWindow = pygame.display.set_mode((WIDTH,HEIGHT)) #create window
pygame.display.set_caption("PLATFORM Creater")  #window name
platFormWindow.fill(BGCOLOR) #fill color in canvas



## animation codes-----------------------------------------------------------------
"""
class platformBlock:
    #path : path of folder
    #size : size of image width and height
    #FPS : frame rate of game
    #animationTime : animation time
    def __init__(self,path,size,postion):
        self.path = path
        self.postion = postion
        self.width, self.height = size
    
    #funtion to show function
    def showAnime(self): 
        frameImg = pygame.image.load(os.path.join(self.path,self.anime[self.__frame]))
        GameWindow.blit(frameImg,(20,20))
        self.updateFrameTime()


"""
#----------------------------------------------

def removeFiletype(x):
    tmp = x.split(".")
    return int(tmp[0])

FileNames = list(map(removeFiletype,np.array(os.listdir("assetes/greenZone/Objects/Bushes"))))
# print(FileNames)



def axis(x):
    return x//50

def updatePlatForm(x,y,block):
    platFormArr[y,x] = block

#create line in canvas
def line(n):
    for lineNum in range(1,n):
        #hori line
        pygame.draw.line(platFormWindow,COLOR,(lineNum*WIDTH//n, 0),(lineNum*WIDTH//n,HEIGHT),1)
        #vartical line
        pygame.draw.line(platFormWindow,COLOR,(0, lineNum*HEIGHT//n),(WIDTH,lineNum*HEIGHT//n),1)


def main():
    run = True
    BLOCK =1

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                print(platFormArr)
            
            # check MOUSE button down 
            if event.type == pygame.MOUSEBUTTONDOWN:
                posX,posY = map(axis,pygame.mouse.get_pos())
                updatePlatForm(posX,posY,BLOCK)

            # control BUTTON
            KEY =pygame.key.get_pressed()
            if (KEY[K_LCTRL] or KEY[K_RCTRL]):              
                    posX,posY = map(axis,pygame.mouse.get_pos())
                    updatePlatForm(posX,posY,BLOCK)
                    print(platFormArr)
                    

            #check of wheel change BLOCK
            if event.type == pygame.MOUSEWHEEL:
                BLOCK +=event.y

                #check Block cross limit or not
                if BLOCK<1 : 
                    BLOCK = len(FileNames)
                elif BLOCK >len(FileNames): 
                    BLOCK =1
                print(BLOCK)      
        
        line(10)#draw in canvas
        pygame.display.update()



if __name__ == "__main__":
    main()