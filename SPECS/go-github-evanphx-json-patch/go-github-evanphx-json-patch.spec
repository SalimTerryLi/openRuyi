# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json-patch
%define go_import_path  github.com/evanphx/json-patch

Name:           go-github-evanphx-json-patch
Version:        5.9.11
Release:        %autorelease
Summary:        JSON Patch and JSON Merge Patch library for Go
License:        BSD-3-Clause
URL:            https://github.com/evanphx/json-patch
#!RemoteAsset:  sha256:3712548f40499ac85538e15b839b3140f4f1bf2480baf42773e4423693d436ae
Source0:        https://github.com/evanphx/json-patch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/v5) = %{version}

Requires:       go(github.com/jessevdk/go-flags)

%description
This package provides implementations of JSON Patch and JSON Merge Patch. It
includes both the original import path and the v5 module from the same source
repository.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
