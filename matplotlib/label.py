import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
plt.title("sports")
plt.xlabel("Average")
plt.ylabel("calorie")
plt.plot(x,y,'o-.r')
plt.show()
