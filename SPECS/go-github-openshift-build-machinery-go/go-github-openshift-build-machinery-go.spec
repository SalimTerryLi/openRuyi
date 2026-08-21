# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           build-machinery-go
%define go_import_path  github.com/openshift/build-machinery-go
%define commit_id       dc5b2804eeeeeaa078f66684085322a32acda241
# These example API types intentionally omit generated DeepCopyObject methods. - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}/make/examples/multiple-binaries/pkg/apis/*

Name:           go-github-openshift-build-machinery-go
Version:        0+git20260817.dc5b280
Release:        %autorelease
Summary:        OpenShift build machinery for Go
License:        Apache-2.0
URL:            https://github.com/openshift/build-machinery-go
#!RemoteAsset:  sha256:fe1d6f671fb2fea2d2eaa00420d9a805e1e9c48787f34910faa442ef6b60c6e2
Source0:        https://github.com/openshift/build-machinery-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/openshift/build-machinery-go) = %{version}

%description
Build machinery and helper tooling used by OpenShift projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
