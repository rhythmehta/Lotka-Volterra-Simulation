#!/usr/bin/env python
# coding: utf-8

# ## Lotka-Volterra Simulation

# ### 1. Simulation Code

# In[2]:


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


# ### 2. Simulation Analysis

# "The Lotka–Volterra equations, also known as the predator-prey equations, are a pair of first-order nonlinear differential equations, frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey." (Lotka–Volterra equations, n.d.)
# 
# ##### + Assumptions
# - Unlimited food availability for preys
# - Predators are dependant on the prey count for food requirement
# - Constant environmental conditions and evolutionary genetic adaptations are insignificant.
# - It's discrete with small step size, whereas in the Lotka-Volterra model the differential calculation follows a continuous time
# - Dependent on the last step for next step whereas in the Lotka-Volterra model, they are independent.
# 
# ##### + Approach Contrast with Lotka-Voltera Model
# 
# - Here we have used a numerical approach using Euler's method while attempting to be as accurate as the Lotka-Volterra model which uses an analytical approach. By applying this method with actual equations, we can obtain a better solution with each iteration and higher efficiency with O(1) notation.
