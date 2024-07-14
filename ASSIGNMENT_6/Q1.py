# solving a chinese puzzle
# define a function
def puzzle(total_heads, total_legs):
    for chicken in range(total_heads+1):
        rabbits = total_heads-chicken
        if (chicken*2+rabbits*4) == total_legs:
            break
    return chicken, rabbits

total_heads = 35
total_legs = 94

# calling the function
chicken,rabbits = puzzle(total_heads, total_legs)

print(f"Total no. of chickens are: {chicken}")
print(f"Total no. of rabbits are: {rabbits}")