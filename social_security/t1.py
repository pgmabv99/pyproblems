import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import mplcursors

death = 90
start = 62
ret1 = 65
ret2 = 70
ss = {65:3289, 
      66:3552, 
      67:3817, 
      68:4083, 
      69:4401, 
      70:4772}
interest = 1.05
agelist = [i for i in range(start, death)]

# Compute payment timeline and investment growth
def line(retirement_age, monthly_amount):
    payment_schedule = []
    investment_growth = []
    for age in range(start, death):
        # Payments start after retirement age
        if age <= retirement_age:
            payment_schedule.append(0)
        else:
            payment_schedule.append(monthly_amount * 12 * (age - retirement_age))
        
        # Compute accumulated investment
        total_investment = 0
        for j in range(retirement_age, age):
            year_amount = 0 if j < retirement_age else monthly_amount * 12
            total_investment += year_amount * (interest ** (age - j))
        
        investment_growth.append(int(total_investment))
    
    return payment_schedule, investment_growth

# Generate payment and investment growth data
pay1, inv1 = line(ret1, ss[ret1])
pay2, inv2 = line(ret2, ss[ret2])

# Plotting
plt.plot(agelist, pay1, label=f'Retirement at {ret1} (Monthly = {ss[ret1]})', color="red")
plt.plot(agelist, pay2, label=f'Retirement at {ret2} (Monthly = {ss[ret2]})', color="blue")
plt.plot(agelist, inv1, label=f'Investment Growth from {ret1}', color="red", linewidth=2.5)
plt.plot(agelist, inv2, label=f'Investment Growth from {ret2}', color="blue", linewidth=2.5)

# Add labels and legend
plt.xlabel('Age')
plt.ylabel('Cumulative Value (Payments and Investment)')
plt.title(f'Investment Growth with Interest Rate = {interest}')
plt.legend()

# Show grid and axes formatting
plt.grid(True)
plt.gca().set_xticks(np.arange(64, 100, 2)) 
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# Use mplcursors to display values without scientific notation
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"Age = {sel.target[0]:.2f}\nCumulative Value = {sel.target[1]:.2f}"
))

# Save the plot as a file
plt.savefig(f'social_security/interest_{interest}.png', dpi=100)
# plt.savefig(f'social_security/interest_{interest}.pdf', dpi=100)
plt.show()
