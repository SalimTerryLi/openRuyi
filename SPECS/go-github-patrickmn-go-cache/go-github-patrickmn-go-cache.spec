# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cache
%define go_import_path  github.com/patrickmn/go-cache

Name:           go-github-patrickmn-go-cache
Version:        2.1.0
Release:        %autorelease
Summary:        In-memory key-value cache for Go
License:        MIT
URL:            https://github.com/patrickmn/go-cache
#!RemoteAsset:  sha256:3ab025f2f580f8818a5357db52596fef1b0ad5945816a022c8b805ba46dc93be
Source0:        https://github.com/patrickmn/go-cache/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-cache is a thread-safe in-memory key-value cache with expiration support for
applications running on a single machine.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
