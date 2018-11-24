#Author: Malay Hazarika
#Data: 23/11/18

#The linear regression algorthm applied to a 2d dataset to learn how it works
#This is not optimal,will work only in 2d datdset.
#In real world this is implimented a littel bit differently
#In real world, you'll use opitimally coded libraries
#This is just to learn


import random
from matplotlib import pyplot as plt
import numpy as np

#Using the class as container to hold various varibles
class Linear_Regression:
    def __init__(self,xs,ys,learning_rate):
        #dataset
        self.xs=xs
        self.ys=ys
        #lenght of dataset
        self.ds_len=len(xs)

        #how big each step is
        self.learning_rate=learning_rate

        #the arbitrary point, from which the ball will start to roll toward the valley
        self.theta_1=random.uniform(0,1)
        self.theta_2=random.uniform(0,1)

    #this is function is the relationship we are trying to eshtablish btween x and y
    #it returns the value of y it guessed for a given value of x
    #it calculates y from the equation y=mx+c, here m is theta_1, c is theta_2
    def hypothesis(self,x):
        return (x*self.theta_1)+self.theta_2

    #this will calculate to total error for a given line
    def error(self):
        error=0
        for x,y in zip(self.xs,self.ys):
            #this is the sum of error
            #not squring it because, the numbers become too big
            #This doesnot affect the required calation, just to see if error is reducing or not
            error+=np.abs(self.hypothesis(x)-y)
        return error/self.ds_len

    #this will perform updates of theta_1 and theta_2 by the update rule we derived
    #you need to specify how many times do you want to perform the update
    def train_model(self,number_of_iteration):
        for i in range(number_of_iteration):
            #This is the amounts by which theta_1 and theta_2 gets updated in each iteration
            theta_1_update=0
            theta_2_update=0
            for x,y in zip(self.xs,self.ys):
                #these are from the update rules we derived
                #this loop find the sum over all elements
                #the summation part of equation (3) and (4)
                theta_1_update+=(self.hypothesis(x)-y)*x
                theta_2_update+=(self.hypothesis(x)-y)

            #division part of equation (3) and (4)
            theta_1_update/=self.ds_len
            theta_2_update/=self.ds_len
            #calculate error for each itaration to see if error is reducing or not
            error=self.error()
            print("Iteration:{} Error:{}".format(i+1,error))

            #actully change the values of theta_1 and theta_2
            #multiplying alpha before updating from equation (3) and (4)
            self.theta_1-=(2*self.learning_rate*theta_1_update)
            self.theta_2-=(2*self.learning_rate*theta_2_update)


if(__name__=="__main__"):
    #Read the dataset
    xs,ys=[],[]
    with open("linear_dataset.txt","r") as ds:
        rows=ds.read().strip().split("\n")
        for row in rows:
            cols=row.split(",")
            xs.append(float(cols[0]))
            ys.append(float(cols[1]))

    #Try increasing it to a bigger number
    #and see what we were talking about in the learning rate part of the post
    learning_rate=0.0001
    lr=Linear_Regression(xs,ys,learning_rate)
    #This will update theta_1 and theta_2 10000 times
    lr.train_model(10000)

    print("Theta 1:{}".format(lr.theta_1))
    print("Theta 2:{}".format(lr.theta_2))

    #plot the original dataset
    plt.plot(xs,ys,".",label="Dataset")
    #plot the line guessed
    plt.plot(xs,[lr.hypothesis(x) for x in xs],label="Line guessed")
    plt.legend()
    plt.show()
