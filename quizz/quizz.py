baguette = 0
breadstick = 0
white = 0
pita = 0

print("First things first, pick some clothes: (b)asic tee, (v)intage print, (d)ress with pockets, (w)arm hoodie.")
answer1 = input()
if answer1 == 'b':
    white+=1
elif answer1 == 'v':
    baguette+=1
elif answer1 == 'd':
    pita+=1
elif answer1 == 'w':
    breadstick+=1
else:
    print("not an answer. NEXT QUESTION")
print("Which drink do you prefer? (t)ea, (l)emonade, (s)oda, (c)offee")
answer2 = input()
if answer2 == 't':
    pita+=1
elif answer2 == 'c':
    baguette+=1
elif answer2 == 'l':
    breadstick+=1
elif answer2 == 's':
    white+=1
else:
    print("not an answer. NEXT QUESTION")
print("Which country would you rather eat fish? (u)k, (n)ew zealand, (j)apan, (p)ortugal")
answer3 = input()
if answer3 == 'u':
    breadstick+=1
elif answer3 == 'n':
    baguette+=1
elif answer3 == 'j':
    white+=1
elif answer3 == 'p':
    pita+=1
else:
    print("not an answer. NEXT QUESTION")
print("which food would you rather eat for dinner? (s)teak, (p)izza, (t)acos, (n)othing")
answer4 = input()
if answer4 == 's':
    white+=1
elif answer4 == 'p':
    baguette+=1
elif answer4 == 't':
    pita+=1
elif answer4 == 'n':
    breadstick+=1
else:
    print("not an answer. NEXT QUESTION")
print("Whats for breakfast? (p)ancakes, (c)offee, (w)hat's breakfast, (i) am asleep")
answer5 = input()
if answer5 == 'p':
    white+=1
elif answer5 == 'c':
    baguette+=1
elif answer5 == 'w':
    breadstick+=1
elif answer5 == 'i':
    pita+=1
else:
    print("not an answer. NEXT QUESTION")
print("What is your favorite kind of bread. (b)aguette, (w)hite, b(r)eadstick), (p)ita")
answer6 = input()
if answer6 == 'w':
    white+=1
elif answer6 == 'r':
    baguette+=1
elif answer6 == 'p':
    breadstick+=1
elif answer6 == 'b':
    pita+=1
else:
    print("not an answer. NEXT QUESTION")
print("FINAL QUESTION: on a scale of 1 to 4, where 1 means 'love it' and 4 means 'would kill for it', how much do you like bread")
answer7 = input()
if answer7 == 1:
    breadstick+=1
elif answer7 == 2:
    baguette+=1
elif answer7 == 3:
    white+=1
elif answer7 == 4:
    pita+=1
#what bread r u
if baguette > breadstick and baguette > white and baguette > pita:
    print("you are baguette")
elif breadstick > baguette and breadstick > white and breadstick > pita:
    print("you are breadstick")
elif white > baguette and white > breadstick and white > pita:
    print("you are white")
elif pita > baguette and pita > breadstick and pita > white:
    print("you are pita")
else:

    for i in range(1000):
        print("you are the bread lord")