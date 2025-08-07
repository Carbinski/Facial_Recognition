import edge_tts
import asyncio
import tempfile
import pygame
import time
import os

async def speak(text):
    communicate = edge_tts.Communicate(text, voice="en-AU-WilliamNeural")
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    await communicate.save(temp_file.name)
    return temp_file.name

def run_tts(text):

    file_path = asyncio.run(speak(text))

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Clean up
    pygame.mixer.quit()
    os.remove(file_path)

if __name__ == "__main__":
    text = "Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills."
    run_tts(text)