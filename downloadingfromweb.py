import wget, termcolor

url = input(termcolor.colored("[+] Enter url: ", "green"))
filename = input(termcolor.colored("[+] Enter filname (without extention): ", "green"))
filextnsion = input(termcolor.colored("[+] Enter file extention (without dot(.)): ", "green"))

try:
    print(termcolor.colored("[+] Downloading started (stay connected with internet)", "yellow"))
    wget.download(url=url, out=f"{filename}.{filextnsion}")
    print(termcolor.colored("\n[+] Downloaded successfully!", "green"))

except:
    print(termcolor.colored("\n[-] Something went wrong!", "red"))