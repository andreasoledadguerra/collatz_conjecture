def steps(number:int) -> int:
    """
    Computes the number of steps required to reach 1 following the Collatz conjecture.

    The function applies the following rules iteratively:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    - Repeat until the number reaches 1, counting the steps taken.

    Parameters:
    number (int): A positive integer to start the Collatz sequence.

    Returns:
    int: The number of steps taken to reach 1.

    Raises:
    ValueError: If the input is not a positive integer.
    """
     
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0 # Initialize step counter

    while number != 1: # Continue until number reaches 1

        if number % 2 == 0: # Even case
            number //= 2

        else:
            number = number * 3 + 1 # Odd case
        steps += 1 #increment step counter
                
    
    print(f"It took {steps} steps to get 1")
    return steps