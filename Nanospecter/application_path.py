from dotenv import load_dotenv
import os


load_dotenv()

TG_PATH = os.getenv("TG_PATH")
OPERA_GX_PATH = os.getenv("OPERA_GX_PATH")
GOOGLE_PATH = os.getenv("GOOGLE_PATH")

HELLO_ONE = os.getenv("HELLO_ONE")
HELLO_TWO = os.getenv("HELLO_TWO")
BYE_ONE = os.getenv("BYE_ONE")
BYE_TWO = os.getenv("BYE_ON")