def store_work():
    notes_date=input("Enter date: ")
    with open(f"C:\\Users\\hp\\Desktop\\File handling\\notes mananger\\{notes_date}.md","w") as file:
        file.write(f">>{notes_date}")
    run=1
    while True:
        notes_work=input(f"Enter {run} work of your day for no work type no:").strip().lower()
        if notes_work=="no":
            break
        notes_time=input(f"Enter time of today's {notes_work} with am/pm: ")
        with open(f"C:\\Users\\hp\\Desktop\\File handling\\notes mananger\\{notes_date}.md","a") as file:
            file.write(f"\n{run}. {notes_work} at {notes_time}")
        run+=1
def  previous_history():
    previous_date=input("Enter date for previous work: ")
    try:
        with open(f"C:\\Users\\hp\\Desktop\\File handling\\notes mananger\\{previous_date}.md","r") as file:
                file_=file.read()
                print(file_)
    except FileNotFoundError:
        print(f"invalid date is entered there is no any work on this {previous_date}")
import msvcrt
def get_input(length):
    text = ""
    while len(text) < length:
        char = msvcrt.getwch()
        if char == "\r":
            break
        print(char, end="", flush=True)
        text += char
    print()
    return text

print(f"Enter 1 for note some work \nEnter 2 for checking previous history:")
work=get_input(1)
match work:
    case"1":
        store_work()
    case"2":
        previous_history()