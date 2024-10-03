import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import mplcursors

death = 90
start = 62
ret1 = 67
ret2 = 70
ss = {ret1: 3817, ret2: 4772}
agelist = [i for i in range(start, death)]

# Create directory if it doesn't exist
output_dir = '/home/pgmabv/pyproblems/social_security/'
os.makedirs(output_dir, exist_ok=True)

# Compute payment timeline and investment growth with varying interest rates
def line(retirement_age, monthly_amount, interest_rate):
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
            total_investment += year_amount * (interest_rate ** (age - j))
        
        investment_growth.append(int(total_investment))
    
    return payment_schedule, investment_growth

# Interest rates to test
interest_rates = [1.08, 1.05, 1.03, 1.01]
labels = ["8%", "5%", "3%", "1%"]
colors = ["red", "blue", "green", "purple"]

# Generate and plot payment and investment growth data for different interest rates
for idx, interest in enumerate(interest_rates):
    pay1, inv1 = line(ret1, ss[ret1], interest)
    pay2, inv2 = line(ret2, ss[ret2], interest)

    # Plot for ret1 (earlier retirement)
    plt.plot(agelist, inv1, label=f'Investment Growth from {ret1} @ {labels[idx]} Interest', color=colors[idx], linestyle="--")
    
    # Plot for ret2 (delayed retirement)
    plt.plot(agelist, inv2, label=f'Investment Growth from {ret2} @ {labels[idx]} Interest', color=colors[idx], linewidth=2.5)

# Add labels and legend
plt.xlabel('Age')
plt.ylabel('Cumulative Value (Payments and Investment)')
plt.title('Investment Growth with Varying Interest Rates')
plt.legend()

# Show grid and axes formatting
plt.grid(True)
plt.gca().set_xticks(np.arange(67, 100, 2)) 
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
plt.savefig(f'{output_dir}/investment_comparison.png', dpi=100)
plt.savefig(f'{output_dir}/investment_comparison.pdf', dpi=100)
plt.show()
