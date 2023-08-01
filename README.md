[comment]: # "Auto-generated SOAR connector documentation"
# Link

Publisher: Mhike  
Connector Version: 1.1.2  
Product Vendor: Mhike  
Product Name: Link  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 4.9.0  

Generates a widget with clickable links

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


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Link asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**https_port** |  optional  | string | Splunk SOAR HTTPS port if your instance uses one other than 443
**auth_token** |  optional  | password | Splunk SOAR auth token if your instance requires auth for internal 127.0.0.1 calls
**debug** |  optional  | boolean | Print debugging statements to log

### Supported Actions  
[add link](#action-add-link) - Generate a widget with clickable links  
[test connectivity](#action-test-connectivity) - Test connectivity to local SOAR instance  

## action: 'add link'
Generate a widget with clickable links

Type: **generic**  
Read only: **False**

Adds the specified links with the descriptor as the link text. Links are added to the existing link widget if one exists, otherwise a new widget will be generated.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  optional  | URL to be added as link, requires the description field | string | 
**description** |  optional  | Description to be added as link text, requires the url field | string | 
**linkset** |  optional  | Add multiple links at once with a list of dictionaries containing a URL and a link descriptor | string | 
**append** |  required  | Append link instead of overwriting | boolean | 
**sort** |  optional  | Sort links alphabetically | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.append | string |  |  
action_result.parameter.description | string |  |  
action_result.parameter.linkset | string |  |  
action_result.parameter.sort | string |  |  
action_result.parameter.url | string |  |  
action_result.data.\*.linkset | string |  |  
action_result.summary | string |  |  
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'test connectivity'
Test connectivity to local SOAR instance

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |  