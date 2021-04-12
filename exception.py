try:
  #  print(10/0)
    if(10%2!=0):
        print("from if statement")
# print("General")
   #  else:
        #print("Inside try block")
        #break error outsside loop
        
         # type of error 

        
       
except(NameError):
     print("Name error  exception")


except(ZeroDivisionError):
     print("Division by zerror error")
else:     # we have esle block in exception handling it is executed when
           #the if block conditin inside try block fails
    print("From else  statement")
# finally block will execute always
finally:
    print("finally block is executed always:")
