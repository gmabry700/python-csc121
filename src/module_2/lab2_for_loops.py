'''For-Loops'''

def main():
    # print(write_letter("Mario", "Princess Peach"))
    # print(write_letter("Luigi", "Princess Peach"))
    # print(write_letter("Daisy", "Princess Peach"))
    # print(write_letter("Yoshi", "Princess Peach"))
    #TODO: reduce the repetitiveness w/ a loop

    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # for i in range(len(names)):
    #     print(write_letter(names[i], "Princess Peach"))

    for name in names:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},
        
        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.
        
        Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()