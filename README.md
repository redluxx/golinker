Go-links
----------

Very simple internal short-linking system.

Usage
----------
Python3 is default python.
* Python2 EOL 01/01/2020 <- Stop using it!

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m golinks.webapp
```


Examples
----------

If you visit http://go/git you would be redirect to https://gitlab.com

However if you visit `http:/go/git go-links`, you would be redirected to search, for "go-links" 


TODO
-----

* Basic authentication
* Ownership of links with restricted editing


Original Author
-----
[https://github.com/daniellawrence/go-links-python](https://github.com/daniellawrence/go-links-python/tree/943b96688f6707d37e76c3d1ea007a639e317e3f) 