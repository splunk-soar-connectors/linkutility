______________________________________________________________________

______________________________________________________________________

This app generates a widget with links. Each link will open in a new tab.

When adding links, they can either be appended to existing links with the append boolean or the new
links can overwrite the old links.

You can either add a single link and description at a time or you can use json to add multiple links
at once.

For a single link, you can add the url in the url field and the link text in the description
field.

For multiple links at once, you can pass in a list of dictionaries in this format:

```
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
```

Make sure the url begins with http(s). If you don't, your links won't open in a new window properly.

______________________________________________________________________

______________________________________________________________________
