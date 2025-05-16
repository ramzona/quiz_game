# quiz_game.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) HTML", "C) Java", "D) C++"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    }
]

score = 0

print("🧠 Welcome to the Quiz Game!")
print("-----------------------------")

for q in questions:
    print(f"\n{q['question']}")
    for option in q['options']:
        print(option)
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}")

print("\n🎉 Quiz Complete!")
print(f"🧾 Your final score is: {score}/{len(questions)}")
