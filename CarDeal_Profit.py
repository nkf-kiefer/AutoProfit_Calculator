# -- Colors --
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

# -- initial greeting block --
print(BOLD + CYAN + "=" * 70 + RESET)
print(BOLD + CYAN + "  WELCOME TO THE VEHICLE PROFIT OR LOSS CALCULATOR ".center(70) + RESET)
print(BOLD + CYAN + "=" * 70 + RESET)
print(
    "How to use? Just enter, when requested, the purchase price, the maintenance cost, and the selling price!"
)
print("-" * 70)

# -- variable declarations --
repeat = int(input("How many times do you want the program to repeat:  "))
cars_loss_count = 0
cars_profit_count = 0
no_profit_no_loss_count = 0
sum_profit = 0
sum_loss = 0

# -- loop until the person wants to repeat --
for i in range(repeat):
    print("\n" + "-" * 70)
    print(BOLD + f"Entry  {i + 1} of {repeat}" + RESET)
    car_cost = float(input("Car purchase price: $ "))
    car_maintenance = float(input("Maintenance cost: $ "))
    car_sold = float(input("Selling price: $"))

    total_spend = car_cost + car_maintenance
    total_profit = car_sold - total_spend

    # -- checking if there was loss or profit --
    if total_profit < 0:
        print(RED + f"This car generated a loss of: ${total_profit:.2f}" + RESET)
        cars_loss_count += 1
        sum_loss += total_profit
    elif total_profit > 0:
        print(GREEN + f"This car generated a profit of: {total_profit:.2f}" + RESET)
        cars_profit_count += 1
        sum_profit += total_profit
    else:
        print(YELLOW + "This car generated neither profit nor loss!" + RESET)
        no_profit_no_loss_count += 1


# -- Calculating the average profit (avoiding division by zero) --
if cars_profit_count > 0:
    average_profit = sum_profit / cars_profit_count
else:
    average_profit = 0.0

# -- Calculating the average loss (avoiding division by zero) --
if cars_loss_count > 0:
    average_loss = sum_loss / cars_loss_count
else:
    average_loss = 0.0


# -- Block to Show the results --
print("\n" + BOLD + CYAN + "=" * 70 + RESET)
print(BOLD + "RESUME".center(70) + RESET)
print(BOLD + CYAN + "=" * 70 + RESET)
print(f"A total of {repeat} cars were processed!")
print(GREEN + f"You had {cars_profit_count} cars with profit!")
print(RED + f"You had {cars_loss_count} cars with loss!")
print(RESET + f"You had {no_profit_no_loss_count} cars with no profit and no loss.")
print(GREEN + f"Your average profit was: $ {average_profit:.2f}")
print(RED + f"Your average loss was: $ {average_loss:.2f}")
print(BOLD + CYAN + "=" * 70 + RESET)
