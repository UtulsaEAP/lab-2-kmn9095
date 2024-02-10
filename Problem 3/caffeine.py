
def caffeine():
    
    
    ''' Type your code here. '''
    import math
    
    initial_quantity = float(input())
    caff_lvl6 = initial_quantity * (math.pow(0.5,1))
    caff_lvl12 = initial_quantity * (math.pow(0.5,2))
    caff_lvl24 = initial_quantity * (math.pow(0.5,4))

    
    print("After 6 hours:" " " + f'{caff_lvl6:.2f}' +  " " +'mg')
    print("After 12 hours:" " " + f'{caff_lvl12:.2f}' + " " + 'mg')
    print("After 24 hours:" " " f'{caff_lvl24:.2f}' + " " + 'mg')
    
    #your_value = x , y , z  
    #print(f'{your_value:.2f}')
if __name__ == "__main__":
    caffeine()