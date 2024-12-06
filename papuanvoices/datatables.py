from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.contributor import Contributors
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol
from clld.web.util import concepticon
from clld.db.models import common
from clld.db.util import get_distinct_values
from clld_audio_plugin.datatables import AudioCol
from clld.web.util.glottolog import url
from clld.web.util.htmllib import HTML
from clld.web.util.helpers import map_marker_img

from papuanvoices import models


class FamCol(Col):
    def format(self, item):
        try:
            return HTML.div(map_marker_img(self.dt.req, item), ' ', HTML.span(item.family))
        except Exception:
            return HTML.div(map_marker_img(
                self.dt.req,
                item.valueset.language),
                ' ',
                HTML.span(item.valueset.language.family))


class PVGlottologCol(Col):
    def format(self, item):
        if item.glottocode:
            return HTML.a(item.glottocode, href=url(item.glottocode))
        return ''


class Languages(datatables.Languages):
    # def base_query(self, query):
    #     return query.join(Family).options(joinedload(models.Variety.family)).distinct()
    def col_defs(self):
        return [
            LinkCol(self, 'name'),
            PVGlottologCol(self, 'Glottocode', model_col=models.Variety.glottocode),
            Col(self, 'description'),
            FamCol(
                self,
                'family',
                sTitle=self.req._('Family'),
                model_col=models.Variety.family,
                choices=get_distinct_values(models.Variety.family)),
            Col(self,
                'latitude',
                sDescription='<small>The geographic latitude</small>'),
            Col(self,
                'longitude',
                sDescription='<small>The geographic longitude</small>'),
            LinkToMapCol(self, 'm'),
        ]


class ConcepticonCol(Col):
    def format(self, item):
        return concepticon.link(self.dt.req, item.concepticon_id, label=item.concepticon_gloss)


class Concepts(datatables.Parameters):
    def col_defs(self):
        return [
            LinkCol(self, 'name', sTitle=self.req._('English')),
            Col(self, 'description', sTitle='Papuan Malay'),
            Col(self, 'count_lexemes',
                sTitle=self.req._('# words'),
                sTooltip=self.req._('number of words per concept'),
                model_col=models.Concept.count_lexemes),
            ConcepticonCol(self, 'concepticon'),
        ]


class CommentCol(Col):
    __kw__ = dict(bSearchable=False, bSortable=False)

    def format(self, item):
        return item.jsondata['comment']


class WordLinkCol(LinkCol):
    def format(self, item):
        if item.name and item.name != '►':
            return super(WordLinkCol, self).format(item)


class Words(datatables.Values):
    def base_query(self, query):
        if not any([self.language, self.parameter, self.contribution]):
            return query\
                .join(common.ValueSet)\
                .join(common.Parameter)\
                .join(common.Language)\
                .options(
                    joinedload(common.Value.valueset).joinedload(common.ValueSet.parameter),
                    joinedload(common.Value.valueset).joinedload(common.ValueSet.language)
                )
        else:
            return datatables.Values.base_query(self, query)

    def get_default_options(self):
        opts = super(datatables.Values, self).get_default_options()
        if not self.language and not self.parameter:
            opts['aaSorting'] = [[0, 'asc'], [3, 'asc'], [2, 'asc']]
        elif self.parameter:
            opts['aaSorting'] = [[1, 'asc'], [0, 'asc'], [3, 'asc']]
        else:
            opts['aaSorting'] = [[0, 'asc'], [2, 'asc']]
        return opts

    def col_defs(self):
        res = []
        if self.language:
            res.extend([
                LinkCol(
                    self,
                    'gloss_en',
                    sTitle=self.req._('English'),
                    model_col=common.Parameter.name,
                    get_object=lambda v: v.valueset.parameter),
                Col(self,
                    'gloss_pm',
                    sTitle=self.req._('Papuan Malay'),
                    get_object=lambda v: v.valueset.parameter,
                    model_col=common.Parameter.description,
                    format=lambda i: i.valueset.parameter.description),
            ])
        elif self.parameter:
            res.extend([
                LinkCol(self, 'language', sTitle=self.req._('Language'),
                        get_object=lambda v: v.valueset.language,
                        model_col=common.Language.name),
                FamCol(
                    self,
                    'family',
                    sTitle=self.req._('Family'),
                    model_col=models.Variety.family,
                    choices=get_distinct_values(models.Variety.family)),
                Col(self,
                    'desc',
                    sTitle=self.req._('Location'),
                    get_object=lambda v: v.valueset.language,
                    model_col=common.Language.description,
                    ),
            ])
        else:
            res.extend([
                LinkCol(
                    self,
                    'gloss_en',
                    sTitle=self.req._('English'),
                    model_col=common.Parameter.name,
                    get_object=lambda v: v.valueset.parameter),
                Col(self,
                    'gloss_pm',
                    sTitle=self.req._('Papuan Malay'),
                    get_object=lambda v: v.valueset.parameter,
                    model_col=common.Parameter.description,
                    format=lambda i: i.valueset.parameter.description),
                LinkCol(self, 'language', sTitle=self.req._('Language'),
                        get_object=lambda v: v.valueset.language,
                        model_col=common.Language.name),
                FamCol(
                    self,
                    'family',
                    sTitle=self.req._('Family'),
                    model_col=models.Variety.family,
                    choices=get_distinct_values(models.Variety.family)),
                # Col(self,
                #     'desc',
                #     sTitle=self.req._('Location'),
                #     get_object=lambda v: v.valueset.language,
                #     model_col=common.Language.description,
                #     ),
                ])
        res.append(WordLinkCol(self, 'name', sTitle=self.req._('Word')))
        res.append(Col(self, 'description', sTitle=self.req._('Segments')))
        res.append(CommentCol(self, 'comment', sTitle='Comment'))
        res.append(AudioCol(self, '#'))
        return res


class PVContributors(Contributors):
    def col_defs(self):
        return [
            Col(self, 'name', sTitle=self.req._('Name')),
            Col(self, 'description', sTitle=self.req._('Role')),
        ]


def includeme(config):
    """register custom datatables"""
    config.register_datatable('parameters', Concepts)
    config.register_datatable('languages', Languages)
    config.register_datatable('values', Words)
    config.register_datatable('contributors', PVContributors)
