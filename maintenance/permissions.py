from rest_framework import permissions


class MaintenanceResponsibleTechnician(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(responsible_technician=request.user)
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.responsible_technician == request.user
