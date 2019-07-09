from odoo import api, fields, models, _
from datetime import datetime, date
from odoo.exceptions import UserError, ValidationError
import speech_recognition as sr  

class speech_to_text(models.Model):
    _name = 'speech.to.text'
    _rec_name = 'title'

    note = fields.Html('Note')
    title = fields.Char('Title')
    date = fields.Datetime('Tanggal')
    lokasi = fields.Char('Lokasi')
    kesimpulan = fields.Text('Kesimpulan & Tindak Lanjut')
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", relation="m2m_ir_attachment_relation", column1="m2m_id", column2="attachment_id", string="Attachments",)
    peserta_ids = fields.Many2many(comodel_name='res.users',string='Peserta')

    # @api.multi
    # def start_speech_to_text(self):
    #     # get audio from the microphone                                                                       
    #     r = sr.Recognizer()                                                                                   
    #     with sr.Microphone() as source:                                                                       
    #         print("Speak:")                                                                                   
    #         audio = r.listen(source)   

    #     try:
    #         print("You said " + r.recognize_google(audio))
    #     except sr.UnknownValueError:
    #         print("Could not understand audio")
    #     except sr.RequestError as e:
    #         print("Could not request results; {0}".format(e))

    #     self.state = 'start'

    # @api.multi
    # def stop_speech_to_text(self):
    #     self.state = 'stop'