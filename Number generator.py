import random
import time
# Constants
MIN = 1
MAX = 6
def main():
    again = 'y'
    # Simulate rolling the dice
    while again == 'y':
        print('Rolling the dice...')
        for i in range(3, 0, -1):
            print(f"{i} second{'s' if i>1 else ''}...")
            time.sleep(1)
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        while True:
            again = input('Roll them again? (y=yes, n=no): ').lower()
            if again == 'y' or again == 'n':
                break
            else:
                print("Invalid input. Press y or n!")
        if again == 'n':
            print('Exiting the program.')
            break
main()