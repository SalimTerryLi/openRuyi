# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-strftime
%define go_import_path  github.com/jehiah/go-strftime
%define commit_id       1d33003b386959af197ba96475f198c114627b5e

Name:           go-github-jehiah-go-strftime
Version:        0+git20260819.1d33003
Release:        %autorelease
Summary:        Strftime implementation for Go
License:        MIT
URL:            https://github.com/jehiah/go-strftime
#!RemoteAsset:  sha256:ded04df0484eca3b57b148fed2071e9b0016f92aa612948ea88aa277c9737e57
Source0:        https://github.com/jehiah/go-strftime/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-strftime formats Go time values using strftime-compatible conversion
specifications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
