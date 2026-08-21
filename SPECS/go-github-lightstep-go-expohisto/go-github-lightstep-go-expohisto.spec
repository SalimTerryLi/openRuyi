# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-expohisto
%define go_import_path  github.com/lightstep/go-expohisto

Name:           go-github-lightstep-go-expohisto
Version:        1.0.0
Release:        %autorelease
Summary:        Base-2 exponential histogram data structures for Go
License:        Apache-2.0
URL:            https://github.com/lightstep/go-expohisto
#!RemoteAsset:  sha256:4d11879395f6dd5c0fd7f6b2274c3c98e8350d8844be5d4e6b5fd98ee2255912
Source0:        https://github.com/lightstep/go-expohisto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides mapping functions and fixed-size data structures for
OpenTelemetry base-2 exponential histograms.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
