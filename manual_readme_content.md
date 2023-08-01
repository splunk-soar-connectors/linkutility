[comment]: # " File: README.md"
[comment]: # "  Copyright (c) Mhike, 2022"
[comment]: # "  Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # "  You may obtain a copy of the License at"
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for the specific language governing permissions"
[comment]: # "  and limitations under the License."
[comment]: # ""
----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------

This app generates a widget with links. Each link will open in a new tab.  
  
When adding links, they can either be appended to existing links with the append boolean or the new
links can overwrite the old links.  
  
You can either add a single link and description at a time or you can use json to add multiple links
at once.  
  
For a single link, you can add the url in the url field and the link text in the description
field.  
  
For multiple links at once, you can pass in a list of dictionaries in this format:

    [
        {
            "descriptor":"Google Search",
            "url":"https://www.google.com"
        },
        {
            "descriptor":"Splunk Documentation",
            "url":"https://docs.splunk.com/Documentation"
        },
        {
            "descriptor":"VirusTotal",
            "url":"https://www.virustotal.com"
        }
    ]

Make sure the url begins with http(s). If you don't, your links won't open in a new window properly.

----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
