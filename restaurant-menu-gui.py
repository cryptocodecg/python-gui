#sekarang kita ngerjain yang ini ya

from tkinter import *

import datetime
import timedelta

f = open('receipt.txt', 'a')
# f.write('\nHello world!')
# f.close()

# f = open('receipt.txt', 'r')
# contents = f.read()
# print(contents)
# f.close()


jakarta_time = datetime.datetime.now() + datetime.timedelta(hours=7)

# print("Today's date is {:%b, %d %Y}".format(jakarta_time))
print("Today's date is {:%Y-%b-%d %H:%M:%S}".format(jakarta_time))

jakarta_time_text = "Today's date is {:%Y-%b-%d %H:%M:%S}".format(jakarta_time)

f.write(jakarta_time_text)





total = 0

def clear():
  global total
  total = 0
  var1.set(0)
  var2.set(0)
  var3.set(0)
  var4.set(0)
  p.set(0)
  e.set(0)
  group_one.set(0)
  group_two.set(0)
  drop5.pack_forget()
  drop6.pack_forget()

def ShowChoice():
    print("You pay with ", end = "")
    print(p.get())
      
    if p.get() == "Cash":
      drop5.pack_forget()
      drop6.pack_forget()
    elif p.get() == "E-Wallet":
      drop6.pack()
      drop5.pack_forget()
    else:
      drop5.pack()
      drop6.forget()

def calc_price():
  global total
  
  order = []
  if var1.get() == 1:
    order.append("Pizza")
    number1 = int(clicked1.get())
    print("Pizza", number1)
    f.write("\nPizza")
    f.write(str(number1))
    total = total + (55000 * number1)
    labelPrice.config(text = "IDR " + str(total)) 
  if var2.get() == 1:    
    order.append("Soup")
    number2 = int(clicked2.get())    
    print("Soup", number2)
    total = total + (38000 * number2)
    labelPrice.config(text = "IDR " + str(total)) 
  if var3.get() == 1:
    order.append("Mineral Water")
    number3 = int(clicked3.get())
    print("Mineral Water", number3)
    total = total + (10000 * number3)
    labelPrice.config(text = "IDR " + str(total)) 
  if var4.get() == 1:
    order.append("Milk")
    number4 = int(clicked4.get())
    print("Milk", number4)
    total = total + (17000 * number4)
    labelPrice.config(text = "IDR " + str(total)) 

  if b.get() == "BCA":   
    print("Payment with BCA")
  elif b.get() == "BNI":   
    print("Payment with BNI")
  elif b.get() == "BRI":   
    print("Payment with BRI")
  elif b.get() == "MANDIRI":   
    print("Payment with MANDIRI")

  if e.get() == "Gopay":   
    print("Payment with Gopay")
  elif e.get() == "OVO":   
    print("Payment with OVO")
  elif e.get() == "Dana":   
    print("Payment with Dana")
  elif e.get() == "LinkAja":   
    print("Payment with LinkAja")
    
    
    
  print(order)
  print("Total purchase = IDR ", total)

  if total > 500000:
      print("After 10% discount: " + str(0.9 * total))
      labelDisc.config(text = "IDR " + str(0.9 * total))

  # if group_one.get() == 1:
  #   print("You pay with Debit/Credit Card")
  # elif group_one.get() == 2:
  #   print("You pay with cash")

  if group_one.get() == 1:
      drop5.pack()

  if group_two.get() == 1:
    print("You order to dine-in")
  elif group_two.get() == 2:
    print("You order to take away")
  elif group_two.get() == 3:
    print("You order to delivery")

  

ws1 = Tk()
ws1.title("Raii Restaurant")
ws1.geometry('640x310')

frame_one = LabelFrame(ws1, text='Food')
frame_one.grid(row=1, column=1, padx=10)
frame_two = LabelFrame(ws1, text='Drinks')
frame_two.grid(row=1, column=3)
frame_three = LabelFrame(ws1, text="Payment Method")
frame_three.grid(row=3, column=1, padx=10)
frame_four = LabelFrame(ws1, text="Order")
frame_four.grid(row=3, column=3)
frame_five = LabelFrame(ws1, text="")
frame_five.grid(row=4, column=1)
frame_six = LabelFrame(ws1, text="Number")
frame_six.grid(row=1, column=2)
frame_seven = LabelFrame(ws1, text="Number")
frame_seven.grid(row=1, column=4)
frame_eight = LabelFrame(ws1, text="Total Price")
frame_eight.grid(row=3, column=4)
frame_nine = LabelFrame(ws1, text="Discount")
frame_nine.grid(row=3, column=5)
frame_ten = LabelFrame(ws1, text="Bank")
frame_ten.grid(row=3, column=2)
frame_eleven = LabelFrame(ws1, text="Date")
frame_eleven.grid(row=5, column=1)


options = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10"
]

bank = [
  "Choose bank",
	"BCA",
  "BNI",
  "BRI",
  "MANDIRI"
]

b = StringVar()
b.set("Choose bank")

payment_opt = [
  "Credit Card",
  "Debit Card",
  "Cash",
  "E-Wallet"
]

p = StringVar()
p.set(0)

ewallet = [
  "Choose wallet"
  "Gopay",
  "OVO",
  "LinkAja",
  "Dana"
]

e = StringVar()
e.set("Choose wallet")

clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()


clicked1.set("1")
clicked2.set("1")
clicked3.set("1")
clicked4.set("1")



drop1 = OptionMenu(frame_six, clicked1, *options)
drop1.pack()
drop2 = OptionMenu(frame_six, clicked2, *options)
drop2.pack()
drop3 = OptionMenu(frame_seven, clicked3, *options)
drop3.pack()
drop4 = OptionMenu(frame_seven, clicked4, *options)
drop4.pack()

drop5 = OptionMenu( frame_ten, b, *bank )
drop5.pack_forget()

drop6 = OptionMenu( frame_ten, e, *ewallet )
drop6.pack_forget()

var1 = IntVar()
var2 = IntVar()


c1 = Checkbutton(frame_one, text='Pizza  IDR 55000',variable=var1, onvalue=1, offvalue=0, pady = 10).pack()
c2 = Checkbutton(frame_one, text='Soup  IDR 38000',variable=var2, onvalue=1, offvalue=0, pady = 10).pack()

var3 = IntVar()
var4 = IntVar()

c1 = Checkbutton(frame_two, text='Mineral Water  IDR 10000',variable=var3, onvalue=1, offvalue=0, pady = 10).pack()
c2 = Checkbutton(frame_two, text='Milk  IDR 17000',variable=var4, onvalue=1, offvalue=0, pady = 10).pack()


group_one = IntVar()
group_two = IntVar()
 
for payment in payment_opt:
    Radiobutton(frame_three, 
                   text=payment,
                   padx = 20, 
                   variable=p, 
                   command=ShowChoice,
                   value=payment).pack()
              

Radiobutton(frame_four, text='Dine-In', variable=group_two, value=1).pack()
Radiobutton(frame_four, text='Take Away', variable=group_two, value=2).pack()
Radiobutton(frame_four, text="Delivery", variable=group_two, value=3).pack()

labelPrice = Label(frame_eight, text = "")
labelPrice.pack()

labelDisc = Label(frame_nine, text = "")
labelDisc.pack()

labelDateTime = Label(frame_eleven, text = "")
labelDateTime.pack()

labelDateTime.config(text = jakarta_time_text)

submitBtn = Button(frame_five, text = "Submit", command = calc_price).pack()
clearBtn = Button(frame_five, text = "Clear", command = clear).pack()

# f.close()

ws1.mainloop()