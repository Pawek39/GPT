"""Services for handling orders and invoices."""

from datetime import datetime
from typing import Optional
from .models import ServiceOrder, ReceiptProtocol, InvoiceInfo


_next_protocol_id = 1
_next_invoice_id = 1


def create_service_order(order_id: int, customer_name: str, service_description: str, price: float) -> ServiceOrder:
    """Create a new ServiceOrder instance."""
    return ServiceOrder(
        order_id=order_id,
        customer_name=customer_name,
        service_description=service_description,
        price=price,
    )


def generate_receipt_protocol(order: ServiceOrder) -> ReceiptProtocol:
    """Generate a receipt protocol for the given service order."""
    global _next_protocol_id
    protocol = ReceiptProtocol(
        protocol_id=_next_protocol_id,
        order=order,
        issued_at=datetime.utcnow(),
    )
    _next_protocol_id += 1
    return protocol


def prepare_invoice_info(protocol: ReceiptProtocol) -> InvoiceInfo:
    """Prepare invoice information based on the receipt protocol."""
    global _next_invoice_id
    invoice = InvoiceInfo(
        invoice_id=_next_invoice_id,
        protocol=protocol,
        total=protocol.order.price,
    )
    _next_invoice_id += 1
    return invoice
