# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PAction.motohours'
        db.add_column('actions_paction', 'motohours', self.gf('django.db.models.fields.IntegerField')(default=444), keep_default=False)

        # Deleting field 'Checkup.motohours'
        db.delete_column('actions_checkup', 'motohours')


    def backwards(self, orm):
        
        # Deleting field 'PAction.motohours'
        db.delete_column('actions_paction', 'motohours')

        # Adding field 'Checkup.motohours'
        db.add_column('actions_checkup', 'motohours', self.gf('django.db.models.fields.IntegerField')(default=333), keep_default=False)


    models = {
        'actions.action': {
            'Meta': {'object_name': 'Action'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['machines.Machine']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'actions.checkup': {
            'Meta': {'object_name': 'Checkup', '_ormbases': ['actions.PAction']},
            'paction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.PAction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'actions.fix': {
            'Meta': {'object_name': 'Fix', '_ormbases': ['actions.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actions.Report']"})
        },
        'actions.maintenance': {
            'Meta': {'object_name': 'Maintenance', '_ormbases': ['actions.PAction']},
            'paction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.PAction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'actions.paction': {
            'Meta': {'object_name': 'PAction', '_ormbases': ['actions.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'motohours': ('django.db.models.fields.IntegerField', [], {})
        },
        'actions.report': {
            'Meta': {'object_name': 'Report', '_ormbases': ['actions.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['actions.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'fixed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'interest': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'paction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['actions.PAction']", 'null': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'machines.machine': {
            'Meta': {'object_name': 'Machine'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'machines'", 'to': "orm['clients.Client']"}),
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

    complete_apps = ['actions']
