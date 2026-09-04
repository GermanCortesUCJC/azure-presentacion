# Sitio de presentacion - ruta de aprendizaje Azure

Sitio estatico (HTML/CSS) que iremos evolucionando para practicar servicios de Azure.

## Fases planeadas

1. **Fase 0:** sitio estatico simple (HTML/CSS).
2. **Fase 1 (listo):** repositorio en GitHub.
3. **Fase 2 (actual):** despliegue en Azure Static Web Apps via GitHub Actions.
4. **Fase 3:** API en Azure Functions (Python, FastAPI via AsgiMiddleware) + Azure Database for MySQL.
5. **Fase 4:** Azure Blob Storage para archivos/imagenes.
6. **Fase 5:** Application Insights para monitoreo.
7. **Fase 6:** Azure Key Vault para secretos.

## Correr en local

Al ser un sitio estatico, basta con abrir `index.html` en el navegador, o servirlo con:

```bash
python -m http.server 8000
```

Abrir http://127.0.0.1:8000
