# Jin-Woo Kong — academic homepage

Personal academic homepage using the official [al-folio](https://github.com/alshedivat/al-folio) template.

Live site: https://wlsdnqqq17.github.io/

## Editing

- `_pages/about.md`: biography, research interests, and profile settings.
- `_config.yml`: name, site metadata, and theme configuration.
- `_data/socials.yml`: email and GitHub links.
- `_news/`: dated announcements.
- `_bibliography/papers.bib`: add verified publications; enable `selected_papers` in the about page when ready.
- `_pages/publications.md`: remove the empty-list message when adding your first publication.
- `assets/img/profile.jpg`: profile photo.

Push to `main` to build and publish automatically using GitHub Actions.
The publication list is intentionally empty until actual papers are provided.

## Previous homepage

The pre-migration website and its full Git history are preserved on branch `backup/pre-al-folio-2026-10-02`.

## Template

Based on al-folio v1.x. Runtime layouts and styling come from the versioned al-folio gems declared in `Gemfile`.
See `docs/INSTALL.md` and `docs/CUSTOMIZE.md` for template documentation.
