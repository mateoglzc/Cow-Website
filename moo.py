
# I don't know if this accuretly represents how many cows how you eaten in your life time 
def moo(beef_per_week: int, years: int) -> int:
    years = int(years)
    beef_per_week = int(beef_per_week)
    years -= 4
    years_weeks = 52*years
    return round((years_weeks*200*beef_per_week)/204117, 2)
