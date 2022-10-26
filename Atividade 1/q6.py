import matplotlib.pyplot as plt
import numpy as np


def f(x):
   y = 2*x - 1*x**2
   return y


x = np.linspace(-1, 2)
# x = [1.2195121951219507,
# 1.0107258849537397,
# 1.00019401167371,
# 1.000003186487126,
# 1.0000000522391037,
# 1.0000000008563792,
# 1.000000000014039,
# 1.00000000000023,
# 1.0000000000000038,
# 1.0]

x = np.array(x)

plt.plot(x, f(x), color='red')
plt.plot(x,x)

# plt.xlim(0.5,1.5)
# plt.ylim(0,2)

plt.show()


 