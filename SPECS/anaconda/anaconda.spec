# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor:   Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname anaconda

Name:           anaconda
Version:        46.4
Release:        %autorelease
Summary:        System installer
License:        GPL-2.0-or-later
URL:            https://fedoraproject.org/wiki/Anaconda
#!RemoteAsset:  sha256:a8012af0ddeb1c0d3ea148abb7f7b8999e2fef8f45136193c9423d16e40e997b
Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# rpm and libarchive are needed for driver disk handling
BuildRequires:  rpm-devel
BuildRequires:  libarchive-devel

# Tools used by the widgets resource bundle generation
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  glib-devel
BuildRequires:  libxml2

Requires:       anaconda-tui = %{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary:        Core of the Anaconda installer
# core/signal.py is under MIT
License:        GPL-2.0-or-later AND MIT
Requires:       python3-libs
Requires:       python3dist(crypt-r)
Requires:       python3dist(libdnf5) >= 5.2.15.0
Requires:       python3dist(blivet) >= 3.14.1
Requires:       python3-blockdev
Requires:       python3dist(python-meh)
Requires:       python3dist(iso639)
Requires:       python3dist(selinux)
Requires:       python3dist(rpm)
Requires:       python3dist(pyparted)
Requires:       python3dist(requests)
Requires:       python3dist(requests-file)
Requires:       python3dist(requests-ftp)
Requires:       python3dist(pykickstart) >= 3.77
Requires:       python3dist(langtable)
Requires:       util-linux
Requires:       python3dist(pygobject)
Requires:       python3dist(pwquality)
Requires:       python3dist(systemd-python)
Requires:       python3dist(productmd)
Requires:       python3dist(dasbus)
Requires:       python3dist(xkbregistry)

# pwquality only "recommends" the dictionaries it needs to do anything useful,
# which is apparently great for containers but unhelpful for the rest of us
Requires:       cracklib-dicts

Requires:       NetworkManager
Requires:       libnm
Requires:       kbd
Requires:       chrony
Requires:       systemd
Requires:       systemd-pam
Requires:       systemd-resolved
Requires:       python3dist(pid)
Requires:       grub
Requires:       anaconda-tui = %{version}-%{release}
Requires:       dbus-daemon
Requires:       /usr/bin/date

%description core
The anaconda-core package contains the program which was used to install your
system.

%package tui
Summary:        Support for text user interface
Requires:       anaconda-core = %{version}-%{release}
Requires:       python3dist(simpleline)

%description tui
The anaconda-tui package contains support for the text-based user interface.

%package widgets
Summary:        Anaconda GTK widgets
Requires:       %{__python3}

%description widgets
The anaconda-widgets package contains the GTK widgets used by the Anaconda
installer.

%package widgets-devel
Summary:        Development files for the Anaconda GTK widgets
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}

%description widgets-devel
This package contains libraries and header files needed for writing the
anaconda installer.

%package dracut
Summary:        The anaconda dracut module
Requires:       dracut
Requires:       xz
Requires:       python3dist(pykickstart)
Requires:       iputils

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%autosetup -p1

%build
# Work around an issue where a version mismatch between the automake version on
# the build system and what was used when the tarball was created will cause
# a failure.
# The glade configuration is passed to m4 via environment variable.
# Glade support is not packaged.
export ANACONDA_DISABLE_GLADE=yes
autoreconf -vfi

# Use the actual build-time release number, not the tarball creation time one.
%configure ANACONDA_RELEASE=%{release} --disable-glade --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

# Create an empty directory for addons
mkdir -p %{buildroot}%{_datadir}/anaconda/addons

# Create an empty directory for post-scripts
mkdir -p %{buildroot}%{_datadir}/anaconda/post-scripts

# The live installer is not packaged yet.
rm -rf \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/liveinst-setup.desktop \
  %{buildroot}/%{_bindir}/liveinst \
  %{buildroot}/%{_libexecdir}/liveinst-setup.sh \
  %{buildroot}/%{_libexecdir}/locale1-x11-sync \
  %{buildroot}/%{_userunitdir}/locale1-x11-sync.service \
  %{buildroot}/%{_datadir}/anaconda/gnome \
  %{buildroot}/%{_datadir}/polkit-1/actions/* \
  %{buildroot}/%{_datadir}/applications/liveinst.desktop

# The GTK frontend is not packaged, so drop its files.
rm -rf \
  %{buildroot}%{python3_sitearch}/pyanaconda/ui/gui \
  %{buildroot}%{_datadir}/anaconda/pixmaps \
  %{buildroot}%{_datadir}/anaconda/ui \
  %{buildroot}%{_datadir}/anaconda/window-manager \
  %{buildroot}%{_datadir}/anaconda/anaconda-gtk.css \
  %{buildroot}%{_datadir}/anaconda/gtk-4.0

%find_lang %{name}

%files

%files core -f %{name}.lang
%license COPYING
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_prefix}/lib/systemd/logind.conf.d/*
%{_bindir}/instperf
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_bindir}/anaconda-nm-disable-autocons
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%config(noreplace) %{_sysconfdir}/pam.d/anaconda
%{_prefix}/libexec/anaconda
%dir %{_datadir}/anaconda/post-scripts
%exclude %{_prefix}/libexec/anaconda/dd_*
%{python3_sitearch}/pyanaconda
%exclude %{python3_sitearch}/pyanaconda/rescue.py*
%exclude %{python3_sitearch}/pyanaconda/ui/tui/*
%{_bindir}/anaconda-cleanup
# Installer configuration files aren't updated post-installation,
# so the noreplace flag doesn't offer a practical benefit in this context.
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/*
%dir %{_sysconfdir}/%{name}/profile.d
%config(noreplace) %{_sysconfdir}/%{name}/profile.d/*

%files tui
%{python3_sitearch}/pyanaconda/rescue.py*
%{python3_sitearch}/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*

%files widgets-devel
%{_includedir}/AnacondaWidgets
%{_libdir}/libAnacondaWidgets.so
%{_datadir}/gtk-doc/html/AnacondaWidgets

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
%autochangelog
