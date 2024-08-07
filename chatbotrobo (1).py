import re
import numpy as np
import sys

greetings = ["hello", "hi", "hey"]
greetings_respo = [
    "hello",
    "hey",
    "hi",
    "hey, how are you?",
    "hi, how is your day?",
    "hello, how can I help you?",
]

greetings_with_quest = ["how are you", "your day", "whats up", "are doing", "you doing"]
greetings_with_quest_respo = ["all good! all going well", "yeah, just chilling!"]

personal = [
    "your age",
    "your religion",
    "you religious",
    "your salary",
    "your income",
    "love me",
    "you love",
    "love anyone",
]
personal_respo = ["seriously? you're asking this to a chatbot!", "it's a secret"]

living = ["you eat", "you drink", "your address", "you live", "you pee","poop"]
living_respo = [
    "why do you want to know this?!",
    "that's a secret",
    "excuse me! we're not that close!",
]

relevant = ["your name", "call you", "your good name"]
relevant_respo = ["I am robo", "you can call me robo", "my good name is robo"]

rude_words = [
    "angry",
    "shutup",
    "shut up",
    "you are bad",
    "kutta",
    "bc",
    "pagal",
    "pgl",
    "dont like you",
    "didn't like you",
    "hate you",
    "you mad",
]
rude_words_respo = [
    "oh, please don't talk to me like this!",
    "you will make me cry!",
    "please don't say this to me!",
]

love_words = ["love you", "loved your", "loved how you", "loved it"]
love_words_respo = ["awww!", "so sweet", "you are making me blush!"]

sad_words = [
    "am upset",
    "am not happy",
    "am feeling depressed",
    "am feeling upset",
    "am feeling sad",
    "am not feeling good",
]
sad_words_respo = [
    "oh! feeling sad for you",
    "please take care of yourself!",
    "don't worry, I am with you!",
]

about_robo = [
    "you happy",
    "you sad",
    "you upset",
    "you angry",
    "you feeling",
    "you fine",
]
about_robo_respo = [
    "I don't have any feelings! hahaha",
    "I am a robot, I don't have feelings!",
]

repeat_same = ["ok", "yes", "fine", "done", "yeah","seriously"]

exit_words = [
    "bye",
    "go now",
    "leave",
    "am leaving",
    "talk to you later",
    "am going",
    "exit",
]

good_words = ["am fine", "good", "nice", "great"]
good_words_respo = ["fab!", "that's great"]

invalid_respo = ["sorry! it's not in my knowledge", "sorry! I didn't get it"]

creator = ["created you", "your creator", "made you", "your owner"]
creator_respo = [
    "oh, actually I was created by Khushi Chadha",
    "Khushi Chadha created me, she is brilliant!",
]

sp_words=["sorry","thank you","welcome","thankyou","thanks"]
sp_words_respo=["its ok",
                "we are and friends dont use these words :) ",
                ]

print("******* Chat with me! ************")
print("Yes? (enter 'exit' to exit)")

user = ""
while user.lower() != "exit":
    user = input("You: ").lower()

    found = False

    for a in greetings_with_quest:
        if re.search(a, user):
            found = True
            print("robo:", np.random.choice(greetings_with_quest_respo))
            break
    if not found:
        for b in greetings:
            if re.search(b, user):
                found = True
                print("robo:", np.random.choice(greetings_respo))
                break
    if not found:
        for c in personal:
            if re.search(c, user):
                found = True
                print("robo:", np.random.choice(personal_respo))
                break
    if not found:
        for d in living:
            if re.search(d, user):
                found = True
                print("robo:", np.random.choice(living_respo))
                break
    if not found:
        for e in relevant:
            if re.search(e, user):
                found = True
                print("robo:", np.random.choice(relevant_respo))
                break
    if not found:
        for f in rude_words:
            if re.search(f, user):
                found = True
                print("robo:", np.random.choice(rude_words_respo))
                break
    if not found:
        for g in love_words:
            if re.search(g, user):
                found = True
                print("robo:", np.random.choice(love_words_respo))
                break
    if not found:
        for h in sad_words:
            if re.search(h, user):
                found = True
                print("robo:", np.random.choice(sad_words_respo))
                break
    if not found:
        for i in about_robo:
            if re.search(i, user):
                found = True
                print("robo:", np.random.choice(about_robo_respo))
                break
    if not found:
        for j in repeat_same:
            if re.search(j, user):
                found = True
                print("robo:", user)
                break
    if not found:
        for l in exit_words:
            if re.search(l, user):
                found = True
                print("robo:", "ok! If you need me, you can call me anytime.")
                sys.exit()
                break
    if not found:
        for k in good_words:
            if re.search(k, user):
                found = True
                print("robo:", np.random.choice(good_words_respo))
                break
    if not found:
        for m in creator:
            if re.search(m, user):
                found = True
                print("robo:", np.random.choice(creator_respo))
                break
    if not found:
        for n in sp_words:
            if re.search(n, user):
                found = True
                print("robo:", np.random.choice(sp_words_respo))
                break

    if not found:
        print("robo:", np.random.choice(invalid_respo))

 


 




