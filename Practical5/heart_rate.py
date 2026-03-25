import matplotlib.pyplot as plt
heart_rates = [72, 85, 55, 98, 122, 68, 145, 88, 76, 102, 59, 130]
num_patients = len(heart_rates)
average_hr = sum(heart_rates) / num_patients
print("Total patients:", num_patients)
print("Average heart rate:", round(average_hr, 1))
low=0
normal=0
high=0
for hr in heart_rates:
    if hr<60:
        low+=1
    elif hr<=120:
        normal+=1
    else:
        high+=1
print("\nLow(<60):",low)
print("Normal(60-120):",normal)
print("High(>120):",high)
counts=[low,normal,high]
max_count=max(counts)
max_index=counts.index(max_count)
categories=["Low","Normal","High"]
max_categories=categories[max_index]
print("The category contains the largest number of patients:",max_categories)
labels=["Low(<60)","Normal(60-120)","High(>120)"]
sizes=[low,normal,high]
colors=["lightblue","lightgreen","lightyellow"]
plt.pie(sizes,labels=labels,colors=colors,autopct="%1.1f%%")
plt.title("Heart Rate Distribution")
plt.show()