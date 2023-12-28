import urllib3, shutil, termcolor

url = input(termcolor.colored("[+] Enter url: ", "green"))
filename = input(termcolor.colored("[+] Enter filname (without extention): ", "green"))
filextnsion = input(termcolor.colored("[+] Enter file extention (without dot(.)): ", "green"))

c = urllib3.PoolManager()

try:
    with c.request("GET", url, preload_content=False) as res, open(f"{filename}.{filextnsion}", "wb") as out_file:
        shutil.copyfileobj(res, out_file)

except Exception as e:
    print(termcolor.colored("\n[-] Something went wrong!", "red"))
    print(termcolor.colored(f"\n[-] Error is {e}", "red"))