import asyncio

# async def fetch_data(delay):
#     print("Fetching data")
#     await asyncio.sleep(delay)
#     print("Fetching data complete")

# async def main():
#     print("Fetching Start")
#     t = fetch_data(2)
#     print("Fetching Complete")
#     await t
#     print("Fetcing main function done")

# asyncio.run(main())



# async def work(id):
#     print("Working... ",id)
#     await asyncio.sleep(2)
#     print("Done => ",id)

# async def main():
#     w1 = asyncio.create_task(work(1))
#     w2 = asyncio.create_task(work(2))
#     w3 = asyncio.create_task(work(3))

#     print("Main has started execution")
#     await w1
#     await w2
#     await w2

# asyncio.run(main())



async def square(x):

    await asyncio.sleep(2)

    return x*x

async def main():

    task = asyncio.create_task(square(5))

    print(task.done())

    result = await task

    print(result)

asyncio.run(main())