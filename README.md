# Brillibot-client

## Overview
This repo gives a python package and CLI to interface with the Brillibot API.

Brillibot is an easy to use speech to command API.

It works by having a user simply define their possible commands in a JSON file with several ways they could say that command, and then provides either a file or access to a microphone to send audio over to sever that will determine what command was said in the audio.

The API is currently rate limited for public use, API keys are a possibility.

Redeployment server side takes a few minutes, thus due to the fact that development is still ongoing, expect periodic downtime.

## Installation

It is reccomended to use a venv before installing.

```pip install git+https://github.com/mallorbc/brillibot-client.git```

### Upgrading

If the repo was updated since you last installed, running may be needed:

```pip install git+https://github.com/mallorbc/brillibot-client.git --no-cache```

## Python Package Examples

Inside the ```/examples``` folder there are two files that show how one can use the Python package either with a file, or with a microphone.

## CLI Usage

To use the CLI, insure that you are inside the venv after installation.  The CLI is called ```brillibot_client```

To see the run options run ```brillibot_client  -h```. Providing an actions file is a must, to do so, use the ```-a``` flag

## Troubleshooting

This repo needs PortAudio to work. 

If you are having issues with the your microphone, try running the following for Ubuntu:
```
sudo apt install portaudio19-dev python3-pyaudio gcc
```
Windows:
```
pip install pipwin
```
```
pipwin install pyaudio
```


## License

This repo is licensed under the AGPL license.  See [LICENSE](LICENSE) for more information.  If you require other license options, contact me.
