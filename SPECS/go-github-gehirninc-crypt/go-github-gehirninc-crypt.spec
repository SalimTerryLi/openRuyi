# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           crypt
%define go_import_path  github.com/GehirnInc/crypt
%define commit_id       8cc1b52080c5761aa65952b1c39dd889bf54d76c

Name:           go-github-gehirninc-crypt
Version:        0+git20260817.8cc1b52
Release:        %autorelease
Summary:        Password crypt functions for Go
License:        BSD-2-Clause
URL:            https://github.com/GehirnInc/crypt
#!RemoteAsset:  sha256:6cf7393b20f4756d517b1da5f913fce8f7e231a2ce34869636cd08e6c44f2e54
Source0:        https://github.com/GehirnInc/crypt/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides pure Go implementations of common Unix crypt
algorithms.

%files
%doc README.rst
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
