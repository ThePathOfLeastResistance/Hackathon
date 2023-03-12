

end = False
goal = int(input("Total Amount Of Hours Wished To Achieve : "))

while end == False:
    volunter = []
    total = 0

    place = input("The Place You Are Volunteering : ")
    numofday = input(f"The Number Of Day Volunteering at {place} : ")
    day = 0
    for i in range(0,int(numofday)):
        num = 0
        day += 1
        numofdayhour = input(f"How Many Hours On Day {day}: ")
        num += int(numofdayhour)
        total += int(numofdayhour)
    d = f"{place}:{num}\n"
    volunter.append(d)

    print(f"Number Of Hours Left To Complete Goal : {goal-total}")
    if goal <= total:
        print("Well Done, You have Completed Your Goal")
        print(volunter)
        end = True