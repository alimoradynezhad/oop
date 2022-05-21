
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

fig = plt.figure()
plt.plot([1,2,3,4], label='blue_line')
plt.ylabel('some numbers')
plt.legend(loc='best')
plt.title('title');