import asyncio

async def add(a,b):
    return a+b


async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # a = await add(2,1)
    # print(a)
    results = [add(5,6),add(95,16),add(5,76),add(5,876),add(5,46),add(15,6)]
    r = await asyncio.gather(*results)
    print(r)
if __name__=='__main__':
    asyncio.run(main())
