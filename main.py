moder = False

try:
    import requests
    import colorama
    import capmonster_python
except:
    moder = True


if moder == True:
    print("Missing Modules Press Enter To Download Them (May Not Always Work): ")
    input("")
    try:
        import os
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pip install capmonster-python")
        print("Problem May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Install Modules")
        input("")
        exit()
    
    


import json
import threading
import time
import random
import os




try:
    import os
    os.system("title " + "Discord Account Creator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass


colorama.init(autoreset=True)
def settings():
    while True:
        error = False
        try:
            global api_key
            global print_fails
            global print_captcha
            global print_taskid
            global print_fingerprint
            global username
            global password
            global print_email
            global print_proxy
            global invite
            global random_letters
            global threads
            global use_proxies
            global random_user
            json_data = open("settings.json")
            json_data = json.load(json_data)
            api_key = json_data["capmonster_key"]
            print_fails = json_data["print_fails_y_or_n"]
            print_captcha = json_data["print_captcha_key_y_or_n"]
            print_taskid = json_data["print_task_id_key_y_or_n"]
            print_fingerprint = json_data["print_fingerprint_y_or_n"]
            username = json_data["tokens_username"]
            password = json_data["tokens_password"]
            print_email = json_data["print_email_y_or_n"]
            print_proxy = json_data["print_proxy_y_or_n"]
            threads = json_data["threads"]
            invite = json_data["invite_code"]
            random_letters = json_data["random_letters_after_token_username_y_or_n"]
            use_proxies = json_data["use_proxies_y_or_n"]
            random_user = json_data["random_username_from_names.txt_y_or_n"]
            try:
                bal = capmonster_python.HCaptchaTask(api_key)
                el = bal.get_balance()
            except:
                error = True
            if print_fails != "y" and print_fails != "n":       
                error = True
            if print_captcha != "y" and print_captcha != "n":       
                error = True    
            if print_taskid != "y" and print_taskid != "n":       
                error = True
            if print_fingerprint != "y" and print_fingerprint != "n":       
                error = True
            if print_email != "y" and print_email != "n":       
                error = True
            if print_proxy != "y" and print_proxy != "n":       
                error = True
            if random_letters != "y" and random_letters != "n":       
                error = True
            if use_proxies != "y" and use_proxies != "n":       
                error = True
            if "-" in str(threads):
                error = True
            if random_user != "y" and random_user != "n":
                error = True
            try:
                threads = int(threads)
            except:
                error = True
            if error == True:
                print(colorama.Fore.RED + "[-] Press Enter When You Have Fixed Settings And All Settings Will Reload")
                input("")
            if error == False:
                break
        except Exception as e:
            print(colorama.Fore.RED + 'Missing "settings.json" File, It Stores All Settings')
            input("")
            exit()


    if str(threads) != "1" and use_proxies == "n":
            print("Cannot Have More Than 1 Thread Without Proxies, Please Restart The Program And Enter Valid Settings")
            input("")
            exit()


settings()



cap = capmonster_python.HCaptchaTask(api_key)



def gen():
    try:
        while True:

            session = requests.session()
            
            if use_proxies == "y":
                prox = open("rotating_proxy.txt", "r")
                proxy = str(prox.readline())
                if print_proxy == "n":
                    print(colorama.Fore.GREEN + "[+] Loaded Proxy")
                if print_proxy == "y":
                    print(colorama.Fore.GREEN + "[+] Loaded Proxy, "+proxy)
            
            while True:
                try:
                    tt = cap.create_task("https://discord.com/register", "4c672d35-0701-42b2-88c3-78380b0db560")
                    if print_taskid == "y":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Task Id, " + str(tt))
                    if print_taskid == "n":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Task Id")
                    break
                except Exception:
                    if print_fails == "y":
                        print(colorama.Fore.RED + "[-] Failed To Get Task Id, Retrying")


            while True:
                try:
                    captcha = cap.join_task_result(tt)
                    captcha = str(captcha.get("gRecaptchaResponse"))
                    if print_captcha == "n":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Captcha Key")
                    if print_captcha == "y":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Captcha Key, " + captcha)
                    break
                except:
                    if print_fails == "y":
                        print(colorama.Fore.RED + "[-] Failed To Get Captcha Key, Retrying")



            while True:
                try:
                    fingerprint = session.get("https://discord.com/api/v9/experiments").json()["fingerprint"]
                    if print_fingerprint == "y":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Fingerprint, " + fingerprint)
                    if print_fingerprint == "n":
                        print(colorama.Fore.GREEN + "[+] Succsesfully Got Fingerprint")
                    break
                except:
                    if print_fails == "y":
                        print(colorama.Fore.RED + "[-] Failed To Get Fingerprint, Retrying")
            session.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
            session.headers = {
                    'Host': 'discord.com', 'Connection': 'keep-alive',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'X-Fingerprint': fingerprint,
                    'X-Super-Properties': session.xsup,
                    'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
                    'Content-Type': 'application/json', 'Authorization': 'undefined',
                    'Accept': '*/*', 'Origin': 'https://discord.com',
                    'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Cookie': 'OptanonConsent=version=6.17.0; locale=th'
                }
            choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            if random_user == "n":
                if random_letters == "y":
                    rande = random.choices(choices, k=5)
                    rande = "".join(rande)
                    rande = str(rande)
                    rande = " | " + rande
                if random_letters == "n":
                    rande = ""

                usa = username + rande

            if random_user == "y":
                fe = open("names.txt", "r")
                er = fe.readlines()
                ee = []
                for t in er:
                    if "\n" in t:
                        ee.append(t[:-1])
                    else:
                        ee.append(t)
                usa = str(random.choice(ee))
                fe.close()

                print("usa ", usa)
            email = random.choices(choices, k=16)
            email = str("".join(email))
            if print_email == "y":
                print(colorama.Fore.GREEN + f"[+] Generated Email, {email}@gmail.com")
            if print_email == "n":
                print(colorama.Fore.GREEN + f"[+] Generated Email")
            payload = {
                "fingerprint": fingerprint,
                "email": f"{email}@gmail.com",
                "username": f"{usa}",
                "password": password,
                "invite": invite,
                "consent": True,
                "date_of_birth": "2003-11-18",
                "gift_code_sku_id": None,
                "captcha_key": captcha,
                "promotional_email_opt_in": True
            }
            while True:
                if use_proxies == "y":
                    session.proxies = {
                        "http": proxy,
                        "https": proxy
                    }
                reg = session.post('https://discord.com/api/v9/auth/register', json=payload)
                res = str(reg)
                jle = reg.json()
                if "201" in res:
                    token = str(jle["token"])
                    file = open("tokens.txt", "a")
                    file.write(token+"\n")
                    file.close()
                    print(colorama.Fore.GREEN + f"[+] Generated Token/Account ({usa}), Saved In tokens.txt And If Invite In settings.json Is Valid Token Shall Auto Join")
                    break
                if "429" in res:
                    time2 = float(jle["retry_after"])
                    if print_fails == "y":
                        print(colorama.Fore.RED + f"[-] Rate Limited, Sleeping For {str(time2)} Seconds")
                    time.sleep((float(time2)))
                if "400" in res:
                    if print_fails == "y":
                        print(colorama.Fore.RED + "[-] Failed To Create Account")
                    break
                if "400" not in res and "429" not in res and "201" not in res:
                    if print_fails == "y":
                        print(colorama.Fore.RED + "[-] Unkown Error")
                    break   
            if str(threads) == "1":
                print(colorama.Fore.LIGHTGREEN_EX + "------------------------")
    except Exception as e:
        print(str(e))
        if print_fails == "y":
            print(colorama.Fore.RED + "[-] Unkown Error")

def clear():
    os.system("cls")

try:
    bal = capmonster_python.HCaptchaTask(api_key)
    el = bal.get_balance()
except:
    print(colorama.Fore.RED + "[-] Capmonster Key Is Invalid")
    while True:
        input("")
while True:
    tools = input("""
    1. Token Generator/Member Botter/Token Creator
    2. Check Capmonster Balance
    3. Reload Settings
    > """)
    if tools == "1":
        er = 0
        for u in range(int(threads)):
            threading.Thread(target=gen).start()
            er = int(er) + 1
            print(colorama.Fore.GREEN + f"[+, {str(er)}] Started Thread")
        while True:
            input("")
    if tools == "2":
        print(colorama.Fore.GREEN + "[+] Getting Balance, Be Patient")
        try:
            bal = capmonster_python.HCaptchaTask(api_key)
            print(colorama.Fore.GREEN + "[+] Balance: " + str(bal.get_balance()) + "$")
        except:
            print(colorama.Fore.RED + "[-] Capmonster Key Is Invalid")
        input("    > ")
        clear()
    if tools == "3":
        settings()
        print(colorama.Fore.GREEN + "[+] Reloaded Settings")
        input("    > ")
        clear()
