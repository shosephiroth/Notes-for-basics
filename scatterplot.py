import matplotlib.pyplot as plt

x = []
y = []

for i in range(-100,101):
     x.append(i)
     y.append(i)

#x = [-100,-99,-98,...,99,100]
#y = [-100,-99,-98,...,99,100]

plt.scatter(x,y)
plt.show()