# ansible-aws_ecr_credential_helper

[![CI](https://github.com/thiagoalmeidasa/ansible-role-aws-ecr-credential-helper/actions/workflows/ci.yml/badge.svg)](https://github.com/thiagoalmeidasa/ansible-role-aws-ecr-credential-helper/actions/workflows/ci.yml)

Ansible role for aws_ecr_credential_helper

## Ansible requirements

### Ansible version

Minimum required ansible version is 2.4.

### Ansible role dependencies

None.

## Installation

### Install with Ansible Galaxy

```shell
ansible-galaxy install thiagoalmeidasa.aws_ecr_credential_helper
```

Basic usage is:

```yaml
- hosts: all
  roles:
    - role: thiagoalmeidasa.aws_ecr_credential_helper
```

### Install with git

If you do not want a global installation, clone it into your `roles_path`.

```shell
git clone git@github.com:thiagoalmeidasa/ansible-role-aws_ecr_credential_helper.git /path/to/roles_path
```

But I often add it as a submdule in a given `playbook_dir` repository.

```shell
git submodule add git@github.com:thiagoalmeidasa/ansible-role-aws_ecr_credential_helper.git <playbook_dir>/roles/aws_ecr_credential_helper
```

As the role is not managed by Ansible Galaxy, you do not have to specify the
github user account.

Basic usage is:

```yaml
- hosts: all
  roles:
  - role: aws_ecr_credential_helper
```

## Role Variables

Variables are divided in three types.

The [default vars](#default-vars) section shows you which variables you may
override in your ansible inventory. As a matter of fact, all variables should
be defined there for explicitness, ease of documentation as well as overall
role manageability.

The [mandatory variables](#mandatory-variables) section contains variables that
for several reasons do not fit into the default variables. As name implies,
they must absolutely be defined in the inventory or else the role will
fail. It is a good thing to avoid reach for these as much as possible and/or
design the role with clear behavior when they're undefined.

The [context variables](#context-variables) are shown in section below hint you
on how runtime context may affects role execution.

### Default vars

Role default variables from `defaults/main.yml`.

```yaml
aws_ecr_cred_helper_bin_version: 0.5.0
aws_ecr_cred_helper_pkg: "amazon-ecr-credential-helper"
aws_ecr_cred_helper_docker_config_dirs:
  - "{{ ansible_user_dir }}"
install_from_binary: false

# cred_helper_config: {}
# credsStore: ecr-login

```

### Mandatory variables

None.

### Context variables

None.



## License

MIT.

## Author Information

Thiago Almeida.
