
# total_holes = [1,2,3,4,5,6]
total_putts = 0

gc_introduction = input("Welcome to GC mini golf! What is your name? ")
holes = input(f"Hi, {gc_introduction}. Would you like to play 3 or 6 holes today? " )

if holes not in ["3"]:
    holes = int(holes)
    for x in range(1, holes + 1):
        user_input = input(f"How many putts for hole {x}? (par is 3) ")
        try:
            user_input = int(user_input)
            total_putts += user_input
        except ValueError:
             print("The score you entered was invalid. Please try again.")
elif holes not in ["6"]:
    holes = int(holes)
    for x in range(1, holes + 1):
        user_input = input(f"How many putts for hole {x}? (par is 3) ")
        try:
            user_input = int(user_input)
            total_putts += user_input
        except ValueError:
            print("The score you entered was invalid. Please try again.")
# else:
#     print("Good try")
expectedPar = holes * 3
parScore = total_putts - expectedPar

if parScore > 0:
    print(f"Nice try, {gc_introduction}... Your total score was: {parScore}.")
elif parScore < 0:
        print(f"Great job, {gc_introduction}! Your total score was: {parScore}.")
else:
    print(f"Good game, {gc_introduction}. Your total score was: 0.")