# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'RecruitmentClass.color'
        db.alter_column('recruitment_recruitmentclass', 'color', self.gf('django.db.models.fields.CharField')(max_length=7))
    
    
    def backwards(self, orm):
        
        # Changing field 'RecruitmentClass.color'
        db.alter_column('recruitment_recruitmentclass', 'color', self.gf('django.db.models.fields.CharField')(max_length=6))
    
    
    models = {
        'recruitment.recruitmentclass': {
            'Meta': {'object_name': 'RecruitmentClass'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'FFFFFF'", 'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['recruitment']
