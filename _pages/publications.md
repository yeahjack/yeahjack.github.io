---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my full and latest papers on <u><a href="https://scholar.google.com/citations?user=hBZs76kAAAAJ">my Google Scholar profile</a></u>.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
