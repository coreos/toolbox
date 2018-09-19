Name:		toolbox
Version:	0.0.1
Release:	1%{?dist}
Summary:	script to launch privileged container with podman

License:	ASLv2.0
URL:		https://github.com/coreos/toolbox
Source0:	https://github.com/coreos/%{name}/archive/%{version}.tar.gz
Requires:	podman

%description
toolbox is a small script that launches a container to let
you bring in your favorite debugging or admin tools.

%define debug_package %{nil}

%prep
%autosetup

%build
# No building required

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 rhcos-toolbox $RPM_BUILD_ROOT/%{_bindir}/toolbox

%files
%license LICENSE
%doc README.md NOTICE
%{_bindir}/toolbox


%changelog
* Thu Sep 6 2018 Yu Qi Zhang <jerzhang@redhat.com> - 0.0.1
- Initial Specfile for Red Hat CoreOS Toolbox
