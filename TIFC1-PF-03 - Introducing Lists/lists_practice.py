new_users = []

for x in range(5):
    new_users.append(input("Enter your first name: "))
    
for y in new_users:
    print(f"useradd {y}") # Send this command through to the Linux terminal

print("All users created.")
