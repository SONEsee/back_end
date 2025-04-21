from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Generate JWT tokens for a custom user model (LCICSystemUser).
    """
    refresh = RefreshToken()
    
    # Manually set the user ID in the token payload using the 'id' field
    refresh['user_id'] = user.id  # Use the 'id' field from LCICSystemUser
    
    # Optionally add additional claims to the token
    refresh['username'] = user.username
    refresh['roles'] = user.roles
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }