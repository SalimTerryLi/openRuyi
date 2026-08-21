# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           camelcase
%define go_import_path  github.com/fatih/camelcase

Name:           go-github-fatih-camelcase
Version:        1.0.0
Release:        %autorelease
Summary:        Camel case word splitting library for Go
License:        MIT
URL:            https://github.com/fatih/camelcase
#!RemoteAsset:  sha256:c131a14b89faa54c71c0d4af47f53839a5deb6db3ac4c22faf90d9e9873f16fc
Source0:        https://github.com/fatih/camelcase/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/fatih/camelcase) = %{version}

%description
Camelcase splits camel case strings into their constituent words, including
Unicode letters, numbers, and common acronym patterns.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
