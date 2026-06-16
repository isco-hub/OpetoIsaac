import random
import time

teams_data = {
    "Mexico":       {"goat":0,"last_wc":22,"cont_cups":12,"fifa_rank":14,"strength":81.2,"form":10,"injuries":1,"coach":18,"fan":5,"epl":2,"laliga":3,"seriea":1,"bundes":0,"ligue1":1,"other":19,"age":27.3,"wc_exp":9,"keeper":79,"defender":80,"midfielder":82,"forward":79},
    "South Korea":  {"goat":0,"last_wc":16,"cont_cups":2,"fifa_rank":25,"strength":79.8,"form":13,"injuries":0,"coach":21,"fan":4,"epl":3,"laliga":0,"seriea":0,"bundes":3,"ligue1":1,"other":19,"age":26.9,"wc_exp":11,"keeper":76,"defender":82,"midfielder":84,"forward":85},
    "Czech Rep.":   {"goat":0,"last_wc":0,"cont_cups":1,"fifa_rank":40,"strength":76.5,"form":10,"injuries":2,"coach":29,"fan":3,"epl":3,"laliga":0,"seriea":2,"bundes":6,"ligue1":0,"other":15,"age":26.4,"wc_exp":0,"keeper":81,"defender":77,"midfielder":79,"forward":81},
    "South Africa": {"goat":0,"last_wc":0,"cont_cups":1,"fifa_rank":60,"strength":71.0,"form":8,"injuries":1,"coach":38,"fan":4,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":1,"other":25,"age":27.8,"wc_exp":0,"keeper":80,"defender":70,"midfielder":72,"forward":71},
    "Switzerland":  {"goat":0,"last_wc":12,"cont_cups":0,"fifa_rank":19,"strength":85.5,"form":8,"injuries":1,"coach":14,"fan":3,"epl":4,"laliga":1,"seriea":3,"bundes":8,"ligue1":2,"other":8,"age":28.1,"wc_exp":15,"keeper":87,"defender":84,"midfielder":85,"forward":79},
    "Canada":       {"goat":0,"last_wc":31,"cont_cups":2,"fifa_rank":38,"strength":80.4,"form":8,"injuries":0,"coach":22,"fan":4,"epl":1,"laliga":1,"seriea":1,"bundes":1,"ligue1":1,"other":21,"age":26.5,"wc_exp":12,"keeper":77,"defender":81,"midfielder":78,"forward":83},
    "Qatar":        {"goat":0,"last_wc":32,"cont_cups":2,"fifa_rank":34,"strength":75.8,"form":10,"injuries":2,"coach":31,"fan":4,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":0,"other":26,"age":27.9,"wc_exp":14,"keeper":74,"defender":75,"midfielder":76,"forward":78},
    "Bosnia":       {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":72,"strength":72.1,"form":5,"injuries":1,"coach":42,"fan":3,"epl":0,"laliga":0,"seriea":2,"bundes":3,"ligue1":0,"other":21,"age":26.8,"wc_exp":0,"keeper":75,"defender":72,"midfielder":74,"forward":73},
    "Scotland":     {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":39,"strength":78.4,"form":10,"injuries":1,"coach":25,"fan":5,"epl":6,"laliga":0,"seriea":3,"bundes":0,"ligue1":0,"other":17,"age":27.2,"wc_exp":0,"keeper":77,"defender":82,"midfielder":83,"forward":75},
    "Morocco":      {"goat":0,"last_wc":4,"cont_cups":1,"fifa_rank":13,"strength":88.5,"form":11,"injuries":0,"coach":11,"fan":4,"epl":3,"laliga":2,"seriea":2,"bundes":1,"ligue1":3,"other":15,"age":25.8,"wc_exp":9,"keeper":85,"defender":86,"midfielder":84,"forward":83},
    "Brazil":       {"goat":0,"last_wc":7,"cont_cups":9,"fifa_rank":5,"strength":93.2,"form":11,"injuries":2,"coach":5,"fan":5,"epl":9,"laliga":5,"seriea":2,"bundes":1,"ligue1":2,"other":7,"age":26.4,"wc_exp":14,"keeper":89,"defender":90,"midfielder":89,"forward":94},
    "Haiti":        {"goat":0,"last_wc":0,"cont_cups":1,"fifa_rank":86,"strength":66.8,"form":5,"injuries":1,"coach":45,"fan":3,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":2,"other":24,"age":26.1,"wc_exp":0,"keeper":68,"defender":66,"midfielder":69,"forward":71},
    "USA":          {"goat":0,"last_wc":14,"cont_cups":10,"fifa_rank":17,"strength":86.4,"form":10,"injuries":1,"coach":16,"fan":5,"epl":5,"laliga":2,"seriea":3,"bundes":2,"ligue1":1,"other":13,"age":25.4,"wc_exp":13,"keeper":80,"defender":82,"midfielder":84,"forward":86},
    "Australia":    {"goat":0,"last_wc":11,"cont_cups":1,"fifa_rank":27,"strength":80.1,"form":10,"injuries":0,"coach":23,"fan":4,"epl":1,"laliga":0,"seriea":1,"bundes":2,"ligue1":1,"other":21,"age":27.4,"wc_exp":10,"keeper":82,"defender":79,"midfielder":78,"forward":77},
    "Türkiye":      {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":22,"strength":83.7,"form":10,"injuries":2,"coach":15,"fan":5,"epl":2,"laliga":1,"seriea":3,"bundes":2,"ligue1":0,"other":18,"age":26.1,"wc_exp":0,"keeper":81,"defender":82,"midfielder":86,"forward":80},
    "Paraguay":     {"goat":0,"last_wc":0,"cont_cups":2,"fifa_rank":41,"strength":75.2,"form":7,"injuries":1,"coach":32,"fan":3,"epl":2,"laliga":1,"seriea":1,"bundes":0,"ligue1":0,"other":22,"age":27.9,"wc_exp":0,"keeper":74,"defender":77,"midfielder":76,"forward":78},
    "Germany":      {"goat":0,"last_wc":17,"cont_cups":4,"fifa_rank":11,"strength":92.8,"form":13,"injuries":1,"coach":6,"fan":4,"epl":3,"laliga":2,"seriea":1,"bundes":19,"ligue1":0,"other":1,"age":26.8,"wc_exp":11,"keeper":88,"defender":89,"midfielder":93,"forward":88},
    "Ivory Coast":  {"goat":0,"last_wc":0,"cont_cups":3,"fifa_rank":31,"strength":82.4,"form":10,"injuries":0,"coach":19,"fan":5,"epl":4,"laliga":1,"seriea":3,"bundes":2,"ligue1":5,"other":11,"age":26.2,"wc_exp":0,"keeper":76,"defender":83,"midfielder":81,"forward":82},
    "Ecuador":      {"goat":0,"last_wc":18,"cont_cups":0,"fifa_rank":29,"strength":81.6,"form":10,"injuries":1,"coach":20,"fan":4,"epl":3,"laliga":0,"seriea":0,"bundes":1,"ligue1":1,"other":21,"age":25.1,"wc_exp":13,"keeper":78,"defender":84,"midfielder":82,"forward":77},
    "Curaçao":      {"goat":0,"last_wc":0,"cont_cups":2,"fifa_rank":84,"strength":64.5,"form":7,"injuries":2,"coach":46,"fan":3,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":0,"other":26,"age":28.3,"wc_exp":0,"keeper":72,"defender":65,"midfielder":66,"forward":68},
    "Sweden":       {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":28,"strength":84.8,"form":10,"injuries":0,"coach":17,"fan":4,"epl":4,"laliga":1,"seriea":2,"bundes":2,"ligue1":1,"other":16,"age":26.3,"wc_exp":4,"keeper":79,"defender":82,"midfielder":83,"forward":89},
    "Japan":        {"goat":0,"last_wc":9,"cont_cups":4,"fifa_rank":15,"strength":87.2,"form":11,"injuries":1,"coach":12,"fan":5,"epl":3,"laliga":1,"seriea":0,"bundes":5,"ligue1":2,"other":15,"age":26.6,"wc_exp":15,"keeper":78,"defender":85,"midfielder":88,"forward":83},
    "Netherlands":  {"goat":0,"last_wc":5,"cont_cups":1,"fifa_rank":7,"strength":91.5,"form":8,"injuries":2,"coach":9,"fan":5,"epl":7,"laliga":2,"seriea":4,"bundes":3,"ligue1":1,"other":9,"age":27.1,"wc_exp":14,"keeper":82,"defender":93,"midfielder":88,"forward":86},
    "Tunisia":      {"goat":0,"last_wc":21,"cont_cups":1,"fifa_rank":43,"strength":73.4,"form":8,"injuries":1,"coach":33,"fan":4,"epl":0,"laliga":0,"seriea":1,"bundes":1,"ligue1":4,"other":20,"age":27.5,"wc_exp":8,"keeper":73,"defender":74,"midfielder":76,"forward":72},
    "Belgium":      {"goat":0,"last_wc":23,"cont_cups":0,"fifa_rank":9,"strength":89.9,"form":13,"injuries":1,"coach":10,"fan":4,"epl":6,"laliga":1,"seriea":3,"bundes":4,"ligue1":1,"other":11,"age":26.9,"wc_exp":10,"keeper":91,"defender":82,"midfielder":90,"forward":87},
    "Egypt":        {"goat":0,"last_wc":0,"cont_cups":7,"fifa_rank":29,"strength":81.4,"form":10,"injuries":0,"coach":22,"fan":5,"epl":1,"laliga":0,"seriea":0,"bundes":1,"ligue1":2,"other":22,"age":27.4,"wc_exp":4,"keeper":78,"defender":77,"midfielder":79,"forward":86},
    "Iran":         {"goat":0,"last_wc":26,"cont_cups":3,"fifa_rank":20,"strength":78.5,"form":13,"injuries":1,"coach":26,"fan":4,"epl":1,"laliga":0,"seriea":1,"bundes":0,"ligue1":0,"other":24,"age":28.5,"wc_exp":12,"keeper":76,"defender":75,"midfielder":78,"forward":82},
    "New Zealand":  {"goat":0,"last_wc":0,"cont_cups":5,"fifa_rank":85,"strength":67.2,"form":8,"injuries":0,"coach":43,"fan":3,"epl":1,"laliga":0,"seriea":0,"bundes":0,"ligue1":0,"other":25,"age":25.8,"wc_exp":1,"keeper":71,"defender":70,"midfielder":68,"forward":74},
    "Spain":        {"goat":0,"last_wc":13,"cont_cups":5,"fifa_rank":3,"strength":95.2,"form":13,"injuries":1,"coach":3,"fan":4,"epl":4,"laliga":18,"seriea":1,"bundes":1,"ligue1":1,"other":1,"age":25.7,"wc_exp":10,"keeper":86,"defender":91,"midfielder":96,"forward":92},
    "Cabo Verde":   {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":63,"strength":72.8,"form":8,"injuries":0,"coach":35,"fan":3,"epl":0,"laliga":1,"seriea":1,"bundes":0,"ligue1":3,"other":21,"age":27.4,"wc_exp":0,"keeper":72,"defender":73,"midfielder":71,"forward":74},
    "Saudi Arabia": {"goat":0,"last_wc":25,"cont_cups":3,"fifa_rank":56,"strength":76.2,"form":10,"injuries":2,"coach":27,"fan":5,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":0,"other":26,"age":27.9,"wc_exp":14,"keeper":75,"defender":76,"midfielder":75,"forward":74},
    "Uruguay":      {"goat":0,"last_wc":20,"cont_cups":17,"fifa_rank":12,"strength":90.5,"form":10,"injuries":1,"coach":4,"fan":4,"epl":2,"laliga":3,"seriea":2,"bundes":0,"ligue1":1,"other":18,"age":26.1,"wc_exp":11,"keeper":81,"defender":88,"midfielder":91,"forward":87},
    "France":       {"goat":0,"last_wc":2,"cont_cups":4,"fifa_rank":2,"strength":95.8,"form":12,"injuries":1,"coach":1,"fan":4,"epl":6,"laliga":5,"seriea":4,"bundes":3,"ligue1":7,"other":1,"age":26.4,"wc_exp":15,"keeper":87,"defender":94,"midfielder":90,"forward":96},
    "Senegal":      {"goat":0,"last_wc":10,"cont_cups":1,"fifa_rank":18,"strength":84.2,"form":10,"injuries":0,"coach":13,"fan":5,"epl":4,"laliga":1,"seriea":2,"bundes":1,"ligue1":6,"other":12,"age":27.2,"wc_exp":13,"keeper":82,"defender":83,"midfielder":81,"forward":84},
    "Iraq":         {"goat":0,"last_wc":0,"cont_cups":1,"fifa_rank":55,"strength":74.0,"form":10,"injuries":1,"coach":30,"fan":4,"epl":1,"laliga":0,"seriea":0,"bundes":0,"ligue1":0,"other":25,"age":25.9,"wc_exp":0,"keeper":73,"defender":72,"midfielder":75,"forward":76},
    "Norway":       {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":24,"strength":86.1,"form":10,"injuries":1,"coach":21,"fan":3,"epl":3,"laliga":2,"seriea":1,"bundes":2,"ligue1":0,"other":18,"age":25.6,"wc_exp":0,"keeper":75,"defender":79,"midfielder":89,"forward":95},
    "Argentina":    {"goat":1,"last_wc":1,"cont_cups":16,"fifa_rank":1,"strength":96.2,"form":13,"injuries":1,"coach":2,"fan":5,"epl":6,"laliga":5,"seriea":4,"bundes":1,"ligue1":1,"other":9,"age":28.2,"wc_exp":16,"keeper":89,"defender":90,"midfielder":92,"forward":95},
    "Algeria":      {"goat":0,"last_wc":0,"cont_cups":2,"fifa_rank":44,"strength":80.5,"form":10,"injuries":0,"coach":24,"fan":5,"epl":1,"laliga":0,"seriea":3,"bundes":1,"ligue1":5,"other":16,"age":27.1,"wc_exp":2,"keeper":76,"defender":79,"midfielder":82,"forward":80},
    "Austria":      {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":23,"strength":85.4,"form":10,"injuries":2,"coach":12,"fan":4,"epl":1,"laliga":1,"seriea":2,"bundes":16,"ligue1":1,"other":5,"age":26.5,"wc_exp":0,"keeper":80,"defender":84,"midfielder":86,"forward":79},
    "Jordan":       {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":68,"strength":70.8,"form":7,"injuries":1,"coach":37,"fan":4,"epl":0,"laliga":1,"seriea":0,"bundes":0,"ligue1":0,"other":25,"age":26.2,"wc_exp":0,"keeper":71,"defender":69,"midfielder":71,"forward":76},
    "Portugal":     {"goat":1,"last_wc":8,"cont_cups":2,"fifa_rank":6,"strength":94.6,"form":13,"injuries":1,"coach":7,"fan":4,"epl":8,"laliga":2,"seriea":2,"bundes":1,"ligue1":4,"other":9,"age":26.9,"wc_exp":13,"keeper":86,"defender":91,"midfielder":94,"forward":92},
    "DR Congo":     {"goat":0,"last_wc":0,"cont_cups":2,"fifa_rank":61,"strength":76.5,"form":8,"injuries":0,"coach":28,"fan":5,"epl":2,"laliga":0,"seriea":0,"bundes":0,"ligue1":6,"other":18,"age":26.4,"wc_exp":0,"keeper":75,"defender":76,"midfielder":77,"forward":80},
    "Uzbekistan":   {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":62,"strength":74.2,"form":13,"injuries":1,"coach":31,"fan":4,"epl":0,"laliga":0,"seriea":1,"bundes":0,"ligue1":2,"other":23,"age":25.5,"wc_exp":0,"keeper":72,"defender":75,"midfielder":74,"forward":77},
    "Colombia":     {"goat":0,"last_wc":0,"cont_cups":1,"fifa_rank":12,"strength":89.8,"form":10,"injuries":1,"coach":9,"fan":5,"epl":4,"laliga":2,"seriea":1,"bundes":0,"ligue1":0,"other":19,"age":26.8,"wc_exp":8,"keeper":80,"defender":85,"midfielder":87,"forward":90},
    "England":      {"goat":0,"last_wc":6,"cont_cups":1,"fifa_rank":4,"strength":94.8,"form":13,"injuries":2,"coach":5,"fan":5,"epl":23,"laliga":1,"seriea":0,"bundes":1,"ligue1":1,"other":0,"age":26.1,"wc_exp":14,"keeper":83,"defender":91,"midfielder":95,"forward":96},
    "Croatia":      {"goat":0,"last_wc":3,"cont_cups":0,"fifa_rank":10,"strength":88.2,"form":10,"injuries":1,"coach":8,"fan":4,"epl":2,"laliga":1,"seriea":3,"bundes":4,"ligue1":0,"other":16,"age":28.4,"wc_exp":15,"keeper":84,"defender":86,"midfielder":89,"forward":80},
    "Ghana":        {"goat":0,"last_wc":24,"cont_cups":4,"fifa_rank":58,"strength":78.6,"form":10,"injuries":1,"coach":25,"fan":4,"epl":4,"laliga":2,"seriea":0,"bundes":0,"ligue1":3,"other":17,"age":24.9,"wc_exp":9,"keeper":74,"defender":78,"midfielder":82,"forward":81},
    "Panama":       {"goat":0,"last_wc":0,"cont_cups":0,"fifa_rank":42,"strength":74.5,"form":7,"injuries":0,"coach":29,"fan":3,"epl":0,"laliga":0,"seriea":0,"bundes":0,"ligue1":1,"other":25,"age":27.2,"wc_exp":2,"keeper":77,"defender":73,"midfielder":74,"forward":72},
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def print_separator(char="=", length=60):
    print(char * length)


def get_effective_strength(team):
    d = teams_data[team]
    base = d["strength"]
    form_bonus = (d["form"] - 5) * 1.5
    injury_penalty = d["injuries"] * 3.0
    coach_bonus = (d["coach"] - 25) * 0.2
    goat_bonus = 3.0 if d["goat"] else 0
    positional_avg = (d["keeper"] + d["defender"] + d["midfielder"] + d["forward"]) / 4
    pos_bonus = (positional_avg - 75) * 0.3
    return base + form_bonus - injury_penalty + coach_bonus + goat_bonus + pos_bonus


def simulate_match(team_a, team_b):
    a_str = get_effective_strength(team_a)
    b_str = get_effective_strength(team_b)
    total = a_str + b_str
    a_score, b_score = 0, 0
    for _ in range(random.randint(2, 6)):
        if random.uniform(0, total) < a_str:
            a_score += 1
        if random.uniform(0, total) < b_str:
            b_score += 1
    return a_score, b_score


def update_after_match(team, won, gf, ga):
    d = teams_data[team]
    if won:
        d["form"] = min(15, d["form"] + random.randint(1, 3))
        d["injuries"] = max(0, d["injuries"] - random.randint(0, 1))
    else:
        d["form"] = max(1, d["form"] - random.randint(1, 3))
    if random.random() < 0.15:
        d["injuries"] += 1
        slow_print(f"  [INJURY] {team} — a player got injured!")
    if gf >= 4:
        d["form"] = min(15, d["form"] + 2)
        slow_print(f"  [BONUS] {team} scored 4+ — momentum building!")


def display_team_status(team):
    d = teams_data[team]
    eff = get_effective_strength(team)
    print(f"  {team:15s} | Strength: {d['strength']:.1f} (eff: {eff:.1f}) | Form: {d['form']}/15 | Injuries: {d['injuries']} | FIFA: {d['fifa_rank']} | WC Exp: {d['wc_exp']}")


REAL_GROUPS = {
    "A": ["Mexico", "South Korea", "South Africa", "Czech Rep."],
    "B": ["Canada", "Switzerland", "Qatar", "Bosnia"],
    "C": ["Brazil", "Morocco", "Scotland", "Haiti"],
    "D": ["USA", "Paraguay", "Australia", "Türkiye"],
    "E": ["Germany", "Ecuador", "Ivory Coast", "Curaçao"],
    "F": ["Netherlands", "Japan", "Tunisia", "Sweden"],
    "G": ["Belgium", "Iran", "Egypt", "New Zealand"],
    "H": ["Spain", "Uruguay", "Saudi Arabia", "Cabo Verde"],
    "I": ["France", "Senegal", "Norway", "Iraq"],
    "J": ["Argentina", "Austria", "Algeria", "Jordan"],
    "K": ["Portugal", "Colombia", "Uzbekistan", "DR Congo"],
    "L": ["England", "Croatia", "Panama", "Ghana"],
}


def build_groups():
    return {label: list(members) for label, members in REAL_GROUPS.items()}


def run_group_stage(groups, user_team):
    slow_print("\n" + "=" * 60)
    slow_print("  GROUP STAGE — 12 Groups of 4")
    slow_print("  Top 2 per group + 8 best third-placed teams advance to R32")
    slow_print("=" * 60)

    standings = {}
    for label, members in groups.items():
        standings[label] = {t: {"pts": 0, "gd": 0, "gf": 0, "ga": 0} for t in members}

    user_group = None
    for label, members in groups.items():
        if user_team in members:
            user_group = label
            break

    match_days = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]

    for md_idx, (i1, j1, i2, j2) in enumerate(match_days):
        print_separator()
        slow_print(f"  MATCH DAY {md_idx + 1}")
        print_separator("-")

        user_result = None

        for label, members in groups.items():
            a, b = members[i1], members[j1]
            c, d = members[i2], members[j2]

            for x, y in [(a, b), (c, d)]:
                gf, ga = simulate_match(x, y)
                standings[label][x]["pts"] += 3 if gf > ga else (1 if gf == ga else 0)
                standings[label][y]["pts"] += 3 if ga > gf else (1 if gf == ga else 0)
                standings[label][x]["gf"] += gf
                standings[label][x]["ga"] += ga
                standings[label][x]["gd"] += gf - ga
                standings[label][y]["gf"] += ga
                standings[label][y]["ga"] += gf
                standings[label][y]["gd"] += ga - gf

                if user_team in (x, y):
                    user_result = f"  >>> {x} {gf:.0f} - {ga:.0f} {y}"
                    if (user_team == x and gf > ga) or (user_team == y and ga > gf):
                        user_result += "  WIN"
                    elif gf == ga:
                        user_result += "  DRAW"
                    else:
                        user_result += "  LOSS"

        if user_result:
            print(user_result)
        else:
            print("  (Your team had no match this day)")

        if md_idx < 2:
            input("\n  Press Enter for the next match day...")

    print("\n--- FINAL GROUP STANDINGS ---")
    for label in sorted(standings.keys()):
        table = sorted(standings[label].items(), key=lambda x: (-x[1]["pts"], -x[1]["gd"], -x[1]["gf"]))
        print(f"Group {label}:")
        for rank, (t, s) in enumerate(table, 1):
            flag = " <- YOU" if t == user_team else ""
            print(f"  {rank}. {t:22s} {s['pts']}pts  GD: {s['gd']:+d}  GF: {s['gf']}  GA: {s['ga']}{flag}")

    group_winners = []
    group_runners = []
    third_placed = []
    for label, members in standings.items():
        table = sorted(members.items(), key=lambda x: (-x[1]["pts"], -x[1]["gd"], -x[1]["gf"]))
        group_winners.append((label, table[0][0]))
        group_runners.append((label, table[1][0]))
        third_placed.append((label, table[2][0], table[2][1]["pts"], table[2][1]["gd"], table[2][1]["gf"]))

    third_placed.sort(key=lambda x: (-x[2], -x[3], -x[4]))
    best_third = third_placed[:8]

    advancing = [t for _, t in group_winners] + [t for _, t in group_runners] + [t for (_, t, _, _, _) in best_third]
    advancing_set = set(advancing)

    slow_print(f"\n--- ADVANCING TO ROUND OF 32 ---")
    slow_print(f"Group winners (12): {', '.join(t for _, t in group_winners)}")
    slow_print(f"Runners-up (12): {', '.join(t for _, t in group_runners)}")
    slow_print(f"Best third-placed (8): {', '.join(t for t, _, _, _, _ in best_third)}")
    slow_print(f"\nTotal: {len(advancing)} teams advance.")

    user_advances = user_team in advancing_set
    if user_advances:
        slow_print(f"\n>>> {user_team} advances to the Round of 32!")
    else:
        slow_print(f"\n>>> {user_team} is ELIMINATED in the group stage.")

    return advancing_set, group_winners, group_runners, best_third


def draw_knockout_bracket(group_winners, group_runners, best_third):
    slow_print("\n--- DRAWING KNOCKOUT BRACKET ---")
    bracket_teams = [t for _, t in group_winners] + [t for _, t in group_runners] + [t for _, _, _, _, _ in best_third]
    random.shuffle(bracket_teams)
    slow_print(f"32 teams enter the knockout phase.")
    return bracket_teams


def knockout_round(teams_left, round_name, user_team):
    slow_print("\n" + "=" * 60)
    slow_print(f"  {round_name}")
    slow_print("=" * 60)
    winners = []
    random.shuffle(teams_left)
    user_eliminated = False

    user_result = None
    other_results = []

    for i in range(0, len(teams_left), 2):
        a, b = teams_left[i], teams_left[i+1]

        if a == user_team or b == user_team:
            my_team = user_team if a == user_team else b
            opp = b if a == user_team else a
            print_separator("-")
            slow_print(f"  YOUR MATCH: {my_team} vs {opp}")
            slow_print(f"  {opp} strength: {get_effective_strength(opp):.1f}")
            display_team_status(my_team)
            print("  Choose your strategy:")
            print("  1. Attacking (+5 attack bonus)")
            print("  2. Balanced")
            print("  3. Defensive (-1 opponent goal)")
            print("  4. Mental talk (morale boost)")
            print("  5. Assess opponent (pass — placeholder)")
            choice = input("  Enter choice (1-5): ").strip()

            if choice == "5":
                pass
                slow_print("  [pass] Opponent assessment coming soon. No action.")

            if choice == "1":
                teams_data[my_team]["strength"] += 5
                slow_print("  Attacking formation — going for goals!")
                gf, ga = simulate_match(my_team, opp)
                teams_data[my_team]["strength"] -= 5
            elif choice == "3":
                gf, ga = simulate_match(my_team, opp)
                ga = max(0, ga - 1)
                slow_print("  Defensive shape — absorbing pressure!")
            elif choice == "4":
                teams_data[my_team]["form"] = min(15, teams_data[my_team]["form"] + 3)
                slow_print("  Inspirational talk — players are fired up!")
                gf, ga = simulate_match(my_team, opp)
            else:
                gf, ga = simulate_match(my_team, opp)

            if gf == ga:
                slow_print("  Level after 90 minutes — extra time...")
                time.sleep(0.5)
                extra_a, extra_b = simulate_match(my_team, opp)
                gf, ga = gf + extra_a, ga + extra_b
            if gf == ga:
                slow_print("  PENALTIES...")
                time.sleep(0.5)
                if random.random() < 0.5:
                    gf += 1
                else:
                    ga += 1

            won = gf > ga
            user_result = f"  >>> YOUR MATCH: {my_team} {gf:.0f} - {ga:.0f} {opp}  {'ADVANCES!' if won else 'ELIMINATED!'}"
            winners.append(my_team if won else opp)
            if not won:
                user_eliminated = True
            update_after_match(my_team, won, gf, ga)

        else:
            gf, ga = simulate_match(a, b)
            if gf == ga:
                gf += 1 if random.random() < 0.5 else 0
                ga += 0 if gf != ga else 1
            winner = a if gf > ga else b
            other_results.append(f"  {a:22s} {gf:.0f} - {ga:.0f} {b:22s}  -> {winner} advances")
            winners.append(winner)

    if user_result:
        slow_print(user_result)
    if other_results:
        print_separator("-")
        slow_print(f"  Other {round_name} results ({len(other_results)} matches):")
        for r in other_results:
            slow_print(r)
    print()

    return winners, user_eliminated


def third_place_match(team_a, team_b, user_team):
    slow_print("\n" + "=" * 60)
    slow_print("  THIRD PLACE PLAY-OFF")
    slow_print("=" * 60)
    slow_print(f"  {team_a} vs {team_b}")
    gf, ga = simulate_match(team_a, team_b)
    if gf == ga:
        gf += 1
    slow_print(f"  FINAL: {team_a} {gf:.0f} - {ga:.0f} {team_b}")
    third = team_a if gf > ga else team_b
    slow_print(f"  {third} wins 3rd place!")
    return third


def pre_tournament_prep(team):
    slow_print(f"\n--- PRE-TOURNAMENT PREPARATION ---")
    slow_print(f"Manager, you have 3 preparation sessions before the World Cup.")
    sessions = ["Training", "Friendly Match", "Recovery"]
    idx = 0

    while idx < len(sessions):
        session = sessions[idx]
        print_separator()
        slow_print(f"Session {idx + 1}: {session}")
        print("  What do you want to do?")
        print(f"  1. Focus on {session}")
        print("  2. Rest the squad")
        print("  3. Skip (use pass — placeholder for future feature)")
        c = input("  Enter choice (1-3): ").strip()

        if c == "1":
            if session == "Training":
                boost = random.uniform(0.5, 2.0)
                teams_data[team]["strength"] = min(100, teams_data[team]["strength"] + boost)
                teams_data[team]["form"] = min(15, teams_data[team]["form"] + 1)
                slow_print(f"  Training went well! Strength +{boost:.1f}, Form +1")
            elif session == "Friendly Match":
                opp = random.choice([t for t in teams_data if t != team])
                slow_print(f"  Playing a friendly against {opp}...")
                gf, ga = simulate_match(team, opp)
                slow_print(f"  Result: {team} {gf:.0f} - {ga:.0f} {opp}")
                update_after_match(team, gf > ga, gf, ga)
                if gf > ga:
                    slow_print("  Positive result — squad is building momentum!")
                else:
                    slow_print("  Disappointing result — but it's just a friendly.")
            elif session == "Recovery":
                healed = random.randint(0, min(2, teams_data[team]["injuries"]))
                teams_data[team]["injuries"] = max(0, teams_data[team]["injuries"] - healed)
                teams_data[team]["form"] = min(15, teams_data[team]["form"] + 2)
                slow_print(f"  Recovery session complete. Injuries healed: {healed}, Form +2")
            idx += 1

        elif c == "2":
            rest_form = random.randint(1, 2)
            rest_injuries = random.randint(0, min(1, teams_data[team]["injuries"]))
            teams_data[team]["form"] = min(15, teams_data[team]["form"] + rest_form)
            teams_data[team]["injuries"] = max(0, teams_data[team]["injuries"] - rest_injuries)
            slow_print(f"  Squad rested. Form +{rest_form}, Injuries healed: {rest_injuries}")
            idx += 1

        elif c == "3":
            pass
            slow_print("  [pass] This session skipped — placeholder for future content.")
            idx += 1

        else:
            slow_print("  Invalid choice. Try again.")
            continue

    slow_print("\n  Pre-tournament preparation complete!")
    display_team_status(team)


def main():
    slow_print("=" * 60)
    slow_print("     2026 FIFA WORLD CUP — TEAM MANAGER SIMULATOR")
    slow_print("          48 Teams | 12 Groups | 32 Knockout")
    slow_print("=" * 60)

    slow_print("\nSelect your team:")
    sorted_teams = sorted(teams_data.items(), key=lambda x: (-x[1]["strength"], x[1]["fifa_rank"]))
    for i, (name, d) in enumerate(sorted_teams, 1):
        print(f"  {i:2d}. {name:20s} (Strength: {d['strength']:.1f}, FIFA: {d['fifa_rank']:2d})")
        if i % 12 == 0:
            print()

    while True:
        choice = input("\nEnter team name: ").strip().title()
        if choice in teams_data:
            break
        alt = {k.lower(): k for k in teams_data}
        if choice.lower() in alt:
            choice = alt[choice.lower()]
            break
        for k in teams_data:
            if choice.lower() in k.lower():
                choice = k
                break
        else:
            slow_print("Team not found. Try again.")
            continue

    slow_print(f"\nYou are managing {choice}!")
    display_team_status(choice)
    input("\nPress Enter to begin...")

    pre_tournament_prep(choice)
    input("\nPress Enter for the Group Stage draw...")

    groups = build_groups()
    advancing, group_winners, group_runners, best_third = run_group_stage(groups, choice)

    user_eliminated = choice not in advancing

    if user_eliminated:
        slow_print(f"\n{choice} did not advance. The tournament continues without your team...")
    else:
        input("\nPress Enter for the Knockout Stage draw...")

    bracket_teams = [t for _, t in group_winners] + [t for _, t in group_runners] + [t for (_, t, _, _, _) in best_third]
    random.shuffle(bracket_teams)

    rounds = [
        ("Round of 32", 32),
        ("Round of 16", 16),
        ("Quarter-Final", 8),
        ("Semi-Final", 4),
    ]

    for round_name, num_teams in rounds:
        if len(bracket_teams) < 2:
            break
        if not user_eliminated:
            input(f"\nPress Enter for the {round_name}...")
        bracket_teams, round_eliminated = knockout_round(bracket_teams, round_name, choice)
        if not user_eliminated and round_eliminated:
            slow_print(f"\n{choice} is eliminated. The tournament continues...")
            user_eliminated = True

    if not user_eliminated:
        input("\nPress Enter for the FINAL...")
    bracket_teams, _ = knockout_round(bracket_teams, "FINAL", choice)

    if choice in bracket_teams:
        slow_print("\n" + "=" * 60)
        slow_print(f"  {choice} ARE THE 2026 FIFA WORLD CUP CHAMPIONS!!!")
        slow_print("=" * 60)
    else:
        slow_print("\n" + "=" * 60)
        slow_print(f"  {bracket_teams[0]} ARE THE 2026 FIFA WORLD CUP CHAMPIONS!!!")
        slow_print("=" * 60)

    slow_print(f"\nFinal team stats:")
    display_team_status(choice)


if __name__ == "__main__":
    main()
