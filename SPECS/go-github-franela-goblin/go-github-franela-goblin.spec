# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goblin
%define go_import_path  github.com/franela/goblin

Name:           go-github-franela-goblin
Version:        0.0.3
Release:        %autorelease
Summary:        Mocha-like BDD testing framework for Go
License:        MIT
URL:            https://github.com/franela/goblin
#!RemoteAsset:  sha256:7b31c9a5c92484ed9c913c0ca6fa30a0b80c1b8cd10886140e60717e210b2c5f
Source0:        https://github.com/franela/goblin/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Goblin is a Mocha-like behavior-driven testing framework for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
