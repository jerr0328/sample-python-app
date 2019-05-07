import json
import os
from typing import Dict

REGISTRY = os.getenv("DOCKER_REGISTRY", "docker.io/jerr0328")
INFRABOX_GIT_TAG = os.getenv("INFRABOX_GIT_TAG")
INFRABOX_GIT_BRANCH = os.getenv("INFRABOX_GIT_BRANCH")
INFRABOX_GITHUB_PULL_REQUEST = os.getenv("INFRABOX_GITHUB_PULL_REQUEST")
INFRABOX_BUILD_NUMBER = os.getenv("INFRABOX_BUILD_NUMBER")


def generate_deployment(image_name: str, tag: str) -> Dict:
    return {
        "type": "docker-registry",
        "host": REGISTRY,
        "repository": image_name,
        "tag": tag,
    }


def add_deployments(job: Dict):
    deployments = job.get("deployments")
    if not deployments:
        return

    image_name = deployments[0]["repository"]

    if INFRABOX_GIT_BRANCH == "master":
        job["deployments"].append(generate_deployment(image_name, "latest"))

    if INFRABOX_GIT_TAG:
        job["deployments"].append(generate_deployment(image_name, INFRABOX_GIT_TAG))


def main():
    with open("infrabox/infrabox.json") as f:
        infrabox_json = json.load(f)

    for job in infrabox_json["jobs"]:
        add_deployments(job)

    with open("/infrabox/output/infrabox.json", "w") as f:
        json.dump(infrabox_json, f, indent=2)


if __name__ == "__main__":
    main()
