# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from checklists.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ChecklistAnswer'
        db.create_table('checklists_checklistanswer', (
            ('id', orm['checklists.ChecklistAnswer:id']),
            ('checklistquestion', orm['checklists.ChecklistAnswer:checklistquestion']),
            ('paction', orm['checklists.ChecklistAnswer:paction']),
            ('comment', orm['checklists.ChecklistAnswer:comment']),
        ))
        db.send_create_signal('checklists', ['ChecklistAnswer'])
        
        # Adding model 'ChecklistQuestion'
        db.create_table('checklists_checklistquestion', (
            ('id', orm['checklists.ChecklistQuestion:id']),
            ('content', orm['checklists.ChecklistQuestion:content']),
            ('machinemark', orm['checklists.ChecklistQuestion:machinemark']),
            ('required', orm['checklists.ChecklistQuestion:required']),
            ('order', orm['checklists.ChecklistQuestion:order']),
        ))
        db.send_create_signal('checklists', ['ChecklistQuestion'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'ChecklistAnswer'
        db.delete_table('checklists_checklistanswer')
        
        # Deleting model 'ChecklistQuestion'
        db.delete_table('checklists_checklistquestion')
        
    
    
    models = {
        'actions.action': {
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.Machine']"})
        },
        'actions.paction': {
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'})
        },
        'checklists.checklistanswer': {
            'checklistquestion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['checklists.ChecklistQuestion']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actions.PAction']"})
        },
        'checklists.checklistquestion': {
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machinemark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineMark']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
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
    
    complete_apps = ['checklists']
