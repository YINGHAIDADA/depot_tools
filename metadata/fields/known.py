#!/usr/bin/env python3
# Copyright 2023 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys
from typing import Union

_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
_ROOT_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))

sys.path.insert(0, _ROOT_DIR)

import metadata.fields.custom.cpe_prefix
import metadata.fields.custom.date
import metadata.fields.types as field_types

# Freeform text fields.
NAME = field_types.FreeformTextField("Name")
SHORT_NAME = field_types.FreeformTextField("Short Name")
REVISION = field_types.FreeformTextField("Revision")
DESCRIPTION = field_types.FreeformTextField("Description", one_liner=False)
LOCAL_MODIFICATIONS = field_types.FreeformTextField("Local Modifications",
                                                    one_liner=False)

# Yes/no fields.
SECURITY_CRITICAL = field_types.YesNoField("Security Critical")
SHIPPED = field_types.YesNoField("Shipped")
LICENSE_ANDROID_COMPATIBLE = field_types.YesNoField(
    "License Android Compatible")

# Custom fields.
CPE_PREFIX = metadata.fields.custom.cpe_prefix.CPEPrefixField()
DATE = metadata.fields.custom.date.DateField()

ALL_FIELDS = (
    NAME,
    SHORT_NAME,
    DATE,
    REVISION,
    SECURITY_CRITICAL,
    SHIPPED,
    LICENSE_ANDROID_COMPATIBLE,
    CPE_PREFIX,
    DESCRIPTION,
    LOCAL_MODIFICATIONS,
)
ALL_FIELD_NAMES = {field.get_name() for field in ALL_FIELDS}
FIELD_MAPPING = {field.get_name().lower(): field for field in ALL_FIELDS}


def get_field(label: str) -> Union[field_types.MetadataField, None]:
  return FIELD_MAPPING.get(label.lower())
