
from tkinter import * 

base = Tk()  
base.geometry("500x500")  
base.title("Sign-up Page")  
  
lb1= Label(base, text="Enter your Name:", width=15, font=("arial",12))  
lb1.place(x=45, y=160) 

en1= Entry(base)  
en1.place(x=200, y=160)  
  
lb3= Label(base, text="Enter your Email:", width=15, font=("arial",12))  
lb3.place(x=45, y=160)  

en3= Entry(base)  
en3.place(x=200, y=160)  
  
lb4= Label(base, text="Your Contact Number:", width=15,font=("arial",12))  
lb4.place(x=45, y=200)  

en4= Entry(base)  
en4.place(x=200, y=200)  
  
lb5= Label(base, text="Select your Gender:", width=15, font=("arial",12))  
lb5.place(x=45, y=240)  
vars = IntVar()  

Radiobutton(base, text="Male", padx=10,variable=vars, value=1).place(x=180, y=240)  
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=240,y=240)   
  
list_of_cntry = ("Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Rep","Chad","Chile","China","Colombia","Comoros","Congo","Congo {Democratic Rep}","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland {Republic}","Israel","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea North","Korea South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar, {Burma}","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russian Federation","Rwanda","St Kitts & Nevis","St Lucia","Saint Vincent & the Grenadines","Samoa","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe")  
cv = StringVar()  

drplist= OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("India")  
lb2= Label(base, text="Select your Country", width=15,font=("arial",12))  
lb2.place(x=45,y=280)  
drplist.place(x=200, y=275)  
  
lb6= Label(base, text="Enter your Password", width=15,font=("arial",12))  
lb6.place(x=45, y=320)  
en6= Entry(base, show='.')  
en6.place(x=200, y=320)  
  
lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
lb7.place(x=45, y=360)  
en7 =Entry(base, show='.')  
en7.place(x=200, y=360)  
  
Button(base, text="Sign-up!", width=10).place(x=200,y=400)  
base.mainloop()  
