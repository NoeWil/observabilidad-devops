# Proyecto de Observabilidad y DevOps

Este repositorio contiene la instrumentación completa de un servidor Linux con múltiples contenedores utilizando el stack de Prometheus, Grafana y Alertmanager.

## Servicios Monitoreados
- Host (Node Exporter)
- Contenedores Docker (cAdvisor)
- Base de Datos (MariaDB Exporter)
- Aplicación Web (Django)
- Servidor Java (Tomcat JMX)
- Disponibilidad Web (WordPress / Blackbox Exporter)

## Instrucciones de despliegue
1. Clonar el repositorio.
2. Copiar `.env.example` a `.env` y colocar las credenciales SMTP.
3. Ejecutar `docker compose up -d`.
