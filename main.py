import asyncio
import os

from src.TTSExecutor import TTSExecutor


async def speech_execute(src: str):
    executor = TTSExecutor(chunks=None)
    await executor.extract_from_source(src)


if __name__ == '__main__':
    print("Sources:")

    for x in os.listdir("./sources"):
        if x.endswith(".txt"):
            print(x.split(".")[0])

    src = input("Indicate a source:\n")
    asyncio.run(speech_execute(src))
