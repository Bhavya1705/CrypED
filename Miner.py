#!/usr/bin/env python
# coding: utf-8

# In[1]:


import platform,socket,re,uuid,json,psutil,logging
from tqdm import tqdm
import numpy as np
import random
import time
def getSystemInfo():
    try:
        info={}
        info['Platform']=platform.system()
        info['Platform-release']=platform.release()
        info['Platform-version']=platform.version()
        info['Architecture']=platform.machine()
        info['Hostname']=socket.gethostname()
        info['IP-address']=socket.gethostbyname(socket.gethostname())
        info['MAC-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['Processor']=platform.processor()
        info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['GPU']="N"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


# In[2]:


def fake_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


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
#    IIIIIIIIIIIIIIIIII     IIIIIIIIIIII                 IIIIIIIIIIIIII         COIN        #
#                                                                                           #
#                                                                                           #
# By YoungMinds - For the Community                                                         #
#############################################################################################
'''


# In[5]:


print(a)
time.sleep(3)
print(json.loads(getSystemInfo()))
time.sleep(3)

# In[10]:


print("Connecting to Server at https://educoin.org")
print("Waiting for connection")
print("Establishing MINING Protocols")
for i in tqdm(range(100000)):
    pass
print("Start Process")
while True:
    choices=[0,1]
    choice=np.random.choice(choices)
    try:
        if choice==1:
            print("Job Found from ",fake_ip())
            print(colored(255, 0, 0,"CPU Usage: "+str(random.randint(10,100))))
            print(colored(0, 255, 0,"GPU Usage: "+str(random.randint(0,100))))
            time.sleep(random.randint(0,10))
            for i in tqdm(range(100000)):
                pass
            print("Job Complete")
            print("Coin Earned = ",random.random())
            print("---------------------------------------------")
            #break
        else:
            print("---------------------------------------------")
            print("Looking for Job")
            print("Network Status - Stable")
            print("Hash Rate = ",random.randint(0,20),"MHz")
            print("---------------------------------------------")
    except:
        break
    


# In[ ]:





# In[ ]:





# In[ ]:




