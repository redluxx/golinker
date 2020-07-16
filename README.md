Go-links
----------

Very simple internal short-linking system.


Examples
----------

```python
DEMO_RECORDS = [
    ('mail', 'https://mail.google.com'),
    ('git', 'https://gitlab.com{/search?terms=^}'),
    ('github', 'https://github.com{/search?terms=^}'),
    ('in', 'https://linkedin.com'),
    ('fb', 'https://www.facebook.com')
]
```

If you visit http://go/git you would be redirect to https://gitlab.com

However if you visit `http:/go/git go-links`, you would be redirected to search, for "go-links" 


TODO
-----

* Basic authentication
* Ownership of links with restricted editing


Original Author
-----
[https://github.com/daniellawrence/go-links-python](https://github.com/daniellawrence/go-links-python/commit/943b96688f6707d37e76c3d1ea007a639e317e3f) 