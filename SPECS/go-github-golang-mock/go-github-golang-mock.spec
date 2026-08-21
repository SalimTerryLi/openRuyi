# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mock
%define go_import_path  github.com/golang/mock

Name:           go-github-golang-mock
Version:        1.6.0
Release:        %autorelease
Summary:        Mocking framework and generator for Go
License:        Apache-2.0
URL:            https://github.com/golang/mock
#!RemoteAsset:  sha256:470174971c3a63361149a30f5b2d3a716a198afeb6cc71daa30712faa7293942
Source0:        https://github.com/golang/mock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-mockgen-restore-environment-after-GOPATH-tests.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)

%description
GoMock provides controller and matcher libraries together with the mockgen
source and reflection-based mock generator.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
