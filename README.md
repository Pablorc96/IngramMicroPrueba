# IngramMicroTest
### DevOps Test - Ingram Micro - Pablo Ruiz Ciudad

This test is composed of a Python script that runs the command `geoiplookup <domain>` using
a list of domains specified in the file `src/domains.txt` as well as an ansible playbook
that fulfills a similar function.

## Instructions

### Task 1
The Python script provided can be run with
```
docker-compose up -d
```

### Task 2
Dockerfile and docker-compose.yaml provided in main directory. This command will build
the docker image and generate a container running the script:
```
docker-compose up -d
```

### Task 3 
Instead of creating an Opsocode Chef cookbook, I decided to use an **ansible playbook**
since I have more experience with it and the functionality is similar.
The domain list in this case is supplied inside the playbook itself.

To run the playbook, make sure ansible is installed and use:
```
ansible-playbook src/ansible/dns_resolver_ansible.yaml
```
