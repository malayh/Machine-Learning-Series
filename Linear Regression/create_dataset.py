#This file will generate a dataset for linear regression
#You can alter the parameters below to generate a dataset
#Author: Malay Hazarika
#Date: 23/11/18

import random

#how many data points in the dataset
no_of_instances=100

#parameters that our model will learn
theta_1=5   #this is m
theta_2=-7  #this is c

#noise to be introduced, to make the data devaite for a perfect line
#so that we can simulate a real dataset
noise=15

#file name to write the datdset to
#will overwrite the previous file if file exists
file_name="linear_dataset.txt"

def create_linear_2d_dataset(no_of_instances,theta_1,theta_2,noise):
    xs=[]
    ys=[]
    for i in range(no_of_instances):
        x=random.uniform(-100,100)
        #y=mx+c
        y=theta_1*x+theta_2

        #Introducing some noise
        x=(x+random.uniform(-noise,noise))
        y=(y+random.uniform(-noise,noise))
        xs.append(x)
        ys.append(y)
        print("{} {}".format(x,y))
    return xs,ys

if(__name__=="__main__"):
    x,y=create_linear_2d_dataset(no_of_instances,theta_1,theta_2,noise)
    with open(file_name,"w") as file:
        for i,j in zip(x,y):
            file.write("{},{}\n".format(i,j))
