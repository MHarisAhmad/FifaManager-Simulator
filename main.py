import random
import time

# --- STEP 1: WELCOME AND SETUP ---
print("====================================")
print("WELCOME TO THE FIFA MANAGER SIMULATOR")
print("====================================")

# Asking the user for their name and club
manager_name = input("Enter your name, Manager: ").title()
club_name = input("What club are you taking over? ").title()

# --- STEP 2: DYNAMIC BUDGET SYSTEM ---
print("\n--- CHOOSE YOUR CLUB'S BOARD EXPECTATIONS ---")
print("1. Elite Club (e.g., Real Madrid, Man City) - High Budget")
print("2. Mid-Table Club (e.g., Aston Villa, Roma) - Medium Budget")
print("3. Road to Glory (e.g., Wrexham, Leicester) - Low Budget")

tier_choice = input("Select your club's tier (1-3): ")

if tier_choice == "1":
    budget = random.randint(150000000, 250000000) 
elif tier_choice == "2":
    budget = random.randint(50000000, 90000000)
elif tier_choice == "3":
    budget = random.randint(5000000, 15000000)
else:
    print("\n[System] Invalid choice! The board gave you a default standard budget.")
    budget = 30000000


# --- STEP 3: ANNOUNCEMENT ---
print("\n====================================")
print(f"Breaking News: {manager_name} has just been announced as the new manager of {club_name}!")
print(f"Board Expectation: You have been given a transfer budget of €{budget:,}")
print("====================================")

# Using our time import to pause before the script finishes
time.sleep(2)

# --- STEP 4: YOUR STARTING SQUAD ---
# A list containing 4 dictionaries (one for each player)
squad = [
    {"Name": "Starter Keeper", "Position": "GK", "OVR": 72, "Energy": 100},
    {"Name": "Starter Defender", "Position": "CB", "OVR": 70,"Energy": 100},
    {"Name": "Starter Midfielder", "Position": "CM", "OVR": 71,"Energy": 100},
    {"Name": "Starter Striker", "Position": "ST", "OVR": 73,"Energy": 100}
]

print("\nLoading squad databases...")
time.sleep(1.5)

print("\n=== YOUR CURRENT SQUAD ===")
# We use a for loop to look at each individual player dictionary inside our squad list
for player in squad:
    print(f"[{player['Position']}] {player['Name']} - OVR: {player['OVR']} | Energy: {player['Energy']}%")
print("==========================")