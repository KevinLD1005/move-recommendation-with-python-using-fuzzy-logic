import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import os

#Clear Terminal
def clear_screen():
    os.system("cls") # Clear screen on windows = "cls", elif on mac/linux = "clear"

#Universe
audience_score = ctrl.Antecedent(np.arange(0, 101, 1), "audience_score")
critic_score   = ctrl.Antecedent(np.arange(0, 101, 1), "critic_score")
audience_count = ctrl.Antecedent(np.arange(0, 10001, 1), 'audience_count')
year           = ctrl.Antecedent(np.arange(1900, 2026, 1), "year")

#Output
recommendation = ctrl.Consequent(np.arange(0, 11, 1), "recommendation")

#Input

#Audience Score
audience_score["low"]    = fuzz.trapmf(audience_score.universe, [0, 0, 50, 60])
audience_score["medium"] = fuzz.trimf(audience_score.universe, [60, 70, 80])
audience_score["high"]   = fuzz.trapmf(audience_score.universe, [70, 90, 100, 100])

#Critic Score
critic_score["low"]    = fuzz.trapmf(critic_score.universe, [0, 0, 50, 60])
critic_score["medium"] = fuzz.trimf(critic_score.universe, [60, 70, 80])
critic_score["high"]   = fuzz.trapmf(critic_score.universe, [70, 90, 100, 100])

#Audience_count
audience_count["low"]    = fuzz.trapmf(audience_count.universe, [0, 0, 500, 1000])
audience_count["medium"] = fuzz.trimf(audience_count.universe, [500, 2500, 4500])
audience_count["high"]   = fuzz.trapmf(audience_count.universe, [3000, 6000, 10000, 10000])

#Year
year["old"]    = fuzz.trapmf(year.universe, [1900, 1900, 1990, 2000])
year["recent"] = fuzz.trimf(year.universe, [1995, 2010, 2020])
year["new"]    = fuzz.trapmf(year.universe, [2015, 2020, 2025, 2025])

#Recommendation
recommendation["low"]    = fuzz.trapmf(recommendation.universe, [0, 0, 4, 5])
recommendation["medium"] = fuzz.trimf(recommendation.universe, [5, 7, 8])
recommendation["high"]   = fuzz.trapmf(recommendation.universe, [7, 8, 10, 10])

rules = [
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["low"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["low"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["medium"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["medium"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["medium"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["high"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["high"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["low"] & audience_count["high"] & year["new"], recommendation["low"]),

    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["low"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["low"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["medium"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["medium"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["medium"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["high"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["high"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["medium"] & audience_count["high"] & year["new"], recommendation["low"]),

    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["low"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["low"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["medium"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["medium"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["medium"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["high"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["high"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["low"] & critic_score["high"] & audience_count["high"] & year["new"], recommendation["low"]),

    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["low"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["low"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["medium"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["medium"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["medium"] & year["new"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["high"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["high"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["low"] & audience_count["high"] & year["new"], recommendation["low"]),

    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["low"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["low"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["medium"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["medium"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["medium"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["high"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["high"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["medium"] & audience_count["high"] & year["new"], recommendation["medium"]),

    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["low"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["low"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["low"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["medium"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["medium"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["medium"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["high"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["high"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["medium"] & critic_score["high"] & audience_count["high"] & year["new"], recommendation["medium"]),

    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["low"] & year["old"], recommendation["low"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["low"] & year["recent"], recommendation["low"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["low"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["medium"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["medium"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["medium"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["high"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["high"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["low"] & audience_count["high"] & year["new"], recommendation["medium"]),

    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["low"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["low"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["low"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["medium"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["medium"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["medium"] & year["new"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["high"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["high"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["medium"] & audience_count["high"] & year["new"], recommendation["medium"]),

    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["low"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["low"] & year["recent"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["low"] & year["new"], recommendation["high"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["medium"] & year["old"], recommendation["medium"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["medium"] & year["recent"], recommendation["high"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["medium"] & year["new"], recommendation["high"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["high"] & year["old"], recommendation["high"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["high"] & year["recent"], recommendation["high"]),
    ctrl.Rule(audience_score["high"] & critic_score["high"] & audience_count["high"] & year["new"], recommendation["high"]),
]

#Bandwidth controls
recommendation_ctrl = ctrl.ControlSystem(rules)
recommendation_result = ctrl.ControlSystemSimulation(recommendation_ctrl)

def main():

    bool = True

    while bool:

        clear_screen()

        print("")
        print('|===============================|')
        print('|  MOVIE RECOMMENDATION SYSTEM  |')
        print('|===============================|')
        print('|                               |')
        print('|      FUZZY LOGIC PROJECT      |')
        print('|                               |')
        print('|===============================|')
        print("")

        movie_name = input("Enter Movie Name: ")

        #User Inputs
        try:
            a_score_input = float(input("Enter Audience Score: "))
            c_score_input = float(input("Enter Critic Score: "))
            a_count_input = float(input("Enter Audience Count: "))
            year_input    = float(input("Enter Year of Release: "))
        except ValueError:
            print("\nValueError!. Enter a float number!")
            input("press enter to continue...")
            clear_screen()
            continue

        #Inputs Universal
        recommendation_result.input["audience_score"] = a_score_input
        recommendation_result.input["critic_score"]   = c_score_input
        recommendation_result.input["audience_count"] = a_count_input
        recommendation_result.input["year"]           = year_input
        recommendation_result.compute()

        result = recommendation_result.output["recommendation"]

        #Recommended or Not
        def recommendation_func(level):
            if level > 7:
                return "Recommended"
            else:
                return "Not Recommended"

        print("")
        print(f"Recommendation Level Result : {result:.2f}")
        print(f"Movie Title: {movie_name} is {recommendation_func(result)}")
        print("")

        #Show Plots
        recommendation.view(sim=recommendation_result)
        plt.yticks([0, 0.5, 1])
        plt.xticks(np.arange(0, 10, 1))
        plt.text(0, 1.1, f"Recommendation Level: {result:.2f}\nMovie is {recommendation_func(result)}", fontsize=12, ha="center")
        plt.show()

        #Return Loop
        conf = input("Retry? (Enter 'Y' to continue, Enter anything else to end): ").upper()
        if conf == "Y":
            pass
        else:
            print(">#==========================#<")
            print(">#                          #<")
            print(">#  Bye Bye!  (づ๑•ᴗ•๑)づ♡  #<")
            print(">#                          #<")
            print(">#==========================#<")
            bool = False

if __name__ == "__main__":
    main()


