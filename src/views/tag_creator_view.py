from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
    responsability for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # lógica de negócio
        tag_creator_controller = TagCreatorController()
        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
