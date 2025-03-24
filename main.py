def steps(number:int) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0 # Track the number of steps

    while number != 1:

        if number % 2 == 0: #Even case
            number //= 2

        else:
            number = number * 3 + 1
        steps += 1 #increment step counter
                
    
    print(f"It took {steps} steps to get 1")
    return steps