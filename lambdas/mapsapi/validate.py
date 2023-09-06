import json
from typing import Any, Dict, Optional
from http import HTTPStatus

from googlemaps import Client
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_env_modeler import get_environment_variables, init_environment_variables
from aws_lambda_powertools.utilities.parser import ValidationError, parse
from aws_lambda_powertools.metrics import MetricUnit
from service.schemas.lex_event import LexEventProxyInputEventModel

from service.utils.http_responses import build_response
from service.utils.observability import logger, metrics, tracer
from service.schemas.env_vars import MapsAPIEnvVars
from service.schemas.exceptions import InternalServerException
from service.schemas.output import BotDialogOutput
from service.schemas.input import BotDialogInput
from service.schemas.address_validation import AddressValidation


@init_environment_variables(model=MapsAPIEnvVars)
@metrics.log_metrics
@tracer.capture_lambda_handler(capture_response=False)
def simple_addressvalidation_handler(
    event: Dict[str, Optional[Any]], context: LambdaContext
) -> Dict[str, None]:
    logger.set_correlation_id(context.aws_request_id)
    logger.info("calling simple_addressvalidation_handler")

    env_vars: MapsAPIEnvVars = get_environment_variables()
    logger.debug("environment variables", extra=env_vars.dict())

    try:
        dialog_input: BotDialogInput = parse(
            event=event, model=BotDialogInput, envelope=LexEventProxyInputEventModel
        )
        logger.info("got validate address request")

    except ValidationError as exc:
        logger.error("event failed input validation", extra={"error": str(exc)})
        return build_response(http_status=HTTPStatus.BAD_REQUEST, body={})

    metrics.add_metric(name="ValidatedAddressEvents", unit=MetricUnit.Count, value=1)
    try:
        client: Client = Client(env_vars.GOOGLE_API_KEY)
        address_lines = ["1600 Amphitheatre Pk"]
        results = client.addressvalidation(
            address_lines, regionCode="US", enableUspsCass=True
        )
        logger.debug("google addressvalidation results", extra=results)

        addres_validation_results = AddressValidation.model_validate(results)
        if addres_validation_results.result.verdict.has_unconfirmed_components:
            logger.info(
                "finished handling simple_addressvalidation_handler request with invalid address"
            )
            response = BotDialogOutput()
            return build_response(http_status=HTTPStatus.OK, body=response)

    except InternalServerException:  # pragma: no cover
        logger.error(
            "finished handling simple_addressvalidation_handler request with internal error"
        )
        return build_response(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, body={})

    response = BotDialogOutput()
    logger.info("finished handling simple_addressvalidation_handler request")
    return build_response(http_status=HTTPStatus.OK, body=response.model_dump())
