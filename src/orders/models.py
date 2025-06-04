from dataclasses import dataclass
from datetime import datetime

@dataclass
class ServiceOrder:
    order_id: int
    customer_name: str
    service_description: str
    price: float

@dataclass
class ReceiptProtocol:
    protocol_id: int
    order: ServiceOrder
    issued_at: datetime

@dataclass
class InvoiceInfo:
    invoice_id: int
    protocol: ReceiptProtocol
    total: float
