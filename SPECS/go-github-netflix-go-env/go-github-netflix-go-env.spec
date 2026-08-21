# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-env
%define go_import_path  github.com/Netflix/go-env

Name:           go-github-netflix-go-env
Version:        0.1.2
Release:        %autorelease
Summary:        Environment variable marshaling for Go structs
License:        Apache-2.0
URL:            https://github.com/Netflix/go-env
#!RemoteAsset:  sha256:7a4d23f206797d1eb80df4250023357f9723bf6d5371c420fece2d492eaac709
Source0:        https://github.com/Netflix/go-env/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Package env marshals and unmarshals environment variables using Go struct
field tags.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
