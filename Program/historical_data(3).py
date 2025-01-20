import pandas as pd
import json

df = pd.read_json(r"historical_data.json")

total_score = df['score'][0]
final_score = float(df['final_score'][0])
negative_score = float(df['negative_score'][0])
accuracy = float(df['accuracy'][0].strip('%'))
correct_answers = df['correct_answers'][0]
incorrect_answers = df['incorrect_answers'][0]
total_questions = df['total_questions'][0]

# Time analysis
duration = df['duration'][0]
minutes, seconds = map(int, duration.split(':'))
total_time_seconds = minutes * 60 + seconds
average_time_per_question = total_time_seconds / (correct_answers + incorrect_answers)

# Error correction analysis
initial_mistakes = df['initial_mistake_count'][0]
mistakes_corrected = df['mistakes_corrected'][0]

# Response map analysis
response_map = df['response_map'][0]
total_attempted = len(response_map)

# Insights
print("=== Performance Analysis ===")
print(f"Total Score: {total_score}")
print(f"Final Score (with penalties): {final_score}")
print(f"Negative Score: {negative_score}")
print(f"Accuracy: {accuracy}%")
print(f"Correct Answers: {correct_answers} ({(correct_answers / total_questions) * 100:.2f}%)")
print(f"Incorrect Answers: {incorrect_answers} ({(incorrect_answers / total_questions) * 100:.2f}%)")

print("\n=== Time Analysis ===")
print(f"Total Duration: {duration} ({total_time_seconds} seconds)")
print(f"Average Time Per Question: {average_time_per_question:.2f} seconds")

print("\n=== Error Correction Analysis ===")
print(f"Initial Mistakes: {initial_mistakes}")
print(f"Mistakes Corrected: {mistakes_corrected}")
print(f"Net Errors Remaining: {initial_mistakes - mistakes_corrected}")

print("\n=== Response Map Analysis ===")
print(f"Total Questions Attempted: {total_attempted}/{total_questions}")
