# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Serial.last_img'
        db.delete_column('serials_serial', 'last_img')

        # Deleting field 'Episode.last_img'
        db.delete_column('serials_episode', 'last_img')


    def backwards(self, orm):
        
        # Adding field 'Serial.last_img'
        db.add_column('serials_serial', 'last_img', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Episode.last_img'
        db.add_column('serials_episode', 'last_img', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)


    models = {
        'serials.episode': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Episode'},
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'}),
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['serials.Serial']"}),
            'watch_online_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'})
        },
        'serials.news': {
            'Meta': {'ordering': "('-pub_date', 'name')", 'object_name': 'News'},
            'full_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_description': ('django.db.models.fields.TextField', [], {})
        },
        'serials.rimage': {
            'Meta': {'object_name': 'RImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'})
        },
        'serials.serial': {
            'Meta': {'ordering': "('-last_modified',)", 'object_name': 'Serial'},
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['serials']
