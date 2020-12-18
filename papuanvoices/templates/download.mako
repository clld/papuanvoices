<%inherit file="home_comp.mako"/>
<%namespace name="mpg" file="clldmpg_util.mako"/>

<h3>${_('Downloads')}</h3>

<div class="alert alert-info">
    <p>
        ${_('Papuan Voices serves the latest')}
        ${h.external_link('https://github.com/lexibank/papuanvoices/releases', label=_('released version'))}
        ${_('of data curated at')}
        ${h.external_link('https://github.com/lexibank/papuanvoices', label='lexibank/papuanvoices')}.
        ${_('All released version are accessible via')} <br/>
        <a href="https://doi.org/10.5281/zenodo.4350690">
            <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4350690.svg" alt="DOI">
        </a>
        <br/>
        ${_('on ZENODO as well')}.
    </p>
        <p>
        Corresponding versions of the audio files are available at<br/>
        <a href="https://doi.org/10.5281/zenodo.4350923">
            <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4350923.svg" alt="DOI">
        </a>
        <br/>
        ${_('on ZENODO as well')}.
    </p>
</div>
