from data import CURRENCY, ZJ_PER_AU, regions, COMMON_ITEMS, RARE_ITEMS

print("Welcome to Sellestial")
print("---------------------")

print("Currency:", CURRENCY)
print("Fuel conversion:", ZJ_PER_AU, "ZJ per AU")

print("\nRegions:")
for region in regions:
    print("-", region)

print("\nCommon Items:")
for item in COMMON_ITEMS:
    print("-", item)

print("\nRare Items:")
for item in RARE_ITEMS:
    print("-", item)int("-", item)