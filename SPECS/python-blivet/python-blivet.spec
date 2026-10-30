# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname blivet

Name:           python-blivet
Version:        3.14.2
Release:        %autorelease
Summary:        Blivet is a python module for system storage configuration.
License:        LGPL-2.1-or-later
URL:            https://github.com/storaged-project/blivet
#!RemoteAsset:  sha256:db2cd996ed354d47fdc60740d912a102250a0fc469bfe17df6bced649c172e5b
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  gettext
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)

Requires:       parted
Requires:       python3-blockdev
Requires:       python3-bytesize
Requires:       python3dist(dasbus)
Requires:       python3dist(packaging)
Requires:       python3-libmount
Requires:       python3dist(pygobject)
Requires:       python3dist(pyparted)
Requires:       python3dist(pyudev)
Requires:       python3dist(selinux)
Requires:       util-linux
Requires:       lsof
Requires:       systemd-udev

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%generate_buildrequires
%pyproject_buildrequires

# The dbus service and translation files are installed outside of pyproject.
%install -a
make install-dbus DESTDIR=%{buildroot}
make -C po install DESTDIR=%{buildroot}
%find_lang %{srcname}

# TODO: check needs ton of other dependencies - 251
%check

%files -f %{pyproject_files} -f %{srcname}.lang
%doc README.md ChangeLog examples
%license COPYING
%{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*
%{_libexecdir}/*
%{_unitdir}/*

%changelog
%autochangelog
