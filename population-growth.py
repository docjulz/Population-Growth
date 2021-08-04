# Population growth of an organism
# This program will demonstrate the exponential growth
# of a population of organisms over a period of days

# Get number of initial organism
num_organism = int(input("What is the starting number of organisms? "))

# Get the percentage increase 
avg_increase = float(input("What percent is the daily increase? "))

# get number of days to measure population growth
num_days = int(input("How many days of population growth? "))

# Display table header
print()
print("Day Approximate\t Population")

# Run for loop for population growth
for count in range(1,num_days+1):

    # Calculate and display the growth of the organism
    # over the defined period
    print(count,'\t\t',num_organism)        # chose not to limit decimal to match assignment
    num_organism += avg_increase*num_organism
