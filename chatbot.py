from datetime import datetime

def chatbot():

    print("=" * 40)
    print("WELCOME TO BASIC CHATBOT")
    print("=" * 40)

    print("\nType 'bye' to exit.")

    while True:

        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! How are you?")

        elif user == "fine!how are you?":
            print("Bot: I am fine. Thanks for asking!")

        elif user == "your name":
            print("Bot: I am CodeAlpha ChatBot.")

        elif user == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current Time is {current_time}")

        elif user == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's Date is {current_date}")

        elif user == "help":
            print("Bot: Try saying hello, time, date, how are you, bye")
       
         elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()