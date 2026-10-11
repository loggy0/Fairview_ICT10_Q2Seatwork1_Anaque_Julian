# candidate Verification System
from pyscript import display, document

# list of club members (made-up names)
club_members = ["Jacob Kerman", "Kendrick Kerman", "Logan Kerman", "Enzo Kerman"]


def verify_candidate(event):
    # clears the result
    document.getElementById("result").innerHTML = ""

    # gets the first and last name from the user
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    # combine them into one full name (.title() matches the capital letters in the list)
    full_name = f"{first_name} {last_name}".title()

    # check if the full name is in the list; this stores True or False
    is_member = full_name in club_members

    # two possible messages: index 0 is for False, index 1 is for True
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the Aerospace club. See you at Kennedy Space Center!",
    ]

    # false counts as 0 and True counts as 1, so is_member picks the right message
    display(messages[is_member], target="result")