from Encoder_decoder import password_encoder, password_decoder, decode_passwords
def main():
    stored_passwords = {}  # Dictionary to store the encoded passwords

    while True:
        # Display the menu
        print("Menu\n-----\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            pass


        elif option == '2':
            decode_passwords(stored_passwords)

        elif option == '3':
            # Quit the program
            break

        else:
            print("Invalid option. Please try again.")

# To run the program, you would uncomment the main() call in a local Python environment
# main()
if __name__ == "__main__":
    main()