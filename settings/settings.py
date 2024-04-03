import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    DISCORD_TOKEN: str = os.environ.get("DISCORD_TOKEN")
    CHANNEL_ID: int = os.environ.get("CHANNEL_ID")
    TEXTCHEST_TOKEN: str = os.environ.get("TEXTCHEST_TOKEN")
    # FLY_TOKEN: str = os.environ.get("FLY_TOKEN")


settings = Settings()
