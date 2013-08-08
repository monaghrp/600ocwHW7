## 1.1 1/8
## 1.2. 1/8
## 1.3. 3/8
## 1.4. 1/2
## 2. 6*(1/6)^5

import random
count=[]
random.seed()
iterations=10000
trials=100
for i in xrange(0,trials):
    count.append(0)
for j in xrange(0,trials):
    for i in xrange(0,iterations):
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        d3=random.randint(1,6)
        d4=random.randint(1,6)
        d5=random.randint(1,6)
        if d1==d2==d3==d4==d5:
            ##print 'Yahtzee!'
            count[j]+=1
chances=float(sum(count)/(float(trials)*float(iterations)))
print 'Chances of Yahtzee! over ' + str(trials) +' trials and ' + str(iterations) +' rolls: ' + str(chances)
