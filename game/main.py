from data import ships, CURRENCY, regions, ZJ_PER_AU

# Player data
player_wallet = 15000
player_ship = "Ymir"
current_region = "Nyx"
current_fuel = 2000
cargo = []
last_profit = 0

print("Initializing pilot registration...\n")

player_name = input("Enter your pilot name: ")
ship_name = input("Name your starting ship: ")

print(f"\nWelcome to Sellestial, Captain {player_name}")
print(f"Your ship '{ship_name}' is ready for departure.")
print("---------------------------------------------")


def display_status():
    print(
        f"\n[Pilot: {player_name} | Ship: {ship_name} ({player_ship}) | "
        f"Wallet: {player_wallet} {CURRENCY} | Fuel: {current_fuel} | "
        f"Current Region: {current_region}]"
    )


def find_region(region_input):
    for region_name in regions:
        if region_name.lower() == region_input.lower():
            return region_name
    return None


def find_item(region_name, item_input):
    for item_name in regions[region_name]["orders"]:
        if item_name.lower() == item_input.lower():
            return item_name
    return None


def find_cargo_item(item_input):
    for item_name in cargo:
        if item_name.lower() == item_input.lower():
            return item_name
    return None


def increase_item_price(region_name, item_name):
    regions[region_name]["orders"][item_name]["buy"] *= 1.10
    regions[region_name]["orders"][item_name]["sell"] *= 1.10

    regions[region_name]["orders"][item_name]["buy"] = round(regions[region_name]["orders"][item_name]["buy"], 2)
    regions[region_name]["orders"][item_name]["sell"] = round(regions[region_name]["orders"][item_name]["sell"], 2)


