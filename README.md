# Sitio de presentacion - ruta de aprendizaje Azure

Proyecto FastAPI simple que iremos evolucionando para practicar servicios de Azure.

## Fases planeadas

1. **Fase 0 (actual):** app FastAPI local con paginas de presentacion.
2. **Fase 1:** repositorio en GitHub.
3. **Fase 2:** despliegue en Azure App Service via GitHub Actions.
4. **Fase 3:** base de datos Azure Database for MySQL + SQLAlchemy.
5. **Fase 4:** Azure Blob Storage para archivos/imagenes.
6. **Fase 5:** Application Insights para monitoreo.
7. **Fase 6:** Azure Key Vault para secretos.

## Correr en local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abrir http://127.0.0.1:8000
