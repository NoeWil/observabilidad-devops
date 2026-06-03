# Evidencia de Configuración de Observabilidad: Django

Para lograr la observabilidad de la aplicación Django dentro del ecosistema de contenedores, se implementó la siguiente estrategia:

1. **Contenerización Estructurada:** La aplicación se ejecuta mediante un contenedor basado en `python:3.10`. Las dependencias se instalan dinámicamente mediante el archivo `requirements.txt`.
2. **Aislamiento de Entorno:** Las credenciales y variables sensibles no están hardcodeadas en el código, sino que se inyectan a través del archivo `.env` gestionado por Docker Compose.
3. **Exposición de Servicios:** La aplicación se expone en el puerto 8000 del host, permitiendo que Prometheus (a través de exportadores externos o librerías internas como `django-prometheus` si se requieren métricas específicas a nivel de código) pueda realizar el *scraping* del estado del servidor web (Apache/WSGI).