# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           renameio
%define go_import_path  github.com/google/renameio/v2

Name:           go-github-google-renameio-v2
Version:        2.0.2
Release:        %autorelease
Summary:        Atomic file replacement library for Go
License:        Apache-2.0
URL:            https://github.com/google/renameio
#!RemoteAsset:  sha256:b46ccf417206ab61191249aa483cda58cae61ff919834cc25cbab35ab2f12b28
Source0:        https://github.com/google/renameio/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Renameio atomically creates or replaces files and symbolic links while
handling temporary files and cleanup.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
