import whisper
from transformers import pipeline
import edge_tts
import asyncio

# Step 1: Speech-to-Text Conversion
def speech_to_text(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, language='en', vad_threshold=0.5)
    return result['text']

# Step 2: Text Input into LLM
def generate_response(input_text):
    llm = pipeline("text-generation", model="Mistral")
    response = llm(input_text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

# Step 3: Text-to-Speech Conversion
async def text_to_speech(text, output_file="output.mp3"):
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural", pitch="+10%", rate="+5%")
    await communicate.save(output_file)

# Example usage
audio_file = "path_to_audio_file.wav"
text_output = speech_to_text(audio_file)
response_text = generate_response(text_output)
output_file = "response_audio.mp3"
asyncio.run(text_to_speech(response_text, output_file))

print("Pipeline Completed! Audio response saved to:", output_file)
