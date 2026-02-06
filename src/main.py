from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='C:\\Users\\m.lukinykh\\yp\\my_project\\.env')
def print_author():
	author=os.getenv('AUTHOR')
	print(f"Автор проекта: {author}")

print_author()
