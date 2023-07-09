""" Tenant Controller Module """

import uuid
import datetime
from .base_controller import BaseController
from ..models import Tenant


class TenantController:
    """The tenant controller for all controllers in the api"""
    _controller: BaseController = None
    
    def __init__(self, controller: BaseController):
        """The constructor for the tenant controller"""
        self._controller = controller
        
    def get_controller(self):
        """The get method for the tenant controller"""
        return self._controller
    
    def get_tenants(self):
        """Get all tenants"""
        return (self.get_controller().get_db_client().get_session().query(Tenant).all())
    
    
    def get_tenant(self, tenant_id):
        """Get a tenant by id"""
        return (self.get_controller().get_db_client().get_session().query(Tenant)\
                .filter_by(id=tenant_id).first())
    
    def create_tenant(self, data):
        """Create a tenant"""
        tenant = Tenant(
            id=str(uuid.uuid4()),
            name=data["name"],
            owner_id=data["owner_id"],
            description=data["description"],
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        self.get_controller().get_db_client().get_session().add(tenant)
        self.get_controller().get_db_client().get_session().commit()
        return tenant
    
    def update_tenant(self, tenant_id, data):
        """Update a tenant"""
        tenant = self.get_tenant(tenant_id)
        tenant.name = data["name"]
        tenant.description = data["description"]
        tenant.updated_at = datetime.datetime.utcnow()
        self.get_controller().get_db_client().get_session().commit()
        return tenant
    
    def delete_tenant(self, tenant_id):
        """Delete a tenant"""
        tenant = self.get_tenant(tenant_id)
        self.get_controller().get_db_client().get_session().delete(tenant)
        self.get_controller().get_db_client().get_session().commit()
        return tenant
    
    def get_tenant_by_name(self, name):
        """Get a tenant by name"""
        return (self.get_controller().get_db_client().get_session().query(Tenant)\
                .filter_by(name=name).first())
        
    def get_tenant_by_owner_id(self, owner_id):
        """Get a tenant by owner_id"""
        return (self.get_controller().get_db_client().get_session().query(Tenant)\
                .filter_by(owner_id=owner_id).first())
        