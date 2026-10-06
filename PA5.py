
def annual_cost(monthly_cost):                                     # defines monthly to yearly conversion function
    return monthly_cost * 12

print("Enter Monthly Expenses Below.\n")                           # user input monthly expense amounts
lp_cost = float(input("Loan Payment Cost: $"))
i_cost = float(input("Insurance Cost: $"))
g_cost = float(input("Gas Cost: $"))
o_cost = float(input("Oil Cost: $"))
t_cost = float(input("Tires Cost: $"))
m_cost = float(input("Maintenance Cost: $"))

month_total = lp_cost + i_cost + g_cost + o_cost + t_cost + m_cost # calculates expenses' total

print("\n\n    Monthly Total:")
print(f"${month_total:.2f}\n")

print("    Annual Costs:")
print(f"Loan Payment: ${annual_cost(lp_cost):.2f}")                # utilizes conversion function for each expense (including total) 
print(f"Insurance: ${annual_cost(i_cost):.2f}")
print(f"Gas: ${annual_cost(g_cost):.2f}")
print(f"Oil: ${annual_cost(o_cost):.2f}")
print(f"Tires: ${annual_cost(t_cost):.2f}")
print(f"Maintenance: ${annual_cost(m_cost):.2f}\n")

print("    Annual Total:")
print(f"${annual_cost(month_total):.2f}")
