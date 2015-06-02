__author__ = 'dima'

# import libardrone
import ps_drone
import math
import time

class Drone(ps_drone.Drone):

    def __init__(self, clock):
        super(Drone, self).__init__()
        self.startup()
        self.clock = clock
        self.x = 0
        self.y = 0
        self.z = 0
        self.direct = 0

    def takeoff(self):
        """Make the drone takeoff."""
        self.at("REF", [290718208]) #290718208=10001010101000000001000000000
        self.z = 80

    def land(self):
        """Make the drone land."""
        self.at("REF", [290717696]) #290717696=10001010101000000000000000000
        self.z = 0

    def set_altitude(self, altitude):
        pass
        # self.move()


    def circle(self, R = 200):
        """ radius R """
        for i in range(6):
            # drone.move(0.1, 0.02, 0, 0)
            self.move(0.1, 0.05, 0, -0.3)
            print('f')
            time.sleep(0.8)

    def spiral(self, R=100, alt=100):
        for i in range(6):
            # drone.move(0.1, 0.02, 0, 0)
            self.move(0.1, 0.03, 0.04, -0.3)
            time.sleep(0.8)

    def back_circle(self):
        for i in range(6):
            # drone.move(0.1, 0.02, 0, 0)
            self.move(-0.1, 0.03, 0, 0.3)
            print('b')
            time.sleep(0.8)

        # LENGTH_SHIFT = 30
        # num_iter = int(2*math.pi*R/LENGTH_SHIFT)
        # print(num_iter)
        # num_iter = 6
        # for i in xrange(2*num_iter):
        #     if i % 2 == 0:
        #         self.setSpeed(0.3)
        #         self.moveLeft()
        #         if i % 4 == 0:
        #             time.sleep(0.1)
        #             self.setSpeed(0.1)
        #             self.moveForward()
        #             self.setSpeed(0.2)
        #
        #         # self.set_speed(0.2)
        #         # if 1/num_iter < 0.1:
        #         # self.clock.tick(150)
        #         time.sleep(0.3)
        #     else:
        #         self.turnAngle(30,0.1)
        #         time.sleep(0.05)
        # # for i in xrange(40):





    def go_to_XYZ(self):
        pass




