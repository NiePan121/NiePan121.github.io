import matplotlib.pyplot as plt
population={
    "UK":{"2020":66.7,"2024":69.2},
    "China":{"2020":1426,"2024":1410},
    "Italy":{"2020":59.4,"2024":58.9},
    "Brazil":{"2020":208.6,"2024":212.0},
    "USA":{"2020":331.6,"2024":340.1}
}
change={}
for country in population:
    pop2020=population[country]["2020"]
    pop2024=population[country]["2024"]
    change[country]=(pop2024-pop2020)/pop2020*100
sorted_change=sorted(change.items(),key=lambda x:x[1],reverse=True)
print("\nThe Population Change (From Largest to Smallest)")
for country,value in sorted_change:
    print(f"{country}:{value:.2f}%")
max=sorted_change[0][0]
min=sorted_change[-1][0]
print("\nLargest Population Increase:",max)
print("Largest Population Decrease:",min)
countries=[]
values=[]
for country,value in sorted_change:
    countries.append(country)
    values.append(value)
plt.bar(countries,values,color="skyblue")
plt.title("Population Percentage Change 2020-2024")
plt.xlabel("Country")
plt.ylabel("Percentage Change(%)")
plt.show()