from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

# --- ENUMS ---
# We redefine these as string Enums so FastAPI knows how to read them from JSON