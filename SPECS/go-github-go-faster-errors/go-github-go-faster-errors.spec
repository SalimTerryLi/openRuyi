# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/go-faster/errors

Name:           go-github-go-faster-errors
Version:        0.8.0
Release:        %autorelease
Summary:        Error wrapping utilities for Go
License:        BSD-3-Clause
URL:            https://github.com/go-faster/errors
#!RemoteAsset:  sha256:a7fa07f056a323d22c3418c1972494f3aaa286b930aab17716abd7b2bd4815a9
Source0:        https://github.com/go-faster/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Errors provides error creation, wrapping, unwrapping, and stack inspection
utilities for Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
