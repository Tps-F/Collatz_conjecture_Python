import time

def collatz(input_input_number):
    if input_number % 2 == 0:
        return int(input_number / 2)
    else:
        return int(3 * input_number + 1)

try:
    input_number = int(input("Input integer: "))
    if input_number == 1:
        print("It's already 1.")
    else:
        while input_number is not 1:
            input_number = collatz(input_number)
            print(input_number)

except ValueError:
    print("You must input integer.")


print("Prosess killing...")
time.sleep(10)