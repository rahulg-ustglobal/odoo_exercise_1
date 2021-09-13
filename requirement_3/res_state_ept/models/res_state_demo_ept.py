from odoo import fields, models

class StateDemo(models.Model):
    _name = "res.state.demo.ept"
    _description = "State Demo Software"

    name = fields.Char(string="State Name",help="It will accepts the name of the state")
    state_code = fields.Char(string="State Code", help="It will accepts the "
                                                           "state code of the country")
    country_name = fields.Char(string="Country Name", help="It will accepts the name of the country",copy=False)
    is_active = fields.Boolean(string="Active", help="It will gives the user like checkbox")


