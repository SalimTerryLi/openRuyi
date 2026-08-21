# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-structform
%define go_import_path  github.com/elastic/go-structform

Name:           go-github-elastic-go-structform
Version:        0.0.12
Release:        %autorelease
Summary:        Structured data formatters for Go
License:        Apache-2.0
URL:            https://github.com/elastic/go-structform
#!RemoteAsset:  sha256:43678e1e1a45be73f6dd972f069250708d8a5363c4f6357377a471710af0db5d
Source0:        https://github.com/elastic/go-structform/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
Go-structform provides efficient serializers, deserializers, and transcoders
for structured data through a common visitor interface.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
