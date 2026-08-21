# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hjson-go
%define go_import_path  github.com/hjson/hjson-go/v4

Name:           go-github-hjson-hjson-go-v4
Version:        4.6.0
Release:        %autorelease
Summary:        Hjson implementation for Go
License:        MIT
URL:            https://github.com/hjson/hjson-go
#!RemoteAsset:  sha256:5ee5ab2b191f4464a9ac98c3047441d94bd9d5fdeb77f651f9d90f1dacd54f74
Source0:        https://github.com/hjson/hjson-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package implements the Hjson human-friendly configuration format in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
