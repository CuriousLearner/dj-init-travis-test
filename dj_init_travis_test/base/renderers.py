from rest_framework.renderers import JSONRenderer


class DjInitTravisTestApiRenderer(JSONRenderer):
    media_type = 'application/vnd.djinittravistest+json'
