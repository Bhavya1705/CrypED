#!/usr/bin/env python
# coding: utf-8

# In[7]:
import warnings
warnings.filterwarnings("ignore")


import time
import random


# In[3]:


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# In[4]:


a='''
#############################################################################################
#                                                                                           #
#                                                                                           #
#    IIIIIIIIIIIIIIIIII     IIIIIIIIIII              III                III                 #
#    III            III     III      IIIII           III                III                 #
#    I  IIIIIIIIIIIIIII     III          IIIII       III                III                 #
#    III                    III             III      III                III                 #
#    III                    III             III      III                III                 #
#    III                    III             III      III                III                 #
#    I  IIIIIIIIIIIIIII     III             III      III                III                 #
#    III            III     III             III      III                III                 #
#    IIIIIIIIIIIIIIIIII     III             III      III                III                 #  
#    III                    III             III      III                III                 #
#    III                    III             III      III                III                 #
#    III                    III             III       III              III                  #
#    I  IIIIIIIIIIIIIII     III          IIIII         III            III                   #
#    III            III     III      IIIII              III          III                    #
#    IIIIIIIIIIIIIIIIII     IIIIIIIIIIII                 IIIIIIIIIIIIII         CONNECT     #
#                                                                                           #
#                                                                                           #
# By YoungMinds - For the Community                                                         #
#############################################################################################
'''


# In[5]:


print(a)


# In[12]:


print(colored(125,125,12,"Mini OS Running"))
print("Loading Connection File")
time.sleep(2)
print("Internet Conncetion Speed ",random.uniform(0.5,1),"Mbps")
print("Authenticating User")
time.sleep(3)
print("User Authenticated")
time.sleep(1)
print("Connecting to Server at https://educoin.org")
time.sleep(5)
print("Login Successful")
print("CPU Bar set at 100%")
print("GPU Bar set at 18 GB")


# In[23]:


def animate(i):
    
    #print(counter)
    

    x = next(index) # counter or x variable -> index
    counter = next(index)
    #print(counter)
    x_values.append(x)
    '''
    Three random value series ->
    Y : 0-5
    Z : 3-8
    Q : 0-10
    '''
    y = random.randint(0, 100)
    z = random.randint(0, 100)
    q = random.uniform(0.5,1)
    # append values to keep graph dynamic
    # this can be replaced with reading values from a csv files also
    # or reading values from a pandas dataframe
    y_values.append(y)
    z_values.append(z)
    q_values.append(q)
    
    
    if counter >40:
        #This helps in keeping the graph fresh and refreshes values after every 40 timesteps
        x_values.pop(0)
        y_values.pop(0)
        z_values.pop(0)
        q_values.pop(0)
        print(counter)
        plt.clf() # clears the values of the graph
    plt.subplot(3,1,1)    
    plt.plot(x_values, y_values,linestyle='--')
    plt.xlabel("Perentage")
    plt.ylabel("Time")
    plt.title('CPU')
    plt.subplot(3,1,2) 
    plt.xlabel("Perentage")
    plt.ylabel("Time")
    plt.title('GPU')
    plt.plot(x_values, z_values,linestyle='--')
    plt.subplot(3,1,3) 
    plt.xlabel("Mbps")
    plt.ylabel("Time")
    plt.title('Speed')
    plt.plot(x_values, q_values,linestyle='--')
    
    plt.legend(["CPU","GPU","Speed"])
    
    
    time.sleep(.25) # keep refresh rate of 0.25 seconds


# In[22]:


import random
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
plt.style.use('fivethirtyeight')
x_values = []
y_values = []
z_values = []
q_values = []
counter = 0
index = count()
ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()


# In[ ]:




