# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ff
%define go_import_path  github.com/peterbourgon/ff/v3

Name:           go-github-peterbourgon-ff-v3
Version:        3.4.0
Release:        %autorelease
Summary:        Flags-first configuration helper for Go
License:        Apache-2.0
URL:            https://github.com/peterbourgon/ff
#!RemoteAsset:  sha256:499c5c5e259323e070976b5233b9104955df92fb7641c2c957f906aff1bf9057
Source0:        https://github.com/peterbourgon/ff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/pelletier/go-toml)
Requires:       go(gopkg.in/yaml.v2)

%description
FF is a flags-first package for configuring Go programs from command-line
flags, environment variables, and configuration files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
