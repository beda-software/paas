from fabric.api import local
import os
import tempfile

inventory_template = """
[bro-host]
{ip}

[bro-host:vars]
ansible_ssh_user=root
swapfile_size=4G
"""

def deploy():
    server_ip = os.environ['SERVER_IP']
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(inventory_template.format(ip=server_ip))
        fp.seek(0)
        local("ansible-playbook -i {0} server.yml".format(fp.name))
