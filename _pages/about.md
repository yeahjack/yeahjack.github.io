---
layout: default
permalink: /
excerpt: "Yijie Xu — Ph.D. Candidate in Artificial Intelligence"
redirect_from:
  - /about/
  - /about.html
---

<div id="academic-home">
  <div class="academic-shell">
    {% include academic-profile.html %}

    <main class="academic-main">
      <section class="academic-intro" aria-label="About me">
        <p>
          I am a Ph.D. Candidate in Artificial Intelligence at
          <a href="https://hkust-gz.edu.cn/" rel="noopener noreferrer">The Hong Kong University of Science and Technology (Guangzhou)</a>,
          advised by <a href="https://scholar.google.com/citations?user=cVDF1tkAAAAJ" rel="noopener noreferrer">Prof. Hui Xiong</a>.
          I also work closely with <a href="https://xuminghu.github.io/" rel="noopener noreferrer">Prof. Xuming Hu</a>,
          <a href="https://exlaw.github.io/" rel="noopener noreferrer">Dr. Aiwei Liu</a> at WeChat AI, and
          <a href="https://weiyuguo.com/" rel="noopener noreferrer">Dr. Weiyu Guo</a> at MMLab, CUHK.
          I am currently a Research Intern at Tencent, working on generative retrieval.
        </p>
        <p class="academic-interests">
          <strong>Research interests.</strong> My research studies how language models acquire and leverage information to adapt and make decisions, with a focus on <strong>test-time self-evolution</strong>, <strong>generative retrieval</strong>, and <strong>retrieval-augmented generation</strong>.
        </p>
        <p class="academic-availability">
          I am open to industry research opportunities in LLM post-training and related areas.
        </p>
      </section>

      <section class="academic-section" aria-labelledby="news-title">
        <div class="academic-section__heading">
          <h2 id="news-title">News</h2>
        </div>
        {% include academic-news.html %}
      </section>

      <section class="academic-section" aria-labelledby="publications-title">
        <div class="academic-section__heading">
          <h2 id="publications-title">Selected Publications</h2>
          <a href="https://scholar.google.com/citations?user=hBZs76kAAAAJ" rel="noopener noreferrer">Full list on Google Scholar</a>
        </div>
        <p class="academic-pub__legend"><sup>†</sup>: Co-first Authors; <sup>‡</sup>: Co-second Authors; <sup>∗</sup>: Corresponding Authors.</p>
        {% include academic-publications.html %}
      </section>

      <p class="academic-contact">For research discussions or industry opportunities, the fastest way to reach me is <a href="mailto:{{ site.author.email }}">email</a>.</p>
    </main>
  </div>
</div>
