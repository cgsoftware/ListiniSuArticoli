# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math
from tools.translate import _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import decimal_precision as dp
import time


from osv import fields, osv



class product_product(osv.osv):
    _inherit = 'product.product'

    

    
    _columns = {
                'righe_listini': fields.one2many('product.pricelist.item', 'product_id', 'Righe Listini Articolo', required=False),
               }

product_product()


