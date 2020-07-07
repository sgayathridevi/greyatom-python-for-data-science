# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#Code starts here
census=np.concatenate([data,new_record])
print(census.shape)
age=np.array([census[:,0]])
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=round(np.std(age),2)
print("\nMax_Age:",max_age)
print("\nMin_Age:",min_age)
print("\nAge_Mean:",age_mean)
print("\nAge_std:",age_std)

r0=census[:,2]
race_0=np.array([r0[census[:,2]==0]])
print(race_0)
race_1=np.array([r0[census[:,2]==1]])
race_2=np.array([r0[census[:,2]==2]])
print(race_2)
race_3=np.array([r0[census[:,2]==3]])
race_4=np.array([r0[census[:,2]==4]])
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
minority_race=-1
if(len_0<len_1)&(len_0<len_2)&(len_0<len_3)&(len_0<len_4):
    minority_race=0
elif(len_1<len_0)&(len_1<len_2)&(len_1<len_3)&(len_1<len_4):
    minority_race=1
elif(len_2<len_0)&(len_2<len_1)&(len_2<len_3)&(len_2<len_4):
    minority_race=2    
elif(len_3<len_0)&(len_3<len_1)&(len_3<len_2)&(len_3<len_4):
    minority_race=3
elif(len_4<len_0)&(len_4<len_1)&(len_4<len_2)&(len_4<len_3):
    minority_race=4
print(minority_race)

senior_citizens=census[census[:,0]>60,:]
working_hours_sum=np.sum(senior_citizens[:,7])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len

print(working_hours_sum)
print(avg_working_hours)

high=census[census[:,1]>10,:]
low=census[census[:,1]<=10,:]
avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)
print(avg_pay_high)
print(avg_pay_low)
print(avg_pay_high > avg_pay_low)


