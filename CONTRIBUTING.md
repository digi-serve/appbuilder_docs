---
title: Contributing
category: home
layout: page
---

Any additions to AppBuilder documentation is welcome. Here are few guidelines to keep our documentation consistent:

1. Follow the [file structure](#file-structure)
1. [Use markdown](#markdown)
1. Follow the [page format](#page-format)

## File Structure

Try to follow the existing hierarchy when adding documentation. Add a page folder under the appropriate topic. Add a Page.md file, and an images folder if needed.

```
📁topic
  📁subtopic
    📁page
      📁images
      Page.md
```

## Markdown

### Learn Markdown

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Github's markdown Guide
- [Markdown Cheetsheet](https://www.markdownguide.org/cheat-sheet/) - Quick markdown reference

### Tools

- [Docs to Markdown](https://github.com/evbacher/gd2md-html/wiki) - Google drive extension to convert an existing document to Markdown
- [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) - Easy tool for creating/formatting a table into markdown

## Format

```markdown
---
title: My Page Title
category: Category
description: This description will show beside the title on the menu page.
---

## Heading

### Sub Heading

...

######
```

### Front matter

The YAML front matter is processed by Jekyll and used to display the page on the correct category pages.

**title** - Page title\
**category** - Which category page should link to this page.\
**description** - (Optional) Adds a description to the Category Page to provide additional context.\
**icon** - (Optional) a font awesome icon (starting with fa-). The icon will display in the breadcrumbs header.

### Content

Start with heading 2 (`##`) and add one level for each nested heading. Do not skip levels.

### Adding Categories

To add a category simply add a markdown file `myCategory.md` with the following yaml front matter:

```yaml
title: My category
description: An optional description of my category
is-category: myCategory
layout: page
category: parentCategory
icon: fa-icon (optional)
```

This will create an index page linked from the parent category which list any page that uses the category `myCategory`

## Tips

1. Jekyll uses Liquid templating. Using {% raw %}`{{`, `}}`, `{%`, or`%}` {% endraw %} in markdown will cause problems. Use
   `{% raw %}{%{% endraw %} raw {% raw %} %} ... {% {% endraw %} endraw {% raw %}%}{% endraw %}` tags to wrap these characters.
3. Font awesome icon can be added to any markdown file using this includes:
  ```liquid
  {% raw %}{% include icon.html i='fa-wrench' %}{% endraw %}
  ```
  {% include icon.html i='fa-wrench' %}
2. You can add notifications using this includes:
   ```liquid
   {% raw %}{% include notification.html message="This is the message for the notification" %}{% endraw %}
   ```
  {% include notification.html message="This is the message for the notification" %}

## Tips for Using This Documentation Site

- **Use the Sidebar:** Navigate topics and subtopics using the sidebar for quick access to all documentation sections.
- **Search:** Use the search bar to find specific topics, keywords, or guides instantly.
- **Breadcrumbs:** Follow the breadcrumbs at the top of each page to understand where you are and easily return to parent topics.
- **Internal Links:** Click on links within the docs to jump to related content and deepen your understanding.
- **Images & Examples:** Look for images and code snippets throughout the docs for visual guidance and practical examples.
- **Contribute:** If you spot errors or have suggestions, check out the contributing guidelines above to help improve the documentation for everyone.

---

## Run Site Locally
Jekyll requires ruby.
```