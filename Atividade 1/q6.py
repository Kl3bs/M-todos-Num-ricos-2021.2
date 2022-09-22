import matplotlib.pyplot as plt
import numpy as np


def f(x):
    y = x**2
    return y


def plotFunction(a, b, delta):
    fig, ax = plt.subplots(figsize=(12, 6))

    #x = np.linspace(-10,10,1)
    x = np.arange(0,10, delta)
    y = f(x)
 
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    

    ax.plot(x,y, color='pink', label='Sine wave', linestyle='dashed')
    
    plt.xlim(a, b)
    plt.ylim(a,b)

    plt.show()


plotFunction(0,1,5)
