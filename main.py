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
    {"Name": "Starter Keeper", "Position": "GK", "OVR": 72, "Energy": 100,"Injury_Duration": 0},
    {"Name": "Starter Defender", "Position": "CB", "OVR": 70,"Energy": 100,"Injury_Duration": 0},
    {"Name": "Starter Midfielder", "Position": "CM", "OVR": 71,"Energy": 100,"Injury_Duration": 0},
    {"Name": "Starter Striker", "Position": "ST", "OVR": 73,"Energy": 100,"Injury_Duration": 0}
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

            print("  Squad completing pre-match warmups and physical therapy...")
            for player in squad:
                if player["Injury_Duration"] == 0:
                    pre_match_boost = random.randint(3, 7)
                    player["Energy"] += pre_match_boost
                
                # Apply the strict "No one is perfect" rule (Cap at 95%)
                    if player["Energy"] >= 98:
                        player["Energy"] = 97
            time.sleep(1.5)


            healthy_players = [p for p in squad if p["Injury_Duration"] == 0]
            
            # Safety check: If your whole team is somehow injured, default to 50%
            if len(healthy_players) > 0:
                total_energy = sum(player["Energy"] for player in healthy_players)
                avg_energy = total_energy / len(healthy_players)
            else:
                avg_energy = 50
                
            print(f"\n Your Team Average Energy: {round(avg_energy, 1)}%")
            
            # 2. Generate opponent energy
            opponent_energy = random.randint(65, 95)
            print(f" Opponent Team Average Energy: {opponent_energy}%")

            # New Micro-Step: Calculate individual player performance scores
            print("\n MATCH DAY INDIVIDUAL PERFORMANCE REPORT:")
            print("------------------------------------")
            for player in squad:
                if player["Injury_Duration"] > 0:
                    print(f" ->  {player['Name']} ({player['Position']}) | Sidelined (Injured for {player['Injury_Duration']} more matches)")
                else:
                    # Healthy player calculations
                    perf_score = (player["OVR"] * 0.6) + (player["Energy"] * 0.4)
                    print(f" -> {player['Name']} ({player['Position']}) | Match Performance: {round(perf_score, 1)}")
                    
                    # Injury risk check for fatigued players
                    if player["Energy"] < 70:
                        if random.random() < 0.15:
                            # Roll random duration between 3 and 6 matches
                            duration = random.randint(3, 6)
                            player["Injury_Duration"] = duration
                            print(f"    CRITICAL MEDICAL ALERT: {player['Name']} suffered a severe injury during the match!")
                            print(f"    [Status: Out of action for the next {duration} matches]")
                        
            print("------------------------------------")
            time.sleep(2)
            
            print("\n Simulating match events...")
            time.sleep(2)

            if avg_energy >= opponent_energy:
                favorite = f"{club_name}"
                underdog = "The Opponent"
            else:
                favorite = "The Opponent"
                underdog = f"{club_name}"
                
            # Apply the 25% upset calculation with polished commentary strings
            upset_roll = random.random()

            if upset_roll < 0.25:
                print("\n====================================")
                print(" MATCH REPORT | FULL-TIME PRESS")
                print("====================================")
                print(f"FT: Against all odds, a masterclass in tactical grit wins it!")
                print(f"Match Winner: {underdog}")
                print("------------------------------------")
            else:
                print("\n====================================")
                print(" MATCH REPORT | FULL-TIME PRESS")
                print("====================================")
                print(f"FT: A dominant, high-energy performance delivers a clean victory.")
                print(f"Match Winner: {favorite}")
                print("------------------------------------")

            print("\n Post-Match Summary:")
            for player in squad:
                if player["Injury_Duration"] > 0:
                    # Reduce their injury countdown by 1 match week
                    player["Injury_Duration"] -= 1
                    if player["Injury_Duration"] == 0:
                        print(f" -> {player['Name']} has fully recovered and returned to light training!")
                else:
                    # Healthy players drain energy
                    drain = random.randint(15, 25)
                    player["Energy"] -= drain
                    if player["Energy"] < 0:
                        player["Energy"] = 0
                    print(f" -> {player['Name']} ran hard and dropped to {player['Energy']}% energy.")
                    
            time.sleep(3)

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