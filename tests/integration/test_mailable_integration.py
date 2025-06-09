from dataclasses import dataclass
from python_mailable.mailable import Mailable


@dataclass
class OrderShipped(Mailable):
    def build(self):
        context = {
            "customer_name": "John Doe",
            "order_id": "123456",
            "shipping_address": "Vijzelstraat 32, Amsterdam, The Netherlands",
            "carrier": "UPS",
            "tracking_number": "1Z999AA10123456784",
        }

        return (
            self.to("john.doe@example.net")
            .subject("Your order has shipped!")
            .template("/tests/integration/templates/order_shipped.html.j2")
            .with_context(context)
        )


def test_order_shipped_renders_successfully():
    email = OrderShipped().build()
    html = email.render()

    assert "John Doe" in html
    assert "123456" in html
    assert "Vijzelstraat 32, Amsterdam, The Netherlands" in html
    assert "UPS" in html
    assert "1Z999AA10123456784" in html
    assert "Your order has shipped!" in html

    # Optional: sanity check to ensure basic structure exists
    assert "<html>" in html
    assert "</html>" in html
