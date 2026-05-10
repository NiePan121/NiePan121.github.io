import numpy as np
import matplotlib.pyplot as plt
np.random.seed(None)
N=10000
S=N-1
I=1
R=0
beta=0.3
gamma=0.05
S_list=[S]
I_list=[I]
R_list=[R]
for day in range(1000):
    new_infected = np.random.binomial(S, beta*(I/N))
    new_recovered=np.random.binomial(I,gamma)
    S=S-new_infected
    I=I+new_infected-new_recovered
    R=R+new_recovered
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(8,5),dpi=150)
plt.plot(S_list,label="Susceptible")
plt.plot(I_list,label="Infected")
plt.plot(R_list,label="Recovered")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Stochastic SIR Model")
plt.legend()
plt.show()