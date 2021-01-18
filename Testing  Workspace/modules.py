#A module is basically a file containg a set of functions to include in your application
#There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


#core modules
import datetime
from datetime import date
import time
from time import time

today = date.today()
timestamp = time()

print(f'{today} {timestamp}')

#pip module
#import camelcase

#import custom module

import validator
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print('email is valid')
else:
    print('bad email')