while True:
    display_status()

    command = input("\nEnter command: ")
    command_lower = command.lower()

    if command_lower == "exit":
        print("\nGoodbye.")
        break

    elif command_lower == "list commands":
        print("\nAvailable Commands:")
        print("-------------------")
        print("list commands : show all commands")
        print("list regions : view a list of regions")
        print("wallet : view your balance")
        print("inv : view ship, fuel, and cargo")
        print("ship wares : view ships for sale")
        print("wares : view items and fuel price in current region")
        print("item wares (region) : view items and fuel price in a region")
        print("compare (region1) (region2) : compare trade prices between two regions")
        print("buy fuel : purchase fuel for your ship")
        print("buy (item) : buy an item from current region")
        print("sell (item) : sell an item from cargo")
        print("travel to (region) : travel to another region")
        print("rename ship : rename your current ship")
        print("exit : quit the game")

    elif command_lower == "list regions":
        print("\nAvailable Regions:")
        print("------------------")

        for region_name in regions:
            print("-", region_name)

    elif command_lower == "wallet":
        print("\nWallet:", player_wallet, CURRENCY)

    elif command_lower == "inv":
        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]
        max_fuel = ship["max_fuel"]

        print("\nInventory")
        print("---------")
        print("Pilot:", player_name)
        print("Ship:", ship_name, f"({player_ship})")
        print("Current Region:", current_region)
        print("Fuel:", current_fuel, "/", max_fuel)
        print("Cargo:", cargo)
        print("Free Cargo Space:", cargo_capacity - len(cargo))

    elif command_lower == "ship wares":
        print("\nShips for Sale:\n")

        for ship_type in ships:
            ship = ships[ship_type]

            print(ship_type)
            print("  Price:", ship["price"], CURRENCY)
            print("  Cargo Capacity:", ship["cargo_capacity"])
            print("  Max Fuel:", ship["max_fuel"])
            print("  Description:", ship["description"])
            print()
            
    elif command_lower.startswith("buy ship "):
        ship_input = command[9:]

        selected_ship = None

        for ship_type in ships:
            if ship_type.lower() == ship_input.lower():
                selected_ship = ship_type

        if selected_ship is None:
            print("\nThat ship is not available.")
        elif selected_ship == player_ship:
            print("\nYou already own that ship type.")
        else:
            new_ship = ships[selected_ship]
            current_ship = ships[player_ship]

            if player_wallet < new_ship["price"]:
                print("\nYou do not have enough money to buy that ship.")
            elif len(cargo) > new_ship["cargo_capacity"]:
                print("\nYou have too much cargo for that ship.")
            else:
                player_wallet -= new_ship["price"]
                player_wallet = round(player_wallet, 2)

                player_ship = selected_ship

                if current_fuel > new_ship["max_fuel"]:
                    current_fuel = new_ship["max_fuel"]

                print("\nShip purchased!")
                print("New Ship Type:", player_ship)
                print("Ship Name:", ship_name)
                print("Cargo Capacity:", new_ship["cargo_capacity"])
                print("Max Fuel:", new_ship["max_fuel"])
                print("Wallet:", player_wallet, CURRENCY)

    elif command_lower == "wares":
        fuel_price = regions[current_region]["fuel_price"]

        print(f"\nMarket Orders in {current_region}")
        print("-------------------------")
        print(f"Fuel Price: {fuel_price} {CURRENCY} per unit\n")

        for item_name in regions[current_region]["orders"]:
            buy_price = regions[current_region]["orders"][item_name]["buy"]
            sell_price = regions[current_region]["orders"][item_name]["sell"]

            print(item_name)
            print(f"  Buy Price:  {buy_price} {CURRENCY}")
            print(f"  Sell Price: {sell_price} {CURRENCY}")
            print()

    elif command_lower.startswith("item wares "):
        region_input = command[11:]
        region_name = find_region(region_input)

        if region_name is None:
            print("\nInvalid region.")
        else:
            fuel_price = regions[region_name]["fuel_price"]

            print(f"\nMarket Orders in {region_name}")
            print("-------------------------")
            print(f"Fuel Price: {fuel_price} {CURRENCY} per unit\n")

            for item_name in regions[region_name]["orders"]:
                buy_price = regions[region_name]["orders"][item_name]["buy"]
                sell_price = regions[region_name]["orders"][item_name]["sell"]

                print(item_name)
                print(f"  Buy Price:  {buy_price} {CURRENCY}")
                print(f"  Sell Price: {sell_price} {CURRENCY}")
                print()

    elif command_lower.startswith("compare "):
        parts = command.split()

        if len(parts) != 3:
            print("\nUsage: compare <region1> <region2>")
        else:
            region1 = find_region(parts[1])
            region2 = find_region(parts[2])

            if region1 is None or region2 is None:
                print("\nInvalid region name.")
            else:
                print(f"\nComparing {region1} → {region2}")
                print("--------------------------------")
                print(f"{region1} Fuel Price: {regions[region1]['fuel_price']} {CURRENCY} per unit")
                print(f"{region2} Fuel Price: {regions[region2]['fuel_price']} {CURRENCY} per unit\n")

                print(f"{'Item':<22}{'Buy':<12}{'Sell':<12}{'Profit/Loss'}")
                print("-" * 58)

                for item_name in regions[region1]["orders"]:
                    if item_name in regions[region2]["orders"]:
                        buy_price = regions[region1]["orders"][item_name]["buy"]
                        sell_price = regions[region2]["orders"][item_name]["sell"]
                        profit = round(sell_price - buy_price, 2)

                        print(f"{item_name:<22}{buy_price:<12}{sell_price:<12}{profit}")

    elif command_lower == "rename ship":
        ship_name = input("Enter new ship name: ")
        print(f"\nYour ship is now called '{ship_name}'.")

    elif command_lower.startswith("travel to "):
        destination_input = command[10:]
        destination = find_region(destination_input)

        if destination is None:
            print("\nInvalid region.")
        elif destination not in regions[current_region]["routes"]:
            print("\nNo route to that region.")
        else:
            distance = regions[current_region]["routes"][destination]
            fuel_cost = distance * ZJ_PER_AU

            if current_fuel >= fuel_cost:
                current_fuel -= fuel_cost
                current_region = destination

                print("\nTravel successful!")
                print("Current Region:", current_region)
                print("Fuel Remaining:", current_fuel)
            else:
                print("\nNot enough fuel to travel.")

    elif command_lower == "buy fuel":
        ship = ships[player_ship]
        max_fuel = ship["max_fuel"]
        fuel_price = regions[current_region]["fuel_price"]

        print("\nFuel Price:", fuel_price, CURRENCY, "per unit")

        amount = int(input("How much fuel do you want to buy? "))
        total_cost = amount * fuel_price

        if current_fuel + amount > max_fuel:
            print("\nCannot exceed max fuel capacity.")
        elif player_wallet < total_cost:
            print("\nNot enough money.")
        else:
            current_fuel += amount
            player_wallet -= total_cost
            player_wallet = round(player_wallet, 2)

            print("\nFuel purchased!")
            print("Current Fuel:", current_fuel, "/", max_fuel)
            print("Wallet:", player_wallet, CURRENCY)

    elif command_lower.startswith("buy "):
        item_input = command[4:]
        item_name = find_item(current_region, item_input)

        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]

        if item_name is None:
            print("\nThat item is not sold in this region.")
        elif len(cargo) >= cargo_capacity:
            print("\nYour cargo hold is full.")
        else:
            price = regions[current_region]["orders"][item_name]["buy"]

            if player_wallet >= price:
                player_wallet -= price
                player_wallet = round(player_wallet, 2)
                cargo.append(item_name)
                last_profit = -price

                increase_item_price(current_region, item_name)

                print("\nPurchase successful!")
                print("Bought:", item_name)
                print("Price Paid:", price, CURRENCY)
                print("New Buy Price:", regions[current_region]["orders"][item_name]["buy"], CURRENCY)
                print("New Sell Price:", regions[current_region]["orders"][item_name]["sell"], CURRENCY)
                print("Wallet:", player_wallet, CURRENCY)
                print("Cargo:", cargo)
                print("Free Cargo Space:", cargo_capacity - len(cargo))
            else:
                print("\nYou do not have enough money.")

    elif command_lower.startswith("sell "):
        item_input = command[5:]
        cargo_item = find_cargo_item(item_input)

        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]

        if cargo_item is None:
            print("\nYou do not have that item in your cargo.")
        else:
            market_item = find_item(current_region, cargo_item)

            if market_item is None:
                print("\nThis region is not buying that item.")
            else:
                price = regions[current_region]["orders"][market_item]["sell"]

                player_wallet += price
                player_wallet = round(player_wallet, 2)
                cargo.remove(cargo_item)
                last_profit = price

                increase_item_price(current_region, market_item)

                print("\nSale successful!")
                print("Sold:", market_item)
                print("Price Received:", price, CURRENCY)
                print("New Buy Price:", regions[current_region]["orders"][market_item]["buy"], CURRENCY)
                print("New Sell Price:", regions[current_region]["orders"][market_item]["sell"], CURRENCY)
                print("Wallet:", player_wallet, CURRENCY)
                print("Cargo:", cargo)
                print("Free Cargo Space:", cargo_capacity - len(cargo))

    else:
        print("\nUnknown command.")