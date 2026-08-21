# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-strftime
%define go_import_path  github.com/ncruces/go-strftime

Name:           go-github-ncruces-go-strftime
Version:        1.0.0
Release:        %autorelease
Summary:        Strftime and strptime compatible time formatting for Go
License:        MIT
URL:            https://github.com/ncruces/go-strftime
#!RemoteAsset:  sha256:ab7541b51163409bdc9722ab4fe64f1085385d86c87abd26678823644b3d404a
Source0:        https://github.com/ncruces/go-strftime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-strftime provides strftime-compatible formatting and strptime-compatible
parsing for Go time values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
