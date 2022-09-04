import re
import sys
import pickle

class Person:
    def __init__(self, last, first, middle,id,phone):
        self.last = last
        self.first = first
        self.middle = middle
        self.id = id
        self.phone = phone

    def display(self):
        print("Employee id: " + self.id)
        print("\t" + self.first + " " + self.middle + " " + self.last)
        print("\t" + self.phone)
        print()

def main():
    if len(sys.argv) != 2:
        print("error need to specify path to input file")


    people = []
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f:
            people.append(line.strip())
    people.pop(0)


    output = {}
    for i in people:
        last, first, middle, id, number = i.split(",")
        # Format first and last names
        last = last.capitalize()
        first = first.capitalize()
        # Format middle intial
        if len(middle) == 0:
            middle = 'X'
        middle = middle.capitalize()
        if len(middle) > 1:
            middle = middle[0]

        # Check for valid ID
        while len(id) != 6 or not id[:2].isalpha() or not id[2:].isdigit():
            print("ID invalid: " + id)
            print("ID is two letters followed by 4 digits")
            id = input("Please enter a valid id: ")
        valid = False
        if len(number) == 10:
            if number.isdigit():
                number = number[0:3] + "-" + number[3:6] + "-" + number[6:]
        # Check phone numbers
        while not valid:
            match = "[0-9][0-9][0-9][\.][0-9][0-9][0-9][\.][0-9][0-9][0-9][0-9]"
            if re.match(match,number):
                valid = True
            match = match.replace("\.","\-")
            if re.match(match,number):
                valid = True
            match = match.replace("\-","\s")
            if re.match(match,number):
                valid = True
            if not valid:
                print("Phone " + number + " is invalid")
                print("Enter phone number in form 123-456-7890")
                number = input("Enter phone number: ")

        number = number.replace(" ", "-").replace(".","-")
        if id in output:
            print("Warning id " + id + "already used")
        output[id] = Person(last,first,middle,id,number)

    pickle.dump(output, open('Person.p', 'wb'))
    output = pickle.load(open('Person.p', 'rb'))

    print("\nEmployee list:\n")
    for id in output:
        output[id].display()


if __name__=="__main__":
    main()