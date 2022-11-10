from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_sekuwa.set('0')
    e_momo.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_thakali.set('0')
    e_plain_rice.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_Hot_Chocolate.set('0')
    e_afocado.set('0')
    e_peach_iced_tea.set('0')
    e_blue_ocean.set('0')
    e_masalatea.set('0')
    e_vanilla_latte.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    text.config(state=DISABLED)
    textsekuwa.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textthakali.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textplain_rice.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textblue_ocean.config(state=DISABLED)
    textafocado.config(state=DISABLED)
    textpeach_iced_tea.config(state=DISABLED)
    textvanilla_latte.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textHot_Chocolate.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')




def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='#F4DEDE')
        root2.geometry('485x620+50+50')

        logoImage=PhotoImage(file='sender.png')
        label=Label(root2,image=logoImage,bg='lightblue')
        label.pack(pady=5)

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='#4F799F')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='#4F799F')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        if costofcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='#4F799F',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_momo.get()!='0':
            textReceipt.insert(END,f'momo\t\t\t{int(e_momo.get())*100}\n\n')

        if e_sekuwa.get()!='0':
            textReceipt.insert(END,f'sekuwa\t\t\t{int(e_sekuwa.get())*60}\n\n')

        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')

        if e_plain_rice.get() != '0':
            textReceipt.insert(END, f'plain_rice:\t\t\t{int(e_plain_rice.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

        if e_thakali.get() != '0':
            textReceipt.insert(END, f'thakali:\t\t\t{int(e_thakali.get()) * 40}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_Hot_Chocolate.get() != '0':
            textReceipt.insert(END, f'Hot_Chocolate:\t\t\t{int(e_Hot_Chocolate.get()) * 80}\n\n')

        if e_peach_iced_tea.get() != '0':
            textReceipt.insert(END, f'peach_iced_tea:\t\t\t{int(e_peach_iced_tea.get()) * 30}\n\n')

        if e_blue_ocean.get() != '0':
            textReceipt.insert(END, f'blue_ocean:\t\t\t{int(e_blue_ocean.get()) * 40}\n\n')

        if e_afocado.get() != '0':
            textReceipt.insert(END, f'afocado:\t\t\t{int(e_afocado.get()) * 60}\n\n')

        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

        if e_vanilla_latte.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_vanilla_latte.get()) * 50}\n\n')

        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n\n')

        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 620}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 700}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_momo.get())
        item2=int(e_sekuwa.get())
        item3=int(e_fish.get())
        item4 = int(e_sabji.get())
        item5 = int(e_thakali.get())
        item6 = int(e_plain_rice.get())
        item7 = int(e_mutton.get())
        item8 = int(e_paneer.get())
        item9 = int(e_chicken.get())

        item10 = int(e_lassi.get())
        item11 = int(e_coffee.get())
        item12 = int(e_Hot_Chocolate.get())
        item13 = int(e_peach_iced_tea.get())
        item14 = int(e_blue_ocean.get())
        item15 = int(e_afocado.get())
        item16 = int(e_masalatea.get())
        item17 = int(e_vanilla_latte.get())
        item18 = int(e_coldrinks.get())

        item19 = int(e_oreo.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())
        item22 = int(e_vanilla.get())
        item23 = int(e_banana.get())
        item24 = int(e_brownie.get())
        item25 = int(e_pineapple.get())
        item26 = int(e_chocolate.get())
        item27 = int(e_blackforest.get())

        priceofFood=(item1*100)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

        priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofcakesvar.set(str(priceofCakes)+ ' Rs')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')



def momo():
    if var1.get()==1:
        text.config(state=NORMAL)
        text.delete(0,END)
        text.focus()
    else:
        text.config(state=DISABLED)
        e_momo.set('0')

def sekuwa():
    if var2.get()==1:
        textsekuwa.config(state=NORMAL)
        textsekuwa.delete(0,END)
        textsekuwa.focus()

    else:
        textsekuwa.config(state=DISABLED)
        e_sekuwa.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def thakali():
    if var5.get() == 1:
        textthakali.config(state=NORMAL)
        textthakali.focus()
        textthakali.delete(0, END)
    elif var5.get() == 0:
        textthakali.config(state=DISABLED)
        e_thakali.set('0')


def plain_rice():
    if var6.get() == 1:
        textplain_rice.config(state=NORMAL)
        textplain_rice.focus()
        textplain_rice.delete(0, END)
    elif var6.get() == 0:
        textplain_rice.config(state=DISABLED)
        e_plain_rice.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def hot_chocolate():
    if var12.get() == 1:
        textHot_Chocolate.config(state=NORMAL)
        textHot_Chocolate.focus()
        textHot_Chocolate.delete(0, END)
    elif var12.get() == 0:
        textHot_Chocolate.config(state=DISABLED)
        e_Hot_Chocolate.set('0')


def peach_iced_tea():
    if var13.get() == 1:
        textpeach_iced_tea.config(state=NORMAL)
        textpeach_iced_tea.focus()
        textpeach_iced_tea.delete(0, END)
    elif var13.get() == 0:
        textpeach_iced_tea.config(state=DISABLED)
        e_peach_iced_tea.set('0')


def blue_ocean():
    if var14.get() == 1:
        textblue_ocean.config(state=NORMAL)
        textblue_ocean.focus()
        textblue_ocean.delete(0, END)
    elif var14.get() == 0:
        textblue_ocean.config(state=DISABLED)
        e_blue_ocean.set('0')


