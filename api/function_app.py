import json
import os

import azure.functions as func
import pymysql

app = func.FunctionApp()


def get_connection():
    return pymysql.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"],
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        ssl={"ssl": {}},
    )


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


@app.route(route="db-check", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def db_check(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
        conn.close()
        return func.HttpResponse(
            json.dumps({"conectado": True, "mysql_version": version}),
            mimetype="application/json",
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"conectado": False, "error": str(e)}),
            mimetype="application/json",
            status_code=500,
        )
