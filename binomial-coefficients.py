def binomial_coefficient(n, k):
    """
    Generate the binomial coefficient C(n, k) using dynamic programming.
    
    Parameters:
    n (int): The total number of elements.
    k (int): The number of elements to choose.
    
    Returns:
    int: The binomial coefficient C(n, k).
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]

# Get user input for n and k
n = int(input("Enter the total number of elements (n): "))
k = int(input("Enter the number of elements to choose (k): "))
print(binomial_coefficient(n, k))
