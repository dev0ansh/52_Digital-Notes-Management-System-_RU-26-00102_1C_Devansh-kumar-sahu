FILE_NAME = "project.txt"  # file name stored in one place, so it can be changed easily

def read_notes():  # reads all notes from the file into a list
    notes=[]
    try:  # the file may not exist on the first run
        with open(FILE_NAME, "r", encoding="utf-8") as f:  # 'with' closes the file automatically
            for line in f:
                line = line.rstrip("\n")  # remove the new-line character at the end
                if not line.strip():  # skip blank lines
                    continue
                part = line.split("|", 2)  # split at '|' at most twice -> [id, title, content]
                if len(part) == 3:  # accept only correctly formatted lines
                    notes.append(part)
    except FileNotFoundError:
        pass  # no file yet, so start with an empty list
    return notes


def write_notes(notes):  # saves all notes to the file
    with open(FILE_NAME, "w", encoding="utf-8") as f:  # "w" replaces the old content
        for note_id, title, content in notes:  # unpack each note into 3 variables
            f.write(f"{note_id}|{title}|{content}\n")  # one note per line: ID|Title|Content

def next_id(notes):  # creates the ID for a new note
    first_id = 0  # starts at 0, so the first ID becomes N1
    for note in notes:
        num = note[0][1:]  # drop the letter N: "N12" -> "12"
        if num.isdigit():
            first_id = max(first_id, int(num))  # keep the highest number found
    return f"N{first_id + 1}"  # highest + 1, with N in front

def clean_notes(text):  # removes extra spaces and keeps the note on a single line
    return text.strip().replace("\n", " ")

def ask_title(prompt="Title: "):  # asks again until the title is valid
    while True:
        title = clean_notes(input(prompt))
        if not title:
            print("Title cannot be empty. ")
        elif "|" in title:  # '|' would break the file format
            print("Title cannot contain the '|' charecter.")
        else:
            return title

def find_notes(notes, note_id):  # returns the note with the given ID, or None
    for note in notes:
        if note[0] == note_id:  # position 0 of a note is its ID
            return note
    return None

def show_note(note):
    print(f"ID: {note[0]}")
    print(f"Title: {note[1]}")
    print(f"Content: {note[2]}")

def add_note(notes):
    title = ask_title()
    content = clean_notes(input("Content: "))
    note_id = next_id(notes)
    notes.append([note_id, title, content])
    write_notes(notes)  # save to the file so the note is permanent
    print(f"Note saved. ID:{note_id} | {title}")

def view_notes(notes):
    if not notes:
        print("No notes found.")
        return
    print("\nID    | Title")
    print("-" * 40)
    for note in notes:
        print(f"{note[0]:<6} / {note[1]}")  # <6 left-aligns the ID in 6 spaces
    note_id = input("\nEnter the ID of the note to view (or press Enter to return): ")
    if note_id:  # empty input means go back to the menu
        note = find_notes(notes, note_id)
        if note:
            show_note(note)
        else:
            print(f"Note {note_id} not found.")

def search_notes(notes):
    keyword = input("Search keyword (Case-sensitive): ")
    if not keyword:
        print("No keyword entered. Returning to main menu.")
        return
    results = [note for note in notes if keyword in note[1] or keyword in note[2]]  # keyword in title or content
    if not results:
        print("No notes found with the given keyword. Returning to main menu.")
        return
    print(f"\n{len(results)} note(s) found:")
    for note in results:
        show_note(note)

def edit_note(notes):
    note_id = input("Enter the ID of the note to edit: ")
    note = find_notes(notes, note_id)
    if not note:
        print("note not found.")
        return
    show_note(note)
    print("\nPress Enter to keep the current value. ")
    new_title = clean_notes(input("New title: "))
    new_content = clean_notes(input("New content: "))
    if new_title:  # blank means keep the old title
        if "|" in new_title:
            print("Title cannot contain '|'. Title unchanged.")
        else:
            note[1]=new_title  # position 1 is the title
    if new_content:  # blank means keep the old content
        note[2] = new_content  # position 2 is the content
    write_notes(notes)
    print(f"Note {note_id} updated.")

def delete_note(notes):
    note_id = input("ID of the note to delete: ").strip()
    note = find_notes(notes, note_id)
    if not note:
        print("Note not found")
        return
    write_notes(notes)
    if input("Delete this note? (y/n): ").strip().lower()=="y":  # lower() accepts both y and Y
        notes.remove(note)
        write_notes(notes)
        print(f"Note {note_id} deleted.")
    else:
        print("Cancelled.")

def main():
    notes = read_notes()  # load saved notes when the program starts
    actions = {  # connects each menu choice to its function
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": edit_note,
        "5": delete_note,
    }
    while True:  # show the menu again and again until the user exits
        print("\n=== Digital Notes ===")
        print("1. Add note")
        print("2. View notes")
        print("3. Search notes")
        print("4. Edit note")
        print("5. Delete note")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            break  # leaves the loop and ends the program
        action = actions.get(choice)  # returns None if the choice is not in the dictionary
        if action:
            action(notes)  # calls the chosen function
        else:
            print("Invalid choice.")

if __name__ == "__main__":  # runs main() only when this file is run directly
    main()
