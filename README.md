# toolbox - bring your tools with you

toolbox is a small script that launches a container to let you bring in your favorite debugging or admin tools.

There are currently two scripts that live within this repository:
 - toolbox: designed for Container Linux, uses rkt and systemd-nspawn
 - rhcos-toolbox: designed for Red Hat CoreOS, uses podman

## Usage

```
$ /usr/bin/toolbox
Spawning container core-fedora-latest on /var/lib/toolbox/core-fedora-latest.
Press ^] three times within 1s to kill container.
[root@localhost ~]# dnf -y install tcpdump
...
[root@localhost ~]# tcpdump -i ens3
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens3, link-type EN10MB (Ethernet), capture size 65535 bytes
```

## Advanced Usage

### Use a custom image

toolbox uses a Fedora-based userspace environment by default, but this can be changed to any Docker image. Simply override environment variables in `$HOME/.toolboxrc`:

#### toolbox

```
core@core-01 ~ $ cat ~/.toolboxrc
TOOLBOX_DOCKER_IMAGE=ubuntu-debootstrap
TOOLBOX_DOCKER_TAG=14.04
core@core-01 ~ $ toolbox
Spawning container core-ubuntu-debootstrap-14.04 on /var/lib/toolbox/core-ubuntu-debootstrap-14.04.
Press ^] three times within 1s to kill container.
root@core-01:~# apt-get update && apt-get install tcpdump
```

#### rhcos-toolbox

```
core@core-01 ~ $ cat ~/.toolboxrc
REGISTRY=registry.redhat.io
IMAGE=rhel7/rhel-tools:latest
core@core-01 ~ $ toolbox
Spawning a container 'toolbox-test' with image 'registry.redhat.io/rhel7/rhel-tools:latest'
```

### Automatically enter toolbox on login

Set an `/etc/passwd` entry for one of the users to `/usr/bin/toolbox`:

```sh
useradd bob -m -p '*' -s /usr/bin/toolbox -U -G sudo,docker,rkt
```

Now when SSHing into the system as that user, toolbox will automatically be started:

```
$ ssh bob@hostname.example.com
Container Linux by CoreOS alpha (1284.0.0)
...
Spawning container bob-fedora-latest on /var/lib/toolbox/bob-fedora-latest.
Press ^] three times within 1s to kill container.
[root@localhost ~]# dnf -y install emacs-nox
...
[root@localhost ~]# emacs /media/root/etc/systemd/system/docker.service
```
