
# Laboratorio: Pruebas de Autoscaling en la Nube con IaC (Pulumi + GCP Cloud Run)

## Descripción general
Este laboratorio demuestra la implementación y evaluación de **autoscaling** en un servicio desplegado sobre **Google Cloud Run**, utilizando **Infraestructura como Código (IaC)** con **Pulumi (Python)**.  

El objetivo principal es analizar el comportamiento dinámico del escalamiento automático bajo condiciones de carga progresiva, asegurando disponibilidad, rendimiento y eficiencia en el uso de recursos.

---

## Arquitectura

**Componentes principales:**
- **Pulumi (Python)**: Define la infraestructura como código.
- **Google Cloud Run**: Servicio sin servidor que ejecuta contenedores con escalamiento automático.
- **Google Cloud Monitoring**: Recolecta métricas de latencia, solicitudes e instancias.
- **k6**: Generador de carga para pruebas de estrés.
- **Imagen docker base**


## Referencias

* [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
* [Pulumi GCP Provider](https://www.pulumi.com/registry/packages/gcp/)
* [Grafana k6 Load Testing](https://k6.io/docs/)

