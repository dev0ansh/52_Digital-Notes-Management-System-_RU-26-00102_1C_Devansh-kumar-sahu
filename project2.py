FILE_NAME = "project.txt" #file is stored inside a str name so that we can use the str name everywhere so if we want to change the file later on you can simply change the file inside the str name here 

def read_notes(): #function defination to read the notes from the file
    notes=[] #an empty list to store the notes 
    try: #try block is used to handle the empty file error
        with open(FILE_NAME, "r", encoding="utf-8") as f: #with open is used to open file in read mode and with is specifically used so that we do not have to close the file 
            for line in f:
                line = line.rstrip("\n") #it will remove the new line character from the end of the string
                if not line.strip(): #it will check after removing the new line does the line still contain any charecter if not then it will skip the line 
                    continue 
                part = line.split("|", 2) #it will split the line into 3 parts where the it will find | and convert it into a list of 3 parts 
                if len(part) == 3: #it will check if the line is acurately split into 3 parts or not 
                    notes.append(part) #if the lines length is 3 then it will append that line into the notes list
    except FileNotFoundError:
        pass #if the file is not found then it will continue without displaying any error
    return notes #it will return the list of notes which is read from the file 


def write_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as f: #it will open the file in write mode and write the notes into the file 
        for note_id, title, content in notes: #all the names written before "in" will itterate through the notes list and unpack the values 
            f.write(f"{note_id}|{title}|{content}\n") #it will write the note into the file in the format given in the f string

def next_id(notes):
    first_id = 0 #to initiate the first id to 0 and then update it on the next line
    for note in notes:
        num = note[0][1:] #it will drop the N and get the number of the note id as an integer
        if num.isdigit(): #it will check if the number is a digit or not 
            first_id = max(first_id, int(num)) #it will get the maximum of the number and compare the highest with the num value and update the first_id with the maximum value which is found
    return f"N{first_id + 1}"       # this will add 1 because the highest id which came to the first_id is taken and we need a new id so it adds up a number to make it one number up from the existing id and then by using the N a prefix we will get (N[the highest number we got after adding]) 

"""we make a function to clean the notes so that we can remove the unwanted space in the start and end of the note and also it will remove the new line charecter if it is present and replace it with a space so that the note will be in a single line 
and the format will not be disturbed"""
def clean_notes(text):
    return text.strip().replace("\n", " ") #by this we can easily remove the spaces from the start and from the end and also if a single line by mistake gets a new line charecter then it will replace that new line charecter with a space so the note will be in a single line and the format will not be disturbed 

"""this will ask for title from the user and it will check if the title is empty or not and if it is empty then it will ask the user to enter the title again and if the title contains | charecter 
then it will ask the user to enter the title again and if the title is valid then it will return the title and exit the function """
def ask_title(prompt="Title: "):
    while True:   #to make a loop until a condition is true and if the condition is false then it will break the loop and exit the function
        title = clean_notes(input(prompt)) #it will take the title from the user and clean it and this function is defined above and we are just using it 
        if not title:
            print("Title cannot be empty. ") #if the title is empty then it will display this message and ask the user to enter the title again
        elif "|" in title: #it will detect | char in file title and if it is found then it will ask the user to enter the title again 
            print("Title cannot contain the '|' charecter.") 
        else:
            return title #if the title is valid then it will return the title and exit the function

"""this line of code will search for the notes on the basis of the note_id that we provide to 
    the function and if the note_id is found then it will return the note and if the note_id is not found then it will return None"""

def find_notes(notes, note_id):
    for note in notes: #it will itterate through the notes list and check if the note_id is present in the list or not
        if note[0] == note_id: #it will check if the note_id is present in the list or not we take 0 as the position of the note_id is at 0 in the list of notes
            return note #if the note_id is found then it will return the note and exit the function
    return None #if the note_id is not found then it will return None and exit the function

"""this function is created to display the note in a proper format so that is will be easy to read and understand """
def show_note(note):
    print(f"ID: {note[0]}") #it will display the note_id of the note
    print(f"Title: {note[1]}") #it will display the title of the note
    print(f"Content: {note[2]}") #it will display the content of the note 

"""this function is created to add the note into the notes list and it will ask the user to enter the title and content of the note and it will check if the title is valid or not and if it is valid then it will 
return the title and exit the function and then it will clean the content of the note and return the content and exit the function and then it will get the next id of the note and return the id and exit the function 
and then it will append the note_id , title and content into the notes list and return the notes list and exit the function and then it will save the notes into the file and exit the function this function is decleared 
above and we are just using it here  and then it will display the message that the note is added successfully and it will display the note_id of the note which is added"""
def add_note(notes):
    title = ask_title() #it will ask the user to enter the title of the note and it will check if the title is valid or not and if it is valid then it will return the title and exit the function
    content = clean_notes(input("Content: ")) #it will ask the user to enter the content of the note and it will clean the content and return the content and exit the function
    note_id = next_id(notes) #it will get the next id of the note and return the id and exit the function
    notes.append([note_id, title, content]) #it will append the note_id , title and content into the notes list and return the notes list and exit the function
    write_notes(notes) #it will save the notes into the file and exit the function this function is decleared above and we are just using it here 
    print(f"Note {note_id} added successfully.") #it will display the message that the note is added successfully and it will display the note_id of the note which is added

