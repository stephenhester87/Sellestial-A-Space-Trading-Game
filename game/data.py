# ======================
# GLOBAL CONSTANTS
# ======================

ZJ_PER_AU = 23
CURRENCY = "SC"


# ======================
# REGION DATA
# ======================

regions = {
    "Nyx": {
        "fuel_price": 0.15,  # SC per ZJ
        "prices": {
            "Medi-gel": 12,
            "CPUs": 25,
            "Polymers": 18,
            "Coolant": 10,
            "Robotics": 40,
            "Silicates": 15,
            "Enriched Uranium": 90
        },
        "routes": {
            "Barak": 3,
            "Azrael": 4,
            "Abaddon": 6
        }
    },

    "Barak": {
        "fuel_price": 0.18,
        "prices": {
            "Medi-gel": 15,
            "CPUs": 20,
            "Polymers": 22,
            "Coolant": 14,
            "Robotics": 35,
            "Silicates": 18,
            "Plutonium Isotopes": 95
        },
        "routes": {
            "Nyx": 3,
            "Azrael": 5,
            "Abaddon": 8
        }
    },

    "Azrael": {
        "fuel_price": 0.12,
        "prices": {
            "Medi-gel": 10,
            "CPUs": 30,
            "Polymers": 16,
            "Coolant": 9,
            "Robotics": 45,
            "Silicates": 20,
            "Nanites": 110
        },
        "routes": {
            "Nyx": 4,
            "Barak": 5,
            "Abaddon": 3
        }
    },

    "Abaddon": {
        "fuel_price": 0.22,
        "prices": {
            "Medi-gel": 18,
            "CPUs": 35,
            "Polymers": 14,
            "Coolant": 20,
            "Robotics": 50,
            "Silicates": 12,
            "Graphene Capacitors": 120
        },
        "routes": {
            "Nyx": 6,
            "Barak": 8,
            "Azrael": 3
        }
    }
}


# ======================
# RARE TRADE ROUTES
# ======================

rare_items = {
    "Enriched Uranium": {
        "origin": "Nyx",
        "destination": "Abaddon",
        "buy_price": 90,
        "sell_price": 180
    },
    "Plutonium Isotopes": {
        "origin": "Barak",
        "destination": "Azrael",
        "buy_price": 95,
        "sell_price": 185
    },
    "Nanites": {
        "origin": "Azrael",
        "destination": "Nyx",
        "buy_price": 110,
        "sell_price": 200
    },
    "Graphene Capacitors": {
        "origin": "Abaddon",
        "destination": "Barak",
        "buy_price": 120,
        "sell_price": 210
    }
}