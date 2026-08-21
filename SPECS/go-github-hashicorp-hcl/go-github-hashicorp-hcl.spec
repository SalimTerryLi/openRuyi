# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hcl
%define go_import_path  github.com/hashicorp/hcl
# Vault's fork rejects duplicate attributes used by old printer fixtures.
%define go_test_exclude %{go_import_path}/hcl/printer

Name:           go-github-hashicorp-hcl
Version:        1.0.1+vault7
Release:        %autorelease
Summary:        HashiCorp Configuration Language library for Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/hcl
#!RemoteAsset:  sha256:94096a9ec3220910f5cf72c35cbd56d0b98142bbc4e608ea5b183566f3b82402
Source0:        https://github.com/hashicorp/hcl/archive/refs/tags/v1.0.1-vault-7.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-1.0.1-vault-7
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)

Provides:       go(%{go_import_path}) = %{version}

%description
This package decodes HashiCorp Configuration Language into Go structures.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
