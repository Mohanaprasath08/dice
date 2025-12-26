import numpy as np

#Number of simulations
num_rolls=1000

#Roll two dice(value from 1 to 6)
dice1=np.random.randint(1, 7, size=num_rolls)
dice2 = np.random.randint(1, 7, size=num_rolls)

# Sum of both dice
sum_of_dice = dice1 + dice2

# Display results
print("First 10 rolls of Dice 1:", dice1[:10])
print("First 10 rolls of Dice 2:", dice2[:10])
print("First 10 sums:", sum_of_dice[:10])
