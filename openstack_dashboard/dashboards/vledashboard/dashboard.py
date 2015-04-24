from django.utils.translation import ugettext_lazy as _

import horizon
import openstack_dashboard.dashboards.vledashboard.stacks

class Vledashboard(horizon.Dashboard):
    slug = "vledashboard"
    name = _("Vledashboard")
    panels = (Stacks)  # Add your panels here.
    default_panel = 'stacks'  # Specify the slug of the dashboard's default panel.


horizon.register(Vledashboard)