def afocado():
    if var15.get() == 1:
        textafocado.config(state=NORMAL)
        textafocado.focus()
        textafocado.delete(0, END)
    elif var15.get() == 0:
        textafocado.config(state=DISABLED)
        e_afocado.set('0')


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')


def vanilla_latte():
    if var17.get() == 1:
        textvanilla_latte.config(state=NORMAL)
        textvanilla_latte.focus()
        textvanilla_latte.delete(0, END)
    elif var17.get() == 0:
        textvanilla_latte.config(state=DISABLED)
        e_vanilla_latte.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')



root=Tk()

root.geometry('1370x790+0+0')

root.resizable(0,0)

root.title(' Ohana Billing System created by Shiv Uchiha')

root.config(bg='#4F799F')

topFrame=Frame(root,bd=10,relief=SUNKEN,bg='#FAF0E6')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Ohana Billing System',font=('arial',30),fg='#4F799F',bd=9,
                 bg='#F4DEDE',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=5,relief=SUNKEN,bg='#F4DEDE')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=SUNKEN,bg='#F4DEDE',pady=5)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='delicacies',bg="#F4DEDE",font=('arial',19,'bold'),bd=10,relief=SUNKEN,fg='#4F799F',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='beverages',bg="#F4DEDE",font=('arial',19,'bold'),bd=10,relief=SUNKEN,fg='#4F799F')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='cakes',bg="#F4DEDE",font=('arial',19,'bold'),bd=10,relief=SUNKEN,fg='#4F799F')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RAISED,bg="#F4DEDE")
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RAISED,bg="#F4DEDE")
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RAISED,bg="#F4DEDE")
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RAISED,bg="#F4DEDE")
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_momo=StringVar()
e_sekuwa=StringVar()
e_sabji = StringVar()
e_plain_rice = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_thakali = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi=StringVar()
e_coffee = StringVar()
e_Hot_Chocolate = StringVar()
e_peach_iced_tea = StringVar()
e_afocado = StringVar()
e_blue_ocean = StringVar()
e_masalatea = StringVar()
e_vanilla_latte = StringVar()
e_coldrinks = StringVar()

e_oreo=StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_momo.set('0')
e_sekuwa.set('0')
e_sabji.set('0')
e_fish.set('0')
e_thakali.set('0')
e_plain_rice.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_Hot_Chocolate.set('0')
e_afocado.set('0')
e_peach_iced_tea.set('0')
e_blue_ocean.set('0')
e_masalatea.set('0')
e_vanilla_latte.set('0')
e_coldrinks.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##FOOD

momo=Checkbutton(foodFrame,text='Momo',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=momo)
momo.grid(row=0,column=0,sticky=W)

sekuwa=Checkbutton(foodFrame,text='sekuwa',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=sekuwa)
sekuwa.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

thakali=Checkbutton(foodFrame,text='thakali',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=thakali)
thakali.grid(row=4,column=0,sticky=W)

plain_rice=Checkbutton(foodFrame,text='plain_rice',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=plain_rice)
plain_rice.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold',),onvalue=1,offvalue=0,variable=var9
                    ,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

text=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_momo)
text.grid(row=0,column=1)

textsekuwa=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sekuwa)
textsekuwa.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textthakali = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_thakali)
textthakali.grid(row=4, column=1)

textplain_rice = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_plain_rice)
textplain_rice.grid(row=5, column=1)

textmutton = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

hot_chocolate=Checkbutton(drinksFrame,text='Hot Chocolate',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=hot_chocolate)
hot_chocolate.grid(row=2,column=0,sticky=W)

peach_iced_tea=Checkbutton(drinksFrame,text='peachicedtea',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=peach_iced_tea)
peach_iced_tea.grid(row=3,column=0,sticky=W)

blue_ocean=Checkbutton(drinksFrame,text='blue_ocean',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=blue_ocean)
blue_ocean.grid(row=4,column=0,sticky=W)

afocado=Checkbutton(drinksFrame,text='afocado',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=afocado)
afocado.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

vanilla_latte=Checkbutton(drinksFrame,text='vanilla latte',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=vanilla_latte)
vanilla_latte.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textHot_Chocolate = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Hot_Chocolate)
textHot_Chocolate.grid(row=2, column=1)

textpeach_iced_tea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_peach_iced_tea)
textpeach_iced_tea.grid(row=3, column=1)

textblue_ocean = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_blue_ocean)
textblue_ocean.grid(row=4, column=1)

textafocado = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_afocado)
textafocado.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textvanilla_latte = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla_latte)
textvanilla_latte.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=banana)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=brownie)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Black Forest',bg="#F4DEDE",fg="#4F799F",font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#F4DEDE',fg='#4F799F')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),bg="black",fg="#F4DEDE",bd=6,padx=10,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),bg="black",fg="#F4DEDE",bd=6,padx=10
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),bg="black",fg="#F4DEDE",bd=6,padx=10
                  ,command=save)
buttonSave.grid(row=0,column=2)

##buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),bg="black",fg="#F4DEDE",bd=4,padx=5,command=send)
##buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),bg="black",fg="#F4DEDE",bd=6,padx=10,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='#F4DEDE',bg='#4F799F',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='#F4DEDE',bg='#4F799F',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='#F4DEDE',bg='#4F799F',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='#F4DEDE',bg='#4F799F',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='#F4DEDE',bg='black',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop() 