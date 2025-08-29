from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Generate JWT tokens for a custom user model (LCICSystemUser).
    """
    refresh = RefreshToken()
    
 
    refresh['user_id'] = user.id  
    
    
    refresh['username'] = user.username
    refresh['roles'] = user.roles
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }