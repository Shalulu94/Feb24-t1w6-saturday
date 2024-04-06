full_name = input("Enter your full name: ")

company_name = input("Enter your company name: ")

full_name_format = full_name.replace(" ", ".")

company_name_format = company_name.replace(" ", "")

predicted_email = f"{full_name_format}@{company_name_format}.com.au".lower()

print(predicted_email)




#    print(f"Remaining attempts: {login_attempts}")