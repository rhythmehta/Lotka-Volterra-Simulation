# Lotka-Volterra-Simulation

# Simulation Analysis

- "The Lotka–Volterra equations, also known as the predator-prey equations, are a pair of first-order nonlinear differential equations, frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey." (Lotka–Volterra equations, n.d.) 

# Assumptions

- Unlimited food availability for preys
- Predators are dependant on the prey count for food requirement
- Constant environmental conditions and evolutionary genetic adaptations are insignificant.
- It's discrete with small step size, whereas in the Lotka-Volterra model the differential calculation follows a continuous time
- Dependent on the last step for next step whereas in the Lotka-Volterra model, they are independent.
 
# Approach

- Here I have used a numerical approach using Euler's method while attempting to be as accurate as the Lotka-Volterra model which uses an analytical approach. By applying this method with actual equations, we can obtain a better solution with each iteration and higher efficiency with O(1) notation.
