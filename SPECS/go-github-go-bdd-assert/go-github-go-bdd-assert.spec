# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/go-bdd/assert
%define commit_id       236f014302814a7115ca2c723734e1781c1af108

Name:           go-github-go-bdd-assert
Version:        0+git20260817.236f014
Release:        %autorelease
Summary:        Minimal assertion library for Go
License:        MIT
URL:            https://github.com/go-bdd/assert
#!RemoteAsset:  sha256:59bf12374240b00ae18fb708c9e1e211ed4a0a467bacc609942689bce8d2cb97
Source0:        https://github.com/go-bdd/assert/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Assert provides simple Go assertion helpers that return errors without
introducing a larger test framework.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
