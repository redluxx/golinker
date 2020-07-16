### 16/07/2020 - v0.1.0
* Removed screenshots folder
* Edited licence with additional copyright holder for new changes
* Debug -> False by default
* Requirments.txt -> removal of oauth2
* Basic handle of duplicate entries
* db folder added for persistant databases
* changes to README
* Removal requirements-dev.txt
* Model changes:
    * Primary key is now a Integer
    * favicon stored in DB
        * Automatic grabbing moved to detect the None's
        * Combined the url adjustments together
    * visits counter added to track links served
        * Future: Display stats page about links.
    * URL regex used to accuratly check urls
* Webapp changes:
    * Index orders links by name ascending.
    * Redirect now increments the visit counter
    * Submit now includes added model data fields
        * No longer duplicate record when changing name <- track edits by gid not name
        * check if URL is correct return if not
        * check if Favicon is not None and is correct. If either then revert to basic attempt

* index.html changes:
    * Title now applies title to page.
    * css for manual favicon entry
    * favicon manual entry when adding / editing links
    * Found Links -> All Links


### 14/07/2020 - v0.0.1
* Forked from [https://github.com/daniellawrence/go-links-python](https://github.com/daniellawrence/go-links-python/commit/943b96688f6707d37e76c3d1ea007a639e317e3f) 
* Versioned as V0.0.1 as per original setup.