from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate fake data
name = fake.name()
address = fake.address()
phone_number = fake.phone_number()
birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
email = fake.email()

# Print the fake data
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Phone Number: {phone_number}")
print(f"Birthday: {birthday}")
print(f"Email: {email}")
