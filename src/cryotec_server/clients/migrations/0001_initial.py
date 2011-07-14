# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('clients_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=3000, blank=True)),
        ))
        db.send_create_signal('clients', ['Client'])

        # Adding model 'ContactFace'
        db.create_table('clients_contactface', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('clients', ['ContactFace'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('clients_client')

        # Deleting model 'ContactFace'
        db.delete_table('clients_contactface')


    models = {
        'clients.client': {
            'Meta': {'object_name': 'Client'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'clients.contactface': {
            'Meta': {'object_name': 'ContactFace'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['clients']
