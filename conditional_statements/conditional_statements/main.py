# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday" 

# Step 1: Determine if the product type is "Fruits" and if the day of the week is "Monday"
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")

# Step 2: Determine if the product type is "Vegetables" and if the day of the week is "Tuesday"
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")

# Step 3: Determine if the product type is "Dairy" and if the day of the week is "Wednesday"
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")

# Step 4: Determine if the product type is something other than fruits, vegetables, or dairy
elif product_type == "Other":
    print("No discount available.")

# Step 5: Utilize an `else` statement to handle cases where the days or product types do not match any prior conditions
else:
    print("No special discounts today.")