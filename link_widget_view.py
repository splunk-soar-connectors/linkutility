# File: link_widget_view.py
#
# Copyright (c) Mhike, 2022-2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
from urllib.parse import urlparse


def _is_safe_rendered_link(url):
    """Allow only absolute HTTP(S) links in the rendered widget."""
    parsed = urlparse(str(url).strip())
    return parsed.scheme.lower() in {"http", "https"} and bool(parsed.netloc)


def get_result(provides, result):
    """Function that parses data.
    :param result: result
    :param provides: action name
    :return: response data
    """

    example_result = {}

    param = result.get_param()
    summary = result.get_summary()
    data = result.get_data()
    message = result.get_message()

    example_result["param"] = param
    example_result["data"] = {}
    example_result["summary"] = {}
    example_result["message"] = message
    example_result["action"] = provides

    if summary:
        example_result["summary"] = summary

    if data:
        rendered_data = dict(data[0])
        linkset = rendered_data.get("linkset")
        if isinstance(linkset, list):
            rendered_data["linkset"] = [link for link in linkset if isinstance(link, dict) and _is_safe_rendered_link(link.get("url", ""))]
        example_result["data"] = rendered_data

    return example_result


def display_view(provides, all_app_runs, context):
    """Function that displays view.
    :param provides: action name
    :param context: context
    :param all_app_runs: all app runs
    :return: html page
    """

    context["results"] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:
            result = get_result(provides, result)
            if not result:
                continue
            results.append(result)

    return "link_widget_view.html"
