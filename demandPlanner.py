import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sales = [9000000, 9000000, 9000000, 9000000, 8100000, 7800000, 7300000, 6800000, 6300000, 6000000, 5300000, 4800000,
         4000000, 3200000, 2600000, 2500000, 2400000, 2300000, 2200000, 2000000, 2000000, 2000000, 2000000, 2000000]
sns.distplot(sales, kde=False)
plt.show()
