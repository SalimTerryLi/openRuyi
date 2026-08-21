# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           flock
%define go_import_path  github.com/gofrs/flock

Name:           go-github-gofrs-flock
Version:        0.13.0
Release:        %autorelease
Summary:        Thread-safe file locking library for Go
License:        BSD-3-Clause
URL:            https://github.com/gofrs/flock
#!RemoteAsset:  sha256:b65b14c43f82d61a0ffd2121ceaf2c4d0d85b13f0468e28127aa736b305d38df
Source0:        https://github.com/gofrs/flock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Flock implements thread-safe blocking and non-blocking file locks for Go
applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
