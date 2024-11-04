import phonenumbers
from phonenumbers import geocoder, carrier, is_valid_number, is_possible_number


# Function to validate if a phone number is Indian, valid, and get state/region info
def validate_and_get_state(phone_number_str):
    try:
        # Parse the phone number string
        phone_number = phonenumbers.parse(phone_number_str, "IN")

        # Check if it's a valid number
        if not is_valid_number(phone_number):
            return "Invalid phone number."

        # Check if the number is a possible number (e.g., length is valid)
        if not is_possible_number(phone_number):
            return "Phone number is not possible."

        # Check if it's an Indian number by looking at the country code
        if phone_number.country_code != 91:
            return "This is not an Indian phone number."

        # Get the state/region associated with the phone number
        state = geocoder.description_for_number(phone_number, "en")

        # Get the carrier (optional, may be blank if not available)
        carrier_info = carrier.name_for_number(phone_number, "en")

        return f"Valid Indian phone number from {state}. Carrier: {carrier_info if carrier_info else 'N/A'}"

    except phonenumbers.phonenumberutil.NumberParseException:
        return "Invalid input. Please enter a valid phone number."


# Example usage
phone_number_str = input("Enter a phone number with country code (e.g., +919876543210): ")
result = validate_and_get_state(phone_number_str)
print(result)
