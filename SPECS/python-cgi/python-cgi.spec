# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname legacy-cgi

Name:           python-%{srcname}
Version:        2.6.4
Release:        %autorelease
Summary:        This is a fork of the standard library modules cgi and cgitb.
License:        PSF-2.0
URL:            https://github.com/jackrosenthal/legacy-cgi
#!RemoteAsset:  sha256:abb9dfc7835772f7c9317977c63253fd22a7484b5c9bbcdca60a29dcce97c577
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/legacy_cgi-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l cgi cgitb

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a fork of the standard library modules cgi and cgitb.
They have been removed from the Python standard libary in Python 3.13 by PEP-594.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
%py3_shebang_fix cgi.py

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
