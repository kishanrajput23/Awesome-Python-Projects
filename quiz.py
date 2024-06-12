def display_question(question, options):
    print(question)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            return answer
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    for question, data in questions.items():
        display_question(question, data['options'])
        user_answer = get_user_answer()
        correct_answer = data['answer']
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
        print()

    print(f"Quiz complete! Your final score is {score} out of {len(questions)}.")

def main():
    questions = {
        "Who is the Current President Of America?": {
            "options": ["Obama", "Biden", "Elon", "Putin"],
            "answer": 2
        },
        "What is 2 + 2?": {
            "options": ["3", "4", "5", "6"],
            "answer": 2
        },
        "Which planet is known as the Red Planet?": {
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        "Who is the Creator of Python?": {
            "options": ["Guido van Rossum", "James Gosling", "Brendan Eich", "Mark Zukerberg"],
            "answer": 1
        }
    }

    run_quiz(questions)

if __name__ == "__main__":
    main()
