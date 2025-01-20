import pandas as pd
import json

df = pd.read_json(r"quiz_endpoint.json")
print(df["quiz"].head())

questions = []
for q in df["quiz"]:
    #for question in q["questions"]:
     if isinstance(q, dict):
        questions.append({
            "Question ID": q["id"],
            "Title": q["title"],
            "Description": q["description"],
            "Difficulty Level": q.get("difficulty_level", "Not Available"),
            "Topic": q.get("topic", "Not Available"),
        })

questions_df = pd.DataFrame(questions)

options = []
if "quiz" in df.columns:
    for quiz_data in df["quiz"]:
        if isinstance(quiz_data, dict) and "questions" in quiz_data:
            for q in quiz_data["questions"]:
                if "options" in q:
                    for option in q["options"]:
                        options.append({
                            "Question ID": q["id"],
                            "Option ID": option["id"],
                            "Option Description": option["description"],
                            "Is Correct": option.get("is_correct", False),
                        })
                #else:
                 #   print(f"No 'options' found for Question ID {q['id']}")
        #else:
           # print("No 'questions' found in the quiz data.")
#else:
   # print("'quiz' column is missing in the JSON data.")

options_df = pd.DataFrame(options)

# 1. Check for correct and incorrect option distribution
#correct_answers = options_df[options_df["Is Correct"] == True]
#incorrect_answers = options_df[options_df["Is Correct"] == False]

#correct_answer_percentage = len(correct_answers) / len(options_df) * 100
#incorrect_answer_percentage = len(incorrect_answers) / len(options_df) * 100

#print(f"Correct Answers: {correct_answer_percentage:.2f}%")
#print(f"Incorrect Answers: {incorrect_answer_percentage:.2f}%")

# 2. Topic-wise analysis (assuming each question belongs to a topic)
#topic_performance = questions_df["Topic"].value_counts()
#print(f"Topic-wise Question Count:\n{topic_performance}")

if not options_df.empty:
    correct_answers = options_df[options_df["Is Correct"] == True]
    incorrect_answers = options_df[options_df["Is Correct"] == False]

    correct_answer_percentage = len(correct_answers) / len(options_df) * 100
    incorrect_answer_percentage = len(incorrect_answers) / len(options_df) * 100

    print(f"Correct Answers: {correct_answer_percentage:.2f}%")
    print(f"Incorrect Answers: {incorrect_answer_percentage:.2f}%")
else:
    print("No options data found to analyze correct/incorrect answers.")

# Topic-wise analysis
if not questions_df.empty and "Topic" in questions_df.columns:
    topic_performance = questions_df["Topic"].value_counts()
    print(f"Topic-wise Question Count:\n{topic_performance}")
else:
    print("No topic data found for analysis.")
