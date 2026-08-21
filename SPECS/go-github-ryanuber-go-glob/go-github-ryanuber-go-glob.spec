# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-glob
%define go_import_path  github.com/ryanuber/go-glob

Name:           go-github-ryanuber-go-glob
Version:        1.0.0
Release:        %autorelease
Summary:        Basic glob matching library for Go
License:        MIT
URL:            https://github.com/ryanuber/go-glob
#!RemoteAsset:  sha256:4e2b03027a6de87825fcf450a728c86b83d9c30b062310323c6009e298da6711
Source0:        https://github.com/ryanuber/go-glob/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides basic glob pattern matching for Go strings.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
