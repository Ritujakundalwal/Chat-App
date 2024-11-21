# Two-user chat program
def chat_between_two_users():
    print("Welcome to the Two-User Chat Program!")
    print("Type 'quit' at any time to exit the chat.\n")
    
    user1 = input("Enter the name of User 1: ")
    user2 = input("Enter the name of User 2: ")
    
    print(f"\n{user1} and {user2}, you can start chatting now!")
    
    while True:
        # User 1's turn
        message1 = input(f"{user1}: ")
        if message1.lower() == "quit":
            print(f"{user1} has left the chat. Goodbye!")
            break
        print(f"{user2}, {user1} said: '{message1}'")
        
        # User 2's turn
        message2 = input(f"{user2}: ")
        if message2.lower() == "quit":
            print(f"{user2} has left the chat. Goodbye!")
            break
        print(f"{user1}, {user2} said: '{message2}'")

# Run the chat program
chat_between_two_users()
