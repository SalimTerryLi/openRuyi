# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uuid
%define go_import_path  github.com/gofrs/uuid

Name:           go-github-gofrs-uuid
Version:        4.4.0
Release:        %autorelease
Summary:        UUID generation and parsing for Go
License:        MIT
URL:            https://github.com/gofrs/uuid
#!RemoteAsset:  sha256:10dd2b8e4c99e4975f11b29ec2e4d48f0bf3574e89541f81d4cd228cffa3057c
Source0:        https://github.com/gofrs/uuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Uuid provides generation, parsing, formatting, and database integration for
universally unique identifiers in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
