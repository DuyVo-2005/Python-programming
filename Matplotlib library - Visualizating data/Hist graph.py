from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])

ax.hist(a, bins = [0,25,50,75,100])

ax.set_title("histogram of result")

ax.set_xticks([0,25,50,75,100])

ax.set_xlabel('marks')

ax.set_ylabel('no. of students')

plt.show()
