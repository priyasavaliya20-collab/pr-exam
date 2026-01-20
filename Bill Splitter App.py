while True:
  print("Welcome to the Bill Splitter App!")
  print("------------------------------------")
   
  while True:
     bill = float(input("Enter total bill amount: "))
     if bill <= 0:
        print("Bill amount is not negative.")
     else:
        break

  while True:
     total = int(input("Enter number of people: "))
     if total <= 0:
          print("People must be more than 0.")
     else:
        break        

      
       
        

  while True:
    tip = int(input("Enter tip percentage (0/5/10/15/20): "))
    if tip not in [0, 5, 10, 15, 20]:
          print("Invalid tip%.")
    else:
     break

  tip_amount = (tip/100)*bill
  total_bill = bill+tip_amount
  per_person = total_bill/total

  print("Tip Amount: $","%.2f" % tip_amount)
  print("Total bill : $","%.2f" % total_bill)
  print("One person pay amount: $","%.2f" % per_person)



  again = input("\nwould you like to calculate another bill?  (y/n): ")
  if again != 'y':
      print("THANKS FOR COMING. VISIT AGAIN!")
      break
