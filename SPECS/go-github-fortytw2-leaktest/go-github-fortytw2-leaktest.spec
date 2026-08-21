# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           leaktest
%define go_import_path  github.com/fortytw2/leaktest

Name:           go-github-fortytw2-leaktest
Version:        1.3.0
Release:        %autorelease
Summary:        Goroutine leak detection for Go tests
License:        MIT
URL:            https://github.com/fortytw2/leaktest
#!RemoteAsset:  sha256:897726ed584a7c442eb660406e3438d4585b00c5f3769360eb19b18cace35292
Source0:        https://github.com/fortytw2/leaktest/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Leaktest provides helpers that detect goroutines leaked by Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
