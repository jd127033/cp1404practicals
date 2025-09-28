"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)

def check_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()



