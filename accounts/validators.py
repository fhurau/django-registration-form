import re
from django.core.exceptions import ValidationError

def validate_password_strength(value):
    """
    Validates that the password meets the required criteria.
    """
    min_length = 8

    if len(value) < min_length:
        raise ValidationError(f'Password must be at least {min_length} characters long.')
    
    if not re.findall(r'[A-Z]', value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    
    if not re.findall(r'[a-z]', value):
        raise ValidationError('Password must contain at least one lowercase letter.')
    
    if not re.findall(r'[0-9]', value):
        raise ValidationError('Password must contain at least one number.')
    
    if not re.findall(r'[@$!%*?&]', value):
        raise ValidationError('Password must contain at least one special character (@, $, !, %, *, ?, &).')
