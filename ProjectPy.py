import datetime
def book_type(type):

   
  if type=='E':
      print('Here the list of our English Books :\n 1-Cruel Prince(A) \n 2-Shadow and Bone(B) \n 3- Six of Crows(C) \n 4- Shatter me(D)')
  elif type=='A'  :
      print('Here is the list of our Arabic Books :\n 1-هيبتا (A)\n 2-لا تقولي انك خائفة (B)\n 3- فاتتني الصلاة (C)\n 4-  (D) العبرات')
  else:
      print('We do not have this type in our Bookstore')  





      


def book_floor(Result):
    if Result=='First shelf':
      print('it is in the Second Floor and the shelf is ',Result)
    elif Result =='Second shelf':
      print('it is in the First Floor and the shelf is',Result)
    elif Result=='Third shelf':
      print('it is in the basement and the shelf is ',Result)
    elif Result =='Fourth shelf':
      print('it is in the Third Floor and the shelf is ',Result)
    elif Result=='Fifth shelf':
      print('it is in the Fourth Floor and the shelf is ',Result)





def book_shelf(string):
    
    
    R1 ='First shelf'
    R2 ='Second shelf'
    R3 ='Third shelf'
    R4 ='Fourth shelf'
    R5 ='Fifth shelf'
    
   
    if string=='A':
      return  book_floor(R1)
    elif string=='B':
       return  book_floor(R2)
    elif string=='C' :
      return  book_floor(R3)
    elif string=='D':
       return  book_floor(R4)
    elif string=='F':
       return book_floor(R5)
    

def invoice (num):
  
   if num=='1':
      print('Red quen \n 45sr and the time is',datetime.datetime.now)
   elif num=='2':
      print('if cats disaooeard from the world \n 36sr and the time is ',datetime.datetime.now)
   elif num  =='3':
      print('before the coffe gets cold \n 50sr and the time is ',datetime.datetime.now)
           

def buy_book ():
 counter=0
 num  =' '
 while counter ==0:
  counter+=1
   
  num= print('We have some books for sale :\n 1- Reed queen (45sr) \n 2- if cats disaooeard from the world (36sr) \n 3- before the coffe gets cold (50) \n Enter the number of the book that you wants to buy it :')
 if num=='1':
    print('Thank you , here is your invoice :',invoice(num))
    
 elif num=='2':
      print('Thank you , here is your invoice :',invoice(num))
      
 elif num=='3':
      print('Thank you , here is your invoice :',invoice(num))
      
    

      




   



# Main code
print('Wellcome to Reema library \n We are here to help you to love reading more \n by: Reema Alhuwaishel')     
user_input = input('Choose What type of Books you like?\n (E)- For english books \n (A)- For Arabic books \n Enter The Letter : ')
book_type(user_input) 


user_input2 =print(input('Enter the code of the book you chose : '))
book_shelf(user_input2) 
buy_book()

print('I hope you are satisfied with our program \n ')
