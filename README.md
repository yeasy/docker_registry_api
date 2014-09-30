Docker Registry APIs
===================

Highlevel wrapper of the Docker registry's APIs

## Usage

### Download the code from Github
```
git clone https://github.com/yeasy/docker_registry_api.git
```

### Import and use the lib
```
from docker_registry_api import DockerRegistryAPI

api = DockerRegistryAPI('192.168.56.101')
```


## Functions

### get_repositories()
return: List of all repositories with name and description, e.g., 
`[{"description": "", "name": "training/webapp"},...]`
### get_images_of_repo(repo):
:param repo: The name of the checked repository.

return: Dict of the images in the repository, e.g., 
`{"10.04": "3db9c44f45209632d6050b35958829c3a2aa256d81b9a7be45b362ff85c54710
",...}`
