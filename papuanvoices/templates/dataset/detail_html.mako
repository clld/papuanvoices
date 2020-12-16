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

