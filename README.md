# What is this?

This a small project that takes a `.txt` file in the `./sources` directory, splits it into chunks, and then transform the chunks with a `TTS`.
Then, it merges the chunks into a big file por other processing.

Just install the requirements and you are good to go.

If you want to change the voice, the `VOICE_ID` in the executor for any of the ones in the list.
This uses `edge-tts` by the way.
Remember, you need `pyaudio` and `ffmpeg`.

To speed up the result:
```commandline
ffmpeg -i input.mp3 -filter:a "atempo=1.25" output.mp3
```


