class Config:
    # Mpesa C2B credentials
    CONSUMER_KEY = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    CONSUMER_SECRET = '2nHEyWSD4VjpNh2g'
    API_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    BUSINESS_SHORT_CODE = "4084887"
    TEST_C2B_SHORTCODE = "600344"
    PASSKEY = 'a5ce9f8f9b6621de9573b4f3eac5d2f3c245e4fefe96722be3ce2c421277f960'
    CALLBACK_URL = "https://7a81-102-0-11-2.ngrok-free.app/c2b/callback"
    CONFIRMATION_URL = "https://7a81-102-0-11-2.ngrok-free.app/c2b/confirmation"
    VALIDATION_URL = "https://7a81-102-0-11-2.ngrok-free.app/c2b/validation"
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mpesa.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
