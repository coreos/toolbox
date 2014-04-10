## toolbox - bring your tools with you

toolbox is a small script that launches a container to let you bring in your favorite debugging or admin tools.

### Usage

```
$ /usr/bin/toolbox
[root@srv-3qy0p ~]# yum install tcpdump
[root@srv-3qy0p ~]# tcpdump -i ens3
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens3, link-type EN10MB (Ethernet), capture size 65535 bytes
```

### Advanced Usage

Set a `/etc/passwd` entry for one of the users to `/usr/bin/toolbox`.

```
useradd bob -m -p '*' -s /usr/bin/toolbox
```

```
ssh bob@hostname.example.com

   ______                ____  _____
  / ____/___  ________  / __ \/ ___/
 / /   / __ \/ ___/ _ \/ / / /\__ \
/ /___/ /_/ / /  /  __/ /_/ /___/ /
\____/\____/_/   \___/\____//____/
[root@srv-3qy0p ~]# yum install emacs
[root@srv-3qy0p ~]# emacs /media/root/etc/systemd/system/docker.service
```
