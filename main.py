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
while True:
    print("\n--- CHOOSE YOUR CLUB'S BOARD EXPECTATIONS ---")
    print("1. Elite Club (e.g., Real Madrid, Man City) - High Budget")
    print("2. Mid-Table Club (e.g., Aston Villa, Roma) - Medium Budget")
    print("3. Road to Glory (e.g., Wrexham, Leicester) - Low Budget")
    print("4. View complete list of real-world clubs by category!")

    tier_choice = input("Select your club's tier (1-4): ").strip()
    if tier_choice == "4":
        print("\n=======================================================================")
        print("  OFFICIAL WORLD FOOTBALL CLUB TIERS (2026 Season Database) ")
        print("=======================================================================")
        
        print("\n ELITE CLUBS (High Budget | Expectation: Win Double/Treble)")
        print("-----------------------------------------------------------------------")
        print("  • Premier League:  Manchester City, Arsenal, Liverpool, Chelsea")
        print("  • La Liga:         Real Madrid, FC Barcelona, Atlético Madrid")
        print("  • Bundesliga:      Bayern Munich, Borussia Dortmund, Bayer Leverkusen")
        print("  • Serie A:         Inter Milan, Juventus, AC Milan")
        print("  • Ligue 1 & Other: Paris Saint-Germain, Sporting CP, Benfica")
        
        print("\n MID-TABLE CLUBS (Medium Budget | Expectation: European Qualification)")
        print("-----------------------------------------------------------------------")
        print("  • Premier League:  Aston Villa, Newcastle United, Tottenham, West Ham")
        print("  • La Liga:         Real Sociedad, Real Betis, Villarreal, Athletic Bilbao")
        print("  • Bundesliga:      RB Leipzig, Eintracht Frankfurt, VfB Stuttgart")
        print("  • Serie A:         AS Roma, Atalanta, SS Lazio, Fiorentina")
        print("  • Other Leagues:   Ajax, PSV Eindhoven, Lyon, Marseille")
        
        print("\n ROAD TO GLORY CLUBS (Low Budget | Expectation: Avoid Degradation/Rebuild)")
        print("-----------------------------------------------------------------------")
        print("  • England:         Wrexham AFC, Leicester City, Ipswich Town, Burnley")
        print("  • Spain:           RCD Espanyol, Real Valladolid, Leganés")
        print("  • Germany:         FC St. Pauli, Holstein Kiel, Schalke 04")
        print("  • Italy:           Como 1907, Parma, Venezia FC")
        print("  • Rest of World:   Inter Miami CF, Al-Nassr, Celtic FC, Rangers FC")
        
        print("=======================================================================")
        input("\nPress Enter to return to the selection menu...")
        continue
    elif tier_choice in ["1", "2", "3"]:
        
        break
    else:
        print(" Invalid selection. Please enter a number between 1 and 4.")

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
time.sleep(0.5)
energy_boost_used = False

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
        print("\n=== YOUR SQUAD ===")
        for player in squad:
            # Check if the player is sidelined to add a medical status flag
            status = " Healthy" if player["Injury_Duration"] == 0 else f" Sidelined ({player['Injury_Duration']} matches)"
            
            
            print(f" {player['Name']} ({player['Position']})")
            print(f"   OVR: {round(player['OVR'], 1)} | Energy: {player['Energy']}% | Status: {status}")
            print("-" * 30)

    elif choice == "2":
        print("\n[System] Opening Transfer Market... (Coming soon!)")
        time.sleep(1.5)
        
    elif choice == "3":
        print("\n=== TRAINING GROUND ===")
        print("Your coaches have prepared drills to improve player attributes.")
        print("WARNING: Intensive training drains player energy!")
        
        # [Your existing training loop code goes here—keep your exact OVR increases and energy drains!]
        print("\n Running training drills...")
        time.sleep(2)
        for player in squad:
            if player["Injury_Duration"] == 0:
                # Use random.uniform for the decimal growth
                ovr_gain = random.uniform(0.1, 0.3)
                energy_loss = random.randint(10, 15)
                
                # Force player["OVR"] to float() before adding to prevent the TypeError
                player["OVR"] = float(player["OVR"]) + ovr_gain
                player["Energy"] = max(0, player["Energy"] - energy_loss)
                
                print(f" {player['Name']} gained +{round(ovr_gain, 1)} OVR but lost -{energy_loss}% Energy.")
        
        print("\n Training session completed successfully.")
        time.sleep(1.5)
        
        # New Micro-Step: Post-Training Energy Boost Feature
        print("\n Gain one-time pre-match energy boost!")
        if energy_boost_used:
            print(" Not available! Try next time.")
        else:
            boost_choice = input("Use energy supplements (y/n): ").strip().lower()
            if boost_choice == 'y':
                print("\n Distributing energy supplements...")
                time.sleep(1)
                for player in squad:
                    if player["Injury_Duration"] == 0:
                        boost_amount = random.randint(8, 12)
                        player["Energy"] = min(100, player["Energy"] + boost_amount)
                        print(f" ->{player['Name']} recovered +{boost_amount}% energy.")
                
                energy_boost_used = True
                print(" Energy boost successfully applied!")
            else:
                print(" Boost available. You can still apply it later.")
        time.sleep(1.5)
        
    elif choice == "4":
        print("\n=== UPCOMING MATCH WEEK ===")
        print("Match fixtures scheduled by the officials\n")
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
            energy_boost_used = False

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