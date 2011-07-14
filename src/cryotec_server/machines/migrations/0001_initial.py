# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MachineType'
        db.create_table('machines_machinetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('machines', ['MachineType'])

        # Adding model 'MachineMark'
        db.create_table('machines_machinemark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('machinetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machines.MachineType'])),
            ('month_default', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('motohours_default', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('machines', ['MachineMark'])

        # Adding model 'Machine'
        db.create_table('machines_machine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='machines', to=orm['clients.Client'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='machines_customer', null=True, to=orm['clients.Client'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('machinemark', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machines.MachineMark'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('manufacturing_year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('motohours', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('machines', ['Machine'])


    def backwards(self, orm):
        
        # Deleting model 'MachineType'
        db.delete_table('machines_machinetype')

        # Deleting model 'MachineMark'
        db.delete_table('machines_machinemark')

        # Deleting model 'Machine'
        db.delete_table('machines_machine')


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
            'machinetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineType']"}),
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
