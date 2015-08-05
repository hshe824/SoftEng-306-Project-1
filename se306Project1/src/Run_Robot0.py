#!/usr/bin/env python

import rospy
from std_msgs.msg import*
from geometry_msgs.msg import*
from nav_msgs.msg import*
from sensor_msgs.msg import*
from tf.transformations import *
import math
import numpy.testing
from Robot import Robot

"""
@MAIN

Main function that creates robot and sets a path

"""

def main():
    #Construction of Robot objects take 3 params... Robot ID, Start X, Start Y. Start X and Start Y correlates to the myworld.world file
    #Can't create more than one robot per main() .... ie can't run more than one robot per terminal running

    robot0 = Robot(0,0,0)

    rospy.Rate(100)
    rospy.sleep(0.1)

    print("Current x pos = " + str(robot0.px))
    print("Current y pos = " + str(robot0.py))


    #You can use RobotNode_cmdvel to simulate movements, place them in the while loop to try it out
    #RobotNode_cmdvel = geometry_msgs.msg.Twist()

    #moveAction = robot0._actions_[1], [40, 40]
    goToAction = robot0._actions_[1],[10,20]
    goToAction1 = robot0._actions_[1],[0,0]
    goToAction2 = robot0._actions_[1],[10,5]

    robot0._actionsStack_.append(goToAction)
    robot0._actionsStack_.append(goToAction1)
    robot0._actionsStack_.append(goToAction2)


    while not rospy.is_shutdown():

    #check if there is an action on the stack or an action already running
        if(robot0._actionsStack_.__len__() > 0 and not robot0._actionRunning_):
            #get top action on stack
            action = robot0._actionsStack_[-1]
            #run action with parameter
            robot0._actionRunning_ = True
            result = action[0](*action[1])
            robot0._actionRunning_=False
            #if action completes succesfully pop it
            if result == 0 or result == 1:
                robot0._actionsStack_.pop()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
