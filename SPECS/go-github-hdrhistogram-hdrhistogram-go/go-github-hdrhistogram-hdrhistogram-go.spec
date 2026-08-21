# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hdrhistogram-go
%define go_import_path  github.com/HdrHistogram/hdrhistogram-go

Name:           go-github-hdrhistogram-hdrhistogram-go
Version:        1.3.0
Release:        %autorelease
Summary:        HDR Histogram implementation for Go
License:        MIT
URL:            https://github.com/HdrHistogram/hdrhistogram-go
#!RemoteAsset:  sha256:26d7d068dc314f85ce1d9ba02ce8137c8d060b506431ddd7ca1c8f5d667c65d0
Source0:        https://github.com/HdrHistogram/hdrhistogram-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
HdrHistogram provides a Go implementation of the High Dynamic Range Histogram
data structure for recording and analyzing sampled values.

%install
%buildsystem_golangmodules_install
# This noarch package provides Go sources, not the upstream command binaries.
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/bin

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
