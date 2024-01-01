from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
# Optimized weekly
prob = LpProblem("Employee_Scheduling", LpMaximize)

# Employee attributes
# - Allowed work hours
# - Flexibility : number of preferred shifts

# Prefrence matrix 
# - Matrix of shift and preferences from 1-3 for all employees

# Shift attributes
# - Day, place, duration

# Fairness
# - How many shifts assigned were highest prefrence / number of shifts


# Define the decision variables
a1 = LpVariable('a1', cat='Binary')  # Employee A works Shift 1
a2 = LpVariable('a2', cat='Binary')  # Employee A works Shift 2
b1 = LpVariable('b1', cat='Binary')  # Employee B works Shift 1
b2 = LpVariable('b2', cat='Binary')  # Employee B works Shift 2

# Define the objective function
# Assume preference scores for each assignment
prob += 3 * a1 + 2 * a2 + 4 * b1 + 3 * b2

# Define the constraints
prob += a1 + a2 <= 1  # Employee A can work only one shift
prob += b1 + b2 <= 1  # Employee B can work only one shift

# Solve the problem
prob.solve()

# Print the results
for v in prob.variables():
    print(v.name, "=", v.varValue)
