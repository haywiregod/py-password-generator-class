import random
class Password():
  '''
  A Password Genrator Class which accepts a string (which user can use to relate the genrated password)
  function create_password() creates a secure password
  '''
  min_length      = 6
  max_length      = 40
  default_length  = 8
  
  def __init__(self,password_for="password_for"):
    
    self.password_for = str(password_for)
    self.password  = False
    self.error        = False
    self.info         = {'password_for':self.password_for,'password':self.password}
    
  def create_password(self,length=default_length,**kwargs):
    '''
    Returna a string which will be the password or returns False if inappropritate length is given or if any other error occurs:\n
    Optional Paramters: length(Default is 8, Minimum length required is 6 and Maximum Length is 405)\n
    Key Word Argument: enable_special (enable special characters for password, default is True)\n
    Key Word Argument: enable_numbers (enable numbers for password, default is True)\n
    '''
    
    caps          = 'MNJIOKLPUHBVCFGTRDESWCXZAQ'
    small         = 'qwaszxerdfcvtyghbnjiuklmop'
    special       = '!@#$%^&*()_+-='
    numbers       = '1234567890'
    choices       = [caps,small]
    used_choices  = []
    password      = ''
    
    try:
      length = int(length)
    except:
      self.error = "Invalid length provided.\nInteger expected!" 
      return False
    
    if(length<Password.min_length or length >Password.max_length):
      self.error = f"Invalid length provided. Reuired Length should be ({Password.min_length} <= LENGTH <= {Password.max_length})" 
      return False
    
    
    if('enable_specials' in kwargs):
      if(kwargs['enable_specials']):
        choices.append(special)
        self.info['special_characters'] = True
      else:
        self.info['special_characters'] = False
    else:
      choices.append(special)
      self.info['special_characters'] = True
    
    if('enable_numbers' in kwargs):
      if(kwargs['enable_numbers']):
        choices.append(numbers)
        self.info['numbers'] = True
      else:
        self.info['numbers'] = False
    else:
      choices.append(numbers)
      self.info['numbers'] = True
    
    for _ in range(length):
      random_choice = random.choice(choices)
      while True:
        if(len(used_choices)==len(choices)):
          used_choices.clear()
        if(random_choice not in used_choices):
          used_choices.append(random_choice)
          break
        else:
          random_choice = random.choice(choices)
      password+=random.choice(random_choice)
      
    self.password = password
    self.info['password'] = self.password
    return self.password

password_for = 'instagram.com'

new_password_object = Password(password_for)
length = 12 
generated_password = new_password_object.create_password(length)
print(generated_password)
print(new_password_object.info)