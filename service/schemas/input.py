from typing import Any

from pydantic import BaseModel


class BotDialogInput(BaseModel):
    sessionAttributes: Any
    type: Any
    dialogAction: Any
