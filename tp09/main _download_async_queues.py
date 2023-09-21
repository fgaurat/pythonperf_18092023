import time
import httpx
from bs4 import BeautifulSoup
import asyncio

async def old_download(url,log,sem):
    url_log = url+log
    async with sem:
        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            path_log = f".\logs\{log}"
            with open(path_log,"w") as log_file:
                log_file.write(response.text)

async def download(d_q,w_q):
    while True:
        info = await d_q.get()
        url_log = info[0]+info[1]

        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            result = {
                "text":response.text,
                'log' : info[1]
            }
            w_q.put_nowait(result)
        d_q.task_done()


async def save(w_q):
    while True:
        info = await w_q.get()
        log = info['log'] 
        text = info['text'] 
        path_log = f".\logs\{log}"
        with open(path_log,"w") as log_file:
            log_file.write(text)        
        w_q.task_done()



async def main():
    sem = asyncio.Semaphore(5)
    url = "https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [a['href'] for a in soup.find_all('a') if '.log' in a['href']] 

    d_q = asyncio.Queue()
    w_q = asyncio.Queue()


    nb_download_workers = 5
    nb_writer_workers = 2

    download_workers = []
    writer_workers = []

    for i in range(nb_download_workers):
        t = asyncio.create_task(download(d_q,w_q))
        download_workers.append(t)

    for i in range(nb_writer_workers):
        t = asyncio.create_task(save(w_q))
        writer_workers.append(t)


    for log in all_logs:
        d_q.put_nowait((url,log))

    await d_q.join()
    await w_q.join()

    [d.cancel() for d in download_workers]
    [d.cancel() for d in writer_workers]


if __name__=='__main__':
    start = time.perf_counter()
    print("avant")
    asyncio.run(main())
    print("après")
    end = time.perf_counter()
    print(end-start)
