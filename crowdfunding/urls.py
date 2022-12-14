from django.urls import path
from . import views

app_name = "crowdfunding"

urlpatterns = [
    path("", views.show_crowdfundings, name="show_crowdfundings"),
    path("<int:id>/", views.show_crowdfunding_by_id, name="show_crowdfunding_by_id"),
    path("create/", views.create_crowdfund, name="create_crowdfund"),
    path("create/mobile", views.create_crowdfund_mobile, name="create_crowdfund"),
    path("edit/<int:id>", views.edit_crowdfund, name="edit_crowdfund"),
    path(
        "edit/mobile/<int:id>",
        views.edit_crowdfund_mobile,
        name="edit_crowdfund_mobile",
    ),
    path("delete/<int:id>", views.delete_crowdfund, name="delete_crowdfund"),
    path("json/", views.show_crowdfundings_json, name="show_crowdfundings_json"),
    path(
        "json/<int:id>",
        views.show_crowdfundings_by_id_json,
        name="show_crowdfundings_by_json",
    ),
    path(
        "add-point-when-contacting/<int:id>",
        views.add_point_when_contacting,
        name="add_point_when_contacting",
    ),
]
