from datetime import datetime

from django_neomodel import DjangoNode
from neomodel import DateTimeProperty, StringProperty, UniqueIdProperty


class Company(DjangoNode):
    uuid = UniqueIdProperty(primary_key=True)
    label = StringProperty(unique_index=True)
    description = StringProperty(required=True)
    created_at = DateTimeProperty(default=datetime.utcnow)

    class Meta:
        app_label = "business_manager"

    def __str__(self) -> str:
        return self.description or self.label
