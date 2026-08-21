# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           name
%define go_import_path  github.com/pascaldekloe/name

Name:           go-github-pascaldekloe-name
Version:        1.0.1
Release:        %autorelease
Summary:        Naming convention conversions for Go
License:        CC0-1.0
URL:            https://github.com/pascaldekloe/name
#!RemoteAsset:  sha256:7282dbac6517db9ef65ca6986f88aff0a7943aa3c1bd253af318c35380418f34
Source0:        https://github.com/pascaldekloe/name/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Name converts identifiers between common naming conventions used in source
code and generated APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
