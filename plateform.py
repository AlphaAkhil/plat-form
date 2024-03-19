import pygame 
from pygame.locals import*
import numpy as np
import os


##improve
""" use module in place of function wheel scroll function"""

#------------------------------------------------------------------------------
# blockWidth, blockHeight
# WIDTH, HEIGHT, 
# platFormMatrix
numOfBlock = 10 # number of block in window lenght
startPoint = 0 #position map start from
ROWSIZE = 15 # length of map



#-----------------------window----variable-----------------------------------------------------
WIDTH,HEIGHT =(500,400) #map(int,input(""))
BGCOLOR = (0,0,0) ##background color
COLOR = (244,244,244) #needed color
#path of assetes


#------------------------BLOCK-VARIBLE-------------------------------------------------------
PATH = "assetes/greenZone/Objects/Bushes"
#PATH =  input("enter path where block assete exist: ")

BLOCKWIDTH,BLOCKHEIGHT = 50,40  #BLOCK SIZE WIDTH AND HEIGHT



#create Matrix for platform
platFormMatrix =np.full((10,15), -1)


#-----------------------windows-variable------------------------------------

platFormWindow = pygame.display.set_mode((WIDTH,HEIGHT)) #create window
pygame.display.set_caption("PLATFORM Creater")  #window name
platFormWindow.fill(BGCOLOR) #fill color in canvas



#----------------------------------------------
""" improve the code here """
            


FileNames = np.array(os.listdir("assetes/greenZone/Objects/Bushes"))

# blit block image to  platform window
def blitBlockImg(index,position):
    blockImg = pygame.transform.scale(pygame.image.load(os.path.join(PATH,FileNames[index])),(BLOCKWIDTH,BLOCKHEIGHT))
    platFormWindow.blit(blockImg,position) 


## check where is the block and its blit to window
#------------not-working-properly--------------------------------------
def showPlatForm(i=0,j=0, n=10,m=10):
    #for loop to check every value
    for row in range(i,n):
        for col in range(j,m):
            if platFormMatrix[row,col] != -1:
                #--------------------------------------------------
                # block item image
                blockitem = platFormMatrix[row,col]
                # print(blockitem)
                blitBlockImg(blockitem,((col-startPoint)*BLOCKWIDTH,row*BLOCKHEIGHT))



def position():
    x,y = pygame.mouse.get_pos()
    return x//BLOCKWIDTH,y//BLOCKHEIGHT

def updatePlatForm(position,block):
    platFormMatrix[position[1],position[0]+startPoint] = block

#create line in canvas
def line(n):
    # platFormWindow.fill(BGCOLOR) #fill color in canvas
    for lineNum in range(1,n):
        #hori line
        pygame.draw.line(platFormWindow,COLOR,(lineNum*WIDTH//n, 0),(lineNum*WIDTH//n,HEIGHT),1)
        #vartical line
        pygame.draw.line(platFormWindow,COLOR,(0, lineNum*HEIGHT//n),(WIDTH,lineNum*HEIGHT//n),1)

#check validation and increament
def checkValidation(BLOCK,y):
    BLOCK +=y
    if BLOCK < 0 : 
        return len(FileNames)-1
    elif BLOCK >len(FileNames)-1: 
        return 0
    return BLOCK

def main():
    global startPoint
    run = True
    BLOCK =0

    while run:
        for event in pygame.event.get():

            #check close window or not
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                print(platFormMatrix)
                return
            
            """
            key : d and delete use to delete item block
            key : left and right arrow use to navigate in map
            key : ctrl use to  set multiple value
            """
             #check of wheel change BLOCK
            if event.type == pygame.MOUSEWHEEL:
                #chenge block while checking validation
                BLOCK = checkValidation(BLOCK,event.y)
                
            # ---------------ERROR/---BUG-----------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                updatePlatForm(position(),BLOCK)
            #------------------------------------------------
                
            #KEY button directry
            KEY =pygame.key.get_pressed()

            # remove block item
           
            if(KEY[K_d] or KEY[K_DELETE]):
                updatePlatForm(position(),-1)

            # multiple   
            if (KEY[K_LCTRL] or KEY[K_RCTRL]):   
                             
                    updatePlatForm(position(),BLOCK)
                    # print(platFormMatrix)

            # move left 
            15-10-0 
            if KEY[K_LEFT]:
                if (KEY[K_RSHIFT] or KEY[K_LSHIFT]):
                    if not(startPoint ==0) and ROWSIZE-numOfBlock-startPoint > 2:
                        startPoint -= 3
                    else:
                        startPoint =0
                    continue
                if not(startPoint ==0):
                    startPoint -=1
                
                
            10+5
            if KEY[K_RIGHT]:
                if (KEY[K_RSHIFT] or KEY[K_LSHIFT]):
                    if not(numOfBlock+startPoint > ROWSIZE-1) and startPoint+numOfBlock > ROWSIZE-3:
                        startPoint+=3
                    else:
                        startpoint = ROWSIZE-numOfBlock-1
                    continue
                if (numOfBlock+startPoint < ROWSIZE-1):
                    startPoint +=1
                    print(startPoint)  

           

               
        line(10) #draw in canvas
        showPlatForm( 0,startPoint,10,numOfBlock+startPoint)    
        
        pygame.display.update() #update frame
        platFormWindow.fill(BGCOLOR) #fill color in canvas
        # print(platFormMatrix)

# 
        
if __name__ == "__main__":
    main()
    

#-----------------------------------terminal work------------------------------------------
"""
-----postion list-------
1. new platform
# path to block : => check path vaild or not
## width hight of block item :
### window size aspect ratio,=> size of block in window(row and col)
2. exiting platform => input the name of map
#  2.1. list of exits platform
3. list of all platform
3. show menu
4. 


"""

def showMenu():
    print("======================================================================")
    print("1.new plaform ")
    print("2.edit exiting platform")
    print("3.list of exiting plaform ")
    print("4.new plaform ")
    print("5.show menu ")
    print("======================================================================")



def terminal():
    showMenu()
    while True:
        ip = int(input("enter option: "))
        if ip in range(1,6):
            print(ip)
        if ip == 0:
            break
        print("please Enter one of the option ")

