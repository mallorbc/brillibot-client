from attr import attrib, attrs

@attrs(auto_attribs=True, frozen=False, auto_detect=True)
class Config:
    url:str = attrib(default="http://127.0.0.1:8000")
    energy_threshold:int = attrib(default=300)
    pause_threshold:int = attrib(default=0.8)
    dynamic_energy_threshold:bool = attrib(default=True)
    actions_file:str = attrib(default="actions_flight.json")
    # actions_file:str = attrib(default="actions_lights.json")
