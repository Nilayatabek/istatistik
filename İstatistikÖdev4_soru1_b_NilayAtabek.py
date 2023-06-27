# Importing library
from scipy import stats
from scipy.stats import f_oneway
import scipy.stats
import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt
from tabulate import tabulate
import math
alpha=0.05
print("alpha=",alpha)

group1 = [6,7,4,5,6,3]
group2 = [8,10,11,7,12,11]
group3 = [10,11,8,6,13,12]

print(group1,"\n",group2,"\n",group3,"\n")

group_number=3
data_number=len(group1)*group_number
dof1=group_number-1
dof2=data_number-group_number
print("dof1=",dof1,"\n","dof2=",dof2)
 
# Conduct the one-way ANOVA
f_value_calculated,p_value_calculated=f_oneway(group1, group2, group3)
print("f_value_calculated=",f_value_calculated)
f_value_critical=scipy.stats.f.ppf(q=1-alpha,dfn=dof1, dfd=dof2)
print("f_value_critical=", f_value_critical)

print("Result: \n")
if f_value_critical <= f_value_calculated:
    print("While f_value_critical < f_value_calculated:")
    print("There is sufficient evidence to reject the H0 hypothesis.")
    print("(We cannot say that all population means are equal.)")
else:
    print("While f_value_critical > f_value_calculated:")
    print("There is not enough evidence to reject the H0 hypothesis.")
    print("(We can say that all population means are equal.)")

x = data = np.arange(0, data_number, 0.01)
plt.plot(x, f.pdf(x, dof1, dof2),'c-', lw=5, alpha=0.5, label='f pdf')

plt.axvline(x = f_value_critical,ymax = 0.50, color = 'red', label = 'f_value_citical')
plt.text(f_value_critical, 0.5, round(f_value_critical, 2))

plt.axvline(x =f_value_calculated, ymax = 0.50, color = 'purple',label = 'f_value_calculated')
plt.text(f_value_calculated,0.5,  round(f_value_calculated, 2))

# place legend outside
plt.legend(bbox_to_anchor = (0.5, 1), loc = 'upper left')
plt.title("One way ANOVA")
plt.show()
