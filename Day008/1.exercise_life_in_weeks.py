def life_in_weeks(age):
    age_in_weeks = age * 52
    average_max_age = 90 * 52
    
    remaining_weeks = average_max_age - age_in_weeks
    
    print(f"You have {remaining_weeks} weeks left.")
    
life_in_weeks(56) # 1768
life_in_weeks(20) # 3640
life_in_weeks(40) # 2600
life_in_weeks(70) # 1040
life_in_weeks(int(input("What is your current age? ")))
