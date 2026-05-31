# Copyright 2026 AlQuraishi Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys


def assert_sole_holder(t) -> None:
    """Assert that `t` is the only live reference to this tensor.

    In Python < 3.14 sys.getrefcount() creates a temporary reference for its
    own argument (so a sole holder gives refcount 2, not 1). Python 3.14
    removed this temporary reference. See:
    https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-refcount
    """
    assert sys.getrefcount(t) + int(sys.version_info >= (3, 14)) == 2
