---
layout: default
permalink: /
title: "Yijie Xu"
excerpt: "Yijie Xu — Ph.D. Candidate in Artificial Intelligence"
redirect_from:
  - /about/
  - /about.html
---

<style>
  #academic-home {
    --academic-ink: #252a2e;
    --academic-muted: #626b70;
    --academic-link: #245f7a;
    --academic-accent: #8c632d;
    --academic-rule: #d7dde0;
    --academic-soft: #f4f6f6;
    --academic-paper: #ffffff;
    max-width: 1240px;
    margin: 0 auto;
    padding: 2.2rem 1.25rem 4rem;
    color: var(--academic-ink);
    font-family: Charter, "Bitstream Charter", Georgia, serif;
    font-kerning: normal;
    text-rendering: optimizeLegibility;
  }

  html[data-theme="dark"] #academic-home {
    --academic-ink: #e8ebed;
    --academic-muted: #aeb6bc;
    --academic-link: #7db5d2;
    --academic-accent: #d0a66a;
    --academic-rule: #4a5157;
    --academic-soft: #2c3135;
    --academic-paper: #25292c;
  }

  #academic-home * {
    box-sizing: border-box;
  }

  #academic-home [hidden] {
    display: none !important;
  }

  #academic-home a {
    color: var(--academic-link);
    text-underline-offset: 0.16em;
  }

  #academic-home a:focus-visible {
    outline: 2px solid var(--academic-link);
    outline-offset: 4px;
  }

  #academic-home ::selection {
    background: rgba(36, 95, 122, 0.16);
  }

  .academic-shell {
    display: grid;
    grid-template-columns: 200px minmax(0, 1fr);
    gap: clamp(2.25rem, 4vw, 3.75rem);
    align-items: start;
  }

  .academic-profile {
    position: sticky;
    top: 5.5rem;
  }

  .academic-profile__photo {
    display: block;
    width: 164px;
    height: 194px;
    margin-bottom: 0.8rem;
    overflow: hidden;
    border: 1px solid var(--academic-rule);
    border-radius: 4px;
    background: var(--academic-soft);
    box-shadow: 0 7px 22px rgba(35, 44, 50, 0.08);
  }

  .academic-profile__photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
  }

  .academic-profile h1 {
    margin: 0 0 0.25rem;
    color: var(--academic-ink);
    font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
    font-size: 1.45rem;
    font-weight: 600;
    letter-spacing: -0.012em;
    line-height: 1.15;
  }

  .academic-profile__role,
  .academic-profile__affiliation {
    margin: 0;
    color: var(--academic-muted);
    font-size: 0.87rem;
    line-height: 1.45;
  }

  .academic-profile__affiliation {
    margin-top: 0.35rem;
  }

  .academic-profile__links {
    display: grid;
    gap: 0.38rem;
    margin-top: 1rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--academic-rule);
    font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
    font-size: 0.77rem;
  }

  .academic-profile__links a {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    width: fit-content;
    color: var(--academic-ink);
    text-decoration: none;
  }

  .academic-profile__links a::before {
    width: 0.72rem;
    height: 1px;
    background: var(--academic-rule);
    content: "";
    transition: width 160ms ease, background-color 160ms ease;
  }

  .academic-profile__links a:hover {
    color: var(--academic-link);
    text-decoration: underline;
  }

  .academic-profile__links a:hover::before {
    width: 0.92rem;
    background: var(--academic-link);
  }

  .academic-intro {
    font-size: 0.96rem;
    line-height: 1.58;
  }

  .academic-intro p {
    margin: 0 0 0.65rem;
  }

  .academic-intro strong {
    color: var(--academic-ink);
  }

  .academic-interests {
    color: var(--academic-muted);
  }

  .academic-availability {
    margin: 1rem 0 0;
    padding: 0.32rem 0 0.32rem 0.9rem;
    border-left: 2px solid var(--academic-accent);
    color: var(--academic-ink);
    font-style: italic;
  }

  .academic-section {
    margin-top: 1.8rem;
  }

  .academic-section__heading {
    position: relative;
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 1rem;
    margin: 0 0 0.25rem;
    padding-bottom: 0.42rem;
    border-bottom: 1px solid var(--academic-rule);
  }

  .academic-section__heading::after {
    position: absolute;
    bottom: -1px;
    left: 0;
    width: 2.65rem;
    height: 1px;
    background: var(--academic-accent);
    content: "";
  }

  .academic-section__heading h2 {
    margin: 0;
    color: var(--academic-ink);
    font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
    font-size: 1.48rem;
    font-weight: 600;
    letter-spacing: -0.018em;
    line-height: 1.2;
  }

  .academic-section__heading a {
    border-bottom: 1px solid rgba(36, 95, 122, 0.35);
    font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
    font-size: 0.78rem;
    text-decoration: none;
    transition: border-color 160ms ease;
  }

  .academic-section__heading a:hover {
    border-color: currentColor;
  }

  .academic-news {
    display: grid;
    grid-template-columns: 1fr;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .academic-news li {
    display: grid;
    grid-template-columns: 5.4rem minmax(0, 1fr);
    gap: 0.55rem;
    padding: 0.42rem 0;
    border-bottom: 1px solid var(--academic-rule);
    font-size: 0.89rem;
    line-height: 1.42;
  }

  .academic-news li:last-child {
    border-bottom: 0;
  }

  .academic-news time {
    color: var(--academic-muted);
    font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
    font-size: 0.72rem;
    font-style: normal;
    font-variant-numeric: tabular-nums;
    font-weight: 600;
    letter-spacing: 0.025em;
    padding-top: 0.08rem;
    white-space: nowrap;
  }

  .academic-pub {
    display: grid;
    grid-template-columns: minmax(180px, 205px) minmax(0, 1fr);
    gap: clamp(1rem, 2vw, 1.35rem);
    padding: 0.92rem 0;
    border-bottom: 1px solid var(--academic-rule);
  }

  .academic-pub:last-child {
    border-bottom: 0;
  }

  .academic-pub__legend {
    margin: 0.42rem 0 0.12rem;
    color: var(--academic-muted);
    font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
    font-size: 0.7rem;
    line-height: 1.45;
  }

  .academic-pub__figure {
    position: relative;
    align-self: start;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border: 1px solid var(--academic-rule);
    border-radius: 3px;
    background: #ffffff;
    box-shadow: 0 2px 8px rgba(35, 44, 50, 0.07);
    transform-origin: left center;
    transition:
      transform 240ms cubic-bezier(0.2, 0.8, 0.2, 1),
      border-color 240ms ease,
      box-shadow 240ms ease;
    will-change: transform;
  }

  .academic-pub__figure img {
    display: block;
    width: 100%;
    height: 100%;
    padding: 0.24rem;
    object-fit: contain;
    transition: opacity 180ms ease;
  }

  @media (hover: hover) and (pointer: fine) {
    .academic-pub__figure:hover,
    .academic-pub__figure:focus-visible {
      z-index: 10;
      border-color: rgba(32, 95, 131, 0.42);
      box-shadow: 0 16px 38px rgba(35, 44, 50, 0.2);
      transform: translateY(-2px) scale(1.65);
    }
  }

  .academic-pub__content {
    align-self: center;
  }

  .academic-pub__title {
    margin: 0 0 0.3rem;
    font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
    font-size: 1.01rem;
    font-weight: 600;
    letter-spacing: -0.006em;
    line-height: 1.35;
  }

  .academic-pub__title a {
    color: var(--academic-link);
    text-decoration-thickness: 1px;
    text-decoration-color: transparent;
    transition: text-decoration-color 160ms ease;
  }

  .academic-pub:hover .academic-pub__title a {
    text-decoration-color: currentColor;
  }

  .academic-pub__authors,
  .academic-pub__venue {
    margin: 0 0 0.26rem;
    color: var(--academic-muted);
    font-size: 0.82rem;
    line-height: 1.38;
  }

  .academic-pub__authors strong {
    color: var(--academic-ink);
    font-weight: 700;
  }

  .academic-pub__authors sup,
  .academic-pub__legend sup {
    color: var(--academic-ink);
    font-size: 0.72em;
    font-weight: 700;
    line-height: 0;
  }

  .academic-pub__venue {
    color: var(--academic-ink);
    font-style: italic;
  }

  .academic-pub__venue strong {
    color: var(--academic-accent);
    font-style: normal;
  }

  .academic-pub__meta {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.25rem 0.75rem;
  }

  .academic-pub__meta .academic-pub__venue {
    margin: 0;
  }

  .academic-pub__links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin: 0;
    font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.018em;
  }

  .academic-pub__links a {
    text-decoration: none;
  }

  .academic-pub__links a:hover {
    text-decoration: underline;
  }

  .academic-contact {
    margin-top: 1.8rem;
    padding-top: 1rem;
    border-top: 1px solid var(--academic-rule);
    color: var(--academic-muted);
    font-size: 0.94rem;
  }

  @media (max-width: 760px) {
    #academic-home {
      padding: 1.35rem 1rem 3.5rem;
    }

    .academic-shell {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .academic-profile {
      position: static;
      display: grid;
      grid-template-columns: 96px minmax(0, 1fr);
      column-gap: 1rem;
      align-items: center;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--academic-rule);
    }

    .academic-profile__photo {
      grid-row: 1 / span 3;
      width: 96px;
      height: 112px;
      margin: 0;
    }

    .academic-profile__links {
      grid-column: 1 / -1;
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem 1rem;
      margin-top: 1rem;
    }

    .academic-news {
      grid-template-columns: 1fr;
    }

    .academic-pub {
      grid-template-columns: 116px minmax(0, 1fr);
      gap: 0.8rem;
    }

    .academic-pub__figure {
      aspect-ratio: 4 / 3;
      max-width: 116px;
    }

  }

  @media (prefers-reduced-motion: reduce) {
    .academic-pub__figure {
      transition: none;
    }
  }

  @media (max-width: 480px) {
    .academic-section__heading {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.3rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .academic-pub__figure img,
    .academic-pub__title a {
      transition: none;
    }
  }
</style>

<div id="academic-home">
  <div class="academic-shell">
    <aside class="academic-profile" aria-label="Profile">
      <div class="academic-profile__photo">
        <img src="/images/profile.png" alt="Portrait of Yijie Xu">
      </div>
      <div>
        <h1>Yijie Xu</h1>
        <p class="academic-profile__role">Ph.D. Candidate in Artificial Intelligence</p>
        <p class="academic-profile__affiliation">HKUST (Guangzhou)</p>
      </div>
      <nav class="academic-profile__links" aria-label="Profile links">
        <a href="mailto:yxu409@connect.hkust-gz.edu.cn">Email</a>
        <a href="https://scholar.google.com/citations?user=hBZs76kAAAAJ">Google Scholar</a>
        <a href="https://github.com/yeahjack">GitHub</a>
        <a href="/cv/">Curriculum Vitae</a>
      </nav>
    </aside>

    <main class="academic-main">
      <section class="academic-intro" aria-label="About me">
        <p>
          I am a Ph.D. Candidate in Artificial Intelligence at
          <a href="https://hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a>,
          advised by <a href="https://scholar.google.com/citations?user=cVDF1tkAAAAJ">Prof. Hui Xiong</a>.
          I also work closely with <a href="https://xuminghu.github.io/">Prof. Xuming Hu</a>,
          <a href="https://exlaw.github.io/">Dr. Aiwei Liu</a> at WeChat AI, and
          <a href="https://weiyuguo.com/">Dr. Weiyu Guo</a> at MMLab, CUHK.
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
        <ul class="academic-news">
          <li><time datetime="2026-07">Jul. 2026</time><span>Our paper on political ideology detection and prediction was accepted by ACM TIST.</span></li>
          <li><time datetime="2026-05">May 2026</time><span>Started working as a Research Intern at Tencent.</span></li>
          <li><time datetime="2026-05">May 2026</time><span><a href="https://dl.acm.org/doi/10.1145/3770855.3817581">SafeBuild-Bench</a> was accepted by the KDD 2026 Datasets &amp; Benchmarks Track.</span></li>
          <li><time datetime="2026-02">Feb. 2026</time><span>One paper on VLM unlearning was accepted by CVPR 2026.</span></li>
          <li><time datetime="2025-11">Nov. 2025</time><span>One paper on source-free domain adaptation was accepted by AAAI 2026.</span></li>
          <li><time datetime="2025-09">Sep. 2025</time><span>Two papers were accepted by NeurIPS 2025.</span></li>
        </ul>
      </section>

      <section class="academic-section" aria-labelledby="publications-title">
        <div class="academic-section__heading">
          <h2 id="publications-title">Selected Publications</h2>
          <a href="https://scholar.google.com/citations?user=hBZs76kAAAAJ">Full list on Google Scholar</a>
        </div>
        <p class="academic-pub__legend"><sup>†</sup>: Co-first Authors; <sup>‡</sup>: Co-second Authors; <sup>∗</sup>: Corresponding Authors.</p>

        <article class="academic-pub">
          <a class="academic-pub__figure" href="https://arxiv.org/abs/2603.15381" aria-label="View You only need 4 extra tokens">
            <img src="/images/home/sytta-method.webp" alt="SyTTA method overview combining input distribution adaptation, output confidence shaping, and dynamic weighting">
          </a>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title"><a href="https://arxiv.org/abs/2603.15381">You only need 4 extra tokens: Synergistic Test-time Adaptation for LLMs</a></h3>
            <p class="academic-pub__authors"><strong>Yijie Xu</strong>, Huizai Yao, Zhiyu Guo, Weiyu Guo, Pengteng Li, Aiwei Liu, Xuming Hu<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>Preprint</strong>, 2026</p>
              <div class="academic-pub__links"><a href="https://arxiv.org/abs/2603.15381">Paper</a></div>
            </div>
          </div>
        </article>

        <article class="academic-pub" hidden>
          <div class="academic-pub__figure" role="img" aria-label="Motivation figure comparing traditional post-training with decoupled ProximalTTA">
            <img src="/images/home/rethinking-introduction.webp" alt="Comparison of traditional post-training and decoupled ProximalTTA">
          </div>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title">Rethinking Test-Time Adaptation for LLMs as Decoupled Unsupervised Post-Training</h3>
            <p class="academic-pub__authors"><strong>Yijie Xu</strong>, Yili Wang, Qianyi Cai, Huizai Yao, Hanqing Wang, Tianfu Wang, Aiwei Liu, Weiyu Guo, Xuming Hu<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
          </div>
        </article>

        <article class="academic-pub">
          <div class="academic-pub__figure" role="img" aria-label="Taxonomy of unsupervised post-training methods">
            <img src="/images/home/upt-survey-taxonomy.webp" alt="Taxonomy tree for unsupervised post-training without external ground truth">
          </div>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title">Unsupervised Post-Training of Foundation Models: A Survey</h3>
            <p class="academic-pub__authors"><strong>Yijie Xu</strong>, Qianyi Cai, Huizai Yao, Yili Wang, Tianfu Wang, Cehao Yang, Xingbo Yao, Zhiyu Guo, Aiwei Liu, Xuming Hu<sup>∗</sup>, Weiyu Guo<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>In submission</strong> to EMNLP 2026</p>
            </div>
          </div>
        </article>

        <article class="academic-pub">
          <div class="academic-pub__figure" role="img" aria-label="Political ideology paper overview">
            <img src="/images/home/tist-introduction.webp" alt="Political ideology dynamics across social media posts, temporal networks, and media-bias ratings">
          </div>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title">Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media</h3>
            <p class="academic-pub__authors"><strong>Yijie Xu</strong>, Chao Wang<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>ACM TIST</strong>, 2026</p>
            </div>
          </div>
        </article>

        <article class="academic-pub">
          <a class="academic-pub__figure" href="https://openreview.net/forum?id=ixMBnOhFGd" aria-label="View SePer">
            <img src="https://arxiv.org/html/2503.01478/extracted/6296347/figures/illustration.png" alt="Overview of semantic perplexity reduction for retrieval evaluation">
          </a>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title"><a href="https://openreview.net/forum?id=ixMBnOhFGd">SePer: Measure Retrieval Utility Through the Lens of Semantic Perplexity Reduction</a></h3>
            <p class="academic-pub__authors">Lu Dai, <strong>Yijie Xu</strong>, Jinhui Ye, Hao Liu<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>ICLR 2025 Spotlight</strong> (3.20%)</p>
              <div class="academic-pub__links"><a href="https://openreview.net/forum?id=ixMBnOhFGd">Paper</a><a href="https://arxiv.org/abs/2503.01478">arXiv</a></div>
            </div>
          </div>
        </article>

        <article class="academic-pub">
          <a class="academic-pub__figure" href="https://dl.acm.org/doi/10.1145/3770855.3817581" aria-label="View SafeBuild-Bench">
            <img src="https://arxiv.org/html/2608.00068v1/GEMS/kdd-intro.png" alt="Overview of the SafeBuild-Bench construction safety benchmark">
          </a>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title"><a href="https://dl.acm.org/doi/10.1145/3770855.3817581">SafeBuild-Bench: A Temporal-Robust Construction Safety Benchmark with Graph-Enhanced Data Mining</a></h3>
            <p class="academic-pub__authors">Yi Cui<sup>†</sup>, Zilin Wang<sup>†</sup>, <strong>Yijie Xu</strong>, Qianyi Cai, Huizai Yao, Shuai Jiang, Bingzhuo Zhong<sup>∗</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>KDD 2026 Datasets &amp; Benchmarks Track</strong></p>
              <div class="academic-pub__links"><a href="https://dl.acm.org/doi/10.1145/3770855.3817581">Paper</a><a href="https://arxiv.org/abs/2608.00068">arXiv</a></div>
            </div>
          </div>
        </article>

        <article class="academic-pub">
          <a class="academic-pub__figure" href="https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_VL-Eraser_Vacuum_Distillation_for_Machine_Unlearning_in_Vision-Language_Models_CVPR_2026_paper.pdf" aria-label="View VL-Eraser">
            <img src="/images/home/vl-eraser-method.webp" alt="VL-Eraser framework with vacuum distillation and arithmetic deletion stages">
          </a>
          <div class="academic-pub__content">
            <h3 class="academic-pub__title"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_VL-Eraser_Vacuum_Distillation_for_Machine_Unlearning_in_Vision-Language_Models_CVPR_2026_paper.pdf">VL-Eraser: Vacuum Distillation for Machine Unlearning in Vision-Language Models</a></h3>
            <p class="academic-pub__authors">Yili Wang, Lu Dai<sup>‡</sup>, Tairan Huang<sup>‡</sup>, <strong>Yijie Xu</strong><sup>‡</sup>, Hui Xiong<sup>∗</sup></p>
            <div class="academic-pub__meta">
              <p class="academic-pub__venue"><strong>CVPR 2026</strong></p>
              <div class="academic-pub__links"><a href="https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_VL-Eraser_Vacuum_Distillation_for_Machine_Unlearning_in_Vision-Language_Models_CVPR_2026_paper.pdf">Paper</a></div>
            </div>
          </div>
        </article>
      </section>

      <p class="academic-contact">For research discussions or industry opportunities, the fastest way to reach me is <a href="mailto:yxu409@connect.hkust-gz.edu.cn">email</a>.</p>
    </main>
  </div>
</div>
