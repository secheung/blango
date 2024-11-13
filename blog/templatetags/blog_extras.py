from django import template
from django.contrib.auth import get_user_model
# from django.utils.html import escape
# from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()
user_model = get_user_model()

@register.filter(name="author_details")
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ""

  if current_user and isinstance(current_user, user_model) and (current_user == author):
    return format_html('<strong>me</strong>')

  if author.first_name and author.last_name:
    #name = escape(f"{author.first_name} {author.last_name}") #escape and mark safe method
    name = f"{author.first_name} {author.last_name}"
  else:
    #name = escape(f"{author.username}") #escape and mark safe method
    name = f"{author.username}"

  if author.email:
    '''#escape and mark safe method
    email = escape(author.email) 
    prefix = f"<a href=mailto:{email}>"
    suffix = "</a>"
    '''
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')
  else:
    prefix = ""
    suffix = ""
  
  return format_html('{}{}{}', prefix, name, suffix)
  #return mark_safe(f"{prefix}{name}{suffix}") #escape and mark safe method