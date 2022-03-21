#!/usr/bin/env python
# coding: utf-8

# ### Problem: Maximize f(x) = x^3-11x^2+150 when x = 0 to 255

# Representation or ecoding solution:
# x can be represented using 8 bits binary number.

# # Step 1: Initialize Population

# In[38]:


import random
def initPopulation(b, n = 10): # n is the number of solutions, b is the length
    p = [] # to store solution set/ initial population
    for i in range(n):
        s = [] # to store a solution as a list
        for j in range(b):
            s.append(random.choice([0,1]))    
        p.append(s)
    return p


# In[39]:


population = initPopulation(8,15)
population


# In[40]:


population[5]


# # Step 2: Reproduction or Parent Selection

# Fitness Calculation

# In[41]:


[i for i in range(4,-2,-2)]


# In[42]:


def getFitness(p): # p is the whole population
    f = [] # to store fitness values
    for sol in p:
        d = 0 # decimel value
        b = len(sol)
        for i in range(b-1,-1,-1): # binary to decimel
            d = d + sol[i]*2**(b-1-i)
        #print(d)
        v = d**3 - 11*d**2 + 150
        if v< 0: f.append(0)
        else: f.append(v) # fitness function
    return f


# In[43]:


fitness = getFitness(population)
fitness


# calculate probability and select parents

# In[44]:


def select_parent(n, pop): # probability, parent selection
    # probability
    fitness = getFitness(pop)
    total_fitness = sum(fitness)
    prob = [round(f/total_fitness,3) for f in fitness]
    # parent selection
    parents = []
    for i in range(n):
        # roullete wheel, generate a random number
        r = random.choice(range(1,1001,1))/1000
        #print(r)
        lim = 0
        # check bin number of r
        for j in range(len(prob)):
            lim = lim + prob[j]
            if r <= lim :#checking the bin
                print(j)
                parents.append(pop[j])
                break
    return parents


# In[45]:


parents = select_parent(6, population)
parents


# # Step 3: Crossover

# In[58]:



def cross(p):
    num_cross = len(p)/2
    print(num_cross)
    offsprings =[]
    for i in range(int(num_cross)):
        cp = random.choice(range(3,6))
        cp
        print(cp)
        a,b=p[2*i], p[2*i+1]
        off1=a[:cp]+ b[cp:]
        off2=b[:cp]+ a[cp:]
        offsprings.append(off1)
        offsprings.append(off2)
    return offsprings
        



# In[59]:


cross(parents)


# # Step 4: Select Survivor
# The selected survivors (solutions) will be added to population

# Select top 2 offspring based on fitness value and add them to population.

# Repeat Step 2 to 4 for further iterations

# In[ ]:


# define a method to select top offsprings (input offsprings, top)


# In[ ]:


import numpy as np
v =np.array( [2,5,8,3,7,4])
print(v.argsort())
ind = v.argsort()[-1:-3:-1]
list(ind)


# In[ ]:





# In[ ]:




