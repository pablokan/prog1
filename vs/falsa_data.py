from faker import Faker

fake = Faker()
print(dir(fake))
for x in range(10):
    print(fake.city(), fake.country())

print(fake.words())

for x in range(10):
    print(fake.first_name())
