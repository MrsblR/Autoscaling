
import pulumi
import pulumi_gcp as gcp

# Enable APIs
for api in ["run.googleapis.com", "cloudbuild.googleapis.com"]:
    gcp.projects.Service(f"api-{api}", service=api, disable_on_destroy=False)

service = gcp.cloudrunv2.Service(
    "autoscale-svc",
    location="us-central1",
    ingress="INGRESS_TRAFFIC_ALL",
    template=gcp.cloudrunv2.ServiceTemplateArgs(
        containers=[gcp.cloudrunv2.ServiceTemplateContainerArgs(
            image="us-docker.pkg.dev/cloudrun/container/hello"
        )],
        container_concurrency=1,
        scaling=gcp.cloudrunv2.ServiceTemplateScalingArgs(
            min_instance_count=0,
            max_instance_count=10,
        ),
    ),
)

gcp.cloudrunv2.ServiceIamMember(
    "invoker-all",
    name=service.name,
    location=service.location,
    role="roles/run.invoker",
    member="allUsers",
)

pulumi.export("url", service.uri)
