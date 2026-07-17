def cube_of_numbers(n):
    for i in range(1, n+1):
        print(f"The cube of {i} is {i**3}")
n=int(input("Enter a number to find the cubes of numbers up to that number: "))
cube_of_numbers(n)
