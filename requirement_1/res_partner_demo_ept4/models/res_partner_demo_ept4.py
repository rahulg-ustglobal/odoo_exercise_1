from odoo import fields,models

class PartnerDemo(models.Model):
    _name = "res.partner.demo.ept4"
    _description = "Partner Demo Software"

    name = fields.Char(string="Name",help="This field will accepts the name of the customer")
    email = fields.Char(string="Email",help="This field will accepts the email of the customer")
    street1 = fields.Char(string="Street1",help="This field will accepts the address of the street1 of the customer")
    street2 = fields.Char(string="Street2",help="This field will accepts the address of the street 2 of the customer")
    city = fields.Char(string="City",help="This field will accepts the city of the customer")
    state = fields.Char(string="State",help="This field will accepts the state of the customer")
    zip_code = fields.Integer(string="Zip code",help="This field will accepts the zipcode of the customer")
    country = fields.Char(string="Country",help="This field will accepts the email of the customer")
    birthdate = fields.Date(string="Birthdate",help="This field will accepts the birthdate of the customer")
    age = fields.Integer(string="Age",help="This field will accepts the age of the customer")
    weight = fields.Float(string="Weight",help="This field will accepts the weight of the customer")
    description = fields.Text(string="Description",help="This field will accepts the description of the customer")
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('other','Transgender')],
                              required=True,default='male',
                              help="It will accepts the dropdown menu about "
                                    "gender of the customer")
    details = fields.Html(string="HTML Details", help="It will accepts the details of the customer")
    is_spactacles = fields.Boolean(string="Is Spactacles", help="It will give the checkbox of the customer")
    photo = fields.Image(string="Photo", help="It will accepts the photo of the customer")
