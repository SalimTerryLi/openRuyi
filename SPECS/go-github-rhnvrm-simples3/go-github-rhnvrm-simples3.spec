# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           simples3
%define go_import_path  github.com/rhnvrm/simples3
# The test suite requires credentials and access to a real S3 service.
%define go_test_exclude %{go_import_path}

Name:           go-github-rhnvrm-simples3
Version:        0.11.1
Release:        %autorelease
Summary:        Simple Amazon S3 client library for Go
License:        BSD-2-Clause
URL:            https://github.com/rhnvrm/simples3
#!RemoteAsset:  sha256:88f84362a643536b18ff02bc6fa3f399c39877156cad60957acc61405e234542
Source0:        https://github.com/rhnvrm/simples3/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a small Go client for manipulating Amazon S3 objects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
