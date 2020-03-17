def rotateClock():
    print("Clockwise")

def rotateAntiClock():
    print("Anti-Clockwise")

def noRotate():
    print("No Rotation")

# Importing trained DNN model
# from model.dnn_1 import model_1
# Predicting using the model
# OUTPUT = model_1.predict(INPUT)

# Assignment of numbers to relevant base case
# 1 - AB
# 2 - AC
# 3 - BC
# 4 - AA
# 5 - BB
# 6 - CC

def rotate_system(peak):
    switcher = {
        1: "rotateAntiClock",
        2: "rotateClock",
        3: "rotateClock",
        4: "noRotate",
        5: "rotateAntiClock",
        6: "rotateClock"
    }
    # Get the relevant switcher function from the base switcher
    func = switcher.get(current, lambda: "switch_invalid")
    func(peak)

if __name__ == "__main__":
    # Current position of the front
    current = 1
    # Peak direction
    peak = 1

    rotate_system(current, peak)