import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import chi2_contingency
from tabulate import tabulate

# defining the table
alpha=0.05
print("alpha=", alpha, "\n")

observed = [[400,55,45,400], [40,5,5,50]]

print("observed data=", observed, "\n")

dof=chi2_contingency(observed).dof
print("dof=",dof, "\n")

chi_square_critical=chi2.ppf(1-alpha, df=dof)
print("chi square_critical=",chi_square_critical, "\n")

expected=chi2_contingency(observed).expected_freq
print("expected table=", expected, "\n")

chi_square_calculated=0

for i in range(len(observed)):
    for j in range(len(observed[i])):
            chi_square_calculated+=(pow(observed[i][j]-expected[i][j],2))/expected[i][j]

print("chi square_calculated=",chi_square_calculated, "\n")

print("Result: \n")
if chi_square_critical <= chi_square_calculated:
    print("While chi_square_critical < chi_square_calculated:")
    print("There is sufficient evidence to reject the H0 hypothesis.")
    print("(We cannot say that it is independent.)")
else:
    print("While chi_square_critical > chi_square_calculated:")
    print("There is not enough evidence to reject the H0 hypothesis.")
    print("(We can say that it is independent.)")

#x-axis ranges from 0 to all with .001 steps

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#data = np.arange(0, len(observed)*len(observed[1]), 0.01)
sns.distplot(random.chisquare(df=dof, size=100000), hist=False)
#plt.plot(data, chi2.pdf(data, df=dof))

plt.axvline(x = chi_square_critical,ymax = 0.50, color = 'red', label = 'chi_square_critical')
plt.text(chi_square_critical, 0.5, round(chi_square_critical, 2))

plt.axvline(x =chi_square_calculated, ymax = 0.50, color = 'purple',label = 'chi_square_calculated')
plt.text(chi_square_calculated,0.5,  round(chi_square_calculated, 2))

# place legend outside
plt.legend(bbox_to_anchor = (0.5, 1), loc = 'upper left')
plt.title("Chi-Square test")
plt.show()
