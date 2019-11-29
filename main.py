import datetime
import random
x = 0
y = 0

wordsList = ["keyboard","cat","house","street","nearby","whatever","microphone","pencil",
             "books","flower","calculator","going","purple","blue","magnificent",
             "around","world","python","chocolate","hungry","wallpaper","singing",
             "difficult","triangle","science","escape","directory","ladder",
             "confusing","number","chair","speaker","plane","motorcycle","backpack",
             "script","bed","technology"]
while x < 1:
    startMessage = input("Press Enter to begin test...\n")
    print("Rewrite below non-sense sentence and confirm it with Enter:")
    start = datetime.datetime.now()
    random.shuffle(wordsList)
    sentence = ' '.join(wordsList[:10])
    userSentence = input(' '.join(wordsList[:10]) + "\n")
    end = datetime.datetime.now()
    elapsed = end - start
    if userSentence.capitalize() == sentence.capitalize():
        # amount of words in sentence times 60 sec, divided by user time
        wordCount = (10 * 60) / elapsed.seconds
        print("Your score is", int(wordCount), "words per minute")
        x = 0
        y = 0
        while y < 1:
            repeat = input("Would you like to repeat the test? (y/n):\n")
            if repeat.lower() == "n":
                y = 1
                x = 1
            elif repeat.lower() == "y":
                y = 1
                x = 0
            else:
                print("Incorrect answer")
                y = 0
    else:
        print("\nYou have to write the sentence with no mistakes.")
        x = 0