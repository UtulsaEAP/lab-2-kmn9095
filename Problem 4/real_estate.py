
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here

    price_change = ((current_price)-(last_month_price))
    mortgage= ((current_price * 0.051) / 12)

    print (f"This house is ${current_price}. The change is ${price_change} since last month.")
    print(f"The estimated monthly mortgage is ${mortgage:.2f}.")
if __name__ == "__main__":
    real_estate()