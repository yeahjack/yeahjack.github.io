# Yijie Xu — https://yjx.me

Academic homepage for Yijie Xu, Ph.D. Candidate in Artificial Intelligence at HKUST (Guangzhou). Built with Jekyll and GitHub Pages.

## Local preview

Ruby 3.2.9 and rbenv are expected on macOS:

```bash
./scripts/jekyll-local.sh install
./scripts/jekyll-local.sh serve
```

The site is served at `http://localhost:4000/`.

## Update content

- Homepage news: [`_data/news.yml`](_data/news.yml)
- Selected publications on the homepage: [`_data/publications.yml`](_data/publications.yml)
- CV PDF: replace [`others/CV.pdf`](others/CV.pdf) by hand after compiling the LaTeX CV. The `/cv/` page previews that file; it is not generated from the homepage YAML.
- Profile photo: [`images/profile.jpg`](images/profile.jpg)
- Site-wide identity: [`_config.yml`](_config.yml)

## Build

```bash
./scripts/jekyll-local.sh build
```

JavaScript is a small vanilla file. After editing `assets/js/_main.js`:

```bash
npm run uglify
```
