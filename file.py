import pygame

from config import *

#function to detect collision
def collide():
    global vel
    global vel1
    global vel2
    global poke, level1, level2, Score1, Score2
    are = [
        [crab.x, crab.y],
        [crab1.x, crab1.y],
        [crab2.x, crab2.y],
        [crab3.x, crab3.y],
        [crab4.x, crab4.y],
        [crab5.x, crab5.y],
        [crab6.x, crab6.y],
        [300, 870],
        [900, 720],
        [700, 540],
        [1650, 360],
        [550, 190],
        [1700, 870],
        [300, 540],
        [400, 360],
        [200, 20],
        [100, 720],
        [1400, 20],
        [1000, 190],
        [1000, 360],
        [1500, 540],
        ]

    # if its Player1's Turn  
    if poke == 1:
        for i in range(0, 21):
            if pika.y >= are[i][1] and pika.y <= are[i][1] + 70:
                if pika.x >= are[i][0] and pika.x <= are[i][0] + 70:
                    poke = poke % 1
                    syduck.x = 800
                    syduck.y = 0
                    Score2 = 0
                    s1.append(Score1)
                    print ('hit')
                elif pika.x + 50 >= are[i][0] and pika.x + 50 \
                    <= are[i][0] + 70:
                    poke = poke % 1
                    syduck.x = 800
                    syduck.y = 0
                    Score2 = 0
                    s1.append(Score1)
                    print ('hit')
            elif pika.y + 50 <= are[i][1] + 70 and pika.y + 50 \
                >= are[i][1]:
                if pika.x >= are[i][0] and pika.x <= are[i][0] + 70:
                    print ('hit')
                    syduck.x = 800
                    syduck.y = 0
                    Score2 = 0
                    s1.append(Score1)
                    poke = poke % 1
                elif pika.x + 50 >= are[i][0] and pika.x + 50 \
                    <= are[i][0] + 70:
                    print ('hit')
                    syduck.x = 800
                    syduck.y = 0
                    Score2 = 0
                    s1.append(Score1)
                    poke = poke % 1

        #when player1 reach the endpoint            
        if pika.y < 10:
            poke = 0
            s1.append(Score1)
            Score1 = 0
            Score2 = 0
            level1 += 1
            vel1 += 2
            print ('Player1 reached end point of ' + str(level1))
            syduck.x = 800
            syduck.y = 0
            pika.x = 800
            pika.y = 950

    #if its Player2's turn        
    else:
        for i in range(0, 21):
            if syduck.y >= are[i][1] and syduck.y <= are[i][1] + 70:
                if syduck.x >= are[i][0] and syduck.x <= are[i][0] + 70:
                    print ('hit')
                    pika.x = 800
                    pika.y = 950
                    poke = 1
                    s2.append(Score2)
                    Score1 = 0
                elif syduck.x + 50 >= are[i][0] and syduck.x + 50 \
                    <= are[i][0] + 70:
                    print ('hit')
                    pika.x = 800
                    pika.y = 950
                    Score1 = 0
                    s2.append(Score2)
                    poke = 1
            elif syduck.y + 50 <= are[i][1] + 70 and syduck.y + 50 \
                >= are[i][1]:
                if syduck.x >= are[i][0] and syduck.x <= are[i][0] + 70:
                    print ('hit')
                    pika.x = 800
                    pika.y = 950
                    Score1 = 0
                    s2.append(Score2)
                    poke = 1
                elif syduck.x + 50 >= are[i][0] and syduck.x + 50 \
                    <= are[i][0] + 70:
                    print ('hit')
                    pika.x = 800
                    pika.y = 950
                    Score1 = 0
                    s2.append(Score2)
                    poke = 1

        #when Player2 reach the end point            
        if syduck.y > 940:
            poke = 1
            level2 += 1
            s2.append(Score2)
            Score2 = 0
            Score1 = 0
            vel2 += 2
            print ('Player2 reached end point of ' + str(level2))
            pika.x = 800
            pika.y = 950
            syduck.x = 800
            syduck.y = 0

