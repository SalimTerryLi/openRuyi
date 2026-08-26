# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pykickstart

Name:           python-%{srcname}
Version:        3.78
Release:        %autorelease
Summary:        Python utilities for manipulating kickstart files.
License:        GPL-2.0-only
URL:            http://fedoraproject.org/wiki/pykickstart
#!RemoteAsset:  sha256:f9752920e48408a21588cf734a49cab6f4bdf7ab80c3262099a775bc9abb1895
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pykickstart

BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python utilities for manipulating kickstart files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
%{_bindir}/ksshell
%{_mandir}/man1/ksflatten.1.gz
%{_mandir}/man1/ksshell.1.gz
%{_mandir}/man1/ksvalidator.1.gz
%{_mandir}/man1/ksverdiff.1.gz

%changelog
%autochangelog
