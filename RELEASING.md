# Releasing clld/papuanvoices

* install the app from source
  ```shell
  git clone https://github.com/clld/papuanvoices
  cd papuanvoices
  pip install -e .[test]
  ```

* [data](https://github.com/lexibank/papuanvoices) is expected to be cloned to `../papuanvoices-cldf`

* create the database
  ```shell
  clld initdb --cldf ../papuanvoices-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog development.ini
  ```

* run tests
  ```shell
  pytest
  ```

* Store the tested requirements:
  ```shell
  pip freeze > requirements.txt
  ```

* Store a db dump:
  ```shell
  pg_dump -xO papuanvoices > papuanvoices.sql
  zip papuanvoices.sql.zip papuanvoices.sql
  rm papuanvoices.sql
  ```

