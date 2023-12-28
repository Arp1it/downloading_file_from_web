import requests, termcolor
from clint.textui import progress

url = input(termcolor.colored("[+] Enter url: ", "green"))
filename = input(termcolor.colored("[+] Enter filname (without extention): ", "green"))
filextnsion = input(termcolor.colored("[+] Enter file extention (without dot(.)): ", "green"))

forwb = ["pdf", "img", "webp", "jpeg", "png"]

try:
    data = requests.get(url=url, stream=True)

    totallength = int(data.headers.get("content-length"))

    if filextnsion in forwb:
        with open(f"{filename}.{filextnsion}", "wb") as pf:
            for ch in progress.bar(data.iter_content(chunk_size=1024), expected_size=(totallength/1024)+1, label=termcolor.colored("Downloading: ", "yellow")):
                if ch:
                    pf.write(data.content)

    else:
        print(termcolor.colored("[+] Downloading started (stay connected with internet)", "yellow"))
        with open(f"{filename}.{filextnsion}", "w+") as pf1:
            pf1.write(data)

    print(termcolor.colored("\n[+] Downloaded successfully!", "green"))

except Exception as e:
    print(termcolor.colored("\n[-] Something went wrong!", "red"))
    print(e)