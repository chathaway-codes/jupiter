from django import template
import datetime
register = template.Library()

def print_timestamp(timestamp):
  return timestamp.strftime("%Y-%m-%d %I:%M%p")

def weight_only(data):
  return data.filter(type='WGHT')
def height_only(data):
  return data.filter(type='HEHT')
def blsg_only(data):
  return data.filter(type='BLSG')
def plse_only(data):
  return data.filter(type='PLSE')
def bprs_only(data):
  return data.filter(type='BPRS')


register.filter(print_timestamp)
register.filter(weight_only)
register.filter(height_only)
register.filter(blsg_only)
register.filter(plse_only)
register.filter(bprs_only)
