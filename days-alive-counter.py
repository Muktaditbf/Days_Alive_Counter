import datetime

# 1. Ask for birth details (Convert to Number immediately)
birth_year = int(input("Enter Birth Year (e.g., 2000): "))
birth_month = int(input("Enter Birth Month (1-12): "))
birth_day = int(input("Enter Birth Day (1-31): "))

# 2. Set the dates
today = datetime.date.today()
birthday = datetime.date(birth_year, birth_month, birth_day)

# 3. Do the math (Subtract dates)
difference = today - birthday

# 4. Convert total days to years (approximate)
age = difference.days // 365 

print("You are approximately", age, "years old.")