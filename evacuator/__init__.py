# SPDX-FileCopyrightText: 2022-2025 MTS PJSC
# SPDX-License-Identifier: Apache-2.0
from evacuator.core import evacuator
from evacuator.exception import NeedEvacuation
from evacuator.version import __version__

__all__ = ["evacuator", "NeedEvacuation", "__version__"]
