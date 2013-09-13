# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('gallery', ['Gallery'])

        # Adding model 'GalleryItem'
        db.create_table('gallery_galleryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uploaded_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('thumb_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('gallery', ['GalleryItem'])


    def backwards(self, orm):
        
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')

        # Deleting model 'GalleryItem'
        db.delete_table('gallery_galleryitem')


    models = {
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'gallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'thumb_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'uploaded_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']
