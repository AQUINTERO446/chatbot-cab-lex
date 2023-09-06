from typing import List, Optional, Union
from pydantic import BaseModel

class Slot(BaseModel):
    name: str
    value: str

class RecentIntentSummaryView(BaseModel):
    intent_name: str
    checkpoint_label: str
    slots: Optional[dict]
    confirmation_status: str
    dialog_action_type: str
    fulfillment_state: str
    slot_to_elicit: Optional[str]

class TimeToLive(BaseModel):
    time_to_live_in_seconds: int
    turns_to_live: int

class ActiveContexts(BaseModel):
    time_to_live: TimeToLive
    name: str
    parameters: dict

class DialogAction(BaseModel):
    type: str

class BotDialogOutput(BaseModel):
    session_attributes: Optional[dict]
    recent_intent_summary_view: Optional[List[RecentIntentSummaryView]]
    active_contexts: Optional[List[ActiveContexts]]
    dialog_action: Optional[DialogAction]