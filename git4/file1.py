def write_to_file():
    with open("notes.txt", "a") as file:
        note = input("Write something to save in file: ")
        file.write(note + "\n")
        print("Saved successfully!")

def read_file():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            print("\n--- File Contents ---")
            print(content)
    except FileNotFoundError:
        print("File not found. Write something first!")

while True:
    print("\n1. Write to Fil

