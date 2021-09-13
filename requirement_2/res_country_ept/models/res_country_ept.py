from odoo import fields, models

class CountryDemo(models.Model):
    _name = "res.country.demo.ept"
    _description = "Country Demo Software"

    name = fields.Char(string="Country Name", help="It will accepts the "
                                                                  "name of the country")
    country_code = fields.Char(string="Country Code", help="It will accepts the "
                                                                        "country code of the country")
    is_active = fields.Boolean(string="Active", help="It will gives the user like checkbox")