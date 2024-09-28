import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import mplcursors

death = 90
start = 62
ret1=67
ret2=70
ss={ret1:3817, ret2:4772}
interest=1.08
agelist = [i for i in range(start,death)]

# payment array and ivestment array
def line(year0,mamount):
    paylist = []
    investlist = []
    for age in range(start,death):
        if age <= year0:
            paylist.append(0)
        else:
            paylist.append(mamount*12*(age-year0))
            
        # accumulated investment   
        invest=0
        for j in range(year0,age):
            
            if j < year0:
                year_amt=0
            else:
                year_amt=mamount*12
            
            # the investment held from J to age
            invest+=year_amt*(interest**(age-j))
            print(f'age={age} j={j} year_amt={year_amt} invest={invest}')
        investlist.append(int(invest))
             
    return paylist,investlist
        
pay1,inv1=line(ret1,ss[ret1])
pay2,inv2=line(ret2,ss[ret2])
# print(pay1)
# print(inv1)
        
plt.plot(agelist, pay1, label=f'year0={ret1} amount={ss[ret1]}', color="red")    
plt.plot(agelist, pay2, label=f'year0={ret2} amount={ss[ret2]}', color="blue")    
plt.plot(agelist, inv1, label=f'{ret1} invest', color="red",   linewidth=2.5)    
plt.plot(agelist, inv2, label=f'{ret2} invest', color="blue",  linewidth=2.5)    


# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'interst rate={interest}')
plt.legend()

# Show the plot
plt.grid(True)
plt.gca().set_xticks(np.arange(67, 100, 2)) 
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

# Use mplcursors to display values without scientific notation
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"x = {sel.target[0]:.2f}\ny = {sel.target[1]:.2f}"
))

# Save the plot as a file
plt.savefig(f'social security/interst{interest}.png', dpi=100)
plt.savefig(f'social security/interst{interest}.pdf', dpi=100)
plt.show()