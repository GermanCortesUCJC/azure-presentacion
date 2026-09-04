import json

import azure.functions as func

app = func.FunctionApp()


@app.route(route="health", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"status": "ok"}),
        mimetype="application/json",
    )


@app.route(route="saludo", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def saludo(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"mensaje": "Hola desde Azure Functions"}),
        mimetype="application/json",
    )
