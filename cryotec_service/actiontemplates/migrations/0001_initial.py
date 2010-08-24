# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ReportLevel'
        db.create_table('actiontemplates_reportlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('actiontemplates', ['ReportLevel'])

        # Adding model 'ReportTemplate'
        db.create_table('actiontemplates_reporttemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machinemark', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['machines.MachineMark'])),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=3000)),
            ('interest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actiontemplates.ReportLevel'])),
        ))
        db.send_create_signal('actiontemplates', ['ReportTemplate'])


    def backwards(self, orm):
        
        # Deleting model 'ReportLevel'
        db.delete_table('actiontemplates_reportlevel')

        # Deleting model 'ReportTemplate'
        db.delete_table('actiontemplates_reporttemplate')


    models = {
        'actiontemplates.reportlevel': {
            'Meta': {'object_name': 'ReportLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'actiontemplates.reporttemplate': {
            'Meta': {'object_name': 'ReportTemplate'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actiontemplates.ReportLevel']"}),
            'machinemark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.MachineMark']"})
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

    complete_apps = ['actiontemplates']
