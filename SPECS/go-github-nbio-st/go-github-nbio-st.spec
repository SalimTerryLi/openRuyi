# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           st
%define go_import_path  github.com/nbio/st
%define commit_id       e9e8d9816f3268def6dcbd2dea03301f40e9de94
# The readme package intentionally demonstrates failing assertion output.
%define go_test_exclude_glob %{go_import_path}/readme

Name:           go-github-nbio-st
Version:        0+git20260817.e9e8d98
Release:        %autorelease
Summary:        Lightweight test assertions for Go
License:        MIT
URL:            https://github.com/nbio/st
#!RemoteAsset:  sha256:5da8dd41c91924265a9f66e53be006e79690ed3f230d1eeeb4d24a9fe3cbb134
Source0:        https://github.com/nbio/st/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
St provides compact assertion helpers for Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
