from ckan.lib import base
from ckan import logic, model
from ckan.plugins import toolkit
from ckan.common import c, _, request
from ckan.controllers import organization
from collections import Counter

get_action = logic.get_action
NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError

abort = base.abort
render = base.render

def _get_context():
    return {
        'model': model,
        'session': model.Session,
        'user': c.user or c.author,
        'auth_user_obj': c.userobj
    }


def _get_action(action, data_dict):
    return toolkit.get_action(action)(_get_context(), data_dict)

class RealTimeWidgetController(base.BaseController):

	def real_time_widget(self):
		return base.render('home/real_time_widget.html')

