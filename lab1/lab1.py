#PROBLEM 4

pounds_per_human = 140
human_population = 7000000000
weight_in_pounds_of_human_population = pounds_per_human * human_population 

kilograms_per_pound = 1/2.204
weight_of_human_population_in_kilograms = weight_in_pounds_of_human_population * kilograms_per_pound

#Density of water and humans are the same according to this problem, remember d = mv 

mass_of_water_in_kilograms = 1
volume_of_water_in_liters = 1 
density_of_water = mass_of_water_in_kilograms / volume_of_water_in_liters 

#Knowing that the density of water and humans is the same allows us to find the volume of humans

density_of_humans = density_of_water 
mass_of_human_population = 4.44646098e11 
volume_of_human_population_in_liters = mass_of_human_population / density_of_humans 

#The volume of the human_population will be in liters 

cube_centimeters_per_liter = 1000 
volume_of_human_population_in_cube_centimeters = volume_of_human_population_in_liters * cube_centimeters_per_liter
cube_centimeters_per_cube_inch = 1/2.54**3 
volume_of_human_population_in_cube_inches = volume_of_human_population_in_cube_centimeters * cube_centimeters_per_cube_inch 
cube_inches_per_cube_foot = 1/12**3 
volume_of_human_population_in_cube_feet = volume_of_human_population_in_cube_inches * cube_inches_per_cube_foot 
cube_feet_per_cube_mile = 1/5280**3 
volume_of_human_population_in_cube_miles = volume_of_human_population_in_cube_feet * cube_feet_per_cube_mile 

print(volume_of_human_population_in_cube_miles)
