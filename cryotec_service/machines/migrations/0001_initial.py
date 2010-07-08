# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from machines.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'MachineMark'
        db.create_table('machines_machinemark', (
            ('id', orm['machines.MachineMark:id']),
            ('name', orm['machines.MachineMark:name']),
            ('machinetype', orm['machines.MachineMark:machinetype']),
            ('to_days_max', orm['machines.MachineMark:to_days_max']),
            ('motohours_max', orm['machines.MachineMark:motohours_max']),
        ))
        db.send_create_signal('machines', ['MachineMark'])
        
        # Adding model 'Machine'
        db.create_table('machines_machine', (
            ('id', orm['machines.Machine:id']),
            ('serial', orm['machines.Machine:serial']),
            ('client', orm['machines.Machine:client']),
            ('motohours', orm['machines.Machine:motohours']),
            ('machinemark', orm['machines.Machine:machinemark']),
        ))
        db.send_create_signal('machines', ['Machine'])
        
        # Adding model 'MachineType'
        db.create_table('machines_machinetype', (
            ('id', orm['machines.MachineType:id']),
            ('name', orm['machines.MachineType:name']),
        ))
        db.send_create_signal('machines', ['MachineType'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'MachineMark'
        db.delete_table('machines_machinemark')
        
        # Deleting model 'Machine'
        db.delete_table('machines_machine')
        
        # Deleting model 'MachineType'
        db.delete_table('machines_machinetype')
        
    
    
    models = {
        'clients.client': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'machines.machine': {
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinemark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineMark']"}),
            'motohours': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'machines.machinemark': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineType']"}),
            'motohours_max': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'to_days_max': ('django.db.models.fields.IntegerField', [], {})
        },
        'machines.machinetype': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['machines']
