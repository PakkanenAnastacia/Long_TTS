import asyncio
import os
from dataclasses import dataclass
from typing import List, Optional, Self
from pydub import AudioSegment

import edge_tts

VOICE_ID = "en-US-AvaNeural"

@dataclass
class TTSExecutor:
    chunks: Optional[List[str]]

    async def extract_from_source(self) -> Self:
        """
        This method takes a file source and then splits the different paragraphs.
        """
        file_path = f"./sources/text.txt"  # Change this to your folder

        if not os.path.isfile(file_path):
            print("This source does not exist!")
            return Self

        # Open the file and read contents
        with open(file_path, "r", encoding="utf-8") as file:
            raw_lines = file.read().splitlines()
            self.chunks = [line for line in raw_lines if line.strip()]

        print("Processing...")

        # We create an AudiSegment to drop the things.
        final_audio = AudioSegment.silent()
        paths_to_delete = []
        # We process each one of the paragraphs.
        for index, paragraph in enumerate(self.chunks):
            print(f"{paragraph}")
            result_path = f"./results/text_{index}.mp3"
            paths_to_delete.append(result_path)
            tts = edge_tts.Communicate(paragraph, VOICE_ID)
            await tts.save(result_path)
            audio_local = AudioSegment.from_file(result_path)
            final_audio += audio_local

        # Export the merged file
        final_audio.export(f"./results/result.mp3", format="mp3")
        print("Complete!")

        print("Cleaning up...")
        for element in paths_to_delete:
            os.remove(element)

        return Self


async def speech_execute():
    executor = TTSExecutor(chunks=None)
    await executor.extract_from_source()


if __name__ == '__main__':
    print("Running...")
    asyncio.run(speech_execute())
