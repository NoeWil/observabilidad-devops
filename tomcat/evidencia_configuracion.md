# Evidencia de Configuración de Observabilidad: Tomcat (Java)

Dado que Tomcat es una aplicación basada en la JVM (Java Virtual Machine), no expone métricas nativas para Prometheus. Para solucionar esto, se implementó el patrón de "Agente JMX":

1. **JMX Exporter:** Se descargó el agente oficial `jmx_prometheus_javaagent.jar` y se colocó como un volumen de solo lectura (`:ro`) dentro del contenedor.
2. **Inyección vía Variables de Entorno:** Se utilizó la variable `CATALINA_OPTS` en el `docker-compose.yml` para inyectar el agente justo en el arranque de la JVM:
   `-javaagent:/jmx/jmx_prometheus_javaagent.jar=9404:/jmx/config.yaml`
3. **Exposición:** El agente traduce las métricas complejas de JMX a texto plano y las expone exitosamente en el puerto `9404`, el cual es raspado periódicamente por Prometheus para medir la memoria Heap, los hilos y el Garbage Collector.