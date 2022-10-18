from gettext import npgettext
import requests
from config import Config
from pydub import AudioSegment
import speech_recognition as sr
import io
import tempfile
import json
from pydantic import BaseModel

class post_data(BaseModel):
    id: str


class BrillibotClient:
    def __init__(self, config: Config):
        self.url = config.url

        self.r = sr.Recognizer()
        self.r.energy_threshold = config.energy_threshold
        self.r.pause_threshold = config.pause_threshold
        self.r.dynamic_energy_threshold = config.dynamic_energy_threshold

        self.json_headers = {"Content-Type": "application/json"}

        
    
    def send_audio(self, audio: AudioSegment):
        audio_bytes = io.BytesIO(audio.raw_data)
        audio_bytes.seek(0)
        result = requests.post(self.url + "/post_audio", files={"file": audio_bytes,"test":"test"})
        return json.loads(result.text)
    
    def send_metadata(self, metadata:str):
        meta_data = post_data(id=metadata).dict()
        result = requests.post(self.url + "/get_result", json=meta_data, headers=self.json_headers)
        return json.loads(result.text)
    

    def listen(self):
        with sr.Microphone(sample_rate=16000) as source:
            self.r.adjust_for_ambient_noise(source, duration = 0.5)
            print("Say something!")
            audio = self.r.listen(source)

            wav_data = io.BytesIO(audio.get_wav_data())
            wav_audio_clip = AudioSegment.from_file(wav_data,format="wav")
            mp3_data = io.BytesIO()
            wav_audio_clip.export(mp3_data,format="mp3")
            mp3_audio_clip = AudioSegment.from_file(mp3_data,format="mp3")


            id = self.send_audio(mp3_audio_clip)["id"]
            print(id)
            result = self.send_metadata(id)
            print(result)
    
    def listen_loop(self):
        while True:
            self.listen()






if __name__ == "__main__":
    config = Config()
    client = BrillibotClient(config)
    client.listen_loop()
