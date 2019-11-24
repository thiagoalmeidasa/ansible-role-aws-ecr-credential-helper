import os

from packaging import version

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ecr_credential_helper_in_path(host):
    cmd = host.exists('docker-credential-ecr-login')

    assert cmd is True


def test_ecr_credential_helper_version(host):
    cmd = host.check_output('docker-credential-ecr-login version')

    assert version.parse(cmd) >= version.parse("0.6")
