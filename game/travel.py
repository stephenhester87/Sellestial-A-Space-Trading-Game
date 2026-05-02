import time

# -----------------------------
# Timed text output
# -----------------------------
def timed_lines(lines, delay=1.0):
    for line in lines:
        print(line)
        time.sleep(delay)


# -----------------------------
# Warp sequence (flavor text)
# -----------------------------
def warp_sequence(start_region, destination, distance, fuel_cost):
    lines = [
        "",
        f"Your warp drive begings to spool as you plot your course \n from {start_region} to {destination}...",
        "",
        "\"Warp drive activated...\"",
        "...",
        "Time seems to slow as your hull begins to shake.",
        "",
        "The stars begin to bend around your hull, as if aware of your passing",
        "",
        "Your ship calms as if frozen in time.",
        "",
        "...",
        "",
        "Your ship trembles back to life.",
        "...",
        f"Exiting warp near {destination}...",
        ""        
    ]

    timed_lines(lines, 0.8)


# -----------------------------
# Travel function: Handles movement, fuel calculation, and validation
# -----------------------------
def travel_to(current_region, destination, current_fuel, regions, ZJ_PER_AU):
    # Validate destination
    if destination not in regions:
        print("\nUnknown region.")
        return current_region, current_fuel

    if destination == current_region:
        print("\nYou are already here.")
        return current_region, current_fuel

    # Get coordinates
    start_coords = regions[current_region]["coords"]
    dest_coords = regions[destination]["coords"]

    # Calculate distance 
    distance = ((start_coords[0] - dest_coords[0]) ** 2 +
                (start_coords[1] - dest_coords[1]) ** 2) ** 0.5

    distance = round(distance, 2)

    # Calculate fuel cost
    fuel_cost = int(distance * ZJ_PER_AU)

    # Check fuel
    if current_fuel < fuel_cost:
        print("\nNot enough fuel.")
        print(f"Required: {fuel_cost} | Available: {current_fuel}")
        return current_region, current_fuel

    # Run warp sequence BEFORE updating state
    warp_sequence(current_region, destination, distance, fuel_cost)

    # Update state
    current_fuel -= fuel_cost
    current_region = destination

    print("\nTravel successful!")
    print("Current Region:", current_region)
    print("Fuel Remaining:", current_fuel)

    return current_region, current_fuel