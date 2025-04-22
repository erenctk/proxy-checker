import asyncio
import aiohttp
import json
import time
from datetime import datetime
from colorama import Fore, Style, init
from tqdm import tqdm
import os

class ProxyChecker:
    def __init__(self):
        self.test_url = "http://www.google.com"
        self.timeout = 10
        self.results = {
            'working': [],
            'not_working': []
        }
        init(autoreset=True)
        
    async def check_proxy(self, proxy, pbar):
        start_time = time.time()
        try:
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                proxy_url = f"http://{proxy}"
                async with session.get(self.test_url, proxy=proxy_url, timeout=self.timeout) as response:
                    end_time = time.time()
                    if response.status == 200:
                        speed = round(end_time - start_time, 2)
                        country = await self.get_proxy_country(proxy)
                        result = {
                            'proxy': proxy,
                            'speed': speed,
                            'country': country,
                            'last_checked': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        self.results['working'].append(result)
                        pbar.set_description(f"{Fore.GREEN}✓ Working: {proxy}{Style.RESET_ALL}")
                    else:
                        self.results['not_working'].append(proxy)
                        pbar.set_description(f"{Fore.RED}✗ Not Working: {proxy}{Style.RESET_ALL}")
        except:
            self.results['not_working'].append(proxy)
            pbar.set_description(f"{Fore.RED}✗ Not Working: {proxy}{Style.RESET_ALL}")
        finally:
            pbar.update(1)

    async def get_proxy_country(self, proxy):
        try:
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(f'http://ip-api.com/json/{proxy.split(":")[0]}', timeout=5) as response:
                    data = await response.json()
                    return data.get('country', 'Unknown')
        except:
            return 'Unknown'

    async def check_proxies(self, proxy_list):
        print(f"\n{Fore.CYAN}Starting Proxy Check...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Total {len(proxy_list)} proxies to test{Style.RESET_ALL}\n")
        
        with tqdm(total=len(proxy_list), bar_format='{l_bar}{bar:30}{r_bar}') as pbar:
            tasks = []
            for proxy in proxy_list:
                if proxy.strip():
                    task = asyncio.create_task(self.check_proxy(proxy.strip(), pbar))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    def save_results(self):
        with open('working_proxies.txt', 'w') as f:
            for proxy in self.results['working']:
                f.write(f"{proxy['proxy']} - Speed: {proxy['speed']}s - Country: {proxy['country']}\n")
        
        with open('not_working_proxies.txt', 'w') as f:
            for proxy in self.results['not_working']:
                f.write(f"{proxy}\n")

    def print_results(self):
        print("\n" + "="*50)
        print(f"{Fore.CYAN}RESULTS:{Style.RESET_ALL}")
        print("="*50)
        
        print(f"\n{Fore.GREEN}WORKING PROXIES ({len(self.results['working'])}){Style.RESET_ALL}")
        print("-"*50)
        for proxy in self.results['working']:
            print(f"{Fore.GREEN}✓ {proxy['proxy']}{Style.RESET_ALL} - "
                  f"Speed: {Fore.YELLOW}{proxy['speed']}s{Style.RESET_ALL} - "
                  f"Country: {Fore.BLUE}{proxy['country']}{Style.RESET_ALL}")
        
        print(f"\n{Fore.RED}NOT WORKING PROXIES ({len(self.results['not_working'])}){Style.RESET_ALL}")
        print("-"*50)
        for proxy in self.results['not_working']:
            print(f"{Fore.RED}✗ {proxy}{Style.RESET_ALL}")
        
        print("\n" + "="*50)
        print(f"{Fore.YELLOW}Results saved:{Style.RESET_ALL}")
        print(f"Working Proxies: {Fore.GREEN}working_proxies.txt{Style.RESET_ALL}")
        print(f"Not Working Proxies: {Fore.RED}not_working_proxies.txt{Style.RESET_ALL}")
        print("="*50 + "\n")

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"""{Fore.CYAN}
╔═══════════════════════════════════════════╗
║             PROXY CHECKER                 ║
║                                          ║
║  Advanced Proxy Checker Tool v1.0        ║
╚═══════════════════════════════════════════╝
{Style.RESET_ALL}""")

    if not os.path.exists('proxy.txt'):
        print(f"{Fore.RED}Error: proxy.txt file not found!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please create proxy.txt file and add proxies (one per line).{Style.RESET_ALL}")
        return

    with open('proxy.txt', 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

    if not proxies:
        print(f"{Fore.RED}Error: proxy.txt file is empty!{Style.RESET_ALL}")
        return

    checker = ProxyChecker()
    await checker.check_proxies(proxies)
    checker.save_results()
    checker.print_results()

if __name__ == '__main__':
    asyncio.run(main()) 