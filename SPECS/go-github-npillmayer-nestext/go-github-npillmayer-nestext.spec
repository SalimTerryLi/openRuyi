# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nestext
%define go_import_path  github.com/npillmayer/nestext
# The release archive does not include the external NestedText test suite.
%define go_test_exclude %{go_import_path}/testsuite

Name:           go-github-npillmayer-nestext
Version:        0.1.3
Release:        %autorelease
Summary:        NestedText processing library for Go
License:        Apache-2.0
URL:            https://github.com/npillmayer/nestext
#!RemoteAsset:  sha256:b6677619008332c3fb6318ec31aacd9624c51ddc77f683341b6847c8ad53ab7e
Source0:        https://github.com/npillmayer/nestext/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides tools for processing the human-friendly NestedText data
format.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
