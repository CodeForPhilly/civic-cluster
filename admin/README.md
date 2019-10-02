# Cluster Administration Project

This project implements a set of Ansible resources
which can be used to build out civic cluster applications
on top of a fresh kubernetes installation. There are two
categories of application which are distinguished between
from an administrative standpoint:

1. Platform applications: These are applications which provide
 services to cluster users, such as ingress controllers, container
 registries, etc. These are typically only exposed within the cluster.
2. Project applications: These are the public facing applications
 run by developers.

## Quick start

Currently, the playbooks only work in the docker-compose environment

```
../admin.sh enter
```

Once in the docker-compose environment, the playbooks may be executed.

```
cd civic-cluster

# Rebuild everything on a newly deployed cluster
ansible-playbook cluster.yaml

# Deploy only platform applications
ansible-playbook platform.yaml

# Deploy only project applications
ansible-playbook projects.yaml

# Run the playbook against only the cert-manager application
ansible-playbook cluster.yaml -l cert-manager

# Do the same but with phlask
ansible-playbook projects.yaml -l phlask
```

## Playbooks

- [cluster.yaml](./cluster.yaml): This playbook will first deploy all
 platform applications to the cluster, followed by all project applications
- [platform.yaml](./platform.yaml): This playbook will deploy all platform applications to the cluster
- [projects.yaml](./projects.yaml): This playbook will deploy all project applications to the cluster

## Adding a new platform application

1. Create a [platform/${app_name}/manifest.yaml](../platform) definition file
2. Add the name specified in `${app_name}` to the [inventory/platform-applications](./inventory/platform-applications) list
3. Deploy the application using either `ansible-playbook platform.yaml` or `ansible-playbook platform.yaml -l ${app_name}`

## Adding a new project application

1. Create a [projects/${app_name}.yaml](../projects) definition file
2. Add the name specified in `${app_name}` to the [inventory/project-applications](./inventory/project-applications) list
3. Deploy the application using either `ansible-playbook projects.yaml` or `ansible-playbook projects.yaml -l ${app_name}`

#### About project applications

Project applications are deployed in two stages:

1. Project initialization
2. Application deployment

The project initialization phase creates a new namespace and populates it with resources common to all projects. These common resources can be found in the [templates/project/init.yaml](./templates/project/init.yaml) template.

The application deployment phase uses the data provided in the application definition file (stored in [projects](../projects))
to determine which template will be used to generate an application
deployment, and further uses the definition data to populate the
deployment template and apply it to the cluster. For an example
deployment template, see [templates/project/public-http.yaml](./templates/project/public-http.yaml)
