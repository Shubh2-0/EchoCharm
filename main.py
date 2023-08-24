import pyttsx3


# Import the 'pyttsx3' module which provides text-to-speech functionality

# Function to list available voices and let the user choose one
def list_available_voices(engine):
    # Get the list of available voices from the engine
    voices = engine.getProperty('voices')

    # Display a message indicating that available voices are being listed
    print("Available Voices:")

    # Enumerate through the available voices and display them with corresponding numbers
    for index, voice in enumerate(voices):
        print(f"{index + 1}. {voice.name}")

    # Loop until the user makes a valid voice choice
    while True:
        try:
            # Ask the user to enter a choice and handle potential ValueError
            choice = int(input("Choose a voice (enter the corresponding number): "))

            # Check if the choice is within the valid range
            if 1 <= choice <= len(voices):
                selected_voice = voices[choice - 1]
                return selected_voice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == '__main__':
    # Initialize the text-to-speech engine
    while True:
        engine = pyttsx3.init()

        # List available voices and choose one
        selected_voice = list_available_voices(engine)

        # Set the chosen voice as the active voice for the engine
        engine.setProperty('voice', selected_voice.id)

        # Get user input
        user_text = input("Enter the text you want to hear (enter 'x' to exit): ")

        # Check if the user wants to exit the loop
        if user_text.lower() == "x":
            break

        # Speak the user input using the selected voice
        engine.say(user_text)
        engine.runAndWait()
        print("\n\n============================\n\n")


print("\n\n\n\nThanks for using this Application...........😇")


