# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           concurrent-map
%define go_import_path  github.com/orcaman/concurrent-map/v2

Name:           go-github-orcaman-concurrent-map-v2
Version:        2.0.1
Release:        %autorelease
Summary:        Generic concurrent map for Go
License:        MIT
URL:            https://github.com/orcaman/concurrent-map
#!RemoteAsset:  sha256:96e64f1af73d608d5122a1816b1b63bd23fcc4881865e8a1a9b4082c38e6327b
Source0:        https://github.com/orcaman/concurrent-map/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Concurrent-map provides a generic, sharded map with thread-safe access for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
