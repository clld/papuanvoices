# Releasing clld/papuanvoices

* data is located [here](https://github.com/lexibank/papuanvoices).  

* create the database (with data repo in `./papuanvoices-data/`)
  ```shell
  clld initdb --cldf ../papuanvoices-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog development.ini
  ```

* run tests
  ```shell
  pytest
  ```

* deploy
  ```
  (appconfig)$ fab deploy:production
  ```
