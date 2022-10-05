# KnapSack Problem

# This is a combinational optimization algorithm.

# In this algorithm, we will be given an array of values with its respective weights.
# We will have a knapsack capacity. We will have to find the maximum value which is
# less than the capacity .

# Note : We cannot break an item. Either we pick a whole item or we do not pick that.


def knapsack(capacity, weights, values, size):

    nums = [0 for i in range(capacity+1)]

    for i in range(1, size+1):
        # starting backwards to store the value of the previous computation.
        for j in range(capacity, 0, -1):

            # calculating the maximum value
            if weights[i-1] <= j:
                nums[j] = max(nums[j], nums[j-weights[i-1]]+values[i-1])

    return nums[capacity]


values = []  # array of the values
weights = []  # array of the weighs

size = int(input("Enter the number of items to be inserted "))

for i in range(0, size):
    val = int(input("Enter value of item "))
    weight = int(input("Enter weight of item "))

    values.append(val)
    weights.append(weight)

capacity = int(input("Enter the knapsack capacity "))

print("The maximum value is ", knapsack(capacity, weights, values, size))
