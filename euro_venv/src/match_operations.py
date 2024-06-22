def display_matches(matches):
    try:
        for match in matches:
            print(f"{match['Date']}: {match['Team A']}: {match['Score A']} - {match['Score B']} {match['Team B']}")
    except KeyError as e:
        print(f"Error displaying matches: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error as occured: {e}")
    
def add_match(matches):
    try:
        team_a = input("Enter Team A: ")
        team_b = input("Enter Team B: ")
        score_a = int(input("Enter Score A: "))
        score_b = int(input("Enter Score B: "))
        date = input("Enter Date (YYYY-MM-DD)")
        
        match = {"Team A": team_a, "Team B": team_b, "Score A": score_a, "Score B": score_b, "Date": date}
        matches.append(match)
        print("Match Successfully added.")

    except ValueError:
        print("Error: Invalid input. Scores must be in integers.")
    except Exception as e:
        print(f"An unexpected error as occured: {e}")
        return []

def total_goals(matches):
    try:
        return sum(match['Score A'] + match['Score B'] for match in matches)
    except KeyError as e:
        print(f"Error calculating goals: Missing key {e}")
        return 0
    except TypeError:
        print("Error Calculating total goals, Invalid match data.")
    except Exception as e:
        print(f"An unexpected error as occured: {e}")
        return 0

def high_scoring_matches(matches, threshold):
    try:
        return [match for match in matches if match['Score A'] + match['Score B'] > threshold]
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []
