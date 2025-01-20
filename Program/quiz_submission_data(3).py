import pandas as pd
import json
file_path = r"quiz_submission_data.json"
with open(file_path, 'r') as file:
    data = json.load(file)
data["accuracy"] = float(data["accuracy"].strip(" %"))

total_questions = data["total_questions"]
attempted_questions = data["correct_answers"] + data["incorrect_answers"]
accuracy = data["accuracy"]
negative_score = float(data["negative_score"])
final_score = float(data["final_score"])
correct_answers = data["correct_answers"]
incorrect_answers = data["incorrect_answers"]
response_map = data["response_map"]
rank_text = data["rank_text"]

insights = {
    "Total Questions": total_questions,
    "Attempted Questions": attempted_questions,
    "Unattempted Questions": total_questions - attempted_questions,
    "Correct Answers": correct_answers,
    "Incorrect Answers": incorrect_answers,
    "Accuracy": accuracy,
    "Final Score": final_score,
    "Negative Score": negative_score,
    "Rank": rank_text
}

recommendations = []
if accuracy < 85:
    recommendations.append("Focus on improving accuracy by reviewing incorrect answers.")
if negative_score > 0:
    recommendations.append("Avoid negative marking by reducing risky guesses.")
if attempted_questions < total_questions * 0.75:
    recommendations.append(f"Attempt more questions to improve rank and score. Currently attempted {attempted_questions}/{total_questions}.")
if correct_answers < incorrect_answers:
    recommendations.append("Focus on topics where most incorrect answers occurred.")

print("---- Quiz Insights ----")
for key, value in insights.items():
    print(f"{key}: {value}")

print("\n---- Recommendations ----")
if recommendations:
    for rec in recommendations:
        print(f"- {rec}")
else:
    print("Great work! Keep practicing to maintain your performance.")
