import numpy as np
import matplotlib.pyplot as plt
N=10000
I0=1
R0=0
beta=0.3
gamma=0.05
vaccine_rates=[0.0,0.3,0.6]
colors=['#1f77b4', '#ff7f0e', '#2ca02c']
labels = ['0% Vaccinated', '30% Vaccinated', '60% Vaccinated']
plt.figure(figsize=(8, 5), dpi=150)
for idx,v_rate in enumerate(vaccine_rates):
    S0=int(N*(1-v_rate))-I0-R0
    S=S0
    I=I0
    R=R0
    S_list=[S]
    I_list = [I]
    R_list = [R]
    for day in range(1000):
        new_infected = np.random.binomial(S, beta * (I / N))
        new_recovered = np.random.binomial(I, gamma)
        I = max(0, I + new_infected - new_recovered)  #Ensure non-negative values
        S = max(0, S - new_infected)
        R = min(N, R + new_recovered)  #Ensure total population does not exceed N
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    plt.plot(I_list, label=labels[idx], color=colors[idx])
plt.xlabel("Time (Days)")
plt.ylabel("Number of Infected People")
plt.title("SIR Model with Different Vaccination Rates")
plt.legend()
plt.grid(alpha=0.3)
plt.show()