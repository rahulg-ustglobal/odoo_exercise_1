from odoo import fields, models

class CityDemo(models.Model):
    _name = "res.city.demo.ept"
    _description = "City Demo Software"

    city_name = fields.Char(string="City Name",help="It will accepts the name of the city")
    state_name = fields.Char(string="State Name", help="It will accepts the "
                                                           "state name",copy=False)
    is_active = fields.Boolean(string="Active", help="It will gives the user like checkbox")


