# 1. Først starter vi med at gamge 999 med 999.
# 2. Så gemmer vi produktet som en variabel(str), så reverser vi det også bruger vi if statement til at checke om det er det samme
# 3. Hvis ja så return value, hvis nej så minus med 1 på tal number 1 også bagefter number 2 også number 1 igen etc.


# To do list få numberene 1 og 2 variablen til at roterer mellem hinanden til at minusse med 1 så
# det går fra 999*999 til 998*999 til 998*998 osv...

Number1 = 999
Number2 = 999
TextAnswer = 0
ReverseTextAnswer = 0
Done = False

while Done is False:
    TextAnswer = Number1*Number2
    TextAnswer = str(TextAnswer)
    ReverseTextAnswer = TextAnswer[::-1]
    if TextAnswer == ReverseTextAnswer:
        print("Reverse " + ReverseTextAnswer, "Text answer " + TextAnswer)
        Done = True
    else:
        Number1 = int(Number1)
        Number2 = int(Number2)
        if Number1 > Number2:
            Number1 = Number1 - 1
        else:
            Number2 = Number2 - 1







