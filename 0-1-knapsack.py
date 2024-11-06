def knapsack_dynamic_programming(items, capacity):
    """
    Solve the 0-1 Knapsack problem using dynamic programming.
    
    Parameters:
    items (list of dict): A list of item dictionaries, where each dictionary has keys 'weight' and 'value'.
    capacity (int): The maximum capacity of the knapsack.
    
    Returns:
    int: The maximum total value that can be obtained.
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1]['weight'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1]['weight']] + items[i - 1]['value'])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Get user input for the items and capacity
num_items = int(input("Enter the number of items: "))
items = []
for i in range(num_items):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    items.append({'weight': weight, 'value': value})

capacity = int(input("Enter the capacity of the knapsack: "))
print(knapsack_dynamic_programming(items, capacity))
