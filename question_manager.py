# Create a class for question manager
class QuestionManager:
# Initialize the class with an empty list to store questions
    def __init__(self):
        self.questions = []
# Loop to add questions through user input
    def add_question(self):
        while True:
            question_text = input("Please enter a question: ").capitalize()
            if not question_text:
                print("Question cannot be empty. Please try again.")
                continue

            choice_a = input("Please enter choice 'A': ").upper()
            choice_b = input("Please enter choice 'B': ").upper()
            choice_c = input("Please enter choice 'C': ").upper()
            choice_d = input("Please enter choice 'D': ").upper()

            if not all([choice_a, choice_b, choice_c, choice_d]):
                print("All choices must be filled. Please try again.")
                continue
        # Create a dictionary for the question and add it to the list
            while True:
                correct_answer = input("Please enter the correct answer [A/B/C/D]: ").upper()
                if correct_answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter only A, B, C, or D.")

            question_data = {
                "question": question_text,
                "choices": {
                    "A": choice_a,
                    "B": choice_b,
                    "C": choice_c,
                    "D": choice_d
                },
                "correct": correct_answer
            }

            self.questions.append(question_data)

            continue_input = input("Do you want to continue input [Y/N]?: ").strip().upper()
            if continue_input == "N":
                break
# Save created questions to a text file
    def save_to_file(self, filename="quiz_data.txt"):
        with open(filename, "w") as file:
            for question in self.questions:
                file.write(f"Question: {question['question']}\n")
                for key, value in question["choices"].items():
                    file.write(f"  {key}: {value}\n")
                file.write(f"Correct Answer: {question['correct']}\n")
                file.write("-" * 40 + "\n")
        print(f"All questions saved to '{filename}' in the same directory.")