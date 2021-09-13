from odoo import fields, models


class CrmDemoApp(models.Model):
    _name = "crm.lead.demo.ept"
    _description = "CRM Demo Software"

    customer_name = fields.Char(string="Customer Name", help="It will accepts the customer name")
    customer_email = fields.Char(string="Customer email", help="It will accepts the Customer email")
    customer_phone = fields.Char(string="Customer phone", help="It will accepts the Customer phone")
    expected_revenue = fields.Float(string="Expected revenue", digits=(1, 3),
                                    help="It will accepts the expected revenue")
    salesperson = fields.Char(string="Salesperson", help="It will accepts the Salesperson")

    sales_team = fields.Char(string="Sales Team", help="It will accepts the sales team")
    campaign = fields.Char(string="Campaign", help="It will accepts the campaign")
    channel = fields.Selection([('facebook', 'Facebook'),
                                ('whatsApp', 'WhatsApp'),
                                ('email', 'Email'),
                                ('newspaper', 'Newspaper'),
                                ('television', 'Television'),
                                ('phone_call', 'Phone Call'),
                                ('sms', 'SMS'),
                                ('google_ads', 'Google Ads'), ], required=True,
                               help="It will accepts the dropdown menu about channel")

    next_follow_up_date = fields.Date(string="Next Follow Up Date", required=True,
                                      help="It will accepts the next follow up date")
    won_date = fields.Date(string="Won Date", help="It will accept the won date")
    lost_reason = fields.Text(string="Lost reason", help="It will accept the won date")
    state = fields.Selection([
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('Proposition', 'Proposition'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ], string="Status", help="State Of The Lead")

    # Button function with name as a action_draft
    def action_won(self):
        self.state = "Won"
        self.won_date = fields.date.today()

    # Button function with name as a action_draft
    def action_lost(self):
        self.state = "Lost"
        self.lost_reason = 'Not Interested'
