from openai import OpenAI
client = OpenAI()

audio_file= open("./out/audio.mp3", "rb")

transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

# Save the transcript to a file
with open('./out/transcript.txt', 'w') as file:
    file.write(transcript)