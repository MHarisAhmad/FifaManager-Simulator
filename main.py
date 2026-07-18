import random
import time


injury_messages = [
    "Clutched ankle",
    "Pulled hamstring",
    "Twisted knee",
    "Muscle strain",
    "Calf strain",
    "Groin strain",
    "Sprained ankle",
    "Torn ligament",
    "Minor concussion",
    "Shoulder dislocation",
    "Back spasms",
    "Foot fracture",
    "Broken toe",
    "Thigh strain",
    "Hip injury",
    "Achilles tendon strain",
    "Shin injury",
    "Bruised ribs",
    "Neck strain",
    "Wrist fracture",
    "Dislocated finger",
    "Ankle ligament damage",
    "Knee ligament injury",
    "Quad strain",
    "Meniscus tear",
    "Hamstring tear",
    "Calf cramp",
    "Lower back injury",
    "Muscle fatigue",
    "Stress fracture",
    "Heel injury",
    "Toe ligament sprain",
    "Facial injury",
    "Broken nose",
    "Eye injury",
    "Chest injury",
    "Abdominal strain",
    "Adductor strain",
    "Patellar tendon injury",
    "ACL tear",
    "MCL sprain",
    "Cartilage damage",
    "Severe ankle sprain",
    "Torn calf muscle",
    "Pelvic injury",
    "Ligament strain",
    "Shin splints",
    "Knock to the head",
    "Heavy collision injury",
    "Overstretched muscle"
]

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
    your_stars = 5.0  
elif tier_choice == "2":
    raw_budget = random.randint(50000000, 90000000)
    budget = round(raw_budget, -5)  
    your_stars = 4.0
elif tier_choice == "3":
    raw_budget = random.randint(5000000, 15000000)
    budget = round(raw_budget, -4)  
    your_stars = 3.0
else:
    print("\n[System] Invalid choice! The board gave you a default standard budget.")
    budget = 30000000


# --- STEP 3: ANNOUNCEMENT ---
print("\n====================================")
print(f"Breaking News: {manager_name} has just been announced as the new manager of {club_name}!")
print(f"Board Expectation: You have been given a transfer budget of €{budget:,}")
print("====================================")
time.sleep(0.5)

league_table = {
    club_name:       {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "PTS": 0},
    "Real Madrid":   {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "PTS": 0},
    "Bayern Munich": {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "PTS": 0},
    "Arsenal":       {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "PTS": 0}
}

