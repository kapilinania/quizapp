questions = [
    {
        'question': 'What is India\'s capital?',
        'option': ['A. Jaipur', 'B. Delhi', 'C. Mumbai', 'D. Jodhpur'],
        'correct': 'B'
    },
    {
        'question': 'What is Rajasthan\'s capital?',
        'option': ['A. Jaipur', 'B. Delhi', 'C. Mumbai', 'D. Jodhpur'],
        'correct': 'A'
    },
    {
        'question': 'What is my name?',
        'option': ['A. Kapil', 'B. Delhi', 'C. Mumbai', 'D. Jodhpur'],
        'correct': 'A'
    },
    {
        'question': 'What is the sum of 2 + 2?',
        'option': ['A. 22', 'B. 040', 'C. 200', 'D. 4'],
        'correct': 'D'
    },
]
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        question = questions[i]
        print(f"Question {i+1}: {question['question']}")
        for option in question['option']:
            print(option)

        user_answer = input("Enter the letter of your answer (A, B, C, or D): ").upper()
        if user_answer == question['correct']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong answer  {question['correct']}\n")

    print(f"Quiz Complete! Your score: {score}/{total_questions}")

run_quiz(questions)
