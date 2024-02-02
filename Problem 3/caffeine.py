
def caffeine():
    
    caffeine_mg = float(input())
    ''' Type your code here. '''
    half_life1 = caffeine_mg/2
    half_life2 = caffeine_mg/4
    half_life3 = caffeine_mg/8
    your_value = "After 6 hours: " + half_life1 + "mg", " After 12 hours: " + half_life2 + "mg", " After 24 hours:  " + half_life3 + "mg"
    print(f'{your_value:.2f}')
if __name__ == "__main__":
    caffeine()