Number = 1
Numberliste = []

while Number < 1000:
    if Number%3==0 or Number%5==0:
        Numberliste.append(Number)
    Number = Number + 1

print(Numberliste)
Answer = sum(Numberliste)
print(Answer)
