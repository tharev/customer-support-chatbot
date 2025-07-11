"""
Database Models for AI-Powered Customer Support Chatbot

This module defines comprehensive SQLAlchemy models for the customer support chatbot system,
including user management, conversation tracking, ticket management, knowledge base,
and analytics components.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any
import uuid
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Enums for status fields
class TicketStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
