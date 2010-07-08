# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from clients.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('clients_client', (
            ('id', orm['clients.Client:id']),
            ('name', orm['clients.Client:name']),
        ))
        db.send_create_signal('clients', ['Client'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('clients_client')
        
    
    
    models = {
        'clients.client': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['clients']
