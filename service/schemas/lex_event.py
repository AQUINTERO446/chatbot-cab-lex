from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel

from aws_lambda_powertools.utilities.parser.types import Literal

from service.schemas import BaseModelCamelInput
from typing import List, Optional, Union


class Resolutions(BaseModelCamelInput):
    value: str

class SlotDetails(BaseModelCamelInput):
    resolutions: List[Resolutions]
    original_value: str

class Slot(BaseModelCamelInput):
    name: str
    value: str

class Intent(BaseModelCamelInput):
    name: str
    nlu_intent_confidence_score: float
    slots: Optional[dict]
    slot_details: Optional[dict]
    confirmation_status: str

class Bot(BaseModelCamelInput):
    name: str
    alias: str
    version: str

class RecentIntentSummaryView(BaseModelCamelInput):
    intent_name: str
    checkpoint_label: str
    slots: Optional[dict]
    confirmation_status: str
    dialog_action_type: str
    fulfillment_state: str
    slot_to_elicit: Optional[str]

class TimeToLive(BaseModelCamelInput):
    time_to_live_in_seconds: int
    turns_to_live: int

class ActiveContexts(BaseModelCamelInput):
    time_to_live: TimeToLive
    name: str
    parameters: dict

class SentimentResponse(BaseModelCamelInput):
    sentiment_label: str
    sentiment_score: str

class KendraResponse(BaseModelCamelInput):
    pass

class LexEventProxyInputEventModel(BaseModelCamelInput):
    current_intent: Intent
    alternative_intents: Optional[List[Intent]]
    bot: Bot
    user_id: str
    input_transcript: str
    invocation_source: str
    output_dialog_mode: str
    message_version: str
    session_attributes: Optional[dict]
    request_attributes: Optional[dict]
    recent_intent_summary_view: Optional[List[RecentIntentSummaryView]]
    sentiment_response: Optional[SentimentResponse]
    kendra_response: Optional[KendraResponse]
    activeContexts: Optional[List[ActiveContexts]]

