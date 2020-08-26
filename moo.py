
# I don't know if this accuretly represents how many cows how you eaten in your life time 
def moo(beef_per_week, years):
    years -= 4
    years_weeks = 52*years
    return ((years_weeks*200*beef_per_week)/204117)

print(moo(3,20))