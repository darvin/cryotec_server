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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('machines', ['MachineType'])

        # Adding model 'MachineMark'
        db.create_table('machines_machinemark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('machinetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machines.MachineType'])),
            ('month_default', self.gf('django.db.models.fields.IntegerField')()),
            ('motohours_default', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('machines', ['MachineMark'])

        # Adding model 'Machine'
        db.create_table('machines_machine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='machines', to=orm['clients.Client'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='machines_customer', null=True, to=orm['clients.Client'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('machinemark', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machines.MachineMark'])),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('motohours', self.gf('django.db.models.fields.IntegerField')()),
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
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'bik': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'kor_schet': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'kpp': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'okpo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'post_addr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rasch_schet': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ur_addr': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'machines.machine': {
            'Meta': {'object_name': 'Machine'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'machines'", 'to': "orm['clients.Client']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'machines_customer'", 'null': 'True', 'to': "orm['clients.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinemark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineMark']"}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'motohours': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'machines.machinemark': {
            'Meta': {'object_name': 'MachineMark'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineType']"}),
            'month_default': ('django.db.models.fields.IntegerField', [], {}),
            'motohours_default': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'machines.machinetype': {
            'Meta': {'object_name': 'MachineType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['machines']
