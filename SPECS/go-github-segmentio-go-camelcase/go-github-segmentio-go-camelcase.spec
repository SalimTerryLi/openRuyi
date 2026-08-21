# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-camelcase
%define commit_id       7085f1e3c734f696a4cd28568c33abae3100126f
%define go_import_path  github.com/segmentio/go-camelcase

Name:           go-github-segmentio-go-camelcase
Version:        0+git20260816.7085f1e
Release:        %autorelease
Summary:        Fast camel case splitting library for Go
License:        MIT
URL:            https://github.com/segmentio/go-camelcase
#!RemoteAsset:  sha256:e88430665acb69666a727d9695992edd501180b844928bb0377253b02c252b48
Source0:        https://github.com/segmentio/go-camelcase/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/segmentio/go-camelcase) = %{version}

%description
Go-camelcase provides a small and fast function for splitting camel case
strings into words.

%prep
%autosetup -n %{_name}-%{commit_id}

%files
%doc Readme.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
