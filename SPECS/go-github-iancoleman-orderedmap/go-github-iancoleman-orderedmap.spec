# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           orderedmap
%define go_import_path  github.com/iancoleman/orderedmap

Name:           go-github-iancoleman-orderedmap
Version:        0.3.0
Release:        %autorelease
Summary:        Ordered map implementation for Go
License:        MIT
URL:            https://github.com/iancoleman/orderedmap
#!RemoteAsset:  sha256:69b0a10cf209e2701421055ea680ca8d4156beca884a9716ae3e08697c469a0f
Source0:        https://github.com/iancoleman/orderedmap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Orderedmap provides a Go map implementation that preserves key insertion
order and supports JSON serialization and deserialization.

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
