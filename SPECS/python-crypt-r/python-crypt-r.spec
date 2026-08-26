# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname crypt-r

Name:           python-%{srcname}
Version:        3.13.1
Release:        %autorelease
Summary:        The crypt_r module is a renamed copy of the crypt module as it was present in Python 3.12 before it was removed.
License:        PSF-2.0
URL:            https://github.com/fedora-python/crypt_r
#!RemoteAsset:  sha256:5bd46ad51f5b7fe5f0ecf49d8ba2cafd6fbd43aa3bb5efbcaa6b44df6340c1a6
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/crypt_r-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l crypt crypt_r _crypt_r

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The crypt_r module is a renamed copy of the crypt module as it was present in Python 3.12 before it was removed.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
