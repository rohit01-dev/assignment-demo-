'''Here's a Python program that calculates simple interest for a bank customer based on their gender and age category:'''

#python
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def get_interest_rate(gender, age):
    if gender.lower() == 'female':
        return 8 if age >= 60 else 6
    elif gender.lower() == 'male':
        return 7 if age >= 60 else 5
    else:
        raise ValueError("Invalid gender - accepted values: 'male', 'female'")


def main():
    try:
        principal = float(input("Enter the principal amount: "))
        time = int(input("Enter the time period in years: "))
        gender = input("Enter the customer's gender (male/female): ")
        age = int(input("Enter the customer's age: "))

        rate = get_interest_rate(gender, age)
        interest = calculate_simple_interest(principal, rate, time)
        
        print("Interest calculated: {:.2f}".format(interest))

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()


'''This program will prompt the user to enter principal amount, time period, customer's gender, and age, and then calculate the simple interest according to the specified rates.'''
