# Releasing clld/papuanvoices

install the app from source
```shell
git clone https://github.com/clld/papuanvoices
git clone --branch v1.3.1 --depth 1 https://github.com/lexibank/papuanvoices papuanvoices-cldf
git clone --branch v5.3 --depth 1 https://github.com/glottolog/glottolog
cd papuanvoices
pip install -e .[test]
```

```shell
pip install -e ../papuanvoices-cldf
clld initdb --cldf ../papuanvoices-cldf/cldf/cldf-metadata.json --glottolog ../glottolog development.ini
```

run tests
```shell
pytest
```

Store the tested requirements:
```shell
pip freeze > requirements.txt
```

Store a db dump:
```shell
pg_dump -xO --compress gzip:9 papuanvoices > papuanvoices.sql.gz
```

