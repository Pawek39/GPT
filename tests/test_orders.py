import unittest
from datetime import datetime

from src.orders.models import ServiceOrder, ReceiptProtocol, InvoiceInfo
from src.orders import services


class ServiceTests(unittest.TestCase):
    def test_create_service_order(self):
        order = services.create_service_order(
            order_id=1,
            customer_name="John Doe",
            service_description="Cleaning",
            price=100.0,
        )
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.customer_name, "John Doe")
        self.assertEqual(order.price, 100.0)

    def test_generate_receipt_protocol(self):
        order = services.create_service_order(1, "John", "Test", 50.0)
        protocol = services.generate_receipt_protocol(order)
        self.assertIsInstance(protocol, ReceiptProtocol)
        self.assertEqual(protocol.order, order)
        self.assertIsInstance(protocol.issued_at, datetime)

    def test_prepare_invoice_info(self):
        order = services.create_service_order(1, "John", "Test", 50.0)
        protocol = services.generate_receipt_protocol(order)
        invoice = services.prepare_invoice_info(protocol)
        self.assertIsInstance(invoice, InvoiceInfo)
        self.assertEqual(invoice.protocol, protocol)
        self.assertEqual(invoice.total, 50.0)


if __name__ == '__main__':
    unittest.main()
