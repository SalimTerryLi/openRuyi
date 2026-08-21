# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nuid
%define go_import_path  github.com/nats-io/nuid

Name:           go-github-nats-io-nuid
Version:        1.0.1
Release:        %autorelease
Summary:        Unique identifier generator for NATS
License:        Apache-2.0
URL:            https://github.com/nats-io/nuid
#!RemoteAsset:  sha256:a0b4fe5b40781add2a9fdb5d723313be5f5d11c1a79ea1dd2671278826ef078d
Source0:        https://github.com/nats-io/nuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
NUID is a high-performance unique identifier generator for NATS.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
