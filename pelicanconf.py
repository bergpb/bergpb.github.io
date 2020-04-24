# Theme-specific settings
SITENAME = 'bergpb'
DOMAIN = 'lbarbosa.netlify.com'
BIO_TEXT = 'Desenvolvedor Web. Entusiasta pela cultura DevOps e tecnologia.'
FOOTER_TEXT = 'Powered by <a class="link" href="http://getpelican.com">Pelican</a>.'

DISQUS_SITENAME = "lbarbosa"

SITE_AUTHOR = 'Berg'
TWITTER_USERNAME = '@lbergpb'
INDEX_DESCRIPTION = None

SIDEBAR_LINKS = [
    '<a class="link" href="/archive/">Posts</a>',
    '<a class="link" href="/tags/">Tags</a>',
    '<a class="link" href="/about/">Sobre</a>',
]

SOCIAL_ICONS = [
    ('mailto:lindembergdepaulo@gmail.com', 'Email (lindembergdepaulo@gmail.com)', 'fa-envelope'),
    ('http://twitter.com/lbergpb', 'Twitter', 'fa-twitter'),
    ('http://github.com/bergpb', 'GitHub', 'fa-github'),
]

THEME_COLOR = '#FF8000'
ICONS_PATH = 'images/icons'

# Pelican settings
RELATIVE_URLS = True
SITEURL = 'https://bergpb.github.io'
TIMEZONE = 'America/Fortaleza'
DEFAULT_DATE = None
DEFAULT_DATE_FORMAT = '%d/%b/%Y'

THEME = 'theme'

ARTICLES_HOME = 5

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

ARCHIVES_URL = '{slug}'
ARCHIVES_SAVE_AS = 'archive/index.html'


FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

CACHE_CONTENT = False
OUTPUT_PATH = 'output'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = { page: page for page in templates }

STATIC_PATHS = ['images']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets', 'neighbors', 'render_math']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]
