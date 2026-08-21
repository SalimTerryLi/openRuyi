# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-perf
%define go_import_path  github.com/elastic/go-perf
%define commit_id       af0ee0c731b75685457e0d7a0b65002f578d6096

Name:           go-github-elastic-go-perf
Version:        0+git20260819.af0ee0c
Release:        %autorelease
Summary:        Linux perf event API client for Go
License:        BSD-3-Clause
URL:            https://github.com/elastic/go-perf
#!RemoteAsset:  sha256:5e140ea3816afb7a73fe07d5dd1d48af9aea81d9775c32788206ddda57e05c72
Source0:        https://github.com/elastic/go-perf/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Go-perf provides access to Linux perf events, including Elastic extensions
used by its kernel profiling implementation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
