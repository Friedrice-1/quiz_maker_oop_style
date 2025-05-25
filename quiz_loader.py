# Create a class for quiz loader
class QuizLoader:
# Initialize the class with filename and an empty list for questions
    def __init__(self, filename="quiz_data.txt"):
        self.filename = filename
        self.questions = []
# Load questions from the file into the question list
    def load_questions(self):
# Start the quiz with user interaction