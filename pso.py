# Nate Fasick
# find max value of: f(x,y) = sin(2/x)+sin(2*x)+cos(x)+sin(20/y)
# using a PSO

import random
from math import sin, cos
from sys import argv
from os import _exit


class Particle:
    def __init__(self):
        self.position = [random.uniform(-5, 5), random.uniform(-5, 5)]  # [x, y]
        self.velocity = [0, 0] # this will be a list: [Vx, Vy]
        self.fitness = calcFitness(self.position[0], self.position[1])
        self.selfbestPosition = [self.position[0], self.position[1]]


def calcFitness(x, y):
    return float(sin(2/x) + sin(2*x) + cos(x) + sin(20/y))


# Vk+1 = (W)(Vk) + (selfsticky)(RAND((Pi-Xk)/dt)) + (globalSticky)(RAND((Pg-Xk)/dt))
def calcVelocity(particle, gs, ss, gBest):
    w = 0.9     # inertia factor: [0.4, 1.4] (i took median)
    v = []
    for vel, pos, best, g in zip(particle.velocity, particle.position, particle.selfbestPosition, gBest):
        v.append(((w*vel) + (ss*random.random()*(best - pos)) + (gs*random.random()*(g - pos))))
    return v


def move(bug, dt):
    for vel, i in zip(bug.velocity, range(2)):
        bug.position[i] += vel*dt
        if bug.position[i] > 5: bug.position[i] = 5
        elif bug.position[i] < -5: bug.position[i] = -5
    bug.fitness = calcFitness(bug.position[0], bug.position[1])


# get the best fitness of a timestep
def getBest(swarm, gBest):
    best = swarm[0]
    for bug in swarm:
        if bug.fitness > best.fitness:
            best = bug
    if gBest is None:    
        return best.position
    if best.fitness > calcFitness(gBest[0], gBest[1]):
        return best.position 
    else:
        return gBest


# initialize the swarm
#   - random position
#   - random velocities
def initSwarm(n):
    swarm = []
    while len(swarm) < n:
        swarm.append(Particle())
    return swarm


if __name__ == '__main__':
    n = 10      # number of particles
    gs = 0.75   # global sticky-ness value
    ss = 0.5    # self sticky-ness value
    t = 0       # our current timeslice
    dt = 0.0001  # how frequently we update our position

    if len(argv) > 1:
        if argv[1] in ['-help', '-h', '--help', 'help']:
            print('python pso.py globalStickyness(default = 0.75) selfStickyness(default = 0.5) numParticles(default = 10)')
            _exit(0)
        elif len(argv) is 4:
            gs = float(argv[1])
            ss = float(argv[2])
            n = int(argv[3])

    swarm = initSwarm(n)
    gBestPosition = getBest(swarm, None)
    
    print('='*40)
    print('GlobalBest: ', gBestPosition)
    for bug in swarm:
        print(bug.position)
    print('='*40)

    count = 0
    while count < 100000:
        count += 1
        for bug in swarm:
            bug.velocity = calcVelocity(bug, gs, ss, gBestPosition)
            move(bug, dt)
        gBestPosition = getBest(swarm, gBestPosition)
    
    print('GlobalBest: ', gBestPosition)
    for bug in swarm:
        print(bug.position)
    print('='*40)


# ** FROM PSO WIKI **
# for each particle i = 1, ..., S do
#   Initialize the particle's position with a uniformly distributed random vector: xi ~ U(blo, bup)
#   Initialize the particle's best known position to its initial position: pi ← xi
#   if f(pi) < f(g) then
#       update the swarm's best known  position: g ← pi
#   Initialize the particle's velocity: vi ~ U(-|bup-blo|, |bup-blo|)
# while a termination criterion is not met do:
#    for each particle i = 1, ..., S do
#       for each dimension d = 1, ..., n do
#          Pick random numbers: rp, rg ~ U(0,1)
#          Update the particle's velocity: vi,d ← ω vi,d + φp rp (pi,d-xi,d) + φg rg (gd-xi,d)
#       Update the particle's position: xi ← xi + vi
#       if f(xi) < f(pi) then
#          Update the particle's best known position: pi ← xi
#          if f(pi) < f(g) then
#             Update the swarm's best known position: g ← pi