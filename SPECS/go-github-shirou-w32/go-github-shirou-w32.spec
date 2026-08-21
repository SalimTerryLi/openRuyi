# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           w32
%define go_import_path  github.com/shirou/w32
%define commit_id       bb4de0191aa41b5507caa14b0650cdbddcd9280b

Name:           go-github-shirou-w32
Version:        0+git20260819.bb4de01
Release:        %autorelease
Summary:        Windows API wrappers for Go
License:        MIT
URL:            https://github.com/shirou/w32
#!RemoteAsset:  sha256:a9f7ba1ef1f0752e0a3a17006dec9c504bcffb27a37446abf30904477135da03
Source0:        https://github.com/shirou/w32/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
W32 provides Go wrappers for selected Windows system and graphical APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