"""This function is created to view the notes in a proper format and it will check if the notes list is empty or not and if it is empty then it will display the message that there are no notes to display and exit the function """
def view_notes(notes):
    if not notes: #it will check if the notes list is empty or not and if it is empty then it will display the message that there are no notes to display and exit the function 
        print("No notes to display.")
        return
    print("\nID    | Title") #it will display the header of the notes list in a proper format
    print("-" * 40) #it will display a line of 40 charecters to seperate the header from the notes list
    for note in notes: #it will itterate through the notes list and display the note_id and title of the note in a proper format
        print(f"{note[0]:<6} / {note[1]}") #it will display the note_id and title of the note in a proper format the : starts the formatting and <6 means it will left align the note_id and make it 6 charecters long and / is used to seperate the note_id and title of the note 
    note_id = input("\nEnter the ID of the note to view (or press Enter to return): ") #it will ask the user to enter the note_id of the note which he wants to view and if the user does not enter any note_id then it will return to the main menu
    if note_id: #it will check if the user has entered any note_id or not and if the user has entered any note_id then it will search for the note in the notes list and if the note is found then it will display the note in a proper format and if the note is not found then it will display the message that the note is not found
        note = find_notes(notes, note_id) #it will search for the note in the notes list and if the note is found then it will return the note and exit the function and if the note is not found then it will return None and exit the function 
        if note: #it will check if the note is found or not and if the note is found then it will display the note in a proper format and if the note is not found then it will display the message that the note is not found 
            show_note(note) #it will display the note in a proper format this function is decleared above and we are just using it here 
        else:
            print(f"Note {note_id} not found.") #it will display the message that the note is not found

""""""
def search_notes(notes):
    keyword = input("Search keyword (Case-sensitive): ") #it will ask the user to enter the keyword which he wants to search in the notes list and it is case-sensitive 
    if not keyword: #it will check if the user has entered any keyword or not and if the user has not entered any keyword then it will return to the main menu
        print("No keyword entered. Returning to main menu.") #it will display the message that no keyword is entered and it will return to the main menu
        return
    results = [note for note in notes if keyword in note[1] or keyword in note[2]] #it will search for the keyword in the title and content of the notes list and if the keyword is found then it will append that note into the results list and return the results list and exit the function 
    if not results: #it will check if the results list is empty or not and if it is empty then it will display the message that no notes are found and it will return to the main menu 
        print("No notes found with the given keyword. Returning to main menu.") #it will display the message that no notes are found with the given keyword and it will return to the main menu
        return 
    print(f"\n{len(results)} note(s) found:") #it will display the total number of notes found in the notes list which contains the keyword and it will display the message that how many notes are found
    for note in results: #it will itterate through the results list and display the note_id and title of the note in a proper format
        show_note(note) #it will display the note in a proper format this function is decleared above and we are just using it here 

"""this function is used to edit the title and content of a particualar note id """
def edit_note(notes):
    note_id = input("Enter the ID of the note to edit: ") #it will ask the user to enter the note_id of the note which he wants to edit and it will search for the note in the notes list and if the note is found then it will display the note in a proper format and if the note is not found then it will display the message that the note is not found
    note = find_notes(notes, note_id) #it will search for the note in the notes list and if the note is found then it will return the note and exit the function and if the note is not found then it will return None and exit the function
    if not note: #it will check if the note is found or not and if the note is not found then it will display the message that the note is not found and it will return to the main menu
        print("note not found.") #this line will display note not found 
        return #it will return to the main menu
    show_note(note) #it will display the note in a proper format this function is decleared above
    print("\nPress Enter to keep the current value. ") 
    new_title = clean_notes(input("New title: ")) #here if we are editing the note we are passing the notes new title through the clean_notes function to remove any space or any \n charecter 
    new_content = clean_notes(input("New content: ")) #here if we are editing the note we are passing the notes new content through the clean_notes function to remove any space or any \n charecter 
    if new_title: #now this block only works when the user gave any title if title is empty this line will not execute 
        if "|" in new_title: #this will check if the title contain | charecter if yes it will print the below message and if it does not contain this loop will not run 
            print("Title cannot contain '|'. Title unchanged.") #this message will be displayed if the new title contains | charecter 
        else: #this line will execute if the new title does not contain any | charecter 
            note[1]=new_title #and if the else loop will run then this line will simply replace the notes lists first index charecter which is the title itself with a new title whic the user gave 
    if new_content: #this loop will also run if the user enters a new content if it does not enter this line will not run 
        note[2] = new_content #then this line will replace the second index of the notes list with the new content which has been provided 
    write_notes(notes) #then after changing it or we can say altering the notes list we use the write_notes function to write the changes back into the notes and then to return it. like we are simply passing the new updated list as and argumment to the parameter above 
    print(f"Note {note_id} updated.") #then we are printing it that which note id has been updated 

def delete_note(notes):
    note_id = input("ID of the note to delete: ").strip()
    note = find_notes(notes, note_id)
    if not note:
        print("Note not found")
        return
    if input("Delete this note? (y/n): ").strip().lower()=="y":
        notes.remove(note)
        write_notes(notes)
        print(f"Note {note_id} deleted.")
    else:
        print("Cancelled.")

def main():
    notes = read_notes()
    actions = {
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": edit_note,
        "5": delete_note,
    }
    while True:
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
            break
        action = actions.get(choice)
        if action:
            action(notes)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


