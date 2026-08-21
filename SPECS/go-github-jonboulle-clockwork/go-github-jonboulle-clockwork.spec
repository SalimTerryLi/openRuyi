# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clockwork
%define go_import_path  github.com/jonboulle/clockwork

Name:           go-github-jonboulle-clockwork
Version:        0.5.0
Release:        %autorelease
Summary:        Replaceable real and fake clocks for Go
License:        Apache-2.0
URL:            https://github.com/jonboulle/clockwork
#!RemoteAsset:  sha256:9cbf34c4fd4e88f317a4b5fb259f6c2cf374d06ad3951b24934ef7d85732de78
Source0:        https://github.com/jonboulle/clockwork/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Clockwork provides a clock interface and a controllable fake clock for
deterministic tests of time-dependent Go code.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
