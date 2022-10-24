import requests
from brillibot_client.config import Config
from pydub import AudioSegment
import speech_recognition as sr
import io
import json
from pydantic import BaseModel

class post_data(BaseModel):
    id: str
    awake_word:str
    actions:dict[str,list[str]]


class BrillibotClient:
    def __init__(self, config: Config):
        self.url = config.url
        self.key = config.key
        self.config = config

        self.r = sr.Recognizer()
        self.r.energy_threshold = config.energy_threshold
        self.r.pause_threshold = config.pause_threshold
        self.r.dynamic_energy_threshold = config.dynamic_energy_threshold

        self.awake_word = config.awake_word

        with open(config.actions_file) as f:
            self.actions = json.load(f)

        self.json_headers = {"Content-Type": "application/json"}

        
    
    def send_audio(self, audio: AudioSegment):
        audio_bytes = io.BytesIO(audio.raw_data)
        audio_bytes.seek(0)
        cookies = {"key":self.key}
        result = requests.post(self.url + "/post_audio", files={"file": audio_bytes},cookies=cookies)
        return json.loads(result.text), result.status_code
    
    def send_metadata(self, id:str):
        meta_data = post_data(id=id,actions=self.actions,awake_word=self.awake_word,key=self.key).dict()
        cookies = {"key":self.key}
        result = requests.post(self.url + "/get_result", json=meta_data, headers=self.json_headers,cookies=cookies)
        return json.loads(result.text), result.status_code
    
    def get_status(self):
        result = requests.get(self.url + "/get_status")
        return json.loads(result.text), result.status_code

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
            if self.config.save_file:
                mp3_audio_clip.export("audio.mp3",format="mp3")

            response,status = self.send_audio(mp3_audio_clip)
            if status == 200:
                id = response["id"]
                response,status = self.send_metadata(id)

            return response,status
    
    def listen_loop(self):
        while True:
            response,status = self.listen()
            print(response)


    def from_file(self, file_path: str,format:str="mp3"):
        audio = AudioSegment.from_file(file_path,format=format)

        response,status = self.send_audio(audio)
        if status == 200:
            id = response["id"]
            response,status = self.send_metadata(id)       
        return response,status 
