#!/usr/bin/env python
# coding: utf-8

# ## Lotka-Volterra Simulation

# ### Simulation Code

import matplotlib.pyplot as plt

#updates prey and predator count with each step
def Euler_steps(prey, predator, step):
    return prey + prey_rate(prey, predator) * step, predator + predator_rate(prey, predator) * step

#calc derivative of prey for particular time
def prey_rate(prey, predator, alpha = 0.005, beta = 0.0001):
    return alpha * prey - beta * prey * predator

#calc derivative of predator for particular time
def predator_rate(prey, predator, delta = 0.0001, gamma = 0.015):
    return delta * prey * predator - gamma * predator

#Lotka Volterra equation simulation with Euler's method
def Lotka_Volterra(prey, predator, time, step):

    #initialize history of both species
    prey_history = [prey]
    predator_history = [predator]

    #iterate until decided time 
    for i in range(int(time/step)):
        #updates prey and predator count
        prey, predator = Euler_steps(prey, predator, step)

        #stores count history
        prey_history.append(prey)
        predator_history.append(predator)

    #plots the species count change over time
    plt.plot(prey_history, label = 'Prey')
    plt.plot(predator_history, label = 'Predator')
    plt.legend(loc='upper right')
    plt.xlabel('Days')
    plt.ylabel('Species Count')

Lotka_Volterra(200, 30, 2000, 1/7)
