# py-password-generator-class
A Python Class made for generating random strong password having 
```
Uppercase A-Z, smallcase a-z, 
special characters !@#$%^&*()_+-= and numbers 0-9.
```
It can generate strong password.
By default it includes special characters and numbers in the generated password, but this can be turned off by using keyword arguments 
```
password_object.create_password(enable_specials = False, enable_numbers = False)
#this will return a default 8 character long string which will only have Uppercase and Small case characters
```

## Example 
```
password_for = 'instagram.com'

new_password_object = Password(password_for)
length = 12 
generated_password = new_password_object.create_password(length)
print(generated_password)
print(new_password_object.info)
```
#### OUTPUT: 
```
0^yC0Ib#Ud2@
{'password_for': 'instagram.com', 'password': '0^yC0Ib#Ud2@', 'special_characters': True, 'numbers': True}
```
