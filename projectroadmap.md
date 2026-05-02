## Sprint 1 Tasks
- [x] Create GitHub repository
- [x] Create README.md
- [x] Write project idea
- [x] Find related Python project on GitHub
- [x] Test existing code and document findings

---

# Sellestial Roadmap

This roadmap outlines the core features of Sellestial, a text-based space-trading game.

---

## Core Features

### Player System
- [x] Starting wallet (money)
- [x] Fuel system
- [x] display list of commands
- [x] Inventory (list of items)
- [x] Cargo capacity (starts at 1)
- [x] Implement "Save Game" feature

### Market System
- [x] Multiple regions
- [x] Different buy/sell prices per region
- [x] Fluctuating prices
- [x] compare two regions' prices and potential profits/losses


### Trading System
- [x] Buy items (if enough money and space)
- [x] Sell items (if owned)
- [x] adjustable markets 
- [ ] Track profit from trades (ledger possibly)

### Travel System
- [x] Travel between regions
- [x] Each trip costs fuel
- [x] Prevent travel if not enough fuel
- [x] add travel sequence for better immersion while warping to a system.

### Ship Upgrades
- [x] Upgrade to a better ship to increase cargo capacity and fuel efficiency
- [x] Each upgrade allows +1 item
- [x] Upgrades cost money

---

## Game Flow
- [x] Add intro sequence
- [x] Name character and ship.
- [x] Display player status (wallet, fuel, inventory)
- [x] Show market prices in the current region
- Allow player to:
  - [x] Buy
  - [x] Sell
  - [x] Travel
  - [x] Upgrade ship
- [x] Repeat actions in a loop until player quits


---

## Goal
- Buy items at lower prices
- Travel to another region
- Sell at higher prices
- Manage fuel costs
- Grow total money over time

---

## Related Project
- https://github.com/abadger/stellarmagnate  
- Both projects share core mechanics, including traveling between regions, buying and selling items at different prices, and growing player wealth over time.  
- Uses basic Python structures such as functions, lists, and dictionaries.
