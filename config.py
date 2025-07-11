"""
Configuration Management System for AI-Powered Customer Support Chatbot
=======================================================================

Comprehensive configuration management with dataclass-based organization covering all aspects
of the AI-powered customer support chatbot system including AI models, databases, integrations,
security, and production deployment settings.

Features:
- Environment-based configuration (development, testing, production)
- AI model configuration (OpenAI, Anthropic, local models)
- Multi-database support (PostgreSQL, MongoDB, Redis)
- Communication platform integrations (Slack, WhatsApp, email)
- Security and authentication settings
- Caching and background processing configuration
- Helpdesk system integrations (Zendesk, Freshdesk)
- Monitoring and analytics configuration
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union
from datetime import timedelta
import secrets
import logging

@dataclass
