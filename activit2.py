amount=int(input("enter the amount"))
note_100=amount//100 # FLOORDIVISION (quotient)
note50=(amount%100)//50
note10=((amount%100)%50)//10
print(f"the number of hundered rupees are {note_100}")
print(f"the number of fifty rupees are {note50}")
print(f"the number of ten rupees are {note10}")
