try:
    from django.http import JsonResponse
except ImportError:  # django < 1.7
    from django.http import HttpResponse
    from django.core.serializers.json import DjangoJSONEncoder
    import json

    class JsonResponse(HttpResponse):
        """
        An HTTP response class that consumes data to be serialized to JSON.

        :param data: Data to be dumped into json. By default only ``dict`` objects
          are allowed to be passed due to a security flaw before EcmaScript 5. See
          the ``safe`` parameter for more information.
        :param encoder: Should be an json encoder class. Defaults to
          ``django.core.serializers.json.DjangoJSONEncoder``.
        :param safe: Controls if only ``dict`` objects may be serialized. Defaults
          to ``True``.
        """

        def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
            if safe and not isinstance(data, dict):
                raise TypeError('In order to allow non-dict objects to be '
                                'serialized set the safe parameter to False')
            kwargs.setdefault('content_type', 'application/json')
            data = json.dumps(data, cls=encoder)
            super(JsonResponse, self).__init__(content=data, **kwargs)


class JsonResponseHttpCreated(JsonResponse):
    status_code = 201


class JsonResponseAccepted(JsonResponse):
    status_code = 202


class JsonResponseMultipleChoices(JsonResponse):
    status_code = 300


class JsonResponsePermanentRedirect(JsonResponse):
    status_code = 301


class JsonResponseRedirect(JsonResponse):
    status_code = 302


class JsonResponseSeeOther(JsonResponse):
    status_code = 303


class JsonResponseNotModified(JsonResponse):
    status_code = 304


class JsonResponseBadRequest(JsonResponse):
    status_code = 400


class JsonResponseUnauthorized(JsonResponse):
    status_code = 401


class JsonResponseForbidden(JsonResponse):
    status_code = 403


class JsonResponseNotFound(JsonResponse):
    status_code = 404


class HttpResponseMethodNotAllowed(JsonResponse):
    status_code = 405


class JsonResponseHttpConflict(JsonResponse):
    status_code = 409


class JsonResponseGone(JsonResponse):
    status_code = 410


class JsonResponseServerError(JsonResponse):
    status_code = 500


class JsonResponseNotImplemented(JsonResponse):
    status_code = 501
