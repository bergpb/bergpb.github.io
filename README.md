## Personal blog

Project build with: [Pelican](https://getpelican.com) (Static Site Generator)

Theme: [Pneumatic](https://github.com/iKevinY/pneumatic)

Instructions:

  1. Clone and enter in repo folder,
  1. Install packages: ```pip install -r requirements.txt```,
  1. Init server: ```pelican -lr```,
  1. Open your browser: [http://localhost:8000](http://localhost:8000)

Generating build:

  1. Run command: ```pelican content```
  1. Files are generated in ```output```

Using ```pygmentize``` to generate css:
  1. ```pygmentize -S monokai -f html -a .highlight > theme/static/css/pygment-monokai.css```