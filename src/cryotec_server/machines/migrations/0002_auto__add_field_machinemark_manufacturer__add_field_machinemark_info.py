# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MachineMark.manufacturer'
        db.add_column('machines_machinemark', 'manufacturer', self.gf('django.db.models.fields.CharField')(default=None, max_length=128), keep_default=False)

        # Adding field 'MachineMark.info'
        db.add_column('machines_machinemark', 'info', self.gf('tinymce.models.HTMLField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'MachineMark.manufacturer'
        db.delete_column('machines_machinemark', 'manufacturer')

        # Deleting field 'MachineMark.info'
        db.delete_column('machines_machinemark', 'info')


    models = {
        'clients.client': {
            'Meta': {'object_name': 'Client'},
            'address_legal': ('django.db.models.fields.TextField', [], {'max_length': '30000', 'blank': 'True'}),
            'address_machine': ('django.db.models.fields.TextField', [], {'max_length': '30000', 'blank': 'True'}),
            'address_phys': ('django.db.models.fields.TextField', [], {'max_length': '30000', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'machines.machine': {
            'Meta': {'object_name': 'Machine'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'machines'", 'to': "orm['clients.Client']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'machines_customer'", 'null': 'True', 'to': "orm['clients.Client']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinemark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineMark']"}),
            'manufacturing_year': ('django.db.models.fields.IntegerField', [], {}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'motohours': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'machines.machinemark': {
            'Meta': {'object_name': 'MachineMark'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'machinetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineType']"}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'month_default': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'motohours_default': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'machines.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['machines']
