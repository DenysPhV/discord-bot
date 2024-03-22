import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    DISCORD_TOKEN: str = os.environ.get("DISCORD_TOKEN")
    CHANNEL_ID: int = os.environ.get("CHANNEL_ID")


settings = Settings()
