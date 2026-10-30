# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor:   Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pykickstart

Name:           python-%{srcname}
Version:        3.78
Release:        %autorelease
Summary:        Python utilities for manipulating kickstart files
License:        GPL-2.0-only
URL:            https://fedoraproject.org/wiki/pykickstart
#!RemoteAsset:  sha256:f9752920e48408a21588cf734a49cab6f4bdf7ab80c3262099a775bc9abb1895
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Needed to install the translations, which are not part of the wheel.
BuildRequires:  make
BuildRequires:  gettext
# Needed by the test suite.
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python utilities for manipulating kickstart files.

This package provides the pykickstart library and the ksvalidator, ksflatten,
ksshell and ksverdiff tools.

%generate_buildrequires
%pyproject_buildrequires

%install -a
make -C po install PYTHON=%{__python3} DESTDIR=%{buildroot}

%check
LC_ALL=C make test-no-coverage PYTHON=%{__python3}

%files -f %{pyproject_files}
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{_bindir}/ksflatten
%{_bindir}/ksshell
%{_bindir}/ksvalidator
%{_bindir}/ksverdiff
%{_mandir}/man1/ksflatten.1*
%{_mandir}/man1/ksshell.1*
%{_mandir}/man1/ksvalidator.1*
%{_mandir}/man1/ksverdiff.1*
%{python3_sitelib}/%{srcname}/locale

%changelog
%autochangelog
