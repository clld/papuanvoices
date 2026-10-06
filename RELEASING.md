# Releasing clld/papuanvoices

* install the app from source
  ```shell
  git clone https://github.com/clld/papuanvoices
  cd papuanvoices
  pip install -e .[test]
  ```

* data is located [here](https://github.com/lexibank/papuanvoices).  

* create the database (with data repo in `./papuanvoices-data/`)
  ```shell
  clld initdb --cldf ../papuanvoices-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog development.ini
  ```

* run tests
  ```shell
  pytest
  ```

