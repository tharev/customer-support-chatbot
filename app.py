"""
AI-Powered Customer Support Chatbot
===================================

A comprehensive Flask-based customer support chatbot system with advanced AI capabilities,
ticket management, knowledge base integration, and multi-channel support.

Features:
- AI-powered conversational interface using OpenAI GPT-4
- Intelligent ticket creation and management
- Knowledge base integration with semantic search
- Multi-channel support (web chat, email, Slack, WhatsApp)
- Real-time chat with live agent handoff
- Customer sentiment analysis and intent recognition
- Automated escalation based on urgency and complexity
- Comprehensive analytics and reporting
- Multi-language support with translation capabilities
- Integration with popular helpdesk systems (Zendesk, Freshdesk)
"""

from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
