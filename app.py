from flask import Flask, jsonify

app = Flask(__name__)

# -------- DATA (same as your Tkinter app) -------- #
programs = {
    "Fat Loss (FL)": {
        "workout": "Mon: 5x5 Back Squat + AMRAP\nTue: EMOM 20min Assault Bike\nWed: Bench Press + 21-15-9\nThu: 10RFT Deadlifts/Box Jumps\nFri: 30min Active Recovery",
        "diet": "B: 3 Egg Whites + Oats Idli\nL: Grilled Chicken + Brown Rice\nD: Fish Curry + Millet Roti\nTarget: 2,000 kcal",
        "color": "#e74c3c"
    },
    "Muscle Gain (MG)": {
        "workout": "Mon: Squat 5x5\nTue: Bench 5x5\nWed: Deadlift 4x6\nThu: Front Squat 4x8\nFri: Incline Press 4x10\nSat: Barbell Rows 4x10",
        "diet": "B: 4 Eggs + PB Oats\nL: Chicken Biryani (250g Chicken)\nD: Mutton Curry + Jeera Rice\nTarget: 3,200 kcal",
        "color": "#2ecc71"
    },
    "Beginner (BG)": {
        "workout": "Circuit Training: Air Squats, Ring Rows, Push-ups.\nFocus: Technique Mastery & Form (90% Threshold)",
        "diet": "Balanced Tamil Meals: Idli-Sambar, Rice-Dal, Chapati.\nProtein: 120g/day",
        "color": "#3498db"
    }
}

# -------- ROUTES -------- #

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "ACEest Fitness API Running 🚀",
        "available_programs": list(programs.keys())
    })


# Get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify({"programs": list(programs.keys())})


# Get specific program details
@app.route('/program/<name>', methods=['GET'])
def get_program(name):
    program = programs.get(name)

    if not program:
        return jsonify({"error": "Program not found"}), 404

    return jsonify({
        "program": name,
        "workout": program["workout"],
        "diet": program["diet"],
        "color": program["color"]
    })


# -------- RUN -------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)