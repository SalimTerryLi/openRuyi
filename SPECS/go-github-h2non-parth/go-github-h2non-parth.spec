# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           parth
%define go_import_path  github.com/h2non/parth

Name:           go-github-h2non-parth
Version:        2.0.1
Release:        %autorelease
Summary:        URL path segment parsing for Go
License:        MIT
URL:            https://github.com/h2non/parth
#!RemoteAsset:  sha256:3c128942ba4158a49d8c03ed040f3e0687b13a49fff976d7b6f54a7bd6fbad25
Source0:        https://github.com/h2non/parth/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Parth extracts and converts URL path segments into Go values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
