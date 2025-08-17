def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
    
    Returns:
        float: The final price after applying the discount if >= 20%, 
            otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final Price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
