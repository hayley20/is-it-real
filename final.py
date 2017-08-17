import time
import turtle
#creating pen
pen2 = turtle.Turtle()
#create paper
paper = turtle.Screen()
#put pen down




def write_letter(letter,pen,x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.write(letter, font = ("Comic Sans MS", 20, "normal"))

def boy():
    x=0
    y = 0
    signsseen=[]
    intro= ''' Your name is Mohammed. You are a junior in Highschool. You're a top athlete at your school; You have some
    honors or AP classes. This week is midterms, and each day you have 2 midterms that last about 2 hours in addition to homework
    assignments. The first midterm you have is English. You receive the midterm face down. Do you pick up the pencil or do you wait
    until everyone has received the test?'''

    pencil= ''' You concentrate and pace yourself well throughout the entire test. The essay was difficult but because of your good time
    management you were able to make corrections before the time was up.'''

    wait=''' You get distracted by the construction going on outside and only finish half of the test, failing it. This leads to a
    feeling of failure and insecurity.'''

    print(intro)
    signs=0
    beep = False
    while not beep:
        answer= input("Pick 'pencil' to begin the exam or pick 'wait' to wait: ")
        if answer== "pencil":
            print(pencil)
            beep= True
        elif answer=="wait":
            print(wait)
            beep= True
            signs+= 1
            signsseen.append("Be easily distracted")
            y = 20
            write_letter("A", pen2, x, y)
            x+=20
        else:
            print("Choose pencil or wait")

    lunch= '''You enter the cafeteria with your friends who quickly enter the lunch line. You stand with them but when it's your turn
    to take a tray, you don't. Your friend sees this and asks if you're ok. Do you lie to your friend or tell them the truth?'''

    lie= ''' You tell your friend that you are just trying to keep your weight down for wrestling and not to worry about you'''

    truth= ''' You tell your friend that you think you are overweight and that you need to lose 10 pounds'''

    time.sleep(5)
    print(lunch)
    beep= False
    while not beep:
        answer= input("Pick 'lie' to tell a lie and pick 'truth' to tell the truth: ")
        if answer=="lie":
            print(lie)
            beep= True
        elif answer=="truth":
            print(truth)
            beep= True
            signs+= 1
            signsseen.append("A relentless pursuit of thinness and unwillingness to maintain a normal or healthy weight")

        else:
            print("Choose lie or truth")

    midterm2= ''' You enter the library for the next midterm: calculus. You did not study before the exam so you feel nervous
    and frustrated. You then realize that you forgot your #2 pencils in the last midterm testing area and acting off of impulse you
    let out an exasperated cry. Do you politely apologize and ask the proctor for a pencil or do you angrily leave school?'''

    ask= ''' You apologize for your disruptive behavior and ask the proctor for a pencil. You have trouble with the test but
    finish in enough time for test corrections.'''

    leave= ''' You angrily leave the testing area and go home'''

    time.sleep(5)
    print(midterm2)
    signs+=1
    beep= False
    while not beep:
        answer= input("Pick 'ask' to ask for a pencil and pick 'leave' to leave the school: ")
        if answer== "ask":
            print(ask)
            beep= True
        elif answer=="leave":
            print(leave)
            beep= True
            signs+=1
            signsseen.append("anger or mood swings")
            y = 20
            write_letter("D", pen2, x, y)
            x+=20
        else:
            print("Choose ask or leave")

    home= ''' You come home to the smell of food in your kitchen and immediately feel sick. Your mom asks you if your ready to eat
    and you wince at the thought of eating. Do you sit down and eat or do you go do homework?'''

    eat=''' You eat a little bit of the food but then rush to the bathroom in the middle of dinner.'''

    homework= ''' You try to focus on your homework but instead end up doodling on the side of the paper.'''

    time.sleep(5)
    print(home)
    beep= False
    while not beep:
        answer= input("Pick 'eat' to eat and pick 'homework' to do homework: ")
        if answer== "eat":
            print(eat)
            beep= True
            signs+=1
            signsseen.append("Have problems sustaining attention in tasks")
        elif answer=="homework":
            print(homework)
            beep= True
            signs+=1
            signsseen.append("Extremely restricted eating")
            y = 20
            write_letter("H", pen2, x, y)
            x +=20
        else:
            print("Choose eat or homework")

    morning= ''' You wake up late due to the lack of sleep the night before
    and realize that you did not complete your homework the night before. Your parents have already left for work.
    You rush to get dressed and contemplate whether you should go to school or not. Do you go to school or skip? '''

    school= ''' You enter the next midterm; History. You briefly studied for this, but it will be easier
    because it is your favorite subject. The test isn't too difficult so you are feeling slightly better. The chemistry
    midterm is easy as well.'''

    skip= ''' You leave your house and go to the park where you get into a fight with a group of people
    in the park. You go home with bruises on your arms and torso.'''

    time.sleep(5)
    print(morning)
    beep= False
    while not beep:
        answer= input("Pick 'school' to go to school or pick 'skip' to skip school: ")
        if answer=="school":
            print(school)
            beep= True
        elif answer=="skip":
            print(skip)
            beep= True
            signs+=1
            signsseen.append("Avoid or dislike tasks that require sustained mental effort")
            y = 20
            write_letter("D", pen2, x, y)
            x += 20
        else:
            print("Choose school or skip")

    practice=''' Around 5 in the evening you go to wrestling practice. The coach tells you that he wants you to move to
    the next weight class up because he needs another good wrestler in that class. You feel uncomfortable with this. Do you
    agree with your coach or do you quit wrestling?'''

    agree=''' The coach tells you that you have to increase your intake of calories; you reluctantly agree.'''

    quit=''' You tell the coach that you unable to participate in the sport for any longer and run away.'''

    time.sleep(5)
    print(practice)
    beep= False
    while not beep:
        answer= input("Pick 'agree' to agree or pick 'quit' to quit wrestling: ")
        if answer=="agree":
            print(agree)
            beep= True
        elif answer=="quit":
            print(quit)
            beep= True
            signs+=1
            signsseen.append("Intense fear of gaining weight")
            print("Choose agree or quit")

    day3= '''Midterms are over. The results are handed back. When you get yours you quickly open the envelope and view your
    scores; Most of the grades are below your average testing score, disappointing you. Your parents are upset with you and
    in turn, you are even more upset with yourself. '''

    time.sleep(5)
    print(day3)

    time.sleep(5)
    end= input("Guess the word: ")
    if end == "adhd":
        print("correct!")
        print("How many signs did you come across?", signs)
        for value in signsseen:
            print(value)
    else:
        print("ADHD")
        print("How many signs did you come across?", signs)
        for value in signsseen:
            print(value)







#GIRL

def girl():
    x = 0
    y= 0

    intro = ''' Your name is Sarah. You are a junior in high school. You're a top student in mostly honors
    and AP classes. This week is midterms. You have 2 midterms a day, each is 2 hours,
    not to mention the homework you still have to complete each night. Your first
    midterm of the day is honors english. You've been procrastinating studying. The teacher
    hands out the test face down. You take a deep breath as you watch the clock.
    The test begins and it's multiple choice for the first half. You start
    shading in bubbles. All of a sudden you get stuck on question 41. You look around
    the room and see your classmates continuing their tests. Do you skip the question
    and move on or do you guess and hope for the best.'''

    guess = ''' You just can't seem to refocus and start to look around the room.
    As you watch your classmates continue to fill out their tests you begin to feel
    as though you'll never finish. You look at the clock and panic even more. Even
    though you're almost halfway done with the test, seeing the clock read about an
    hour left in the test has you panicked. You take a deep breath and force yourself
    to rush through the rest of the multiple choice to get to the essay section.'''

    skip = ''' You finish the rest of the multiple choice and come back to the question.
    You just don't know the answer so you close your eyes and pick a random letter.'''

    print(intro)
    signs = 0
    beep = False
    while not beep:
        answer= input("To choose type guess or skip: ")
        if answer == "guess":
            print(guess)
            beep = True
            signs += 1
            my_signs.append("panic and inability to focus")
        elif answer == "skip":
            print(skip)
            beep = True
        else:
            print("Choose guess or skip")

    lunch_intro = '''
    It's now lunch. You're very nervous about the results of that midterm, so you throw yourself into studying
    for the next one: AP calculus. Your friend Mandy sees you rush by the table, food in hand and calls
    out to you. You try to ignore her but she follows you. You're already so anxious for your
    next test, do you really have to talk to her. Do you either talk to her for a hot second, or tell her
    you have no time and you need to study.'''

    talk = '''
    Mandy catches up with you. She asks what's wrong. All of a sudden you feel very overwhelmed by the need
    to tell her how you've been feeling as of late. But then you feel guilty, you don't want to
    put your problems on her. You lie and tell her everything is fine, you just need to study.
    Mandy looks confused. She asks why you would need to study, since you're the top student
    in the class. Instantly you get frustrated. This is taking time away from studying.
    You say goodbye to Mandy and hurry off to find a place to study.'''

    study = '''
    Your temper flashes when you tell Mandy you are busy. She calls you a bitch, scoffs and walks back to your table of friends.
    You stalk away to find a place to study'''

    time.sleep(5)
    print(lunch_intro)
    beep = False
    while not beep:
        answer= input("Please type 'talk' to talk to Mandy or 'study' to get away from Mandy: ")
        if answer == "talk":
            print(talk)
            beep = True
            signs += 1
            my_signs.append("guilt and frustration at minor things")
            y = 20
            write_letter("D", pen2, x,y)
            x+= 20
        elif answer == "study":
            print(study)
            beep = True
        else:
            print("Choose talk or study")

    calculusintro = '''
    After going over some more practice problems you feel much better. You walk to your seat.
    You used to love math, in fact it's your best subject but today you just feel so tired
    and you're not really looking forward it. You feel plenty confident you'll pass though that's for sure.
    During the test you start to develop a migraine. Do you excuse yourself to go to the nurse taking time away from the test
    or stay and push through'''

    nurse = '''
    You go to the nurse but when you get there they tell you to lie down before giving you any advil.
    This causes you to miss the rest of the test and fail your midterm.'''

    stay = '''
    You make it through the test but you still have a headache. You rush down to the nurse's office
    only to find the door locked and the lights off. You go to wait for the bus to take you home'''

    time.sleep(5)
    print(calculusintro)
    signs += 1
    beep = False
    midtermfail = True
    my_signs.append("migraine")
    y = 20
    write_letter("E", pen2, x,y)
    x += 20
    while not beep:
        answer= input("Please type 'nurse' to go to the nurse or 'stay' to continue the test: ")
        if answer == "nurse":
            print(nurse)
            beep = True
            midtermfail = True
        elif answer == "stay":
            print(stay)
            beep = True
            midtermfail = False
        else:
            print("Choose nurse or stay")

    homeintro = '''
    Life at home only seems to be getting hard to balance with school. Your parents
    are getting on your case to get a job and always about the slightest drop in a grade.
    Your parents watch over you like a hawk, every missed assignment is garenteed to end up with you grounded.
    You know midterm grades won't be out for a couple days, and you want to hang out
    with your friends. You've been studying for physics and history for weeks.
    You contemplate asking for a night out with friends or just staying home and studying.'''

    studying = '''
    Your parents burst into your room to give you the lecture about helping around the house and
    paying for college. You end up bursting into tears out of frustration. You're constantly told you're overreacting
    but lately it feels less like an overreaction and more genuine feelings. Now you can't focus
    and you decide to go to bed with your homework incomplete. '''

    friends = '''
    Your parents say no and you end up staying home studying and doing homework. '''


    time.sleep(5)
    print(homeintro)
    beep = False
    while not beep:
        answer= input("Please type 'studying' to stay home and study, or 'friends' to go out with friends: ")
        if answer == "studying":
            print(studying)
            beep = True
            signs += 1
            y = 20
            write_letter("P", pen2, x,y)
            x += 20
            my_signs.append("frustration")
        elif answer == "friends":
            print(friends)
            beep = True
        else:
            print("Choose friends or studying")



    day2_intro = '''
    Last night was spent tossing and turning. You got maybe an hour of sleep
    meaning you're not ready for today's finals. When you get to school you head to
    the library to do more studying. History is not your best subject so you
    know you'll be studying through lunch.'''

    physics_intro = '''
    As you sit down for yet another 2 hour honors test your mind wanders.
    You don't realize when the teacher says to begin the test. You waste half an hour
    not doing anything. When you do finally realize you rush through the test, not doing your
    best work. You can just feel yourself picking the wrong answers but your priority
    is to actually finish the test. Your mind keeps wandering, do you ask to be excused
    or do you stay and finish the test.'''

    finish = '''
    You end up not finishing the test because you find yourself so overwhelmed.
    You start to breath harder and faster, the room starts to feel smaller. You start
    to shake and look around the room. You rush out of the room. '''

    leave = '''
    You take a quick trip to the bathroom where you recollect yourself. You end up
    finishing the test with enough time to check and change some answers.'''

    time.sleep(5)
    print(day2_intro)
    time.sleep(5)
    print(physics_intro)
    beep = False
    signs +=2
    my_signs.append("lack of sleep")
    my_signs.append("inability to focus")
    y = 20
    write_letter("R", pen2, x, y)
    x += 20

    write_letter("E", pen2, x,y)
    x+=20
    midterm_fail = True
    while not beep:
        answer= input("Please type 'finish' to stay and finish the test, or 'leave' to be excused: ")
        if answer == "finish":
            print(finish)
            beep = True
            signs += 1
            midterm_fail= True
            my_signs.append("panic attack")
        elif answer == "leave":
            print(leave)
            beep = True
            midterm_fail= False
        else:
            print("Choose leave or finish")

    lunch2 = '''
    you decide you've studied enough but because of the fight with Mandy you're unsure
    that you can sit with your friends. You pass the table hoping that someone asks you to
    sit down but no one does. Just as well you needed to study anyway. As you're walking through
    the halls you bump into Jenny. As you're both apologizing you recognize each other. Do you catch up or brush her off?'''

    catchup = '''
    You guys have a great conversation about school and what's new. You find out she too
    has a history final next so you end up studying together.'''

    brushoff  = '''
    You explain you have to study for history. She reveals that she does too so you end up sitting
    together studying separately. You're glad for the company while you get lost in thought. '''

    time.sleep(5)
    print(lunch2)
    beep = False
    while not beep:
        answer= input("Please type 'catchup' to talk to Jenny or 'brushoff' to go study: ")
        if answer == "catchup":
            print(catchup)
            beep = True
        elif answer == "brushoff":
            print(brushoff)
            beep = True
        else:
            print("Choose brushoff or catchup")

    day3_intro = '''
    Midterms are over. A few days have passed and now grades are out.'''

    fail = '''
    Your parents find out you failed your midterm. They start yelling at you about
    how disappointed they are and how you aren't even trying. They also call you some
    very rude names making you feel even worse. You run out of the house crying.'''

    ace = '''
    You passed midterms but your problems haven't gone away. Life is still extremly stressful.'''


    if midtermfail or midterm_fail == True:
        print(fail)

    else:
        print(ace)

    end= input("Guess what the word is?: ")
    if end == "depression":
        print(signs)
        for value in my_signs:
            print(value)
    else:
        print("depression")
        print(signs)
        for value in my_signs:
            print(value)

my_signs=[]
character = input("Choose your character. Pick boy or girl: ")
if character == "boy":
    boy()
elif character == "girl":
    girl()
else:
    print("Choose boy or girl")
