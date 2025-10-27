import pulumi
import pulumi_gcp as gcp

# Habilitar APIs (run y cloudbuild). Compute ya lo habilitaste con gcloud arriba.
for api in ["run.googleapis.com", "cloudbuild.googleapis.com"]:
    gcp.projects.Service(f"api-{api}", service=api, disable_on_destroy=False)

service = gcp.cloudrunv2.Service(
    "autoscale-svc",
    location="us-central1",
    ingress="INGRESS_TRAFFIC_ALL",
    # 👇 OJO: scaling va AQUÍ (top-level), no dentro de template
    scaling=gcp.cloudrunv2.ServiceScalingArgs(
        max_instance_count=10,   # techo de autoscaling
        # min_instance_count no existe a este nivel en v2; el valor por defecto es 0
    ),
    template=gcp.cloudrunv2.ServiceTemplateArgs(
        containers=[
            gcp.cloudrunv2.ServiceTemplateContainerArgs(
                image="us-docker.pkg.dev/cloudrun/container/hello",
            )
        ],
        # ⚠️ container_concurrency=1  ❌  (no soportado aquí en v2)
    ),
)

# Hacerlo público
gcp.cloudrunv2.ServiceIamMember(
    "invoker-all",
    name=service.name,
    location=service.location,
    role="roles/run.invoker",
    member="allUsers",
)

pulumi.export("url", service.uri)
