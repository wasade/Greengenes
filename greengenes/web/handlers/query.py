from json import dumps

from wtforms import Form, TextField, SubmitField

from greengenes.web import db
from greengenes.web.handlers.base import BaseHandler


def _format_record(rec):
    result = []
    seqs = []
    for k in sorted(rec):
        if k == 'ncbi_acc_w_ver':
            result.append((k, '<a href="http://www.ncbi.nlm.nih.gov/nuccore/%s">%s</a>' % (rec[k], rec[k])))
        elif k == 'pubmed':
            result.append((k, '<a href="http://www.ncbi.nlm.nih.gov/pubmed/%s">%s</a>' % (rec[k], rec[k])))
        elif '_seq' in k:
            if len(rec[k]) > 80:
                seq = ''.join([rec[k][start:start+80]+'<br>' for start in range(0, len(rec[k])+1, 80)])
            seqs.append((k, '<font face="monospace">' + seq + '</font>'))
        else:
            result.append((k, rec[k]))
    result.extend(seqs)

    return result

from collections import Counter


def _summarize_cluster(details):
    def summarize(taxa):
        cnt = Counter()
        for tax in taxa:
            cnt[tax] += 1
        print cnt
        return sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    gg = summarize(details['gg_tax'])
    ncbi = summarize(details['ncbi_tax'])
    silva = summarize(details['silva_tax'])
    return (gg, ncbi, silva)


class Query(Form):
    QueryID = TextField('query_id')
    QuerySubmit = SubmitField('Submit')


class OTUHandler(BaseHandler):
    def get(self, clusterid=None):
        if clusterid is None:
            self.render("index.html", user=self.current_user, loginerror='')
        else:
            details = db.get_otu_cluster_detail(int(clusterid))
            self.render("otu.html", otu=details, user=self.current_user)


class OTUSummaryHandler(BaseHandler):
    def get(self, clusterid=None):
        if clusterid is None:
            self.render("index.html", user=self.current_user, loginerror='')
        else:
            details = db.get_otu_cluster_detail(int(clusterid))
            gg_sum, ncbi_sum, silva_sum = _summarize_cluster(details)
            self.render("otu_summary.html", gg_summary=gg_sum,
                        rep_id=details['rep_id'],
                        size=len(details['member_id']),
                        silva_summary=silva_sum,
                        ncbi_summary=ncbi_sum,
                        user=self.current_user)
class QueryHandler(BaseHandler):
    def _process_query(self, query):
        msg = []
        otu_details = []
        try:
            query = int(query)
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            if query in db:
                msg = db.select_record(query)
                otu_details = db.get_otu_membership(query, '13_5')
        return msg, otu_details

    def get(self, queryid=None):
        query = Query()

        if queryid is None:
            queryid = self.get_argument('QueryID', None)

        if queryid is None:
            self.render("query.html", user=self.current_user, form=query,
                        msg=[], otu_details=[])
        else:
            msg, otu_details = self._process_query(queryid)

            formatted = _format_record(msg)
            self.render("query.html", user=self.current_user, form=query,
                        msg=formatted, otu_details=otu_details,
                        queryid=queryid)

    def post(self):
        query = Query()

        queryid = self.get_argument('QueryID', None)
        msg, otu_details = self._process_query(queryid)
        formatted = _format_record(msg)
        self.render("query.html", user=self.current_user, msg=formatted,
                    form=query, otu_details=otu_details, queryid=queryid)
