# coding: utf-8

# This file is part of the Adblock Plus web scripts,
# Copyright (C) 2006-2013 Eyeo GmbH
#
# Adblock Plus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# Adblock Plus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Adblock Plus.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import re
import sitescripts.stats.common as common

class Test(unittest.TestCase):
  longMessage = True
  maxDiff = None

  def test_fileencoding(self):
    tests = [
      ("foo_bar", True),
      ("1234.txt", True),
      ("xYz.DAT", True),
      ("foo/bar.txt", False),
      ("foo/bar+bas-xyz.txt", False),
      (u"foo\u1234-bar\u4321", False),
    ]
    for name, expect_identical in tests:
      path = common.filename_encode(name)
      if expect_identical:
        self.assertEqual(path, name, "Encoding '%s' shouldn't change string" % name)
      else:
        self.assertTrue(re.match(r"^[\w\.\-]*$", path), "Encoding '%s' should replace all special characters" % name)
      self.assertEqual(common.filename_decode(path), name, "Encoding and decoding '%s' should produce the original string" % name)

if __name__ == '__main__':
  unittest.main()
