import random

gk_questions = [
    ("Which Indian state has the longest coastline?", ["Tamil Nadu", "Gujarat", "Andhra Pradesh", "Maharashtra"], "b"),
    ("The Sanchi Stupa was originally commissioned by which ruler?", ["Ashoka", "Chandragupta Maurya", "Kanishka", "Harshavardhana"], "a"),
    ("Which Article of the Indian Constitution deals with the Right to Constitutional Remedies?", ["Article 19", "Article 21", "Article 32", "Article 44"], "c"),
    ("Which planet has the shortest day in our Solar System?", ["Mars", "Jupiter", "Mercury", "Venus"], "b"),
    ("The headquarters of the International Monetary Fund (IMF) is located in:", ["New York", "Geneva", "Washington, D.C.", "Paris"], "c"),
    ("Who was the first Indian to win an individual Olympic gold medal?", ["Abhinav Bindra", "Neeraj Chopra", "Leander Paes", "Rajyavardhan Singh Rathore"], "a"),
    ("Which river is known as the 'Sorrow of Bihar'?", ["Gandak", "Son", "Kosi", "Bagmati"], "c"),
    ("The SI unit of electric resistance is:", ["Volt", "Ampere", "Ohm", "Watt"], "c"),
    ("Which Mughal emperor built the Buland Darwaza?", ["Babur", "Akbar", "Shah Jahan", "Aurangzeb"], "b"),
    ("Which Indian city is known as the Silicon Valley of India?", ["Hyderabad", "Pune", "Bengaluru", "Chennai"], "c"),
    ("Which gas is primarily responsible for the greenhouse effect among the following?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"], "c"),
    ("The Battle of Plassey was fought in:", ["1757", "1761", "1764", "1772"], "a"),
    ("Which country is known as the 'Land of the Rising Sun'?", ["China", "South Korea", "Japan", "Thailand"], "c"),
    ("Who among the following is associated with the discovery of the Raman Effect?", ["Homi J. Bhabha", "C. V. Raman", "S. N. Bose", "Vikram Sarabhai"], "b"),
    ("Which Schedule of the Indian Constitution contains the provisions related to anti-defection?", ["Eighth Schedule", "Ninth Schedule", "Tenth Schedule", "Eleventh Schedule"], "c"),
    ("The Great Barrier Reef is located off the coast of:", ["India", "Australia", "South Africa", "Brazil"], "b"),
    ("Which is the largest gland in the human body?", ["Pancreas", "Thyroid", "Liver", "Pituitary"], "c"),
    ("The term 'repo rate' is associated with:", ["Stock market", "Banking and monetary policy", "Foreign trade", "Insurance"], "b"),
    ("Which Indian classical dance form originated in Kerala?", ["Kathak", "Kuchipudi", "Kathakali", "Odissi"], "c"),
    ("Which organization publishes the World Economic Outlook?", ["World Bank", "IMF", "WTO", "UNDP"], "b"),
]

cse_questions = [
    ("What will be the output of the following Python code?\n   x = 10\n   y = 3\n   print(x // y)", ["3.33", "3", "4", "1"], "b"),
    ("Which of the following is used to create a list in Python?", ["{1, 2, 3}", "(1, 2, 3)", "[1, 2, 3]", "<1, 2, 3>"], "c"),
    ("What will be the output of the following code?\n   a = [10, 20, 30, 40]\n   print(a[-1])", ["10", "20", "30", "40"], "d"),
    ("Which keyword is used to define a function in Python?", ["function", "define", "def", "fun"], "c"),
    ("What will be the output?\n   x = 5\n   if x > 3:\n       print(\"Yes\")\n   else:\n       print(\"No\")", ["Yes", "No", "Error", "Nothing"], "a"),
    ("Which data type is used to store True or False values in Python?", ["int", "str", "bool", "float"], "c"),
    ("What will be the output of the following code?\n   s = \"Python\"\n   print(s[1:4])", ["Pyt", "yth", "tho", "ytho"], "b"),
    ("Which Python data structure stores data as key-value pairs?", ["List", "Tuple", "Set", "Dictionary"], "d"),
    ("What is the time complexity of accessing an element by index in a Python list, on average?", ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a"),
    ("What will be the output of the following code?\n   for i in range(2, 6):\n       print(i, end=\" \")", ["2 3 4 5", "2 3 4 5 6", "1 2 3 4 5", "3 4 5 6"], "a"),
]


correct_replies = [
    "Correct! Nice one!",
    "Yes, spot on!",
    "Well done, that's right!",
    "Boom! You got it!",
    "Exactly right, great going!",
]

wrong_replies = [
    "Not quite, but no worries.",
    "Oops, that's not it.",
    "Close, but not this time.",
    "Nope, but you'll get the next one!",
]


def ask_questions(questions, name):
    score = 0
    number = 1
    total = len(questions)

    for question, options, correct in questions:
        print(f"\nQuestion {number} of {total}: {question}")

        letters = ["a", "b", "c", "d"]
        for i in range(4):
            print(f"   {letters[i]}) {options[i]}")

        answer = input("Your answer (a/b/c/d): ").lower()
        while answer not in letters:
            answer = input("Hmm, that's not an option. Please type a, b, c or d: ").lower()

        if answer == correct:
            print(random.choice(correct_replies))
            score += 1
        else:
            right_text = options[letters.index(correct)]
            print(random.choice(wrong_replies))
            print(f"The right answer was {correct}) {right_text}")

        if number == total // 2:
            print(f"\nHalfway there, {name}! You have {score} correct so far.")

        number += 1

    return score


def show_result(name, score, total):
    print("\n" + "=" * 40)
    print(f"{name}, you scored {score} out of {total}")
    print("=" * 40)

    if score == total:
        print(f"Wow {name}, a perfect score! Absolutely brilliant!")
    elif score >= total * 0.7:
        print(f"Great job, {name}! You really know your stuff.")
    elif score >= total * 0.4:
        print(f"Good effort, {name}! A little more practice and you'll ace it.")
    else:
        print(f"Don't worry, {name}, everyone starts somewhere. Give it another go!")


print("=" * 40)
print("      Welcome to the Quiz App!")
print("=" * 40)

name = input("\nHi there! What's your name? ")
while name == "":
    name = input("I'd love to know what to call you. What's your name? ")

print(f"\nNice to meet you, {name}! Let's have some fun.")

play = "yes"
while play == "yes":
    print("\nWhat would you like to be quizzed on?")
    print("   1) General Knowledge")
    print("   2) CSE")

    choice = input("Enter 1 or 2: ")
    while choice != "1" and choice != "2":
        choice = input("Please enter just 1 or 2: ")

    if choice == "1":
        print(f"\nGreat choice, {name}! Here comes the General Knowledge quiz.")
        chosen = random.sample(gk_questions, 10)
    else:
        print(f"\nGreat choice, {name}! Here comes the CSE quiz.")
        chosen = random.sample(cse_questions, 10)

    score = ask_questions(chosen, name)
    show_result(name, score, len(chosen))

    play = input("\nFancy another round? (yes/no): ").lower()

print(f"\nThanks for playing, {name}! Come back soon!")
