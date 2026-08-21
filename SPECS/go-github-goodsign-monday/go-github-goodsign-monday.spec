# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           monday
%define go_import_path  github.com/goodsign/monday

Name:           go-github-goodsign-monday
Version:        1.0.2
Release:        %autorelease
Summary:        Localized date formatting and parsing for Go
License:        BSD-2-Clause
URL:            https://github.com/goodsign/monday
#!RemoteAsset:  sha256:0f01a6f60034a2add64192d649c7c4727c1727d599f6347bb0ff6cff27c77e40
Source0:        https://github.com/goodsign/monday/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Monday formats and parses localized month and weekday names while retaining
the layout conventions of Go's standard time package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
