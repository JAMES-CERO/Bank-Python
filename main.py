# Question 1:
# Send your loan requests to the bank manager: 
# The contact information for this bank manager is pulled from file where the fields are seperated by semicolons - let's split the string into specific values:
# bank_manager = "Mo;55;Los Angeles;MoSmith@email.com"
bank_manager = 'Mo;55;Los Angeles;MoSmith@email.com'
keys = ['name', 'age', 'location', 'e-mail']

values = bank_manager.split(';')
bank_managerDict = {}

for key, value in zip(keys, values):
  bank_managerDict[key] = value

def ContactInfo(**kwargs):
  for k, value in kwargs.items():
    print(f'{k}:{value}')


ContactInfo(**bank_managerDict)

