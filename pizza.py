def distribute_pizza(num_people):
    slices_large = 8
    slices_medium = 6
    slices_regular = 4
    slices_small = 1

    
    pizzas_large = num_people // slices_large
    pizzas_medium = (num_people % slices_large) // slices_medium
    pizzas_regular = ((num_people % slices_large) % slices_medium) // slices_regular
    pizzas_small = ((num_people % slices_large) % slices_medium) % slices_regular

    
    total_people_served = (pizzas_large * slices_large) + (pizzas_medium * slices_medium) + (pizzas_regular * slices_regular) + (pizzas_small * slices_small)

    
    print(f"If there are {num_people} individuals:")
    print(f"1. We will have {pizzas_large} Large pizza(s)")
    print(f"2. We will have {pizzas_medium} Medium pizza(s)")
    print(f"3. We will have {pizzas_regular} Regular pizza(s)")
    print(f"4. We will have {pizzas_small} Small pizza(s)")
    print(f"\nTotal people served: {total_people_served}")


if __name__ == "__main__":
    n = int(input("Enter the number of people: "))
    distribute_pizza(n)
