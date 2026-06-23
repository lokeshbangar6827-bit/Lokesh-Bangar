units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

gst = bill * 0.18
total_bill = bill + gst

print("Bill Amount =", bill)
print("GST (18%) =", gst)
print("Total Bill =", total_bill)