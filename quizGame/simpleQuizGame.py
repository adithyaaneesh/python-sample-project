# 2. Simple Quiz Game 

import random
questionsFile = "/Users/adith/OneDrive/Documents/Desktop/www/Python/simpleProject/quizGame/question.txt"

def load_questions():
    questions = []
    try:
        with open(questionsFile, "r") as f:
            for i in f:
                if "|" in i:
                    question , answer = i.strip().split("|")
                    questions.append({"question": question, "answer": answer})
    except FileNotFoundError:
        print("File not found")
    return questions

def quiz_game():
    questions = load_questions()
    if not questions:
        print("No questions available!")
        return 
    
    random.shuffle(questions)
    score = 0
    ques_no = 1
    print("Quiz Game")
    for i  in questions:
        print(f"\nQ{ques_no}. {i['question']}")
        answer = input("Your answer: ").strip()
        if answer.lower() == i["answer"].lower():
            print("Correct Answer!")
            score += 1
        else:
            print(f"Wrong! Correct Answer: {i['answer']}")
        ques_no += 1
    print(f"\n Final Score: {score}/{len(questions)}")
if __name__ == "__main__":
    quiz_game()