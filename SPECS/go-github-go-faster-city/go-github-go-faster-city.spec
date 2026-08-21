# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           city
%define go_import_path  github.com/go-faster/city

Name:           go-github-go-faster-city
Version:        1.0.1
Release:        %autorelease
Summary:        CityHash implementation for Go
License:        MIT
URL:            https://github.com/go-faster/city
#!RemoteAsset:  sha256:f6f7dfa5c392223303aac101999d0949be0cafef6e674ee085b0b58e45161bd4
Source0:        https://github.com/go-faster/city/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
City implements the CityHash family of non-cryptographic hash functions in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
