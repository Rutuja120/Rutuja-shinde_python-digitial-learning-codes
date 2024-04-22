def print_sorted_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    print("Sorted Dictionary:")
    for name, phone in sorted_dict.items():
        print(f"{name}: {phone}")

def main():
    friends = {
        "shiva": "123-456-7890",
        "pratiksha": "987-654-3210",
        "sanika": "555-123-4567"
    }

    print_sorted_dict(friends)

    name = input("\nEnter a name to check if it's present in the dictionary: ")
    if name in friends:
        print(f"{name} is present in the dictionary. Phone number: {friends[name]}")
    else:
        phone = input("Enter the phone number for this friend: ")
        friends[name] = phone
        print(f"{name} and their phone number {phone} added to the dictionary.")

    print_sorted_dict(friends)

if __name__ == "__main__":
    main()
