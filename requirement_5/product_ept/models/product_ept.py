from odoo import fields, models

class ProductEpt(models.Model):
    _name = "product.demo.ept"
    _description = "ProductEpt Software"

    product_name = fields.Char(string="Product Name",help="It will accepts the product name")
    sku = fields.Char(string="SKU", help="It will accepts the product sku")
    product_barcode = fields.Char(string="Product Barcode",help="It will accepts the product barcode")
    sold = fields.Boolean(string="Sold",help="It will showing the checkbox for sold or not sold")
    product_type = fields.Selection([('storable','Storable'),
                                     ('consumable','Consumable'),
                                     ('service','Service')],required=True,default='storable',
                                    help="It will accepts the dropdown menu about product typr of the customer")
    sale_price = fields.Float(string="Sale Price",digits=(6,2),help="It will accept the sale price from the customer")
    cost_price = fields.Float(string="Cost Price",digits=(6,2),help="It will accept the cost price of the product from the customer")
    is_active = fields.Boolean(string="Active", help="It will gives the user like checkbox")
    warehouse = fields.Char(string="Warehouse",help="It will accept the warehouse")
    product_image = fields.Image(string="Product Image",help="It will accepts the product image")
    website_description = fields.Html(string="Website Description",help="It will accepts the Website Description")
    internal_note = fields.Text(string="Internal Note",help="It will accepts the Internal Note in the form of text")



