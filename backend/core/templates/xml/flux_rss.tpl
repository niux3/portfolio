<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
    <channel>
        <title>{{ title }}</title>
        <link>{{ url_site }}</link>
        <description>{{ description }}</description>
        <language>fr</language>
        <lastBuildDate>{{ today }}</lastBuildDate>
        {% for object in object_list %}
        <item>
            <title>{{ object.title }}</title>
            <link>{{ object.url_article }}</link>
            <description><![CDATA[{{ object.meta_description }}]]></description>
            <pubDate>{{ object.created }}</pubDate>
            <guid>{{ object.url_article }}</guid>
        </item>
        {% endfor %}
    </channel>
</rss>
