# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           atomic
%define go_import_path  github.com/natefinch/atomic

Name:           go-github-natefinch-atomic
Version:        1.0.1
Release:        %autorelease
Summary:        Atomic file writing library for Go
License:        MIT
URL:            https://github.com/natefinch/atomic
#!RemoteAsset:  sha256:4027dfa69d6ef36b20666ee3bf646d399041c4ddd0da5164f8ef0cae4a849eb0
Source0:        https://github.com/natefinch/atomic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides atomic file replacement operations for Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
