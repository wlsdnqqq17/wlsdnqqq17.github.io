# Jin-Woo Kong — academic homepage

Personal academic homepage using the official [al-folio](https://github.com/alshedivat/al-folio) template.

Live site: https://wlsdnqqq17.github.io/

## Editing

- `_pages/about.md`: biography, research interests, and profile settings.
- `_config.yml`: name, site metadata, and theme configuration.
- `_data/socials.yml`: email and GitHub links.
- `_news/`: dated announcements.
- `_bibliography/papers.bib`: publication metadata, figure filenames, and optional `website` / `arxiv` fields.
- `_layouts/academic_bib.liquid`: publication figures and citation display.
- `assets/img/profile.jpg`: profile photo.
- `_layouts/academic.liquid` and `assets/css/academic.css`: site-owned sidebar layout, inspired by https://shin-dong-yeon.github.io/.

The custom academic layout does not shadow a gem-owned layout. The al-folio theme, plugins, bibliography support, and automatic deployment remain in place. The upstream starter-boundary check applies only to the upstream repository; user-site layouts are supported by al-folio.

Push to `main` to build and publish automatically using GitHub Actions.
The publication list includes the SIGGRAPH Asia Posters 2026 paper supplied by the author and listed on the AMI Lab website. Project and arXiv links appear only when actual URLs are provided.

## Previous homepage

The pre-migration website and its full Git history are preserved on branch `backup/pre-al-folio-2026-10-02`.

## Template

Based on al-folio v1.x. Runtime layouts and styling come from the versioned al-folio gems declared in `Gemfile`.
See `docs/INSTALL.md` and `docs/CUSTOMIZE.md` for template documentation.
