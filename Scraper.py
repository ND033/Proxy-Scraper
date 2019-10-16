import wget

print("1. HTTP/s\n2. Socks 4\n3. Socks 5")

type = input("Enter proxy type. ")

if type == "1":
    wget.download(
        'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all',
        out='https.txt')
    input("Done! ")

if type == "2":
    wget.download('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all',
                  out='socks4.txt')
    input("Done! ")

if type == "3":
    wget.download('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all',
                  out='socks5.txt')
    input("Done! ")

else:
    input("Value must be 1, 2 or 3. 1")