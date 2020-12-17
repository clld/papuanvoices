<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>

<%block name="head">
    <link rel="stylesheet" href="${req.static_url('clld_audio_plugin:static/clld_audio_plugin.css')}">
</%block>

<h2>${_('Parameter')} ${ctx.name}</h2>

% if ctx.description:
<p>${ctx.description}</p>
% endif

<div style="clear: both"/>
% if map_ or request.map:
${(map_ or request.map).render()}
% endif

${request.get_datatable('values', h.models.Value, parameter=ctx).render()}
