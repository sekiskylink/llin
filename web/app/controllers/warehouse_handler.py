# -*- coding: utf-8 -*-

"""This module contains the main handler of the application.
"""

import web
from . import csrf_protected, db, require_login, render
from settings import PAGE_LIMIT
from app.tools.pagination import doquery, countquery, getPaginationString
from app.tools.utils import lit, default


class WarehouseData:
    @require_login
    def GET(self):
        params = web.input(page=1)
        try:
            page = int(params.page)
        except:
            page = 1

        limit = PAGE_LIMIT
        start = (page - 1) * limit if page > 0 else 0

        dic = lit(relations='national_deliery_log', fields="*", criteria="", order="id desc", limit=limit, offset=start)
        res = doquery(db, dic)
        count = countquery(db, dic)
        pagination_str = getPaginationString(default(page, 0), count, limit, 2, "warehousedata", "?page=")
        countries = db.query("SELECT id, name FROM countries ORDER BY name")

        l = locals()
        del l['self']
        return render.warehousedata(**l)

    @csrf_protected
    def POST(self):
        pass
