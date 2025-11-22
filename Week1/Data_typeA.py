
# String: Stores text inside quotes
name = "John Doe"

# Integer: Whole number without decimal
age = 28

# List: Ordered, changeable collection of items
skills = ["Python", "SQL", "Power BI"]

# Tuple: Ordered, unchangeable collection
education = ("BSc Computer Science", 2020)

# Dictionary: Key-value pairs for structured information
contact_details = {
    "email": "john.doe@example.com",
    "phone": "+64 222 444 555"
}

# Set: Unordered collection with unique values (duplicates removed automatically)
certifications = {"Azure", "AWS", "Azure"}  # "Azure" appears twice but set keeps one

# Printing the table
print("Component\t\tData Type\tExample")
print("---------------------------------------------------------------")
print(f"Name\t\t\tString\t\t{name}")
print(f"Age\t\t\tInteger\t\t{age}")
print(f"Skills\t\t\tList\t\t{skills}")
print(f"Education\t\tTuple\t\t{education}")
print(f"Contact Details\tDictionary \t{contact_details}")
print(f"Certifications\tSet\t\t{certifications}")
