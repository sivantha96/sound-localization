def rotateClock():
    print("Clockwise")

def rotateAntiClock():
    print("Anti-Clockwise")

# Assignment of numbers to relevant base case
# 1 - AA
# 2 - AB
# 3 - BB
# 4 - BC
# 5 - CC
# 6 - AC

def switch_aa(argument):
    switcher = {
        1: 
    }

def rotate_system(argument):
    switcher = {
        1: "switch_aa",
        2: "switch_ab",
        3: "switch_bb",
        4: "switch_bc",
        5: "switch_cc",
        6: "switch_ac"
    }
    # Get the relevant switcher function from the base switcher
    func = switcher1.get(argument, lambda: "switch_invalid")

if __name__ == "__main__":
    # Current position of the front
    current = 1
    # Peak direction
    peak = 1

    rotate_system(current)