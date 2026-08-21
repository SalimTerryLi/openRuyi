# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           perfstat
%define go_import_path  github.com/power-devops/perfstat
%define commit_id       5aafc221ea8c1ff54b0835cbd5f2386a8410be11

Name:           go-github-power-devops-perfstat
Version:        0+git20260817.5aafc22
Release:        %autorelease
Summary:        AIX perfstat interface for Go
License:        MIT
URL:            https://github.com/power-devops/perfstat
#!RemoteAsset:  sha256:934ca193f7d0b1333581727d8d2e86e00f0f89026243f07a40587d510eab64bb
Source0:        https://github.com/power-devops/perfstat/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/power-devops/perfstat) = %{version}

Requires:       go(golang.org/x/sys)

%description
Perfstat is a Go library for retrieving perfstat information on AIX systems.

%check
# AIX tests require IBM libperfstat; compile the upstream non-AIX stub here.
export GO111MODULE=off
go test -v doc.go types_*.go

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
