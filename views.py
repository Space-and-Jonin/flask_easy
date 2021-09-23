import typing as t
from flask.typing import ResponseReturnValue
from flask.views import MethodView, MethodViewType
from flask import request


class EasyView(MethodView, metaclass=MethodViewType):
    """A class-based view that dispatches requests to the view
    specified. For example, if you implement a ``get`` method and specify
    a view_name of create, it will be used to handle ``GET `` requests
    """

    def dispatch_request(self, *args: t.Any, **kwargs: t.Any) -> ResponseReturnValue:

        view_args = request.view_args
        view_name = view_args.get("view_name", None)
        if not view_name:
            return super().dispatch_request(*args, **kwargs)

        else:
            meth = getattr(self, view_name.lower(), None)
            assert meth, "Request view does not match any endpoint"
            del request.view_args["view_name"]
            del kwargs["view_name"]
            return meth(*args, **kwargs)
