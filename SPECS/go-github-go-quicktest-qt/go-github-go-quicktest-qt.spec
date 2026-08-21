# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           qt
%define go_import_path  github.com/go-quicktest/qt

Name:           go-github-go-quicktest-qt
Version:        1.102.0
Release:        %autorelease
Summary:        Testing assertions and helpers for Go
License:        MIT
URL:            https://github.com/go-quicktest/qt
#!RemoteAsset:  sha256:9e99100ed5d8b05088842e111e4cd0429cbe7a9c1fe0a6efeb53e43a76c5b51e
Source0:        https://github.com/go-quicktest/qt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Adjust test diagnostics for the encoding/json v2 implementation in Go 1.27.
Patch2000:      2000-tests-support-encoding-json-v2-diagnostics.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/rogpeppe/go-internal)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/kr/pretty)

%description
The qt package provides assertions and helpers for writing Go tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
