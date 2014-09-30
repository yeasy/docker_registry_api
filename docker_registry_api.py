__author__ = 'baohua'

import json
from urllib2 import urlopen

class DockerRegistryAPI():
    """
    Provide high level wrappers to use docker-registry's api
    """

    def __init__(self, server='127.0.0.1', port=5000):
        self.server = server
        self.port = port
        self.base_url = 'http://%s:%s/v1' %(server, port)

    def get_repositories(self):
        """
        :return: List of all repositories with name and description, e.g.,
        [{"description": "", "name": "training/webapp"},...]
        """
        response = urlopen(self.base_url+'/search').read()
        raw_result = json.loads(response)
        repositories = raw_result["results"]
        #repositories = [e["name"] for e in raw_result["results"]]
        return repositories

    def get_images_of_repo(self, repo):
        """
        :param repo: The name of the checked repository.
        :return: Dict of the images in the repo, e.g., {"10.04":
        "3db9c44f45209632d6050b35958829c3a2aa256d81b9a7be45b362ff85c54710",...}
        """
        response = urlopen(self.base_url+'/repositories/%s/tags' % repo).read()
        raw_result = json.loads(response)
        return raw_result


if __name__ == '__main__':
    api = DockerRegistryAPI('192.168.56.101')
    repos = api.get_repositories()
    for repo in repos['name']:
        print "Repo=%s" % repo
        images = api.get_images_of_repo(repo)
        print "Images=%s" % images.keys()
