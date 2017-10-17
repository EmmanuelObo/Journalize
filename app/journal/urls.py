from django.conf.urls import url
from . import views
from .views import JournalList, JournalDrafts, PublishEntry


entry_urls = [
    url(r'(?P<id>[0-9]+)$', views.EntryView.as_view(), name="view_entry"),
    url(r'^(?P<id>[0-9]+)/edit$', views.EditEntry.as_view(), name="edit_entry"),
    url(r'^create/$', views.CreateEntry.as_view(), name="create_entry"),
    url(r'^(?P<id>[0-9]+)/delete$', views.delete_entry, name="delete_entry"),
    url(r'^drafts/$', JournalDrafts.as_view(), name="drafts"),
    url(r'^drafts/(?P<id>[0-9]+)/publish$', PublishEntry.as_view(), name="publish_draft"),
    url(r'^$', JournalList.as_view(), name="entries")
]
