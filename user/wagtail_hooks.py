from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse

class WelcomePanel(Component):
    order = 50

    def render_html(self, parent_context):
        return mark_safe("""
        <section class="panel summary nice-padding">
          <h3>No, but seriously -- welcome to the admin homepage.</h3>
        </section>
        """)

@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())

@hooks.register('construct_main_menu')
def hide_explorer_menu_item_from_frank(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'help']
    menu_items[:] = [item for item in menu_items if item.name != 'reports']
  # if request.user.username == 'frank':
  #
  #     for menu_item in menu_items:
  #       print(menu_item.name)

# @hooks.register('register_admin_menu_item')
# def register_frank_menu_item():
#   return MenuItem('Frank', 'localhost', icon_name='folder-inverse', order=10000)