import os
from dotenv import load_dotenv

# loads env variables
load_dotenv()

if 'TESTING' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL_TEST']
else:
    DATABASE_URL = os.environ['DATABASE_URL']