#Function to form the game window till one exits the window
def redrawGameWindow():
    global count
    global pika
    global syduck
    global poke, second1, second2, minute1, minute2
    total_seconds1 = frame_count1 // frame_rate
    total_seconds2 = frame_count2 // frame_rate
    minutes1 = total_seconds1 // 60
    minutes2 = total_seconds2 // 60
    second1 = total_seconds1 % 60
    second2 = total_seconds2 % 60
    game.fill((62, 73, 87))
    pygame.draw.rect(game, (41, 23, 3), (0, 0, 1800, 90))
    pygame.draw.rect(game, (41, 23, 3), (0, 180, 1800, 90))
    pygame.draw.rect(game, (41, 23, 3), (0, 360, 1800, 90))
    pygame.draw.rect(game, (41, 23, 3), (0, 540, 1800, 90))
    pygame.draw.rect(game, (41, 23, 3), (0, 720, 1800, 90))
    pygame.draw.rect(game, (41, 23, 3), (0, 900, 1800, 100))
    pygame.draw.rect(game, (11, 102, 35), (0, 950, 1800, 50))
    pygame.draw.rect(game, (11, 102, 35), (0, 0, 1800, 50))
    text1 = font.render('START', 1, (0, 0, 0))
    text2 = font.render('END', 1, (0, 0, 0))
    text3 = font.render('Player1', 1, (0, 0, 0))
    text4 = font.render('Player2', 1, (0, 0, 0))
    text5 = font.render('Score1: ' + str(Score1), 1, (0, 0, 0))
    text6 = font.render('Score2: ' + str(Score2), 1, (0, 0, 0))
    text7 = font.render('Time: ' + str(minutes1) + ':' + str(second1),
                        1, (0, 0, 0))
    text8 = font.render('Time: ' + str(minutes2) + ':' + str(second2),
                        1, (0, 0, 0))
    if poke == 1:
        vel = vel1
        pika.make(game)
        game.blit(text1, (900, 970))
        game.blit(text2, (900, 10))
        game.blit(text3, (10, 970))
        game.blit(text5, (100, 970))
        game.blit(text7, (250, 970))
    else:
        vel = vel2
        syduck.make(game)
        game.blit(text1, (900, 10))
        game.blit(text2, (900, 970))
        game.blit(text6, (100, 0))
        game.blit(text8, (250, 0))
        game.blit(text4, (10, 0))
    crab.draw(game, vel)
    crab1.draw(game, vel)
    crab2.draw(game, vel)
    crab3.draw(game, vel)
    crab5.draw(game, vel)
    crab4.draw(game, vel)
    crab6.draw(game, vel)
    plant.draw(game)
    plant1.draw(game)
    plant2.draw(game)
    plant3.draw(game)
    plant4.draw(game)
    plant5.draw(game)
    plant6.draw(game)
    plant7.draw(game)
    plant8.draw(game)
    plant9.draw(game)
    plant10.draw(game)
    plant11.draw(game)
    plant12.draw(game)
    plant13.draw(game)
    
    #calling collide function
    collide()
    pygame.display.update()


