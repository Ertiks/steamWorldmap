import os
from dotenv import load_dotenv

load_dotenv()

test_var = os.getenv("TEST_VAR")
print(test_var)