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

# --- STEP 5: THE MAIN MENU LOOP ---
while True:
    print(f"\n--- {club_name.upper()} MANAGER HUB ---")
    print(f"Current Budget: €{budget:,}")
    print("1. View Squad")
    print("2. Visit Transfer Market")
    print("3. Train Players")
    print("4. Play Match")
    print("5. Exit Game")
    
    choice = input("Select an option (1-5): ")

    if choice == "1":
        print("\n--- CURRENT SQUAD ---")
        for player in squad:
            print(f"[{player['Position']}] {player['Name']} - OVR: {player['OVR']} | Energy: {player['Energy']}%")
        print("==========================")
        input("\nPress Enter to return to the hub...")

    elif choice == "2":
        print("\n[System] Opening Transfer Market... (Coming soon!)")
        time.sleep(1.5)
        
    elif choice == "3":
        print("\n=== WELCOME TO THE TRAINING GROUND ===")
        for index, player in enumerate(squad):
            print(f"{index + 1}. [{player['Position']}] {player['Name']} (OVR: {player['OVR']}) | Energy: {player['Energy']}%")
        print("5. Back to Hub")

        # Asking the manager to select a player to train
        train_choice = input("Select a player to train (1-4) or go back (5): ")
        if train_choice in ["1", "2", "3", "4"]:
            # New Step: Convert string input to the correct list index integer
            player_index = int(train_choice) - 1
            selected_player = squad[player_index]
            print(f"\n Training {selected_player['Name']}...")
            time.sleep(1.5)
            
            # New Step: Generate a random boost and update the player's OVR key
            ovr_boost = random.uniform(0.1, 0.3)
            selected_player["OVR"] += ovr_boost
            selected_player["OVR"] = round(selected_player["OVR"], 1)

            energy_drain = random.randint(4, 8)
            selected_player["Energy"] -= energy_drain
            
            # Keep energy within valid bounds (0-100)
            if selected_player["Energy"] < 0:
                selected_player["Energy"] = 0

            print(f" Success! {selected_player['Name']} gained +{round(ovr_boost, 1)} OVR.  New OVR: {selected_player['OVR']}")

            print(f" Fitness Tax: {selected_player['Name']} lost -{energy_drain}% Energy (Current: {selected_player['Energy']}%).")
            print(" Reminder: Make sure to let your players rest to recover their fitness!")
            time.sleep(2)
        elif train_choice == "5":
            print("\nReturning to Manager Hub...")
            time.sleep(1)
        else:
            print("\n[System] Invalid choice, returning to hub.")
        time.sleep(1.5)
        
    elif choice == "4":
        print("\n=== UPCOMING MATCH WEEK ===")
        print("Officials have scheduled your next fixture.")
        print("1. Kick Off Match")
        print("2. Forfeit Match (Rest Squad completely)")
        
        # Capture the manager's match strategy choice
        match_choice = input("\nManager, what is your strategy? (1-2): ")
        
        if match_choice == "1":
            print("\n Analyzing squad fitness...")
            time.sleep(1)
            
            # New Step: Calculate the squad's total and average energy
            total_energy = sum(player["Energy"] for player in squad)
            avg_energy = total_energy / len(squad)
            
            # Print the result for the manager
            print(f" Team Average Energy: {round(avg_energy, 1)}%")

            # New Step: Generate a random average energy for the opponent team
            opponent_energy = random.randint(65, 95)
            print(f" Opponent Team Average Energy: {opponent_energy}%")
            
            print("\n Simulating match events... (Winner logic coming next!)")
            time.sleep(2)

            print("\n Post-Match Summary:")
            for player in squad:
                drain = random.randint(15, 25)
                player["Energy"] -= drain
                
                # Safety check to make sure energy doesn't drop below 0
                if player["Energy"] < 0:
                    player["Energy"] = 0
                    
                print(f" -> {player['Name']} ran hard and dropped to {player['Energy']}% energy.")
            time.sleep(2)

        elif match_choice == "2":
            # Generate a random goal deficit between 1 and 4
            goals_conceded = random.randint(1, 4)
            
            print(f"\n [Official] Club has submitted a forfeit for this fixture. Match scored as a 0-{goals_conceded} loss.")
            print(" The calendar advances.")
            print(" Your squad spent the week resting at the training ground...")
            time.sleep(2)
            
            # Micro-step addition: Running recovery calculation loop
            for player in squad:
                recovery = random.randint(15, 22)
                player["Energy"] = min(100, player["Energy"] + recovery)
                
            print(" Energy recovered successfully for the next fixture!")
            time.sleep(2)
        else:
            print("\n[System] Invalid choice, returning to hub.")
            time.sleep(1.5)
        
    elif choice == "5":
        print("\nSaving data...")
        time.sleep(1)
        print("Thanks for playing! Goodbye, Boss.")
        break  
        
    else:
        print("\n[System] Invalid choice, please choose a number between 1 and 5.")
        time.sleep(1.5)