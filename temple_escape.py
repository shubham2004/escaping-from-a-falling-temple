
# coding: utf-8

"""

you are in a pre-historic temple and accidently step on a foundation stone
and temple start shaking.you have the map of the temple but you need shorted
way out to survive lets see if this code can save you

Q-learning:
Q-learning is a reinforcement learning technique used in machine learning.
The goal of Q-Learning is to learn a policy, which tells an agent what action
to take under what circumstances. It does not require a model of the
environment and can handle problems with stochastic transitions and rewards,
without requiring adaptations.


"""

# lets design the teple map all rooms and rewards of each transition

import random
from random import randint
w, h = 6,6;
q = [[0 for x in range(w)] for y in range(h)] 
r = [[-99 for x in range(w)] for y in range(h)] 
r[1][5]=100
r[4][5]=100
r[5][5]=100
r[0][4]=0
r[1][3]=0
r[2][3]=0
r[3][1]=0
r[3][2]=0
r[3][4]=0
r[4][0]=0
r[4][3]=0
r[5][2]=0
r[5][4]=0

g=0.8

"""
# now we will train our q learning environment to solve the maze for this we
select a random position in the maze and try to go to any random location from
there and according to that we will train the model just to transit from one
room to adjacent room.

"""


for a in range(500000):
    l1=[]
    k=randint(0,5)
    R=random.choice(r[k])
    for i in [i for i,x in enumerate(r[k]) if x == R]:
        l1.append(i)
    z=random.choice(l1)
    q[k][z]=R+(g*(max(r[z])))

    


# after training the q matrix lets see the status of each element

print(q)

"""
so from above we can see that each element got some values like if we see
first row its [-99.0, -19.0, -99.0, -99.0, 80.0, -19.0]
we can say this that it is the chance of tasnsition from 1st row room to
other rooms i.e. from room 0 to other rooms.
we will use highest chance of a tansition chance as it will lead us to our
destination which is room 5. like in this case we will choose room 4 to go to
from room 0.
"""


while(1):
    nin=int(input('enter the urrent room'))
    nout=5
    while(1):
        print(nin)
        if nin==nout:
            print('you are on destination')
            break
        else:
            x=max(q[nin])
            nin=q[nin].index(x)

