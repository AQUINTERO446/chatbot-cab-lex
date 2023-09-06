from typing import List, Literal, Optional
from pydantic_extra_types.coordinate import Longitude, Latitude
from service.schemas import BaseModelCamelInput


class ComponentNameModel(BaseModelCamelInput):
    text: str
    language_code: Optional[str] = None

class AddressComponentModel(BaseModelCamelInput):
    component_name: ComponentNameModel
    component_type: str
    confirmation_level: Literal['CONFIRMATION_LEVEL_UNSPECIFIED', 'CONFIRMED', 'UNCONFIRMED_BUT_PLAUSIBLE', 'UNCONFIRMED_AND_SUSPICIOUS']
    replaced: Optional[bool] = None
    inferred: Optional[bool] = None

class PostalAddressModel(BaseModelCamelInput):
    region_code: str
    language_code: str
    postal_code: str
    administrative_area: str
    locality: str
    address_lines: List[str]

class VerdictModel(BaseModelCamelInput):
    input_granularity: str
    validation_granularity: str
    geocode_granularity: str
    address_complete: bool = None
    has_inferred_components: bool
    has_replaced_components: bool
    has_unconfirmed_components: bool = None

class LocationModel(BaseModelCamelInput):
    latitude: Latitude
    longitude: Longitude

class PlusCodeModel(BaseModelCamelInput):
    global_code: str

class BoundsModel(BaseModelCamelInput):
    low: LocationModel
    high: LocationModel

class USPSDataModel(BaseModelCamelInput):
    standardized_address: dict 

class AddressModel(BaseModelCamelInput):
    formatted_address: str
    postal_address: PostalAddressModel
    address_components: List[AddressComponentModel]

class Geocode(BaseModelCamelInput):
    location: LocationModel
    plus_code: PlusCodeModel
    bounds: BoundsModel
    feature_size_meters: float
    place_id: str
    place_types: List[str]

class ResultModel(BaseModelCamelInput):
    verdict: VerdictModel
    address: AddressModel 
    geocode: Geocode 
    metadata: dict 
    usps_data: USPSDataModel

class AddressValidation(BaseModelCamelInput):
    result: ResultModel
    response_id: str
