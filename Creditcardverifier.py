#this is a simple program which verifies the creditcard number using luhns algorithm 

while True:
    card_number=list(map(int,input("Enter the card number here")))
    if len(card_number)==16:
        break

checker=card_number.pop()
for x in range(14,-1,-2):
    card_number[x]*=2
    if card_number[x]/10>=1:
        card_number[x]=card_number[x]%10+1
new=sum(card_number)
new =(new*9)%10
if new ==checker:
    print("yes that is a valid card number")
else:   print("no that is not a valid card number")

    
        

