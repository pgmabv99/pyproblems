import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import mplcursors

death = 90
start62 = 62
retirement_age1 = 65
retirement_age2 = 67
fra_age = 67
# fra_age = 65
max_before_fra = 1860
ss = {64:3174,
    65:3289, 
     66:3552, 
     67:3817, 
     68:4083, 
     69:4401, 
     70:4772}
interest = 1.04
agelist = [i for i in range(start62, death)]

# Compute payment timeline and investment growth
def line(retirement_age, monthly_amount):
    cum_payment_list = []
    cum_invest_list = []
    for age in range(start62, death):
       # age at year start
       # cum_payment and investment at year end
      
       cum_payment = 0
       cum_invest = 0
       if age >= retirement_age:
          #  go over all early ages add payments and investment
          for j_age in range(retirement_age, age+1):
             monthly_amount2 = monthly_amount
             if j_age < fra_age:
                # adjust to before FRA year max benefit
                monthly_amount2 = max_before_fra 
             year_payment = monthly_amount2 * 12
             n_year_to_grow = age - j_age
             year_invest=year_payment * (interest ** (n_year_to_grow))
             cum_payment += year_payment
             cum_invest += year_invest
          
       cum_payment_list.append(cum_payment)
       cum_invest_list.append(int(cum_invest))
    
    return cum_payment_list, cum_invest_list

# Generate payment and investment growth data
pay1, inv1 = line(retirement_age1, ss[retirement_age1])
pay2, inv2 = line(retirement_age2, ss[retirement_age2])
dpay = [p1 - p2 for p1, p2 in zip(pay1, pay2)]
dinv = [i1 - i2 for i1, i2 in zip(inv1, inv2)]

# Plotting
plt.figure(figsize=(10, 5))

# First chart
plt.subplot(1, 2, 1)
plt.plot(agelist, pay1, label=f'Payment from  {retirement_age1} (Monthly = {ss[retirement_age1]})', color="red")
plt.plot(agelist, pay2, label=f'Payment from  {retirement_age2} (Monthly = {ss[retirement_age2]})', color="blue")
plt.plot(agelist, inv1, label=f'Investment Growth from {retirement_age1}', color="red", linewidth=2.5)
plt.plot(agelist, inv2, label=f'Investment Growth from {retirement_age2}', color="blue", linewidth=2.5)

plt.xlabel('Age')
plt.ylabel('Cumulative Value (Payments and Investment)')
plt.title(f'Investment Growth Comparison\nInterest Rate = {interest} FRA = {fra_age} and work income > {max_before_fra}')
plt.legend()
plt.grid(True)
plt.gca().set_xticks(np.arange(62, 100, 2))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(62, color='black', linewidth=0.5)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# Second chart
plt.subplot(1, 2, 2)
plt.plot(agelist, dpay, label=f'Delta in Payments for {retirement_age1} vs {retirement_age2}', color="black", linewidth=2.5)
plt.plot(agelist, dinv, label=f'Delta in Investment for {retirement_age1} vs {retirement_age2}', color="green", linewidth=2.5)

plt.xlabel('Age')
plt.ylabel('Cumulative Value (Payments and Investment)')
plt.title(f'Delta\nInterest Rate = {interest} FRA = {fra_age} and work income > {max_before_fra}')
plt.legend()
plt.grid(True)
plt.gca().set_xticks(np.arange(62, 100, 2))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(62, color='black', linewidth=0.5)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# Use mplcursors to display values without scientific notation
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"Age = {sel.target[0]:.2f}\nCumulative Value = {sel.target[1]:.2f}"
))

# Save the plot as a file
plt.tight_layout()
plt.savefig(f'social_security/interest_{interest}.png', dpi=100)
# plt.savefig(f'social_security/interest_{interest}.pdf', dpi=100)
plt.show()
