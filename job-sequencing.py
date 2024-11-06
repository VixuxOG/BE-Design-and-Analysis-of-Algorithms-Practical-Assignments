def job_sequencing(jobs):
    """
    Solve the job sequencing problem with deadlines using a greedy approach.
    
    Parameters:
    jobs (list of dict): A list of job dictionaries, where each dictionary has keys 'id', 'deadline', and 'profit'.
    
    Returns:
    list: The list of job IDs in the order they should be completed.
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x['profit'], reverse=True)
    
    result = []
    time_slot = [False] * max(job['deadline'] for job in jobs)
    
    for job in jobs:
        for i in range(job['deadline'] - 1, -1, -1):
            if not time_slot[i]:
                time_slot[i] = True
                result.append(job['id'])
                break
    
    return result

# Get user input for the jobs
num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    job_id = input(f"Enter job {i+1} ID: ")
    deadline = int(input(f"Enter job {i+1} deadline: "))
    profit = int(input(f"Enter job {i+1} profit: "))
    jobs.append({'id': job_id, 'deadline': deadline, 'profit': profit})

print(job_sequencing(jobs))
