# populate_faq.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportigo.settings")
django.setup()

from app.models import FAQ

def populate_faq():
    # Clear existing data
    FAQ.objects.all().delete()

    # Add new FAQ entries
    faq_entries = [
        {'question': 'How do I book a turf?', 'answer': 'You can book a turf by navigating to the booking page and following the instructions.'},
        {'question': 'What are the available payment options?', 'answer': 'We accept payments via credit/debit card, online wallets, and cash on delivery.'},
        {'question': 'Can I cancel my turf booking?', 'answer': 'Yes, you can cancel your turf booking. Please refer to our cancellation policy for details.'},
        {'question': 'Is there a minimum booking duration for turfs?', 'answer': 'Yes, the minimum booking duration for turfs is one hour.'},
        {'question': 'Do you provide equipment for turf activities?', 'answer': 'Yes, we provide equipment such as balls, bats, and goal posts for turf activities. Additional charges may apply.'},
        {'question': 'Can I bring my own equipment?', 'answer': 'Yes, you can bring your own equipment for turf activities. Please ensure that it complies with our safety regulations.'},
        {'question': 'What happens if it rains on the day of my booking?', 'answer': 'In case of rain, we will reschedule your booking to another available time slot. Alternatively, you can request a refund.'},
        {'question': 'Do you offer discounts for bulk bookings?', 'answer': 'Yes, we offer discounts for bulk bookings. Please contact our customer support team for more information.'},
        {'question': 'Is there a membership program available?', 'answer': 'Yes, we offer a membership program with exclusive benefits such as discounted rates and priority booking.'},
        {'question': 'How do I contact customer support?', 'answer': 'You can contact our customer support team via phone, email, or live chat on our website.'},
        # Add more FAQ entries as needed
    ]

    # Create FAQ objects and save them to the database
    for entry in faq_entries:
        FAQ.objects.create(question=entry['question'], answer=entry['answer'])

    print('FAQ data populated successfully.')

if __name__ == '__main__':
    populate_faq()
