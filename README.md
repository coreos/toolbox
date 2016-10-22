# toolbox - bring your tools with you

toolbox is a small script that launches a container to let you bring in your favorite debugging or admin tools.

## Usage

```
$ /usr/bin/toolbox
...
-bash-4.3# dnf install tcpdump
...
-bash-4.3# tcpdump -i ens3
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens3, link-type EN10MB (Ethernet), capture size 65535 bytes
```

## Advanced Usage

### Use a custom image

toolbox uses a Fedora-based userspace environment by default, but this can be changed to any Docker image. Simply override environment variables in `$HOME/.toolboxrc`:

```
core@core-01 ~ $ cat ~/.toolboxrc
TOOLBOX_DOCKER_IMAGE=ubuntu-debootstrap
TOOLBOX_DOCKER_TAG=14.04
core@core-01 ~ $ toolbox
...
root@core-01:~# apt-get update && apt-get install tcpdump
```

### Automatically enter toolbox on login

Set an `/etc/passwd` entry for one of the users to `/usr/bin/toolbox`:

```
useradd bob -m -p '*' -s /usr/bin/toolbox -U -G sudo
```

Now when SSHing into the system as that user, toolbox will automatically be started:

```
$ ssh bob@hostname.example.com
CoreOS alpha (633.1.0)
...
-bash-4.3 # dnf install emacs
...
-bash-4.3 # emacs /media/root/etc/systemd/system/docker.service
```

### Custom shell profile in the container

When the container starts, the host root directory is mounted at `/media/root`, so shell commands can reference this path for loading startup files. Write the following example script to `~/.bashrc-toolbox` on the host:

```sh
# Allow accessing host services with systemctl
ln -fns /media/root/run/dbus /run/dbus
alias systemctl='capsh --drop=CAP_SYS_PTRACE -- -c '\''exec /usr/bin/systemctl "$@"'\'' --'

# Chain-load the default rcfile in the container
[ ! -r "$HOME/.bashrc" ] || . "$HOME/.bashrc"
```

Start the toolbox with this custom command to read it:

```sh
toolbox /bin/bash --login --rcfile "/media/root/$HOME/.bashrc-toolbox"
```

## Bugs

Please use the [CoreOS issue tracker][bugs] to report all bugs, issues, and feature requests.

[bugs]: https://github.com/coreos/bugs/issues/new?labels=component/toolbox
