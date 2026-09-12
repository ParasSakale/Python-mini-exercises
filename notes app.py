
#Notes App
print("")
print("Welcome to the Notes App")
print("")
notes = {}
while True:
    print("1. Add a note")
    print("2. View notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Exit")
    user_choice = input("Enter your choice (1/2/3/4/5) : ")
    #Add a note
    if user_choice == "1":
        key = "note" + str(len(notes) + 1)
        content = input("Enter your note: ")
        notes[key] = content

    #View a note
    elif user_choice == "2":
        for key, content in notes.items():
            print(f"{key} : {content}")

    #Edit a note
    elif user_choice == "3":
        choose_note = input("Enter the note you want to edit:")
        if choose_note in notes:
            change_notes = input("Enter the changes you want to make: ")
            notes[choose_note] = change_notes
        else:
            print("Note not found")

    #delete a note
    elif user_choice == "4":
        delete_a_note = input("Choose the note you want to delete: ")
        if delete_a_note in notes:
            notes.pop(delete_a_note)
        else:
            print("Note not found")

    #Exit
    elif user_choice == "5":
        print("Thank you for using the note app!")

        break
    else:
        print("Invalid choice")


