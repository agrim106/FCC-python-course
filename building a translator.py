from smtpd import DebuggingServer


#agrim language
#vowels -> q
#---------
#dog -> dqw
#cat -> cqt

def translate(phrase):
    translation = "" 
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "q"
        else:
            translation = translation + letter 
    return translation 

print(translate(input("Enter a phrase")))
