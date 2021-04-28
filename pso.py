import random
import numpy as np 
import rastrign
import ackley
import eggholder
import math


W = 0.5
c1 = 0.8
c2 = 0.9
tab = []
tabParticlePosition = []
tabPbestPosition = []
tabLocalOptimum = []
target_error = 0
teority_optimum = 0

class Particle():
    def __init__(self,checked):
        
        self.checked = checked

        if(checked==1):
            self.position = np.random.uniform(-1, 1, 2)
        elif(checked==2):
            self.position = np.random.uniform(-30, 30, 2)
        elif(checked==3):
            self.position = np.random.uniform(-512, 512, 2)
        
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])
        
    def move(self):
        self.position = self.position + self.velocity


class Space():

    def __init__(self, target, target_error, n_particles, checked):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*50, random.random()*50])
        self.gbest_optimum = float(-math.inf)
        self.checked = checked

    def optimum(self,particle):
        if(self.checked==1):
            return rastrign.rastrign(particle.pbest_position[0], particle.pbest_position[1])
        elif(self.checked==2):
            return ackley.ackley(particle.pbest_position[0], particle.pbest_position[1])
        elif(self.checked==3):
            return eggholder.eggholder(particle.pbest_position[0], particle.pbest_position[1])
 
    def set_gbestoptimum(self):
        i = 0
        for particle in self.particles:
            optimum_candidate = self.optimum(particle)
            tabLocalOptimum.append(str(optimum_candidate))
            print(i, ". Optimum cand", optimum_candidate)
            i=i+1
            if(optimum_candidate > self.gbest_optimum):
                self.gbest_optimum = optimum_candidate
            
   
    def fitness(self, particle):
        return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):
        i = 0
        
        for particle in self.particles:
            tabParticlePosition.append(str(particle.position))
            print(i, ". Particle postion: ", particle.position)
            fitness_cadidate = self.fitness(particle)
            
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position

            tabPbestPosition.append(str(particle.pbest_position))
            print(i, ". Particle pbest: ", particle.pbest_position)
            i=i+1
            
    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position


    def move_particles(self):
        for particle in self.particles:
            global W
            new_velocity = (W*particle.velocity) + (c1*random.random()) * (particle.pbest_position - particle.position) + \
                            (random.random()*c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
            

def main(n_iterations, n_particles,checked):

    search_particle = Particle(checked)
    search_space = Space(1, target_error, n_particles, checked)
    particles_vector = [Particle(checked) for _ in range(search_space.n_particles)]
    search_space.particles = particles_vector
    #search_space.print_particles()

    iteration = 0
    while(iteration < n_iterations):
        search_space.set_pbest()    
        search_space.set_gbest()
        search_space.set_gbestoptimum()

        if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
            break

        search_space.move_particles()
        iteration += 1
    

    a =  ("Global Best Optimum is: " + str(search_space.gbest_optimum))
    return a

def plotingAnimation(n_iterations, n_particles):
    options = {'c1':c1, 'c2':c2, 'w':W}
    optimizer = ps.single.GlobalBestPSO(n_particles=n_particles, dimensions=2, options=options)
    cost, pos = optimizer.optimize(fx.sphere, iters=n_iterations)

    m = Mesher(func=fx.sphere)

    animation = plot_contour(pos_history=optimizer.pos_history,mesher=m,mark=(0,0))
    plt.show()

def plotingChart(n_iterations, n_particles):
    options = {'c1':c1, 'c2':c2, 'w':W}
    optimizer = ps.single.GlobalBestPSO(n_particles=n_particles, dimensions=2, options=options)
    cost, pos = optimizer.optimize(fx.sphere, iters=n_iterations)

    plot_cost_history(cost_history=optimizer.cost_history)
    plt.show()



#main(20,10,1)