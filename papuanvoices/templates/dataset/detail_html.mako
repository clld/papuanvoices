<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <img src="${req.static_url('papuanvoices:static/ico-WestPapua.jpg')}" class="img-rounded">
    </div>
</%def>

<h2>Welcome to Papuan Voices</h2>
    <p class="lead">
        ${_('Papuan Voices presents phonetically-transcribed primary recordings of languages from West Papua.')}
    </p>

    <p>
        ${_('Cite the Papuan Voices dataset as')}
    </p>
    <blockquote>
        Yusuf Sawaki, Jeanete Lekeneny, Apriani Arilaha, Jimmi Kirihio, Emanuel Tutorop, Boas Wabia, Infak Mayor, Simon Tabuni, Stevani Karesina, Paul Heggarty, Darja Dërmaku-Appelganz. (2020). Papuan Voices (Version v1.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4350691
        <br>
        <a href="https://doi.org/10.5281/zenodo.4350691"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4350691.svg" alt="DOI"></a>
    </blockquote>
