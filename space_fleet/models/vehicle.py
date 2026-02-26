from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SpaceFleetVehicle(models.Model):
    _name = "space.fleet.vehicle"
    _description = "Veículo (Space Fleet)"
    _order = "name asc"
    #teste

    name = fields.Char(string="Nome", required=True)
    manufacturer = fields.Char(string="Fabricante")
    year = fields.Integer(string="Ano")
    cls = fields.Char(string="classe")
    speed_min = fields.Float(string="velocidade minima")
    speed_max = fields.Float(string="velocidade maxima")
    speed_vacuum = fields.Float(string="Velocidade no vácuo")
    speed_atm_1_1 = fields.Float(string="Velocidade em atm 1:1")

    weight = fields.Float(string="Peso")
    height = fields.Float(string="Altura")
    length = fields.Float(string="Comprimento")
    width = fields.Float(string="Largura")

    active = fields.Boolean(default=True)

    @api.constrains("year")
    def _check_year(self):
        for rec in self:
            if rec.year and (rec.year < 1800 or rec.year > 3000):
                raise ValidationError("Ano fora do intervalo (1800 a 3000).")

    @api.constrains("speed_vacuum", "speed_atm_1_1", "weight", "height", "length", "width")
    def _check_positive_values(self):
        for rec in self:
            for fname in ["speed_vacuum", "speed_atm_1_1", "weight", "height", "length", "width"]:
                val = rec[fname]
                if val is not None and val < 0:
                    raise ValidationError("Valores numéricos não podem ser negativos.")