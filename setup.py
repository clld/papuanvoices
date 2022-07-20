from setuptools import setup, find_packages


setup(
    name='papuanvoices',
    version='0.0',
    description='papuanvoices',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=9.2.1',
        'clld-audio-plugin',
        'clld-glottologfamily-plugin>=4.0',
        'pyglottolog>=3.6.0',
        'clldmpg>=4.2.0',

],
extras_require={
        'dev': ['flake8', 'waitress', 'psycopg2'],
        'test': [
            'mock',
            'pytest>=5.4',
            'pytest-clld',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="papuanvoices",
    entry_points="""\
    [paste.app_factory]
    main = papuanvoices:main
""")
