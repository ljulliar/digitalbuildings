# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for generate_universe.py"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

sys.path.append('..')

from instance_validator import generate_universe
from absl.testing import absltest

class GenerateUniverseTest(absltest.TestCase):

    def setUp(self):
        print('setting up')

if __name__ == '__main__':
  absltest.main()
