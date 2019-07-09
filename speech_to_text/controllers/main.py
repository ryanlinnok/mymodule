from odoo import models, fields, api
from odoo.exceptions import except_orm, Warning, RedirectWarning
import random
import time
from itertools import islice
import json
import xml.etree.ElementTree as ET
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import dateutil.parser
import logging
import re
import werkzeug.utils
import urllib2
import werkzeug.wrappers
import odoo
from odoo import  http
from odoo.http import request

logger = logging.getLogger(__name__)

class speech_to_text_dashboard(http.Controller):

	@http.route('/speech_to_text/main', type='http', auth='user', website=True)
	def dashboard_speech_to_text_main(self, **kw):
		return http.request.render('speech_to_text.dashboard_speech_to_text_main_view', {})


	@http.route('/speech_to_text/save', type='http', auth="user", website=True, method="POST")
	def save_recording(self, **kw):
		speech_to_text_ids = request.env['speech.to.text']
		note = kw['note']
		title = kw['title']
		date = fields.datetime.now()
		if note:
			speech_to_text_ids.create({
				'note' : note,
				'date' : date,
				'title' : title,
				})
		return request.render('speech_to_text.dashboard_speech_to_text_main_view2')