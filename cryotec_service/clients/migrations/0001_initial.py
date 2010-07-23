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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ur_addr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('post_addr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('inn', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('kpp', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('okpo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('rasch_schet', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('kor_schet', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bik', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('clients', ['Client'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('clients_client')


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
        }
    }

    complete_apps = ['clients']
