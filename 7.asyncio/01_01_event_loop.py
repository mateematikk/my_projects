import time
import asyncio
from multithreading.decorators import async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


async def main():
    asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print('coroutines have finished')
    finally:
        loop.close()
        print('loop is closed')
