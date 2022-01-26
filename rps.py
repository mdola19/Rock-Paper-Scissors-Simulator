import pygame
import math
import os
import time
import random

pygame.init()

screen = pygame.display.set_mode((600, 600)) 
pygame.display.set_caption("Rock Paper Scissors")

title_Font = r"C:\Users\Owner\Desktop\Programming\Python\Beginner Python Projects\Rock Paper Scissors\fonts/yoster.ttf"

rock = pygame.image.load(r"C:\Users\Owner\Desktop\Programming\Python\Beginner Python Projects\Rock Paper Scissors\icons/rock.png")
paper = pygame.image.load(r"C:\Users\Owner\Desktop\Programming\Python\Beginner Python Projects\Rock Paper Scissors\icons/paper.png")
scissors = pygame.image.load(r"C:\Users\Owner\Desktop\Programming\Python\Beginner Python Projects\Rock Paper Scissors\icons/scissors.png")

rock = pygame.transform.scale(rock, (110, 90))
paper = pygame.transform.scale(paper, (90, 90))
scissors = pygame.transform.scale(scissors, (110, 90))

class Hand(pygame.sprite.Sprite):
    def __init__(self, sprites_list, pos_x, pos_y):

        super().__init__() 

        self.current_sprite = 0
        self.image = sprites_list[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, sprites_list, boolean):
        
        self.current_sprite += 0.2

        if self.current_sprite > 14:
            #time.sleep(0.25)
            self.current_sprite = 0

        if boolean == True:
            return
        
        self.image = sprites_list[int(self.current_sprite)]

# Animation Folder Directory
directory = r'C:\Users\Owner\Desktop\Programming\Python\Beginner Python Projects\Rock Paper Scissors\animation'

# Game Move Images
L_scissors = pygame.image.load(os.path.join(directory, r'L_scissors.png'))
L_paper = pygame.image.load(os.path.join(directory, r'L_paper.png'))
L_scissors = pygame.transform.scale(L_scissors, (290, 340))
L_paper = pygame.transform.scale(L_paper, (290, 340))

sprites = []  

sprites.append(pygame.image.load(os.path.join(directory, r'1.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'2.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'3.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'4.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'5.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'6.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'7.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'8.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'9.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'10.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'11.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'12.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'13.png')))
sprites.append(pygame.image.load(os.path.join(directory, r'14.png')))
sprites.append(L_scissors)
sprites.append(L_paper)

sprites2 = []
x = 0

for x in range(len(sprites)):
    flipped_image = pygame.transform.flip(sprites[x].copy(), True, False)
    sprites2.append(flipped_image)

# Creating sprites and groups
moving_sprites = pygame.sprite.Group()
moving_sprites2 = pygame.sprite.Group()
hand = Hand(sprites, 0, 80)
hand2 = Hand(sprites2, 330, 80)
moving_sprites.add(hand)
moving_sprites2.add(hand2)


def text(font, size, text, x, y, color):
    style = pygame.font.Font(font, size)
    drawText = style.render(text, True, color)
    screen.blit(drawText, (x, y))

def isCollision(aX, aY, bX, bY, collision_distance):
    distance = math.sqrt((math.pow(aX - bX, 2)) + (math.pow(aY - bY, 2)))

    if distance < collision_distance:
        return True
    else:
        return False

def intersection(intersectorX, intersectorY, x_Boundary1, x_Boundary2, y_Boundary1, y_Boundary2):

    if intersectorX > x_Boundary1 and intersectorX < x_Boundary2:
        x_Check = True
    else:
        x_Check = False
    
    if intersectorY > y_Boundary1 and intersectorY < y_Boundary2:
        y_Check = True
    else:
        y_Check = False
    
    if x_Check == True and y_Check == True:
        return True

