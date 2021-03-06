# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for appengine_config.py."""

from upvote.gae.lib.testing import basetest


class AppEngineConfigTest(basetest.UpvoteTestCase):

  def testImport(self):
    # pylint: disable=g-import-not-at-top,unused-import,unused-variable
    from upvote.gae import appengine_config


if __name__ == '__main__':
  basetest.main()
