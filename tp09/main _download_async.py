import time
import httpx
from bs4 import BeautifulSoup
import asyncio

async def download(url,log,sem):
    url_log = url+log
    async with sem:
        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            path_log = f".\logs\{log}"
            with open(path_log,"w") as log_file:
                log_file.write(response.text)

async def main():
    sem = asyncio.Semaphore(5)
    url = "https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [a['href'] for a in soup.find_all('a') if '.log' in a['href']] 
    tasks = [download(url,log,sem) for log in all_logs]
    await asyncio.gather(*tasks)



if __name__=='__main__':
    start = time.perf_counter()
    print("avant")
    asyncio.run(main())
    print("après")
    end = time.perf_counter()
    print(end-start)