def menuScreen():

    # Game Loop
    run = True
    while run:
        
        screen.fill((219, 219, 219)) 

        for event in pygame.event.get():

            mouseX, mouseY = pygame.mouse.get_pos() 

            if event.type == pygame.QUIT:
                run = False

        detected_intersection = intersection(mouseX, mouseY, 200, 400, 430, 530)

        rect1_X = 200
        rect1_Y = 430

        if detected_intersection == True:
            rect1_X = 190
            rect1_Y = 440

            mouse_presses = pygame.mouse.get_pressed()

            if mouse_presses[0]:
                break

        shadow = pygame.draw.rect(screen, (45, 145, 150),(190,440,200,90), border_radius = 5)
        rect1 = pygame.draw.rect(screen, (47, 196, 204),(rect1_X, rect1_Y,200,90), border_radius = 5)
    
        text(title_Font, 75, "Rock  Paper", 53, 190, (0, 0, 0))
        text(title_Font, 75, "Scissors", 115, 290, (0, 0, 0))
        text(title_Font, 30, "START", rect1_X + 45, rect1_Y + 30, (0, 0, 0))

        screen.blit(rock, (90, 50))
        screen.blit(paper, (250, 50))
        screen.blit(scissors, (400, 50))

        pygame.display.update()

def gameScreen():
    # Game Loop
    run = True
    controller = False
    time.sleep(.25)
    player_score = 0
    cpu_score = 0  

    while run:
        screen.fill((219, 219, 219))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controller = False
    
        text(title_Font, 32, "Player", 20, 20, (0, 0, 255))
        text(title_Font, 32, "CPU", 480, 21, (255, 0, 0))
        text(title_Font, 32, str(player_score) + " : " + str(cpu_score), 265, 21, (0, 0, 0))

        r, g, b = 47, 196, 204
        r2, g2, b2 = 47, 196, 204
        r3, g3, b3 = 47, 196, 204
        mouseX, mouseY = pygame.mouse.get_pos()

        detected_intersection1 = intersection(mouseX, mouseY, 35, 195, 415, 575)
        detected_intersection2 = intersection(mouseX, mouseY, 218, 378, 415, 575)
        detected_intersection3 = intersection(mouseX, mouseY, 405, 565, 415, 575)

        cpu_choices = [0, 14, 15]

        # Player chooses Rock
        if detected_intersection1 == True:
            r, g, b = 45, 145, 150

            mouse_presses = pygame.mouse.get_pressed()

            if mouse_presses[0]:
                controller = True
                time.sleep(.2)
                hand.image = sprites[0]
                cpu_choice = random.choice(cpu_choices)
                hand2.image = sprites2[cpu_choice]

                if cpu_choice == 14:
                    player_score += 1

                if cpu_choice == 15:
                    cpu_score += 1

        # Player Chooses Paper
        if detected_intersection2 == True:
            r2, g2, b2 = 45, 145, 150

            mouse_presses = pygame.mouse.get_pressed()

            if mouse_presses[0]:
                controller = True
                time.sleep(.1)
                hand.image = sprites[15] 
                cpu_choice = random.choice(cpu_choices)
                hand2.image = sprites2[cpu_choice]

                if cpu_choice == 0:
                    player_score += 1

                if cpu_choice == 14:
                    cpu_score += 1               

        # Player Chooses Scissors
        if detected_intersection3 == True:
            r3, g3, b3 = 45, 145, 150

            mouse_presses = pygame.mouse.get_pressed()

            if mouse_presses[0]:
                controller = True
                time.sleep(.1)
                hand.image = sprites[14]
                cpu_choice = random.choice(cpu_choices)
                hand2.image = sprites2[cpu_choice]

                if cpu_choice == 15:
                    player_score += 1

                if cpu_choice == 0:
                    cpu_score += 1

        rect1 = pygame.draw.rect(screen, (r, g, b),(35, 415, 160, 160), border_radius = 8)
        rect2 = pygame.draw.rect(screen, (r2, g2, b2),(218, 415, 160, 160), border_radius = 8)
        rect3 = pygame.draw.rect(screen, (r3, g3, b3),(405, 415, 160, 160), border_radius = 8)

        screen.blit(rock, (60, 450))
        screen.blit(paper, (255, 450))
        screen.blit(scissors, (430, 450))

        moving_sprites.draw(screen)
        moving_sprites.update(sprites, controller)

        moving_sprites2.draw(screen)
        moving_sprites2.update(sprites2, controller)

        pygame.display.update()

menuScreen()
gameScreen()