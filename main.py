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
    raw_budget = random.randint(150000000, 250000000) 
    budget = round(raw_budget, -6)  
elif tier_choice == "2":
    raw_budget = random.randint(50000000, 90000000)
    budget = round(raw_budget, -5)  
elif tier_choice == "3":
    raw_budget = random.randint(5000000, 15000000)
    budget = round(raw_budget, -4)  
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
matches_played_counter = 0
season_match_day = 0  

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
        time.sleep(0.3)
        input("\n  Press Enter to return to the main menu...")

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
                if player["Position"] == "GK":
                    energy_loss = random.randint(3, 6)
                else:
                    energy_loss = random.randint(8, 13)

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
            boost_choice = input(" Use energy supplements (y/n): ").strip().lower()
            if boost_choice == 'y':
                print("\n Distributing energy supplements...")
                time.sleep(1)
                for player in squad:
                    if player["Injury_Duration"] == 0:
                        # 1. Calculate the exact deficit up to 100%
                        energy_needed = 100 - player["Energy"]
                        # 2. Roll the potential boost amount
                        potential_boost = random.randint(10, 20)
                        # 3. The actual boost is the smaller of what they need vs what the supplement gives
                        actual_boost = min(energy_needed, potential_boost)
                        # 4. Apply the accurate boost to the player
                        player["Energy"] += actual_boost
                        print(f" ->{player['Name']} recovered +{actual_boost}% energy.")
                
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

        healthy_players = [p for p in squad if p["Injury_Duration"] == 0]
            
            # Safety check: If your whole team is somehow injured, default to 50%
        if len(healthy_players) > 0:
                total_energy = sum(player["Energy"] for player in healthy_players)
                avg_energy = total_energy / len(healthy_players)
        else:
                avg_energy = 50
                
        print(f"\n Your Team Average Energy: {round(avg_energy, 1)}%")
            
            # 2. Generate opponent energy
        if season_match_day == 0:
            opponent_energy = random.randint(96, 99)
        else:
            max_possible_energy = max(70, 100 - (season_match_day * 3))
            min_possible_energy = max(55, 85 - (season_match_day * 3))
            opponent_energy = random.randint(min_possible_energy, max_possible_energy)
                
        print(f" Opponent Team Average Energy: {opponent_energy}%")

        
        # Capture the manager's match strategy choice
        match_choice = input("\nManager, what is your strategy? (1-2): ")
        
        if match_choice == "1":

            print("\n  Squad completing pre-match warmups and physical therapy...")
            for player in squad:
                if player["Injury_Duration"] == 0:
                    pre_match_boost = random.randint(3, 7)
                    player["Energy"] += pre_match_boost
                
                # Apply the strict "No one is perfect" rule (Cap at 95%)
                    if player["Energy"] >= 98:
                        player["Energy"] = 97
            time.sleep(1.5)


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


            if avg_energy >= opponent_energy:
                favorite = f"{club_name}"
                underdog = "The Opponent"
            else:
                favorite = "The Opponent"
                underdog = f"{club_name}"
                
            # Apply the 25% upset calculation with polished commentary strings
            upset_roll = random.random()

            player_goals = 0
            opponent_goals = 0

            

            if upset_roll < 0.25:

                if underdog == club_name:
                    player_goals = random.randint(1, 3)
                    opponent_goals = random.randint(0, player_goals - 1)
                else:
                    opponent_goals = random.randint(1, 3)
                    player_goals = random.randint(0, opponent_goals - 1)

                print("\n====================================")
                print(" MATCH REPORT | FULL-TIME PRESS")
                print("====================================")
                print(f"\nFT: Against all odds, a masterclass in tactical grit wins it!")
                print(f"Match Winner: {underdog}")
                print(f"Final Score: {club_name} {player_goals} - {opponent_goals} Opponent")
                print("------------------------------------")
                # Dynamic Budget Reward for Upset Win
                if underdog == club_name:
                    # You were the underdog and you pulled off a massive upset! Extra bonus!
                    raw_bonus = random.randint(4000000, 7000000)
                    match_bonus = round(raw_bonus, -5)
                    budget += match_bonus
                    print(f" UPSET BONUS! The board is ecstatic! Earned: €{match_bonus:,}")
                else:
                    print(" Disappointing defeat. No prize money awarded by the sponsors.")
            else:
                print("\n====================================")
                print(" MATCH REPORT | FULL-TIME PRESS")
                print("====================================")
                print(f"\nFT: A dominant, high-energy performance delivers a clean victory.")
                print(f"Match Winner: {favorite}")
                print("------------------------------------")
                if favorite == club_name:
                    if favorite == club_name:
                        player_goals = random.randint(1, 4)
                        opponent_goals = random.randint(0, player_goals - 1)
                    else:
                        opponent_goals = random.randint(1, 4)
                        player_goals = random.randint(0, opponent_goals - 1)

                    # You were expected to win and you delivered. Standard bonus.
                    raw_bonus = random.randint(2500000, 4500000)
                    match_bonus = round(raw_bonus, -5)
                    budget += match_bonus
                    print(f" VICTORY! Match performance prize money added: €{match_bonus:,}")
                    print(f"Final Score: {club_name} {player_goals} - {opponent_goals} Opponent")
                else:
                    print(" DEFEAT! You lost to the stronger team. No match day prize money.")
            energy_boost_used = False

            player_scorer_names = []
            healthy_outfield_players = [p for p in squad if p["Injury_Duration"] == 0 and p["Position"] != "GK"]
            if len(healthy_outfield_players) > 0 and player_goals > 0:
                
                for _ in range(player_goals):
                    position_weights = []
                    for p in healthy_outfield_players:
                        if p["Position"] == "ST":
                            position_weights.append(65)  # 65% chance for clinical strikers
                        elif p["Position"] == "CM":
                            position_weights.append(25)  # 25% chance for midfielders
                        else:
                            position_weights.append(10)
                    # Pick 1 random player using our custom percentage weights
                    chosen_scorer = random.choices(healthy_outfield_players, weights=position_weights, k=1)[0]
                    goal_minute = random.randint(1, 90)
                    goal_data = {
                        "minute": goal_minute,
                        "text": f"{chosen_scorer['Name']} ({chosen_scorer['Position']})"
                    }
                    # Save their name to our scorer list
                    player_scorer_names.append(goal_data)
            
            player_scorer_names.sort(key=lambda x: x["minute"])
            
            print("\n REFEREE BLOWS THE WHISTLE! KICK-OFF! ")
            print("------------------------------------")
            time.sleep(1)

            # Define some realistic non-goal football events for atmosphere
            match_events = [
                "intercepts a dangerous pass in the midfield!",
                "lofts a beautiful cross into the box, but the keeper punches it clear.",
                "attempts a long-range shot! It goes just wide of the post.",
                "makes a brilliant sliding tackle to break up the opponent's counter-attack.",
                "dribbles past two defenders but loses control near the touchline.",
                "is caught offside by the referee's assistant."
            ]

            # We create a list of all minutes from 1 to 90
            match_timeline = list(range(1, 91))
            
            # Pick 3 random minutes during the game to show regular match action
            action_minutes = sorted(random.sample(match_timeline, 3))

            # Combine our goals and action minutes into a master timeline
            # We will use this loop to print events chronologically
            for minute in range(1, 91):

                for goal in player_scorer_names:
                    if goal["minute"] == minute:
                        print(f" \033[92m[{minute}'.]  GOAL!!! {goal['text']} finds the back of the net! The crowd goes wild!\033[0m")
                        time.sleep(1.5)
                
                # Check if a goal was scored by your team in this exact minute
                # (We will link your actual player_scorer_names here in the next step!)
                
                # Check if it's a regular action minute to show game buildup
                if minute in action_minutes:
                    random_player = random.choice(healthy_players)
                    random_phrase = random.choice(match_events)
                    print(f" [{minute}'.] {random_player['Name']} {random_phrase}")
                    time.sleep(1.2) # Dramatic pause between commentary lines

            print("------------------------------------")
            print(" CODE 90: Referee blows the final whistle! ")
            time.sleep(1)

            

            print("\n MATCH EVENTS:")
            print("------------------------------------")
              

            print("\n Post-Match Summary:")
            for player in squad:
                if player["Injury_Duration"] > 0:
                    # 1.Reduce their injury countdown by 1 match week
                    player["Injury_Duration"] -= 1

                    # 2. NEW: Give them +20% energy because they rested this week!
                    injured_recovery = 20
                    player["Energy"] = min(97, player["Energy"] + injured_recovery)

                    if player["Injury_Duration"] == 0:
                        print(f" -> {player['Name']} has fully recovered, gained +{injured_recovery}% energy, and returned.(Energy: {player['Energy']}%)")
                    else:
                        print(f" -> {player['Name']} spent the week resting. Recovered +{injured_recovery}% energy. (Current: {player['Energy']}% | Matches left: {player['Injury_Duration']})")
                else:
                    # Healthy players drain energy
                    if player["Position"] == "GK":
                        drain = random.randint(4, 8)
                    else:
                        drain = random.randint(15, 25)
                    player["Energy"] -= drain
                    if player["Energy"] < 0:
                        player["Energy"] = 0
                    print(f" -> {player['Name']} ran hard and dropped to {player['Energy']}% energy.")

            # --- NEW AUTOMATIC ENGINE BALANCING FEATURE ---
            # 1. Advance our global match counter
            matches_played_counter += 1
            season_match_day += 1
            
            # 2. Randomly decide if recovery triggers after 2 or 3 matches
            # We pick a random target threshold (either 2 or 3)
            recovery_threshold = random.randint(1, 3)
            
            if matches_played_counter >= recovery_threshold:
                print("\n========================================================")
                print(" AUTOMATIC TEAM ALERT: Rest and recovery energy boost added!")
                print("========================================================")
                time.sleep(1)
                
                for player in squad:
                    if player["Injury_Duration"] == 0:
                        recovery_bonus = random.randint(15, 20)
                        # Cap it safely at 100% using our min() function
                        player["Energy"] = min(100, player["Energy"] + recovery_bonus)
                        print(f" -> {player['Name']} rested up and recovered +{recovery_bonus}% energy (Current: {player['Energy']}%).")
                
                print("========================================================")
                # 3. Reset the counter back to 0 so the cycle starts over
                matches_played_counter = 0
                    
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