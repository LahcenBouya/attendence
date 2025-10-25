attendees = input("Enter the names of attendees separated by comma....: ").split(", ")

for name in attendees:
    print(f"\n{name}\n")
    confirmed =  input("is this person attending? (yes or no): ").lower()
    if confirmed == "yes":
        print("attendance cofirmed!")
    else:
        print("attendance not confirmed!")
    print("-----------------")