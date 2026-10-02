"""Check the built homepage and its local asset/navigation targets."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        for key in ("href", "src"):
            value = attributes.get(key)
            if value:
                self.targets.append(value)


root = Path("_site")
homepage = root / "index.html"
html = homepage.read_text()
assert "Jin-Woo" in html and "Kong" in html
assert "jwkong3" in html and "kaist.ac.kr" in html
assert "3D Reconstruction" in html and "Neural Rendering" in html
assert "Einstein" not in html and "Write your biography here" not in html

for page in (homepage, root / "publications/index.html"):
    parser = Links()
    parser.feed(page.read_text())
    for value in parser.targets:
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = unquote(parsed.path)
        target = root / path.lstrip("/") if path.startswith("/") else page.parent / path
        if target.is_dir():
            target /= "index.html"
        assert target.is_file(), f"Broken target on {page}: {value}"

print("Profile, homepage navigation, publication page, and local assets verified.")
