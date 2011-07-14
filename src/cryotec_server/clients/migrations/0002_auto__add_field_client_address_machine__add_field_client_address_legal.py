# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Client.address_machine'
        db.add_column('clients_client', 'address_machine', self.gf('django.db.models.fields.TextField')(default='', max_length=30000, blank=True), keep_default=False)

        # Adding field 'Client.address_legal'
        db.add_column('clients_client', 'address_legal', self.gf('django.db.models.fields.TextField')(default='', max_length=30000, blank=True), keep_default=False)

        # Adding field 'Client.address_phys'
        db.add_column('clients_client', 'address_phys', self.gf('django.db.models.fields.TextField')(default='', max_length=30000, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Client.address_machine'
        db.delete_column('clients_client', 'address_machine')

        # Deleting field 'Client.address_legal'
        db.delete_column('clients_client', 'address_legal')

        # Deleting field 'Client.address_phys'
        db.delete_column('clients_client', 'address_phys')


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
