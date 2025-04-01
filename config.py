import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-123'
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'