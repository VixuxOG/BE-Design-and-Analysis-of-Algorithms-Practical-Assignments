def fractional_knapsack(items, capacity):
    """
    Solve the fractional Knapsack problem using a greedy approach.
    
    Parameters:
    items (list of dict): A list of item dictionaries, where each dictionary has keys 'weight' and 'value'.
    capacity (int): The maximum capacity of the knapsack.
    
    Returns:
    float: The maximum total value that can be obtained.
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for item in items:
        if item['weight'] <= remaining_capacity:
            total_value += item['value']
            remaining_capacity -= item['weight']
        else:
            total_value += item['value'] * (remaining_capacity / item['weight'])
            break
    
    return total_value

# Get user input for the items and capacity
num_items = int(input("Enter the number of items: "))
items = []
for i in range(num_items):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    items.append({'weight': weight, 'value': value})

capacity = int(input("Enter the capacity of the knapsack: "))
print(fractional_knapsack(items, capacity))
