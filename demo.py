from dotenv import load_dotenv
load_dotenv()
import os

print(os.getenv('AWS_ACCESS_KEY_ID'))