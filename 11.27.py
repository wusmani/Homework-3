roster_dict = {}

for i in range(5):
    print("Enter player" + str (i + 1) + ";s jersey number:")
    jersey = int(input())
    print("Enter player" + str(i + 1)+ "'s rating:")
    rating = int(input())
    roster_dict[jersey] = rating

print('ROSTER')
for i in sorted(roster_dict.keys()):
    print('Jersey number: '+ str(i) + ', Rating: ' + str(roster_dict[i]))

while True:
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output Roster')
    print('q - Quit')
    choice = input('Choose an option: ')

    if choice == 'o':
        print("ROSTER")
        for i in sorted(roster_dict.keys()):
            print('Jersey number:' + str(i) + ', Rating: ' + str(roster_dict[i]))

    if choice == 'a':
        print("Enter a new player's jersey number: ")
        jersey = int(input())
        print("Enter player's rating: ")
        rating = int(input())
        roster_dict[jersey] = rating

    if choice == "d":
        print("Enter a jersey number: ")
        jersey = int(input())
        roster_dict.pop(jersey)

    if choice =='u':
        print("Enter a jersey number: ")
        jersey = int(input())
        print("Enter a new rating for player: ")
        rating = int(input())
        roster_dict[jersey] = rating

    if choice =='r':
        print('Enter a rating: ')
        rating = int(input())
        print('\nABOVE 5')

        for i in roster_dict.keys():
            if roster_dict[i]> rating:
                print('Jersey number: '+ str(i)+", Rating:" + str(roster_dict[i]))

                if choice == 'q':
                    break

