# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from actions.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Report'
        db.create_table('actions_report', (
            ('action_ptr', orm['actions.Report:action_ptr']),
            ('paction', orm['actions.Report:paction']),
            ('fixed', orm['actions.Report:fixed']),
        ))
        db.send_create_signal('actions', ['Report'])
        
        # Adding model 'Maintenance'
        db.create_table('actions_maintenance', (
            ('paction_ptr', orm['actions.Maintenance:paction_ptr']),
        ))
        db.send_create_signal('actions', ['Maintenance'])
        
        # Adding model 'PAction'
        db.create_table('actions_paction', (
            ('action_ptr', orm['actions.PAction:action_ptr']),
        ))
        db.send_create_signal('actions', ['PAction'])
        
        # Adding model 'Checkup'
        db.create_table('actions_checkup', (
            ('paction_ptr', orm['actions.Checkup:paction_ptr']),
            ('motohours', orm['actions.Checkup:motohours']),
        ))
        db.send_create_signal('actions', ['Checkup'])
        
        # Adding model 'Fix'
        db.create_table('actions_fix', (
            ('action_ptr', orm['actions.Fix:action_ptr']),
            ('report', orm['actions.Fix:report']),
        ))
        db.send_create_signal('actions', ['Fix'])
        
        # Adding model 'Action'
        db.create_table('actions_action', (
            ('id', orm['actions.Action:id']),
            ('machine', orm['actions.Action:machine']),
            ('comment', orm['actions.Action:comment']),
            ('date', orm['actions.Action:date']),
        ))
        db.send_create_signal('actions', ['Action'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Report'
        db.delete_table('actions_report')
        
        # Deleting model 'Maintenance'
        db.delete_table('actions_maintenance')
        
        # Deleting model 'PAction'
        db.delete_table('actions_paction')
        
        # Deleting model 'Checkup'
        db.delete_table('actions_checkup')
        
        # Deleting model 'Fix'
        db.delete_table('actions_fix')
        
        # Deleting model 'Action'
        db.delete_table('actions_action')
        
    
    
    models = {
        'actions.action': {
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.Machine']"})
        },
        'actions.checkup': {
            'motohours': ('django.db.models.fields.IntegerField', [], {}),
            'paction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.PAction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'actions.fix': {
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actions.Report']"})
        },
        'actions.maintenance': {
            'paction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.PAction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'actions.paction': {
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'})
        },
        'actions.report': {
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'fixed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'paction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actions.PAction']"})
        },
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
    
    complete_apps = ['actions']
