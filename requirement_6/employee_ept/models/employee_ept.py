from odoo import fields, models

class ProductEpt(models.Model):
    _name = "employee.demo.ept"
    _description = "EmployeeEpt Software"

    emp_name = fields.Char(string="Employee Name", help="It will accepts the employee name")
    dept_name = fields.Char(string="Department Name", help="It will accepts the Department Name")
    job_position = fields.Char(string="Job Position", help="It will accepts the job position")
    salary = fields.Float(string="Salary", digits=(6, 2), help="It will accepts the salary of the employee")
    hire_date = fields.Date(string="Hire Date", help="It will accepts the Hire Date of the employee")
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('transgender', 'Transgender')], required=True, default='male',
                              help="It will accepts the dropdown menu about gender of the employee")
    job_type = fields.Selection([('permanent', 'Permanent'),
                                 ('ad_hoc', 'Ad Hoc')], required=True,
                                help="It will accepts the dropdown menu about job type of the employee")
