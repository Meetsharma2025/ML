import random

def player(prev_play, opponent_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(["R","P","S"])

    # -------- PATTERN ANALYSIS --------
    pattern = "".join(opponent_history)

    last4 = "".join(opponent_history[-4:])
    possible = {}

    for i in range(len(pattern)-4):
        if pattern[i:i+4] == last4:
            next_move = pattern[i+4]
            if next_move in possible:
                possible[next_move] += 1
            else:
                possible[next_move] = 1

    if possible:
        prediction = max(possible, key=possible.get)
    else:
        prediction = random.choice(["R","P","S"])

    # -------- COUNTER MOVE --------
    counter = {
        "R":"P",
        "P":"S",
        "S":"R"
    }

    return counter[prediction]
