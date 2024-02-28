from fastapi_amis_admin import (
    amis,
    admin
)

from fastapi_amis_admin.admin import AdminApp
from .models import Employee

from core.globals import site


@site.register_admin
class ProfileApp(admin.AdminApp):
    page_schema = amis.PageSchema(label='profile', icon='fa fa-person')
    router_prefix = '/profile'

    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        self.register_admin(EmployeeAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    page_schema = amis.PageSchema(label='Employee', icon='fa fa-person')
    model = Employee
    list_display = [
        Employee.id,
        Employee.first_name,
        Employee.middle_name,
        Employee.last_name,
        Employee.is_active
    ]
    search_fields = [Employee.id, Employee.first_name,
                     Employee.last_name]
    list_filter = [Employee.is_active]
    update_fields = [Employee.id, Employee.first_name, Employee.last_name,
                     Employee.bio, Employee.is_active]
    enable_bulk_create = True