on = True
while on:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    keys = pygame.key.get_pressed()

    #keys For player1
    if keys[pygame.K_LEFT] and pika.x > pika.vel:
        pika.x -= pika.vel
    if keys[pygame.K_RIGHT] and pika.x < 1800 - pika.vel - pika.width:
        pika.x += pika.vel
    if keys[pygame.K_UP] and pika.y > pika.vel - 10:
        pika.y -= pika.vel
    if keys[pygame.K_DOWN] and pika.y < 1000 - pika.height - pika.vel \
        + 10:
        pika.y += pika.vel

    #keys For player2
    if keys[pygame.K_a] and syduck.x > syduck.vel:
        syduck.x -= syduck.vel
    if keys[pygame.K_d] and syduck.x < 1800 - syduck.vel - syduck.width:
        syduck.x += syduck.vel
    if keys[pygame.K_w] and syduck.y > syduck.vel - 10:
        syduck.y -= syduck.vel
    if keys[pygame.K_s] and syduck.y < 1000 - syduck.height \
        - syduck.vel + 10:
        syduck.y += syduck.vel

    if poke == 1:
        frame_count1 += 1
    else:
        frame_count2 += 1

    #Scoring For Player1
    if 1000 - pika.y > 140:
        Score1 = 10
    if 1000 - pika.y > 190:
        Score1 = 20
    if 1000 - pika.y > 280:
        Score1 = 30
    if 1000 - pika.y > 370:
        Score1 = 40
    if 1000 - pika.y > 460:
        Score1 = 55
    if 1000 - pika.y > 550:
        Score1 = 75
    if 1000 - pika.y > 640:
        Score1 = 90
    if 1000 - pika.y > 730:
        Score1 = 100
    if 1000 - pika.y > 820:
        Score1 = 110
    if 1000 - pika.y > 910:
        Score1 = 130
    if 1000 - pika.y > 960:
        Score1 = 140

    #Scoring For Player2
    if syduck.y > 90:
        Score2 = 10
    if syduck.y > 180:
        Score2 = 30
    if syduck.y > 260:
        Score2 = 40
    if syduck.y > 360:
        Score2 = 50
    if syduck.y > 450:
        Score2 = 65
    if syduck.y > 540:
        Score2 = 85
    if syduck.y > 630:
        Score2 = 100
    if syduck.y > 720:
        Score2 = 110
    if syduck.y > 820:
        Score2 = 120
    if syduck.y > 910:
        Score2 = 130
    if syduck.y > 940:
        Score2 = 140
    redrawGameWindow()

    #when key x is pressed that means user wants to exit
    if keys[pygame.K_x]:
        length1 = len(s1)
        length2 = len(s2)
        sum1 = 0
        sum2 = 0
        for i in range(0, length1):
            sum1 = sum1 + s1[i]
        for i in range(0, length2):
            sum2 = sum2 + s2[i]
        text10 = font.render('Player1    ' + 'Score: ' + str(sum1)
                             + '   ' + 'Time:  ' + str(minute1) + ' :  '
                              + str(second1) + '    Level:   '
                             + str(level1), 1, (0, 0, 0))
        text11 = font.render('Player2    ' + 'Score: ' + str(sum2)
                             + '   ' + 'Time:  ' + str(minute2) + ' :  '
                              + str(second2) + '    Level:   '
                             + str(level2), 1, (0, 0, 0))
        if sum1 > sum2:
            p1 = 1
            text9 = font1.render('Player1 won', 1, (0, 0, 0))
        elif sum1 < sum2:
            p1 = 2
            text9 = font1.render('Player2 won', 1, (0, 0, 0))
        else:
            if minute1 > minute2:
                p1 = 2
                text9 = font1.render('Player2 won', 1, (0, 0, 0))
            elif minute2 > minute1:
                p1 = 1
                text9 = font1.render('Player1 won', 1, (0, 0, 0))
            else:
                if second1 > second2:
                    p1 = 2
                    text9 = font1.render('Player2 won', 1, (0, 0, 0))
                elif second2 > second1:
                    p1 = 1
                    text9 = font1.render('Player1 won', 1, (0, 0, 0))
                else:
                    p1 = 0
                    text9 = font1.render('No one won the match', 1, (0,
                            0, 0))
        on = False
on = True


#when user press x this should show on screen
while on:
    game.fill((255, 0, 0))
    game.blit(text9, (500, 400))
    if p1 == 1:
        game.blit(pikachuwin, (400, 600))
        game.blit(crown, (800, 600))
        game.blit(text10, (100, 100))
        game.blit(text11, (1000, 100))
    elif p1 == 2:
        game.blit(syduckwin, (400, 600))
        game.blit(crown, (800, 600))
        game.blit(text10, (100, 100))
        game.blit(text11, (1000, 100))
    else:
        game.blit(pikachuwin, (400, 600))
        game.blit(syduckwin, (800, 600))
        game.blit(text10, (100, 100))
        game.blit(text11, (1000, 100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
pygame.quit()