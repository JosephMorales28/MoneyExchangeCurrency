print("\n\n\n\t\t\tWelcome to my Money Exchange Currency by Joseph Morales\n\n\n")

currency=['USD','JPN YEN','PESO','South Korean Won','EURO','CANADIAN DOLLAR','SAUDI RIYAL',"CHINESE YUAN"] 

for classcurrency in currency:
    classcurrency=input("what is your class Money:\n")
    if classcurrency in currency:
       print("Select Currency you want to exchange:")
       exchange=input()
       if exchange in currency:
          print("Enter amount of money you want to exchange")
          money=float(input())
          if exchange == currency[0]:
             usd=0.018
             amount=money*usd
             print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
             break
          elif exchange == currency[1] or exchange =='japan':
               japan=2.33
               amount=money*japan
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
               break
          elif exchange == currency[2] or exchange =='peso':
               peso=54.93
               amount=money*peso
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
               break
          elif exchange == currency[3] or exchange =='south korean won':
               skw=22.53
               amount=money*skw
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
               break
          elif exchange == currency[4] or exchange =='euro':
               euro=0.017
               amount=money*euro
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
               break
          elif exchange == currency[5] or exchange =='canadian dollar':
               cnd=0.024
               amount=money*cnd
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
               break
          elif exchange == currency[6] or exchange =='saudi riyal':
               riyal=0.068
               amount=money*riyal
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
          elif exchange == currency[7] or exchange =='chinese yuan':
               yuan=0.12
               amount=money*yuan
               print("the amount money of",money,classcurrency, "to", exchange, "is",amount)
    else:
        print("Invalid")
    break
