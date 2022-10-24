from attr import attrib, attrs
import os

@attrs(auto_attribs=True, frozen=False, auto_detect=True)
class Config:
    url:str = attrib(default="https://brillibot.brillibits.com")
    key:str = attrib(default="13456")
    # key = os.environ['SECRET_PASSWORD']
    save_file:bool = attrib(default=False)
    energy_threshold:int = attrib(default=200)
    pause_threshold:int = attrib(default=0.8)
    dynamic_energy_threshold:bool = attrib(default=True)
    awake_word:str = attrib(default="computer")
    actions_file:str = attrib(default="actions_flight.json")
    # actions_file:str = attrib(default="actions_lights.json")
