import random

class LanguageApp:
    def __init__(self):
        self.learn_spanish_words = {
            "Hi!": "¡Hola!",
            "How are you doing?": "¿Cómo estás?",
            "I am fine.": "Estoy bien.",
            "What is your name?": "¿Cuál es tu nombre?",
            "My name is": "Me llamo ____"
        }

    def main_menu(self):
        while True:
            print("\nWelcome to the Language App!")
            print("1. Learn Spanish")
            print("2. Take a quiz")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.learn_spanish()
            elif choice == "2":
                self.take_quiz()
            elif choice == "3":
                print("Thank you for using the Language App!")
                break
            else:
                print("Invalid choice. Please try again.")

    def learn_spanish(self):
        print("\nWelcome to the Spanish learning section!")
        print("Here are some words and phrases:")
        for english, spanish in self.learn_spanish_words.items():
            print(f"{english} - {spanish}")

    def take_quiz(self):
        print("\nWelcome to the quiz!")
        print("1. Spanish to English")
        print("2. English to Spanish")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.quiz_spanish_to_english()
        elif choice == "2":
            self.quiz_english_to_spanish()
        else:
            print("Invalid choice. Please try again.")
            self.take_quiz()

    def quiz_spanish_to_english(self):
        items = list(self.learn_spanish_words.items())
        english, spanish = zip(*items)
        index = random.randint(0, len(spanish) - 1)
        question = spanish[index]
        correct_answer = english[index]
        user_input = input(f"What does '{question}' mean in English? ")
        if user_input.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    def quiz_english_to_spanish(self):
        items = list(self.learn_spanish_words.items())
        english, spanish = zip(*items)
        index = random.randint(0, len(english) - 1)
        question = english[index]
        correct_answer = spanish[index]
        user_input = input(f"What is the Spanish translation of '{question}'? ")
        if user_input.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")


if __name__ == "__main__":
    app = LanguageApp()
    app.main_menu()
