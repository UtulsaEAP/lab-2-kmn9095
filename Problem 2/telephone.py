#Name: Kelsey Nock
#Class : Friday 15:00 
def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    firstDig = str(int(phone_number / 10000000))
    print(firstDig)
    
    phone_number = phone_number % 10000000
    print(phone_number)
    
    middleDig = str(int(phone_number / 10000))
    
    lastDig = str(int(phone_number %10000))
    
    print("(" + firstDig + ") "+ middleDig + "-" + lastDig)
    
if __name__ == "__main__":
    telephone()