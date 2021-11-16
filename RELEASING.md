# Releasing clld/papuanvoices

* data is located [here](https://github.com/lexibank/papuanvoices).  

* create the database (with data repo in `./papuanvoices-data/`)
  ```
  clld initdb --cldf ./papuanvoices-data/ --glottolog <local-glottolog-repo> development.ini
  ```

* run tests
  ```
  pytest
  ```

* deploy
  ```
  (appconfig)$ fab deploy:production
  ```
