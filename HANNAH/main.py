"""
    HANNAH

    Desc: An ELIZA program written in Python
    Dev:  Josh Taro.
    Date: 2/21/2024
"""
import responses as hannah


def greeting() -> None:
    """Introduces the user to what the program is and what it does, and how to use."""
    print("#########################################################################")
    print("##                You are now chatting with HANNAH                     ##")
    print("##     An ELIZA therapist chatbot written in Python by Josh Taro!      ##")
    print("#########################################################################")
    print("It's recommended that you chat using short, single sentences with HANNAH.")
    print("To stop chatting, just say \"Bye\"\n")


def main() -> None:
    """Main loop of the program"""
    print("HANNAH: Hello. How are you feeling today?")
    while True:
        user_input: str = input("You:\t")
        # Check to end chat session
        if hannah.end_chat(user_input):
            print("HANNAH:\tGoodbye. Have a nice day!\n")
            break
        # Continue chatting
        else:
            print(f"HANNAH:\t{hannah.match_response(user_input)}")

    input("\nPress any key to close terminal...")


if __name__ == "__main__":
    greeting()
    main()
