# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Serial'
        db.create_table('serials_serial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('full_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('origin_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('last_img', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('serials', ['Serial'])

        # Adding model 'Episode'
        db.create_table('serials_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('full_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('origin_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('last_img', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('serial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['serials.Serial'])),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=250, blank=True)),
            ('watch_online_url', self.gf('django.db.models.fields.URLField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('serials', ['Episode'])

        # Adding model 'News'
        db.create_table('serials_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('full_description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('serials', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'Serial'
        db.delete_table('serials_serial')

        # Deleting model 'Episode'
        db.delete_table('serials_episode')

        # Deleting model 'News'
        db.delete_table('serials_news')


    models = {
        'serials.episode': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Episode'},
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'}),
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_img': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
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
        'serials.serial': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Serial'},
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_img': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_description': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['serials']
