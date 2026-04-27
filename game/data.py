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
        "fuel_price": 0.15,
        "orders": {
            "Medi-gel": {"buy": 70, "sell": 50},
            "CPUs": {"buy": 95, "sell": 70},
            "Polymers": {"buy": 130, "sell": 95},
            "Coolant": {"buy": 85, "sell": 60},
            "Robotics": {"buy": 120, "sell": 90},
            "Silicates": {"buy": 150, "sell": 105},
            "Enriched Uranium": {"buy": 250, "sell": 180},
            "Nanites": {"buy": 500, "sell": 450}
        },
        "routes": {
            "Barak": 3,
            "Azrael": 4,
            "Abaddon": 6
        }
    },

    "Barak": {
        "fuel_price": 0.18,
        "orders": {
            "Medi-gel": {"buy": 120, "sell": 95},
            "CPUs": {"buy": 80, "sell": 60},
            "Polymers": {"buy": 90, "sell": 65},
            "Coolant": {"buy": 140, "sell": 100},
            "Robotics": {"buy": 95, "sell": 70},
            "Silicates": {"buy": 145, "sell": 120},
            "Plutonium Isotopes": {"buy": 260, "sell": 190},
            "Graphene Capacitors": {"buy": 550, "sell": 500}
        },
        "routes": {
            "Nyx": 3,
            "Azrael": 5,
            "Abaddon": 8
        }
    },

    "Azrael": {
        "fuel_price": 0.12,
        "orders": {
            "Medi-gel": {"buy": 95, "sell": 75},
            "CPUs": {"buy": 150, "sell": 115},
            "Polymers": {"buy": 110, "sell": 85},
            "Coolant": {"buy": 45, "sell": 30},
            "Robotics": {"buy": 175, "sell": 205},
            "Silicates": {"buy": 100, "sell": 75},
            "Plutonium Isotopes": {"buy": 500, "sell": 430},
            "Nanites": {"buy": 275, "sell": 200}
        },
        "routes": {
            "Nyx": 4,
            "Barak": 5,
            "Abaddon": 3
        }
    },

    "Abaddon": {
        "fuel_price": 0.22,
        "orders": {
            "Medi-gel": {"buy": 160, "sell": 125},
            "CPUs": {"buy": 185, "sell": 145},
            "Polymers": {"buy": 70, "sell": 50},
            "Coolant": {"buy": 130, "sell": 105},
            "Robotics": {"buy": 210, "sell": 165},
            "Silicates": {"buy": 50, "sell": 35},
            "Enriched Uranium": {"buy": 500, "sell": 425},
            "Graphene Capacitors": {"buy": 300, "sell": 230}
        },
        "routes": {
            "Nyx": 6,
            "Barak": 8,
            "Azrael": 3
        }
    }
}


# ======================
# SHIP DATA
# ======================

ships = {
    "Ymir": {
        "cargo_capacity": 1,
        "max_fuel": 2000,
        "price": 0,
        "description": "A rugged, aging freighter issued to new pilots.\nBuilt from salvaged war-era hulls, the Ymir won’t impress anyone—but it will get you from system to system if you treat it right."
    },
    "Huldra": {
        "cargo_capacity": 2,
        "max_fuel": 3000,
        "price": 2200,
        "description": "A sleek civilian hauler favored by independent traders.\nEfficient, reliable, and built for those ready to start making real profit."
    },
    "Fafnir": {
        "cargo_capacity": 3,
        "max_fuel": 4000,
        "price": 6500,
        "description": "A heavily reinforced industrial freighter.\nDesigned for high-risk trade routes and serious merchants."
    },
    "Jotunn": {
        "cargo_capacity": 4,
        "max_fuel": 5000,
        "price": 12000,
        "description": "A massive deep-space carrier.\nMore than a ship—it’s a moving economy."
    }
}