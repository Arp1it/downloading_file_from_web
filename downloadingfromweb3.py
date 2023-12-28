import urllib.request, termcolor

url = input(termcolor.colored("[+] Enter url: ", "green"))
filename = input(termcolor.colored("[+] Enter filname (without extention): ", "green"))
filextnsion = input(termcolor.colored("[+] Enter file extention (without dot(.)): ", "green"))

try:
    print(termcolor.colored("[+] Downloading started (stay connected with internet)", "yellow"))
    urllib.request.urlretrieve(url, f"{filename}.{filextnsion}")
    print(termcolor.colored("\n[+] Downloaded successfully!", "green"))

except Exception as e:
    print(termcolor.colored("\n[-] Something went wrong!", "red"))
    print(termcolor.colored(f"\n[-] Error is {e}", "red"))