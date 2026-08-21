# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           envload
%define go_import_path  github.com/lestrrat-go/envload
%define commit_id       a3eb8ddeffccdbca0eb6dd6cc7c7950c040a6546

Name:           go-github-lestrrat-go-envload
Version:        0+git20260819.a3eb8dd
Release:        %autorelease
Summary:        Scoped environment variable loader for Go
License:        MIT
URL:            https://github.com/lestrrat-go/envload
#!RemoteAsset:  sha256:22083031641e7fae1277b326f952894ad795d22e415b1fed9e1b89597bd6975e
Source0:        https://github.com/lestrrat-go/envload/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
Envload saves and restores environment variables so applications and tests
can make temporary environment changes without leaking them to later work.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
