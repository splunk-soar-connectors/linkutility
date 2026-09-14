# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from link_widget_view import get_result


class _Result:
    def __init__(self, linkset):
        self._linkset = linkset

    def get_param(self):
        return {}

    def get_summary(self):
        return {}

    def get_data(self):
        return [{"linkset": self._linkset}]

    def get_message(self):
        return ""


class WidgetLinkPolicyTests(unittest.TestCase):
    def test_filters_unsafe_stored_links_before_rendering(self):
        links = [
            {"url": "https://safe.example/path", "descriptor": "safe"},
            {"url": "HTTP://safe.example/path", "descriptor": "case-safe"},
            {"url": "javascript:alert(1)", "descriptor": "script"},
            {"url": "data:text/html,unsafe", "descriptor": "data"},
            {"url": "//unsafe.example/path", "descriptor": "protocol-relative"},
            {"url": "/relative", "descriptor": "relative"},
            {"descriptor": "missing"},
            "not-a-link-record",
        ]

        rendered = get_result("add link", _Result(links))["data"]["linkset"]

        self.assertEqual(
            rendered,
            [
                {"url": "https://safe.example/path", "descriptor": "safe"},
                {"url": "HTTP://safe.example/path", "descriptor": "case-safe"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
