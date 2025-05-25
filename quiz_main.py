# Import the QuestionManager class from question_manager module
from question_manager import QuestionManager
# Import the QuizLoader class from quiz_loader module
from quiz_loader import QuizLoader
# Create a function for a menu
def menu():
    print("Welcome to the Quiz App")
# Ask user what they want to do
    while True:
        mode = input("Select mode: [1] Create Quiz [2] Take Quiz [Q] Quit: ").strip().upper()
# Load question manager
        if mode == "1":
            question_manager = QuestionManager()
            question_manager.add_question()
            question_manager.save_to_file()
# Load quiz loader
        elif mode == "2":
            quiz_loader = QuizLoader()
            quiz_loader.load_questions()
            quiz_loader.start_quiz()
        elif mode == "Q":
            print("Goodbye")
            break
        else:
            print("Invalid option. Please choose 1, 2 or Q.")
# Check if this file is being run directly
if __name__ == "__main__":
    menu()