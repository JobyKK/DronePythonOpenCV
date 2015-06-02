__author__ = 'dima'

import libardrone
import pygame
import move
import time
import cv2

f = open('log.txt','a\n')

pygame.init()
W, H = 320, 240
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()


# drone = move.Drone(clock)
drone = move.Drone(clock)
# drone.reset()
# drone.takeoff()

drone.useDemoMode(True)                            # Set 15 basic dataset/sec

##### Mainprogram begin #####
drone.setConfigAllID()                              # Go to multiconfiguration-mode
drone.sdVideo()                                     # Choose lower resolution (try hdVideo())
drone.frontCam()                                    # Choose front view
CDC = drone.ConfigDataCount
while CDC==drone.ConfigDataCount: time.sleep(0.001) # Wait until it is done (after resync)
drone.startVideo()                                 # Start video-function                                  # Display the video

def move_in_m(drone, count, clock):
    i = 0
    while (i < count):
        drone.move_forward()
        clock.tick(50)
        i+=1


running = True
i_m = 0
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                f.write('quit\n')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drone.land()
                    f.write('land\n')
                if event.key == pygame.K_UP:
                    drone.moveUp()
                    f.write('move_up\n')
                if event.key == pygame.K_ESCAPE:
                    running = False
                    f.write('Exit\n')
                if event.key == pygame.K_DOWN:
                    drone.moveDown()
                    f.write('move_down\n')
                if event.key == pygame.K_1:
                    move_in_m(drone, 10, clock)
                    f.write('10\n')
                if event.key == pygame.K_2:
                    move_in_m(drone, 10, clock)
                    f.write('20\n')
                if event.key == pygame.K_RETURN:
                    drone.takeoff()
                    f.write('takeoff\n')
                    print('take off')
                # if event.key == pygame.K_LCTRL:
                #     drone.reset()
                #     f.write('reset\n')
                    f.write('forward\n')
                if event.key == pygame.K_s:
                    drone.moveBackward()
                    f.write('back\n')
                if event.key == pygame.K_a:
                    drone.moveLeft()
                    f.write('left\n')
                if event.key == pygame.K_d:
                    drone.moveRight()
                    f.write('right\n')
                if event.key == pygame.K_w:
                    drone.moveForward()
                    f.write('forward\n')
                if event.key == pygame.K_LEFT:
                    drone.turnLeft()
                    f.write('left\n')
                if event.key == pygame.K_RIGHT:
                    drone.turnRight()
                    f.write('right\n')
                if event.key == pygame.K_LCTRL:
                    bat = drone.getBattery()
                    f.write(str(bat))
                    print(bat)
                if event.key == pygame.K_q:
                    print('rotation')
                    drone.circle()
                if event.key == pygame.K_e:
                    print('rotation')
                    drone.spiral()
                if event.key == pygame.K_b:
                    print('rotation')
                    drone.back_circle()
                if event.key == pygame.K_p:
                    try:
                        print('image has been saved')
                        # drone.
                        frame = drone.getImage()
                        #img_process(frame)
                        i_m+=1
                        cv2.imwrite('test'+ i_m +'.jpeg', frame)
                    except:
                        print('cry')
#<<<<<<< Updated upstream:python-ardrone-master/main.py
        # try:
        #     clock.tick(50)
        #
        # except:
        #     f.write('err\n')
#=======
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_1):
                #     drone.speed = 0.1
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_2):
                #     drone.speed = 0.2
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_3):
                #     drone.speed = 0.3
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_4):
                #     drone.speed = 0.4
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_5):
                #     drone.speed = 0.5
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_6):
                #     drone.speed = 0.6
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_7):
                #     drone.speed = 0.7
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_8):
                #     drone.speed = 0.8
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_9):
                #     drone.speed = 0.9
                # if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_0):
                #     drone.speed = 1.0

        try:
            clock.tick(50)
            date = drone.getData()
            f.write(str(date) + '\n')
        except:
            f.write('err\n')
#>>>>>>> Stashed changes:python-ardrone-master/main.py

#end demonstration
drone.land()
# drone.halt()