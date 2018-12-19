from .models import Business_Type

state_choices = {
    'Alberta': 'Alberta',
    'British Columbia': 'British Columbia',
    'Manitoba': 'Manitoba',
    'New Brunswick': 'New Brunswick',
    'Newfoundland and Labrador': 'Newfoundland and Labrador',
    'Nova Scotia': 'Nova Scotia',
    'Nunavut': 'Nunavut',
    'Northwest Territories': 'Northwest Territories',
    'Ontario': 'Ontario',
    'Prince Edward Island': 'Prince Edward Island',
    'Quebec': 'Quebec',
    'Saskatchewan': 'Saskatchewan',
    'Yukon': 'Yukon',
}

price_choices = {
    '100000': '$100,000',
    '200000': '$200,000',
    '300000': '$300,000',
    '400000': '$400,000',
    '500000': '$500,000',
    '600000': '$600,000',
    '700000': '$700,000',
    '800000': '$800,000',
    '900000': '$900,000',
    '1000000': '$1M+',
}

# business_type = Business_Type.objects.all()

businessType_choices = {}

# for k in business_type:
# businessType_choices[k] = k