TOTAL_SEASON_MATCHES = 6

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
    print("5. View League Table Standings")
    print("6. Exit Game")
    
    choice = input("Select an option (1-6): ")

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


        opponent_tier = random.choice(["Elite", "Mid-Table", "Road to Glory"])
        
        if opponent_tier == "Elite":
            opponent_stars = random.choice([4.5, 5.0])
            opponent_name = random.choice(["Real Madrid", "Manchester City", "Arsenal", "Bayern Munich", "FC Barcelona"])
        elif opponent_tier == "Mid-Table":
            opponent_stars = random.choice([3.5, 4.0])
            opponent_name = random.choice(["Aston Villa", "AS Roma", "Newcastle United", "Villarreal"])
        else:
            opponent_stars = random.choice([1.5, 2.0, 2.5, 3.0])
            opponent_name = random.choice(["Wrexham AFC", "Como 1907", "St. Pauli", "Ipswich Town"])

        print(f"\n MATCH FIXTURE: {club_name} vs {opponent_name}")
        print(f" Your Team Rating: {'⭐' * int(your_stars)}{'✨' if your_stars % 1 != 0 else ''} ({your_stars} Stars)")
        print(f" Opponent Rating:  {'⭐' * int(opponent_stars)}{'✨' if opponent_stars % 1 != 0 else ''} ({opponent_stars} Stars)")

        
        # Capture the manager's match strategy choice
        match_choice = input("\nManager, what is your strategy? (1-2): ")
        
        if match_choice == "1":

            print("\n  Pre-match warmups ...")
            for player in squad:
                if player["Injury_Duration"] == 0:
                    pre_match_boost = random.randint(3, 7)
                    player["Energy"] += pre_match_boost
                
                # Apply the strict "No one is perfect" rule (Cap at 95%)
                    if player["Energy"] >= 98:
                        player["Energy"] = 97
            time.sleep(1.5)
            


            your_skill_score = ((your_stars * 20) * 0.6) + (avg_energy * 0.4)
            opponent_skill_score = ((opponent_stars * 20) * 0.6) + (opponent_energy * 0.4)

            if your_skill_score >= opponent_skill_score:
                favorite = f"{club_name}"
                underdog = opponent_name
            else:
                favorite = opponent_name
                underdog = f"{club_name}"
                
            # Keep this so our draw calculations use the new master skill score gap!
            skill_gap = your_skill_score - opponent_skill_score
                
            # Apply the 25% upset calculation with polished commentary strings
            upset_roll = random.random()
            player_goals = 0
            opponent_goals = 0
            is_upset = upset_roll < 0.25

            if random.random() < 0.07:
                player_goals = 0
                opponent_goals = 0

            elif abs(skill_gap) <= 5 and random.random() < 0.50:
                player_goals = random.randint(0, 2)
                opponent_goals = player_goals

            elif 5 < abs(skill_gap) <= 12 and random.random() < 0.35:
                player_goals = random.randint(0, 3)
                opponent_goals = player_goals
            

            else:
                if is_upset:
                    if underdog == club_name:
                        player_goals = random.randint(1, 3)
                        opponent_goals = random.randint(0, player_goals - 1)
                    else:
                        opponent_goals = random.randint(1, 3)
                        player_goals = random.randint(0, opponent_goals - 1)
                else:
                    # RARE SUPER BLOWOUT TRIGGER
                    # 10% chance to trigger a massive blowout if the skill gap favorability is huge
                    is_super_blowout = abs(skill_gap) >= 15 and random.random() < 0.10

                    if favorite == club_name:
                        if is_super_blowout:
                            player_goals = random.randint(5, 6)  # Rare massive victory
                        else:
                            player_goals = random.randint(1, 3)  # Normal favorite victory
                        opponent_goals = random.randint(0, max(0, player_goals - 2))
                    else:
                        if is_super_blowout:
                            opponent_goals = random.randint(5, 6)  # Rare massive defeat
                        else:
                            opponent_goals = random.randint(1, 3)  # Normal favorite defeat
                        player_goals = random.randint(0, max(0, opponent_goals - 2))

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
            
            print("\n KICK-OFF! ")
            print("------------------------------------")
            time.sleep(1)

            
            # We create a list of all minutes from 1 to 90
            match_timeline = list(range(1, 91))
            
            # Pick 3 random minutes during the game to show regular match action
            action_minutes = sorted(random.sample(match_timeline, 3))

            opponent_scorer_minutes = sorted([random.randint(1, 90) for _ in range(opponent_goals)])

            has_injury = random.random() < 0.15
            has_yellow = random.random() < 0.25
            has_red = random.random() < 0.05

            # Assign random minutes for these events if they triggered
            injury_minute = random.randint(1, 90) if has_injury else -1
            yellow_minute = random.randint(1, 90) if has_yellow else -1
            red_minute = random.randint(1, 90) if has_red else -1

            # Combine our goals and action minutes into a master timeline
            # We will use this loop to print events chronologically
            for minute in range(1, 91):

                for goal in player_scorer_names:
                    if goal["minute"] == minute:
                        print(f" \033[92m[{minute}'.]  GOAL!!! {goal['text']} \033[0m")
                        time.sleep(1.5)
                
                if minute in opponent_scorer_minutes:
                    
                    goals_this_minute = opponent_scorer_minutes.count(minute)
                    for _ in range(goals_this_minute):
                        print(f" \033[91m[{minute}'.]  GOAL FOR THE OPPONENT! \033[0m")
                        time.sleep(1.5) # Extra pause for dramatic tension!
                
                if minute == yellow_minute and len(healthy_players) > 0:
                    card_player = random.choice(healthy_players)
                    print(f" \033[93m[{minute}'.]  YELLOW CARD! {card_player['Name']} \033[0m")
                    time.sleep(1)

                # 4. RED CARDS
                if minute == red_minute and len(healthy_players) > 0:
                    card_player = random.choice(healthy_players)
                    print(f" \033[31m[{minute}'.]  RED CARD!! {card_player['Name']} is sent off the pitch!\033[0m")
                    time.sleep(1)

                # 5. INJURIES DURING PLAY
                if minute == injury_minute and len(healthy_players) > 0:
                    injured_p = random.choice(healthy_players)
                    duration = random.randint(1, 3)
                    
                    # Save both duration AND the random reason inside the player dictionary
                    injured_p["Injury_Duration"] = duration
                    injured_p["Injury_Reason"] = random.choice(injury_messages)
                    
                    print(f" \033[33m[{minute}'.] INJURY NEWS: {injured_p['Name']}: {injured_p['Injury_Reason']}. (Out for {duration} matches)\033[0m")
                    time.sleep(1.5)

            print("------------------------------------")
            print(" FULL TIME! ")
            time.sleep(1)

            if player_goals == opponent_goals:
                print(f"\n FULL TIME DRAW! {player_goals}-{opponent_goals}! ")
                print("1. Extra-time (30 mins)")
                print("2. Penalty Shootout")
                
                tiebreaker_choice = input("Manager, how do you want to settle this? (1-2): ").strip()

                # --- OPTION 1: EXTRA TIME SIMULATION ---
                if tiebreaker_choice == "1":
                    print(f"\n  EXTRA TIME! (30 Mins) ")
                    print("------------------------------------")
                    time.sleep(1.5)

                    player_et_goal = random.random() < 0.15
                    opponent_et_goal = random.random() < 0.15
                    et_card_minute = random.randint(91, 120) if random.random() < 0.20 else -1

                    p_et_minute = random.randint(91, 120) if player_et_goal else -1
                    o_et_minute = random.randint(91, 120) if opponent_et_goal else -1

                    for minute in range(91, 121):
                        if minute == p_et_minute:
                            player_goals += 1
                            scorer_text = random.choice(healthy_outfield_players)["Name"] if len(healthy_outfield_players) > 0 else "Striker"
                            print(f" \033[92m[{minute}'.]  EXTRA TIME GOAL!!! {scorer_text} breaks the deadlock!\033[0m")
                            time.sleep(1.5)

                        if minute == o_et_minute:
                            opponent_goals += 1
                            print(f" \033[91m[{minute}'.]  EXTRA TIME GOAL FOR {opponent_name}! They smash it in!\033[0m")
                            time.sleep(1.5)

                        if minute == et_card_minute and len(healthy_players) > 0:
                            card_p = random.choice(healthy_players)
                            print(f" \033[93m[{minute}'.]  YELLOW CARD! {card_p['Name']} commits an extra-time tactical foul.\033[0m")
                            time.sleep(1)

                    print("------------------------------------")
                    print(" END OF EXTRA TIME! ")
                    time.sleep(1)

                # --- OPTION 2: PENALTY SHOOTOUT STARTER (Placeholder) ---
                elif tiebreaker_choice == "2" or player_goals == opponent_goals:
                    print("\n PENALTY SHOOTOUT! ")
                    print("------------------------------------")
                    time.sleep(0.5)
                    print("--------------------------------------------------")
                    time.sleep(1.0)

                    p_pens_scored = 0
                    o_pens_scored = 0
                    round_num = 1

                    # Best of 5 rounds loop, continuing to sudden death if tied
                    while round_num <= 5 or p_pens_scored == o_pens_scored:
                        if round_num > 5:
                            print(f"\n  ROUND {round_num}! ")
                        else:
                            print(f"\n PENALTY ROUND {round_num} ")
                        
                        # 1. YOUR TEAM SHOTS
                        # Higher OVR outfield players have better conversion probabilities
                        if len(healthy_outfield_players) > 0:
                            penalty_taker = random.choice(healthy_outfield_players)
                            penalty_taker = random.choice(healthy_outfield_players)
                            taker_ovr = penalty_taker["OVR"]
                            
                            # Your exact tier logic converted to score probabilities:
                            if taker_ovr < 70:
                                score_chance = 0.55  # 45% chance to miss
                            elif 70 <= taker_ovr < 80:
                                score_chance = 0.70  # 30% chance to miss
                            elif 80 <= taker_ovr < 90:
                                score_chance = 0.85  # 15% chance to miss
                            else:
                                score_chance = 0.90  # 10% chance to miss
                        else:
                            score_chance = 0.70

                        print(f" Up to the spot: {penalty_taker['Name'] if len(healthy_outfield_players) > 0 else 'Your Player'}...")
                        time.sleep(1)

                        if random.random() < score_chance:
                            p_pens_scored += 1
                            print(f"  \033[92mSCORED! ({p_pens_scored} - {o_pens_scored})\033[0m")
                        else:
                            print(f"  \033[91mSAVED/MISSED! \033[0m")
                        time.sleep(1)

                        # Check if shootout is mathematically finished early during first 5 rounds
                        if round_num <= 5:
                            p_remaining_shots = 5 - round_num
                            o_remaining_shots = 5 - (round_num - 1)
                            if p_pens_scored > o_pens_scored + o_remaining_shots or o_pens_scored > p_pens_scored + p_remaining_shots:
                                break
                        opponent_taker_ovr = int(opponent_stars * 15) + random.randint(-5, 5)
                        if opponent_taker_ovr < 70:
                            opponent_score_chance = 0.55
                        elif 70 <= opponent_taker_ovr < 80:
                            opponent_score_chance = 0.70
                        elif 80 <= opponent_taker_ovr < 90:
                            opponent_score_chance = 0.85
                        else:
                            opponent_score_chance = 0.90

                        # 2. OPPONENT SHOTS
                        print(f" Up to the spot: {opponent_name}'s penalty taker...")
                        time.sleep(1)

                        # Opponent baseline conversion chance based on their team stars
                        opponent_score_chance = 0.65 + (opponent_stars * 0.03)
                        if random.random() < opponent_score_chance:
                            o_pens_scored += 1
                            print(f"  \033[91mSCORED FOR OPPONENT! ({p_pens_scored} - {o_pens_scored})\033[0m")
                        else:
                            print(f"  \033[92mSAVED BY YOUR KEEPER!!! \033[0m")
                        time.sleep(1)

                        # Check math conditions again after opponent shoots
                        if round_num <= 5:
                            o_remaining_shots = 5 - round_num
                            p_remaining_shots = 5 - round_num
                            if p_pens_scored > o_pens_scored + o_remaining_shots or o_pens_scored > p_pens_scored + p_remaining_shots:
                                break

                        round_num += 1

                    # Apply the definitive shootout outcome to the match score values
                    print("\n--------------------------------------------------")
                    print(f" SHOOTOUT COMPLETE! Final Penalties Score: {p_pens_scored} - {o_pens_scored} ")
                    print("--------------------------------------------------")
                    time.sleep(1.5)

                    if p_pens_scored > o_pens_scored:
                        player_goals += 1 # Gift the winner a technical +1 to secure the structural victory
                    else:
                        opponent_goals += 1
                    
                else:
                    print("\n[System] Invalid choice! Referee flips a coin and forces Extra Time.")
                    time.sleep(1)

            print("\n====================================")
            print(" MATCH REPORT | FULL-TIME PRESS")
            print("====================================")
            
            if player_goals > opponent_goals:
                if is_upset:
                    print(f"Match Winner: {club_name}")
                else:
                    print(f"Match Winner: {club_name}")
                
                if is_upset:
                    raw_bonus = random.randint(4000000, 7000000)
                    match_bonus = round(raw_bonus, -5)
                    print(f" BONUS! Earned: €{match_bonus:,}")
                else:
                    raw_bonus = random.randint(2500000, 4500000)
                    match_bonus = round(raw_bonus, -5)
                    print(f" VICTORY! Prize money added: €{match_bonus:,}")
                
                budget += match_bonus

            elif player_goals < opponent_goals:
                if is_upset:
                    print(f"Match Winner: The Opponent")
                else:
                    print(f"Match Winner: The Opponent")
                print(" Disappointing defeat. No prize money awarded. ")

            else:
                print(f"Match Draw!")
                draw_bonus = random.randint(500000, 1200000)
                budget += round(draw_bonus, -4)
                print(f" DRAW! Shared match prize money added: €{round(draw_bonus, -4):,}")

            print(f"Final Score: {club_name} {player_goals} - {opponent_goals} Opponent")
            print("------------------------------------")

            league_table[club_name]["P"] += 1

            if player_goals > opponent_goals:
                league_table[club_name]["W"] += 1
                league_table[club_name]["PTS"] += 3
                print(f"\n VICTORY! +3 Points added to your league tally.")
            elif player_goals == opponent_goals:
                league_table[club_name]["D"] += 1
                league_table[club_name]["PTS"] += 1
                print(f"\n DRAW! +1 Point added to your league tally.")
            else:
                league_table[club_name]["L"] += 1
                print(f"\n DEFEAT! 0 Points added.")
            
            league_table[club_name]["GF"] += player_goals       
            league_table[club_name]["GA"] += opponent_goals
              

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
            
            print("\n MATCH PERFORMANCE REPORT:")
            print("------------------------------------")
            for player in squad:
                if player["Injury_Duration"] > 0:
                    # Retrieve the exact reason saved during the match, default to 'Injured' if missing
                    reason = player.get("Injury_Reason", "Muscle strain")
                    print(f" -> {player['Name']}: Sidelined ({reason} - {player['Injury_Duration']} matches left)")
                else:
                    perf_score = (player["OVR"] * 0.6) + (player["Energy"] * 0.4)
                    print(f" -> {player['Name']}: Rating {round(perf_score, 1)}")
                        
            print("------------------------------------")
            time.sleep(2)

            ai_teams = [team for team in league_table.keys() if team != club_name]
            
            print("\n Simulating other league fixtures for this match week...")
            time.sleep(1)

            # Randomly shuffle the AI teams to determine matchups
            random.shuffle(ai_teams)
            
            # Team 1 plays Team 2
            t1, t2 = ai_teams[0], ai_teams[1]
            league_table[t1]["P"] += 1
            league_table[t2]["P"] += 1
            
            ai_roll = random.random()
            if ai_roll < 0.10: # Draw
                goals = random.randint(0, 3) # e.g., 0-0, 1-1, 2-2
                t1_goals, t2_goals = goals, goals
                
                league_table[t1]["D"] += 1; league_table[t1]["PTS"] += 1
                league_table[t2]["D"] += 1; league_table[t2]["PTS"] += 1
            elif ai_roll < 0.55: # Team 1 Wins
                t1_goals = random.randint(1, 4)
                t2_goals = random.randint(0, t1_goals - 1) # Assures t2 has fewer goals
                
                league_table[t1]["W"] += 1; league_table[t1]["PTS"] += 3
                league_table[t2]["L"] += 1
            else: # Team 2 Wins
                t2_goals = random.randint(1, 4)
                t1_goals = random.randint(0, t2_goals - 1) # Assures t1 has fewer goals
                
                league_table[t2]["W"] += 1; league_table[t2]["PTS"] += 3
                league_table[t1]["L"] += 1

            # Save the simulated goals to their GF and GA counters
            league_table[t1]["GF"] += t1_goals; league_table[t1]["GA"] += t2_goals
            league_table[t2]["GF"] += t2_goals; league_table[t2]["GA"] += t1_goals

            # Team 3 plays an unmanaged outside team (Wildcard match)
            t3 = ai_teams[2]
            league_table[t3]["P"] += 1
            wildcard_roll = random.random()
            
            if wildcard_roll < 0.10: # Draw
                goals = random.randint(0, 3)
                t3_goals, opp_goals = goals, goals
                league_table[t3]["D"] += 1; league_table[t3]["PTS"] += 1
            elif wildcard_roll < 0.55: # Win
                t3_goals = random.randint(1, 4)
                opp_goals = random.randint(0, t3_goals - 1)
                league_table[t3]["W"] += 1; league_table[t3]["PTS"] += 3
            else: # Loss
                opp_goals = random.randint(1, 4)
                t3_goals = random.randint(0, opp_goals - 1)
                league_table[t3]["L"] += 1

            # Save the simulated goals for Team 3
            league_table[t3]["GF"] += t3_goals
            league_table[t3]["GA"] += opp_goals

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
                
            print(" Energy recovered successfully! ")
            time.sleep(2)
        else:
            print("\n[System] Invalid choice, returning to hub.")
            time.sleep(1.5)
        
        
    
    elif choice == "5":
            print("\n=========================================================================")
            print("                       OFFICIAL LEAGUE STANDINGS                        ")
            print("=========================================================================")
            print(f" {'POS':<4} {'CLUB':<18} {'P':<4} {'W':<4} {'D':<4} {'L':<4} {'GF':<4} {'GA':<4} {'GD':<4} {'PTS':<5}")
            print("-------------------------------------------------------------------------")

            # Dynamic Sorting: Sorts primarily by PTS
            sorted_teams = sorted(league_table.items(), key=lambda item: item[1]["PTS"], reverse=True)

            pos = 1
            for team_name, stats in sorted_teams:
                # Calculate Goal Difference on the fly (GF - GA)
                goal_diff = stats["GF"] - stats["GA"]
                # Format GD to show a + sign for positive numbers (e.g., +3 or -2)
                gd_str = f"+{goal_diff}" if goal_diff > 0 else str(goal_diff)

                # Use a simple text pointer instead of an emoji
                display_name = f">> {team_name}" if team_name == club_name else team_name
                print(f" [{pos}]  {display_name:<18} {stats['P']:<4} {stats['W']:<4} {stats['D']:<4} {stats['L']:<4} {stats['GF']:<4} {stats['GA']:<4} {gd_str:<4} {stats['PTS']:<5}")
                pos += 1

            print("=========================================================================")
            
            # End of season report check
            current_week = league_table[club_name]["P"]
            print(f" Match Week: {current_week} / {TOTAL_SEASON_MATCHES}")
            
            if current_week >= TOTAL_SEASON_MATCHES:
                winner_team = sorted_teams[0][0]
                if winner_team == club_name:
                    print("\nTHE SEASON IS OVER! YOU ARE THE CHAMPIONS! CONGRATULATIONS!")
                else:
                    print(f"\nTHE SEASON IS OVER! {winner_team} has won the championship trophy.")
            else:
                print("Keep winning matches to climb to the top of the table!")

            input("\nPress Enter to return to the Main Hub...")
        
    elif choice == "6":
        print("\nSaving data...")
        time.sleep(1)
        print("Thanks for playing! Goodbye, Boss.")
        break  
        
    else:
        print("\n[System] Invalid choice, please choose a number between 1 and 5.")
        time.sleep(1.5)