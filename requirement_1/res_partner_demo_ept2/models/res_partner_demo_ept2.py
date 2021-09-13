from odoo import fields, models

class PartnerDemo(models.Model):
    _name = "res.partner.demo.ept2"
    _description = "Partner Demo Software"

    name = fields.Char(string="Name",help="It will accepts the name of the customer")
    email = fields.Char(string="Email",help="It will accepts the Email of the customer")
    street1 = fields.Char(string="Street1",help="It will accepts the Street1 about address of the customer")
    street2 = fields.Char(string="Street2",help="It will accepts the Street2 about address of the customer")
    city = fields.Char(string="City",help="It will accepts the Email of the customer")
    state = fields.Char(string="State",help="It will accepts the state of the customer")
    zip_code = fields.Integer(string="Zip Code",help="It will accepts the zip_code of the customer")
    country = fields.Char(string="Country",help="It will accepts the country of the customer")
    birthdate = fields.Date(string="Birthdate",help="It will accepts the birthdate of the customer")
    age = fields.Integer(string="Age",help="It will accepts the age of the customer")
    weight = fields.Float(string="Weight",help="It will accepts the weight of the customer")
    description = fields.Text(string="Description",help="It will accepts the description of the customer")
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('others','Others')],
                              required=True,default='male',help="It will accepts the dropdown menu about gender"
                                                                " of the customer")
    details = fields.Html(string="HTML Details",help="It will accepts the details of the customer")
    is_spactacles = fields.Boolean(string="Is Spactacles",help="It will give the checkbox of the customer")
    photo = fields.Image(string="Photo",help="It will accepts the photo of the customer")

