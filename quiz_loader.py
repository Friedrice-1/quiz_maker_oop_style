# Create a class for quiz loader
class QuizLoader:
# Initialize the class with filename and an empty list for questions
    def __init__(self, filename="quiz_data.txt"):
        self.filename = filename
        self.questions = []
# Load questions from the file into the question list
    def load_questions(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()

        index = 0
        while index < len(lines):
            if lines[index].startswith("Question"):
                question_text = lines[index].strip().split("Question: ")[1]
                choices = {}
                for offset in range(1, 5):
                    line = lines[index + offset].strip()
                    key, value = line.split(": ")
                    choices[key] = value
                correct_line = lines[index + 5].strip()
                correct_answer = correct_line.split(": ")[1]

                self.questions.append({
                    "question": question_text,
                    "choices": choices,
                    "correct": correct_answer
                })
                index += 7
            else:
                index += 1
# Start the quiz with user interaction