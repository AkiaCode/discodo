from .AudioSource import *
from .gateway import VoiceSocket
from .manager import AudioManager
from .natives import *
from .node import *
from .player import Player
from .stat import getStat
from .utils import *
from .voice_client import VoiceClient
from .voice_connector import VoiceConnector

try:
    import discord
except ModuleNotFoundError:
    pass
else:
    from .DPYClient import DPYClient
