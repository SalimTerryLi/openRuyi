# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname crypt-r
%global pypi_name crypt_r

Name:           python-%{srcname}
Version:        3.13.1
Release:        %autorelease
Summary:        A copy of the crypt module that was removed in Python 3.13
License:        Python-2.0.1
URL:            https://github.com/fedora-python/%{pypi_name}
#!RemoteAsset:  sha256:5bd46ad51f5b7fe5f0ecf49d8ba2cafd6fbd43aa3bb5efbcaa6b44df6340c1a6
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l crypt crypt_r _crypt_r

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  libxcrypt-devel

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The crypt_r module is a renamed copy of the crypt module as it was present in
Python 3.12 before it was removed.

Unlike crypt, this library always exposes the crypt_r(3) function, not crypt(3).

%generate_buildrequires
%pyproject_buildrequires

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} tests/test_crypt_r.py

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
