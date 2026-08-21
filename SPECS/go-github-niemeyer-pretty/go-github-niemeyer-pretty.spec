# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pretty
%define go_import_path  github.com/niemeyer/pretty
%define commit_id       a10e7caefd8e0d600cea437f5c3613aeb1553d56

Name:           go-github-niemeyer-pretty
Version:        0+git20260817.a10e7ca
Release:        %autorelease
Summary:        Pretty-print Go values
License:        MIT
URL:            https://github.com/niemeyer/pretty
#!RemoteAsset:  sha256:ed0607dac88ec8f79ee6993f4ef08d43513f5f9505d728bf9300eb7f6df9b3eb
Source0:        https://github.com/niemeyer/pretty/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Make the intended rune conversion explicit for current Go vet.
Patch2000:      2000-format-flags-with-explicit-rune-conversion.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/kr/text)

%description
Pretty provides recursive formatting and human-readable differences for Go
values.

%files
%doc Readme
%license License
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
